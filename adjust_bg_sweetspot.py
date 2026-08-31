import os
import re

css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .page-hero from 0% to 35%
css = re.sub(r'(\.page-hero\[style\*="background-image"\]\{\s*background-size:cover;\s*background-position:)center 0% !important;', r'\1center 35% !important;', css)

# Replace .cta-band from 0% to 35%
css = re.sub(r'(\.cta-band\[style\*="background-image"\]\{\s*background-size:cover;\s*background-position:)center 0% !important;', r'\1center 35% !important;', css)

# Replace .section--dark from 0% to 15% (just slightly down from 0%)
css = re.sub(r'(\.section--dark\[style\*="background-image"\]\{\s*background-size:cover;\s*background-position:)center 0% !important;', r'\1center 15% !important;', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated with new percentages.")
