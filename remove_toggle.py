import os, re
for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Remove the button
        content = re.sub(r'<button class="theme-toggle".*?</button>\s*', '', content, flags=re.DOTALL)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
