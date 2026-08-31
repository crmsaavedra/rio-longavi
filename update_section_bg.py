import os
import re

css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Update .section--dark background-position
target = '.section--dark[style*="background-image"]{\n    background-size:cover;\n    background-position:center;\n    position:relative;\n  }'
replace = '.section--dark[style*="background-image"]{\n    background-size:cover;\n    background-position:center 10% !important;\n    position:relative;\n  }'
css = css.replace(target, replace)
if target not in css:
    css = re.sub(r'(\.section--dark\[style\*="background-image"\]\{\s*background-size:cover;\s*background-position:)center;(\s*position:relative;\s*\})', r'\1center 10% !important;\2', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated .section--dark background.")
