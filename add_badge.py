import os
import glob

html_files = glob.glob('*.html')
badge_html = '\n<div class="floating-badge">Competitivo en el mercado</div>\n'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'floating-badge' not in content:
        content = content.replace('</body>', badge_html + '</body>')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done inserting badges.")
