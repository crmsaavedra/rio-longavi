import os

css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# 1. Change body background
if 'background:var(--white);' in css:
    css = css.replace('background:var(--white);', 'background:#e8f4f8;')
elif 'background:#ffffff;' in css:
    css = css.replace('background:#ffffff;', 'background:#e8f4f8;')

# 2. Add background properties to .page-hero
# Find .page-hero{ ... } and inject properties
hero_target = '.page-hero{\n    position:relative;'
hero_replace = '.page-hero{\n    position:relative;\n    background-size:cover !important;\n    background-position:center 30% !important;'
if hero_target in css:
    css = css.replace(hero_target, hero_replace)
else:
    # try another way
    css = css.replace('.page-hero{', '.page-hero{\n    background-size:cover !important;\n    background-position:center 30% !important;')

# 3. Update .cta-band background-position
cta_target = '.cta-band[style*="background-image"]{\n    background-size:cover;\n    background-position:center;\n  }'
cta_replace = '.cta-band[style*="background-image"]{\n    background-size:cover;\n    background-position:center 30% !important;\n  }'
css = css.replace(cta_target, cta_replace)

# Just in case, update .hero-home background if there's any
# wait, .hero-home uses video, not image. But .hero-home has video absolutely positioned.

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated.")
