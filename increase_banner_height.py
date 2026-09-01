import re

css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Make page-hero taller
css = css.replace('padding:40px 0 46px;', 'padding:90px 0 96px;')

# Make cta-band taller
css = css.replace('padding:64px 0;', 'padding:100px 0;')

# Make section--dark with background image taller
css = css.replace('.section--dark[style*="background-image"]{', '.section--dark[style*="background-image"]{\n  padding: 110px 0 !important;')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS padding updated for taller banners.")
