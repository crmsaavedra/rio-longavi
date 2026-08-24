import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove footer link
    content = re.sub(r'<li><a href="servicios\.html">Comunidad</a></li>', '', content)
    content = re.sub(r'<li><a href="servicios\.html">Comunidad</a></li>', '', content)
    
    # In index.html remove the service-mini block
    if file == 'index.html':
        content = re.sub(
            r'<div class="service-mini">\s*<div class="icon-tile">.*?</svg></div>\s*<h4>Comunidad</h4>\s*<p>Talleres.*?Cotiza aquí.*?</div>', 
            '', 
            content, flags=re.DOTALL)
            
    # In servicios.html remove the service-block
    if file == 'servicios.html':
        content = re.sub(
            r'<div class="service-block">\s*<div>\s*<div class="step-no">05</div>\s*<h3>Comunidad</h3>.*?</div>\s*</div>', 
            '', 
            content, flags=re.DOTALL)
            
    # In proyectos.html remove the filter pill
    if file == 'proyectos.html':
        content = re.sub(r'<button class="filter-pill" data-filter="comunidad">Comunidad</button>', '', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Removed Comunidad blocks and links.")
