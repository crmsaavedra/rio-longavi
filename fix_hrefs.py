import re

proyectos_path = 'proyectos.html'
with open(proyectos_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Just remove href="ficha-proyecto.html" so they aren't clickable links to the wrong page
content = content.replace(' href="ficha-proyecto.html"', '')

with open(proyectos_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed links in proyectos.html")
