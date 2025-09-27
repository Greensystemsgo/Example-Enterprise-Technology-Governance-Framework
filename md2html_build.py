#!/usr/bin/env python3
"""Build script that converts Markdown content in ./content into HTML output in ./docs."""
from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import List, Tuple

try:
    import markdown  # type: ignore
except ImportError as exc:  # pragma: no cover - guidance for missing dependency
    raise SystemExit(
        "The 'markdown' package is required. Install it with 'pip install markdown'."
    ) from exc

ROOT_DIR = Path(__file__).resolve().parent
SOURCE_DIR = ROOT_DIR / "content"
OUTPUT_DIR = ROOT_DIR / "docs"
INDEX_PATH = OUTPUT_DIR / "index.html"

CSS_BLOCK = """
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    margin: 2rem auto;
    max-width: 900px;
    line-height: 1.6;
    color: #1a1a1a;
    background-color: #ffffff;
    padding: 0 1.5rem 4rem;
}
nav.site-nav {
    margin-bottom: 2rem;
}
nav.site-nav a {
    color: #17479e;
    text-decoration: none;
    font-weight: 600;
}
nav.site-nav a:hover,
nav.site-nav a:focus {
    text-decoration: underline;
}
main.content h1,
main.content h2,
main.content h3 {
    line-height: 1.3;
}
pre {
    background: #f5f5f5;
    padding: 1rem;
    border-radius: 6px;
    overflow: auto;
}
code {
    background: #f5f5f5;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
}
a {
    color: #17479e;
}
ul.page-list {
    list-style: none;
    padding-left: 0;
}
ul.page-list li {
    margin-bottom: 0.4rem;
}
""".strip()

def title_from_path(md_path: Path) -> str:
    """Create a page title from the Markdown filename."""
    name = md_path.stem.replace('_', ' ').replace('-', ' ')
    cleaned = " ".join(part for part in name.split() if part)
    return cleaned.title() or md_path.stem

def ensure_source_dir() -> None:
    if not SOURCE_DIR.exists():
        raise SystemExit(f"Source directory not found at {SOURCE_DIR}.")

def reset_output_dir() -> None:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def read_markdown(md_file: Path) -> str:
    return md_file.read_text(encoding="utf-8")

def convert_markdown(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", "toc", "sane_lists"],
        output_format="html5",
    )

def wrap_html(title: str, nav_href: str, body_html: str) -> str:
    nav_link = nav_href.replace('\\', '/')
    return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>{title}</title>
<style>
{CSS_BLOCK}
</style>
</head>
<body>
<nav class=\"site-nav\"><a href=\"{nav_link}\">&larr; Back to index</a></nav>
<main class=\"content\">
{body_html}
</main>
</body>
</html>
"""

def build_page(md_file: Path) -> Tuple[str, Path]:
    rel_md = md_file.relative_to(SOURCE_DIR)
    rel_html = rel_md.with_suffix(".html")
    output_path = OUTPUT_DIR / rel_html
    output_path.parent.mkdir(parents=True, exist_ok=True)

    title = title_from_path(md_file)
    md_text = read_markdown(md_file)
    body_html = convert_markdown(md_text)

    nav_rel = os.path.relpath(INDEX_PATH, output_path.parent)
    html = wrap_html(title, nav_rel, body_html)
    output_path.write_text(html, encoding="utf-8")
    return title, rel_html

def copy_non_markdown_files() -> None:
    """Copy all non-Markdown files from source to output directory."""
    for source_file in SOURCE_DIR.rglob("*"):
        if source_file.is_file() and not source_file.suffix == ".md":
            rel_path = source_file.relative_to(SOURCE_DIR)
            output_path = OUTPUT_DIR / rel_path
            output_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, output_path)

def build_index(pages: List[Tuple[str, Path]]) -> None:
    items = []
    for title, rel_html in pages:
        href = rel_html.as_posix()
        items.append(f"<li><a href=\"{href}\">{title}</a></li>")

    page_list = "\n        ".join(items)
    body_html = f"""<h1>Documentation Index</h1>
<ul class=\"page-list\">
        {page_list}
</ul>
"""
    index_html = wrap_html("Documentation Index", "index.html", body_html)
    INDEX_PATH.write_text(index_html, encoding="utf-8")

def main() -> None:
    ensure_source_dir()
    reset_output_dir()

    md_files = sorted(SOURCE_DIR.rglob("*.md"))
    if not md_files:
        print("No Markdown files found under ./content.")
        return

    pages: List[Tuple[str, Path]] = []
    for md_file in md_files:
        title, rel_html = build_page(md_file)
        pages.append((title, rel_html))

    copy_non_markdown_files()
    build_index(pages)
    print(f"Converted {len(pages)} Markdown files into HTML under {OUTPUT_DIR}.")

if __name__ == "__main__":
    main()
