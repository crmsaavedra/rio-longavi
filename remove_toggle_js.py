import re
with open('js/main.js', 'r', encoding='utf-8') as file:
    content = file.read()

content = re.sub(r'\s*// Toggle claro/oscuro.*?}\s*', '\n\n  ', content, flags=re.DOTALL)

with open('js/main.js', 'w', encoding='utf-8') as file:
    file.write(content)
