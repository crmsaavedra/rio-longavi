import re

css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Change floating badge from bottom to top
css = css.replace('bottom: 30px;', 'top: 100px;') # usually top 30px might overlap header, let's see. header is sticky?
css = css.replace('bottom: 20px;', 'top: 80px;') # mobile

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated floating badge position")
