from pathlib import Path
import re

badge = re.compile(r'(?m)^[ \t]*<div class="floating-badge">Competitivo en el mercado</div>[ \t]*\r?\n?')
removed = 0
for page in Path(".").glob("*.html"):
    content = page.read_text(encoding="utf-8")
    updated, count = badge.subn("", content)
    if count:
        page.write_text(updated, encoding="utf-8", newline="")
        removed += count

print(f"Removed {removed} floating badges.")
