import os, re
for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = re.sub(r'</span>\s*Río Longaví', r'</span>', content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
