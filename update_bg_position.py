import os
import re

css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Replace .page-hero background-position
css = re.sub(r'(\.page-hero\[style\*="background-image"\]\{\s*background-size:cover;\s*background-position:)center;(\s*\})', r'\1center 30% !important;\2', css)

# Replace .cta-band background-position
css = re.sub(r'(\.cta-band\[style\*="background-image"\]\{\s*background-size:cover;\s*background-position:)center;(\s*\})', r'\1center 30% !important;\2', css)

# Replace .section--dark background-position
css = re.sub(r'(\.section--dark\[style\*="background-image"\]\{\s*background-size:cover;\s*background-position:)center;(\s*\})', r'\1center 30% !important;\2', css)


with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated backgrounds.")
