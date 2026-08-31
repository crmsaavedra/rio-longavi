import os
import re

css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# 1. Update body background
# Match exactly the body block to replace background
body_pattern = r'(body\{[^}]*?background:)(\s*var\(--white\);)'
css = re.sub(body_pattern, r'\1#e6f2f5;', css)

# 2. Update .page-hero
hero_target = '.page-hero{\n    position:relative;'
hero_replace = '.page-hero{\n    position:relative;\n    background-size:cover !important;\n    background-position:center 30% !important;'
css = css.replace(hero_target, hero_replace)

# 3. Update .cta-band background image centering
cta_target = '.cta-band[style*="background-image"]{\n    background-size:cover;\n    background-position:center;\n  }'
cta_replace = '.cta-band[style*="background-image"]{\n    background-size:cover;\n    background-position:center 30% !important;\n  }'
css = css.replace(cta_target, cta_replace)

# Also update the video in .hero-video in case they meant the video?
video_pattern = r'(\.hero-video\{[^}]*?object-fit:cover;)'
css = re.sub(video_pattern, r'\1 object-position:center 30%;', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS precisely updated.")
