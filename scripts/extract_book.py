#!/usr/bin/env python3
"""Extract readable text and metadata from txt/md/pdf/epub/fb2 for book2skill.

No dependency installation. Uses available local tools/libraries only:
- txt/md: direct read
- pdf: pdftotext if installed, then pypdf/PyPDF2, then PyMuPDF, then pdfminer.six
- epub: ebooklib+bs4 if installed, then stdlib zip/html parser fallback
- fb2: stdlib XML parser, including basic .fb2.zip support

Writes:
- <out-dir>/full_text.txt
- <out-dir>/metadata.json
"""

from __future__ import annotations

import argparse
import html
import html.parser
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional, Tuple

WORDS_PER_TOKEN = 0.75


def estimate_tokens(text: str) -> int:
    return int(len(text.split()) / WORDS_PER_TOKEN) if text.strip() else 0


def read_text_file(path: Path) -> Tuple[str, str]:
    for enc in ("utf-8", "utf-8-sig", "cp1251", "latin-1"):
        try:
            return path.read_text(encoding=enc), f"text:{enc}"
        except UnicodeDecodeError:
            continue
    return path.read_text(errors="replace"), "text:replace"


def extract_pdf_pdftotext(path: Path) -> Optional[str]:
    if not shutil.which("pdftotext"):
        return None
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", str(path), "-"],
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout
    except Exception:
        return None
    return None


def extract_pdf_pypdf2(path: Path) -> Optional[str]:
    try:
        try:
            import pypdf as pdf_lib  # type: ignore
        except Exception:
            import PyPDF2 as pdf_lib  # type: ignore
        parts = []
        with path.open("rb") as f:
            reader = pdf_lib.PdfReader(f)
            for page in reader.pages:
                try:
                    parts.append(page.extract_text() or "")
                except Exception:
                    parts.append("")
        text = "\n\n".join(parts)
        return text if text.strip() else None
    except Exception:
        return None


def extract_pdf_pymupdf(path: Path) -> Optional[str]:
    try:
        import fitz  # type: ignore  # PyMuPDF

        parts = []
        with fitz.open(str(path)) as doc:
            for page in doc:
                try:
                    parts.append(page.get_text("text") or "")
                except Exception:
                    parts.append("")
        text = "\n\n".join(parts)
        return text if text.strip() else None
    except Exception:
        return None


def extract_pdf_pdfminer(path: Path) -> Optional[str]:
    try:
        from pdfminer.high_level import extract_text  # type: ignore
        text = extract_text(str(path))
        return text if text and text.strip() else None
    except Exception:
        return None


def count_pdf_pages(path: Path) -> int:
    if shutil.which("pdfinfo"):
        try:
            result = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True, timeout=20)
            for line in result.stdout.splitlines():
                if line.startswith("Pages:"):
                    return int(line.split(":", 1)[1].strip())
        except Exception:
            pass
    try:
        try:
            import pypdf as pdf_lib  # type: ignore
        except Exception:
            import PyPDF2 as pdf_lib  # type: ignore
        with path.open("rb") as f:
            return len(pdf_lib.PdfReader(f).pages)
    except Exception:
        pass
    try:
        import fitz  # type: ignore
        with fitz.open(str(path)) as doc:
            return len(doc)
    except Exception:
        return 0


class HtmlTextExtractor(html.parser.HTMLParser):
    skip_tags = {"script", "style", "head", "noscript"}
    block_tags = {"p", "br", "div", "li", "h1", "h2", "h3", "h4", "h5", "h6", "section", "article"}

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.skip_depth += 1
        if tag in self.block_tags:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.skip_tags and self.skip_depth:
            self.skip_depth -= 1
        if tag in self.block_tags:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip_depth:
            self.parts.append(data)

    def text(self) -> str:
        raw = html.unescape("".join(self.parts))
        return re.sub(r"\n{3,}", "\n\n", raw)


def extract_epub_ebooklib(path: Path) -> Optional[str]:
    try:
        import ebooklib  # type: ignore
        from ebooklib import epub  # type: ignore
        from bs4 import BeautifulSoup  # type: ignore
        book = epub.read_epub(str(path))
        parts = []
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            soup = BeautifulSoup(item.get_content(), "html.parser")
            parts.append(soup.get_text(separator="\n"))
        text = "\n\n".join(parts)
        return text if text.strip() else None
    except Exception:
        return None


def extract_epub_zip(path: Path) -> Optional[str]:
    try:
        with zipfile.ZipFile(path) as zf:
            names = zf.namelist()
            html_names = sorted(n for n in names if n.lower().endswith((".xhtml", ".html", ".htm")))
            if not html_names:
                return None
            parts = []
            for name in html_names:
                try:
                    raw = zf.read(name).decode("utf-8", errors="replace")
                    parser = HtmlTextExtractor()
                    parser.feed(raw)
                    text = parser.text().strip()
                    if text:
                        parts.append(text)
                except Exception:
                    continue
            text = "\n\n".join(parts)
            return text if text.strip() else None
    except Exception:
        return None


def count_epub_items(path: Path) -> int:
    try:
        with zipfile.ZipFile(path) as zf:
            return sum(1 for n in zf.namelist() if n.lower().endswith((".xhtml", ".html", ".htm")))
    except Exception:
        return 0


def _strip_ns(tag: str) -> str:
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


def _read_fb2_bytes(path: Path) -> bytes:
    if path.suffix.lower() == ".zip" or path.name.lower().endswith(".fb2.zip"):
        with zipfile.ZipFile(path) as zf:
            fb2_names = [n for n in zf.namelist() if n.lower().endswith(".fb2")]
            if not fb2_names:
                raise RuntimeError("ZIP does not contain an .fb2 file")
            return zf.read(fb2_names[0])
    return path.read_bytes()


def extract_fb2(path: Path) -> Tuple[str, dict]:
    raw = _read_fb2_bytes(path)
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        # Some FB2 files declare legacy encodings. Decode manually and retry.
        text = raw.decode("utf-8", errors="replace")
        root = ET.fromstring(text.encode("utf-8"))

    title_parts = []
    body_parts = []
    sections = 0
    top_sections = []

    for body in root.iter():
        if _strip_ns(body.tag) != "body":
            continue
        for child in list(body):
            if _strip_ns(child.tag) != "section":
                continue
            title_elem = None
            for section_child in list(child):
                if _strip_ns(section_child.tag) == "title":
                    title_elem = section_child
                    break
            if title_elem is not None:
                title = " ".join("".join(title_elem.itertext()).split())
                if title:
                    top_sections.append(title)

    for elem in root.iter():
        tag = _strip_ns(elem.tag)
        if tag == "book-title":
            value = " ".join("".join(elem.itertext()).split())
            if value:
                title_parts.append(value)
        elif tag == "section":
            sections += 1
            title = None
            for child in list(elem):
                if _strip_ns(child.tag) == "title":
                    title = " ".join("".join(child.itertext()).split())
                    break
            if title:
                body_parts.append(f"\n\n{title}\n")
        elif tag in {"p", "v", "subtitle", "text-author", "cite"}:
            value = " ".join("".join(elem.itertext()).split())
            if value:
                body_parts.append(value)

    text = "\n\n".join(body_parts).strip()
    if not text:
        text = "\n\n".join(" ".join(t.split()) for t in root.itertext() if t and t.strip()).strip()
    if not text:
        raise RuntimeError("Could not extract text from FB2")

    return text, {
        "fb2_sections": sections,
        "fb2_title": title_parts[0] if title_parts else None,
        "fb2_top_sections": top_sections[:80],
    }


def detect_structure(text: str) -> dict:
    sample = text[:80000]
    lines = sample.splitlines()
    chapter_re = re.compile(r"^\s*((chapter|глава|часть|part)\s+[\wIVXLCА-Яа-я.-]+|\d+[.)]\s+\S)", re.I)
    headings = []
    for line in lines:
        s = line.strip()
        if 3 <= len(s) <= 120 and chapter_re.match(s):
            headings.append(s)
        if len(headings) >= 30:
            break
    lower = sample.lower()
    return {
        "chapters_detected": len(headings),
        "chapter_headings_sample": headings[:12],
        "has_toc_hint": any(x in lower for x in ("table of contents", "contents", "оглавление", "содержание")),
    }


def extract(path: Path) -> Tuple[str, str, dict]:
    ext = path.suffix.lower()
    meta_extra = {}
    header = path.read_bytes()[:512]
    header_lower = header.lower()

    if ext in {".txt", ".md", ".markdown"}:
        text, method = read_text_file(path)
        return text, method, meta_extra

    if ext == ".pdf" or header[:4] == b"%PDF":
        for method, fn in (
            ("pdftotext", extract_pdf_pdftotext),
            ("pypdf/PyPDF2", extract_pdf_pypdf2),
            ("PyMuPDF", extract_pdf_pymupdf),
            ("pdfminer.six", extract_pdf_pdfminer),
        ):
            text = fn(path)
            if text:
                meta_extra["pages"] = count_pdf_pages(path)
                return text, method, meta_extra
        raise RuntimeError("Could not extract PDF text. Install poppler-utils (pdftotext), pypdf/PyPDF2, PyMuPDF, or pdfminer.six. If this is a scanned PDF, OCR is required.")

    if ext == ".fb2" or path.name.lower().endswith(".fb2.zip") or b"<fictionbook" in header_lower:
        text, fb2_meta = extract_fb2(path)
        meta_extra.update(fb2_meta)
        return text, "fb2-xml", meta_extra

    if ext == ".epub" or header[:2] == b"PK":
        for method, fn in (("ebooklib+bs4", extract_epub_ebooklib), ("zipfile-htmlparser", extract_epub_zip)):
            text = fn(path)
            if text:
                meta_extra["spine_or_html_items"] = count_epub_items(path)
                return text, method, meta_extra
        raise RuntimeError("Could not extract EPUB text. Try installing ebooklib and beautifulsoup4, or provide exported text.")

    raise RuntimeError(f"Unsupported format: {ext}. Supported: .txt, .md, .pdf, .epub, .fb2, .fb2.zip")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract book text for book2skill")
    parser.add_argument("source", help="Path to txt/md/pdf/epub/fb2/fb2.zip")
    parser.add_argument("--out-dir", default="/tmp/book2skill_extract", help="Output directory")
    parser.add_argument("--max-chars", type=int, default=0, help="Optional cap for full_text.txt; 0 means no cap")
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    if not source.exists() or not source.is_file():
        print(f"ERROR: file not found: {source}", file=sys.stderr)
        return 2

    out_dir = Path(args.out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        text, method, extra = extract(source)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    original_chars = len(text)
    truncated = False
    if args.max_chars and len(text) > args.max_chars:
        text = text[: args.max_chars]
        truncated = True

    (out_dir / "full_text.txt").write_text(text, encoding="utf-8")
    detected_format = source.suffix.lower().lstrip(".") or "unknown"
    if method.startswith("fb2"):
        detected_format = "fb2"

    metadata = {
        "source_file": str(source),
        "filename": source.name,
        "format": detected_format,
        "method": method,
        "file_size_mb": round(source.stat().st_size / (1024 * 1024), 2),
        "chars": len(text),
        "original_chars": original_chars,
        "truncated": truncated,
        "words": len(text.split()),
        "estimated_tokens": estimate_tokens(text),
        **extra,
        **detect_structure(text),
    }
    (out_dir / "metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(metadata, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
