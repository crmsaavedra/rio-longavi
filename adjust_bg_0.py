import os

css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace all occurrences of center 30% and center 10% with center 0%
css = css.replace('center 30% !important', 'center 0% !important')
css = css.replace('center 10% !important', 'center 0% !important')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Changed background positions to center 0%")
