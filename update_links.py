import os
import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple replace
    new_content = content.replace('href="sarcom.html" class="btn btn-login"', 'href="https://sarcom2.aguaslongavi.cl/" class="btn btn-login" target="_blank"')
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Updated links.")
