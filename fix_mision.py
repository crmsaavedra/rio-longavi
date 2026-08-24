import os
with open('nosotros.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Recursos/Misión.webp', 'Recursos/Mision.webp')

with open('nosotros.html', 'w', encoding='utf-8') as f:
    f.write(content)
