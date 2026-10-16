"""Inline fonts, images and the logo into each proposal so every file is self-contained.

Usage: python3 proposals/build.py   (reads proposals/src/*.html, writes proposals/*.html)
Placeholders: {{font:path}} -> data URI, {{img:path}} -> data URI, {{logo}} -> inline wordmark SVG.
"""
import base64, pathlib, re

root = pathlib.Path(__file__).resolve().parent
repo = root.parent
mime = {".woff2": "font/woff2", ".jpg": "image/jpeg", ".png": "image/png", ".svg": "image/svg+xml"}

index = (repo / "index.html").read_text()
logo = re.search(r'<svg class="logo"[^>]*>.*?</svg>', index, re.S).group(0)
logo = logo.replace('<svg class="logo"', '<svg class="logo"').replace(' height="40"', "")

def data_uri(rel):
    p = (root / rel).resolve()
    return f"data:{mime[p.suffix]};base64," + base64.b64encode(p.read_bytes()).decode()

for src in sorted((root / "src").glob("*.html")):
    s = src.read_text()
    s = re.sub(r"\{\{(font|img):([^}]+)\}\}", lambda m: data_uri(m.group(2)), s)
    s = s.replace("{{logo}}", logo)
    (root / src.name).write_text(s)
    print(f"{src.name}: {len(s) // 1024} KB")
