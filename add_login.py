import os
import glob

# 1. Modify css/style.css
css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

btn_login_css = """
.btn-login{background:var(--navy-800);color:var(--cyan-500);border-color:var(--navy-700);padding:8px 18px;font-size:12.5px;gap:6px;}
.btn-login:hover{background:var(--navy-700);color:var(--white);}
.btn-login svg{width:16px;height:16px;}
"""

if '.btn-login' not in css:
    css = css.replace('.btn-sm{padding:9px 18px;font-size:12.5px;}', '.btn-sm{padding:9px 18px;font-size:12.5px;}\n' + btn_login_css.strip())
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Modify html files
html_files = glob.glob('*.html')

button_html = """<a href="sarcom.html" class="btn btn-login">
        <svg viewBox="0 0 24 24" fill="none"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="7" r="4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        ACCESO SARCOM
      </a>"""

target_str = '<div class="header-actions">'
replace_str = f'<div class="header-actions">\n      {button_html}'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'ACCESO SARCOM' not in content:
        content = content.replace(target_str, replace_str)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done")
