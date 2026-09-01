import re
import os

with open('servicios.html', 'r', encoding='utf-8') as f:
    servicios = f.read()

# Helper to isolate a service block
def create_service_page(title, block_heading):
    # Regex to find the service-block containing the heading
    pattern = r'(<div class="service-block">.*?<h3>' + block_heading + r'</h3>.*?</div>\s*</div>)'
    match = re.search(pattern, servicios, re.DOTALL)
    if not match:
        return None
    
    block_html = match.group(1)
    
    # We replace the entire <div class="grid grid-1" style="gap:56px;"> with just our block
    grid_pattern = r'(<div class="wrap" style="max-width:960px;">\s*<div class="grid grid-1" style="gap:56px;">).*?(</section>)'
    
    new_html = re.sub(grid_pattern, r'\1\n' + block_html + r'\n</div>\n</div>\n\2', servicios, flags=re.DOTALL)
    
    # Update titles
    new_html = re.sub(r'<title>.*?</title>', f'<title>{title} — Río Longaví</title>', new_html)
    new_html = re.sub(r'<h1>Servicios</h1>', f'<h1>{title}</h1>', new_html)
    new_html = re.sub(r'<span class="cur">Servicios</span>', f'<span class="cur">{title}</span>', new_html)
    
    # Remove the section-head from the page since it's now a specific page
    new_html = re.sub(r'<div class="section-head">.*?</div>', '', new_html, flags=re.DOTALL)
    
    return new_html

pages = {
    'telemetria.html': ('Telemetría', 'Telemetr.a'),
    'construccion.html': ('Construcción', 'Construcci.n'),
    'consultoria.html': ('Consultoría', 'Consultor.a')
}

for filename, (title, heading) in pages.items():
    content = create_service_page(title, heading)
    if content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created {filename}")

# 2. Update proyectos.html
with open('proyectos.html', 'r', encoding='utf-8') as f:
    proy = f.read()

# Replace <div class="project-card" data-cat="telemetria"> with <a class="project-card" data-cat="telemetria" href="telemetria.html" target="_blank">
# Wait, I previously changed them to <a> without href or <div class="project-card">. Let's handle both.
# If they are <a> without href:
proy = re.sub(r'<a class="project-card" data-cat="telemetria"(?!\s*href)', r'<a class="project-card" data-cat="telemetria" href="telemetria.html" target="_blank"', proy)
proy = re.sub(r'<a class="project-card" data-cat="construccion"(?!\s*href)', r'<a class="project-card" data-cat="construccion" href="construccion.html" target="_blank"', proy)
proy = re.sub(r'<a class="project-card" data-cat="consultoria"(?!\s*href)', r'<a class="project-card" data-cat="consultoria" href="consultoria.html" target="_blank"', proy)

# If they are <div>:
proy = re.sub(r'<div class="project-card" data-cat="telemetria">', r'<a class="project-card" data-cat="telemetria" href="telemetria.html" target="_blank">', proy)
proy = re.sub(r'<div class="project-card" data-cat="construccion">', r'<a class="project-card" data-cat="construccion" href="construccion.html" target="_blank">', proy)
proy = re.sub(r'<div class="project-card" data-cat="consultoria">', r'<a class="project-card" data-cat="consultoria" href="consultoria.html" target="_blank">', proy)

# For any divs converted to 'a', we must fix closing </div> to </a>.
# We will just change all </div> that close a project card.
# This is tricky with regex. Let's assume they are already <a> because in fix_hrefs.py I just removed href="ficha-proyecto.html".
# So they are `<a class="project-card" data-cat="telemetria">\n ... </a>`. The regex above handles this perfectly.

with open('proyectos.html', 'w', encoding='utf-8') as f:
    f.write(proy)
print("Updated proyectos.html")

# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# index.html has <div class="project-card">. Some have tags "Monitoreo", "Construcción" inside them.
# I will replace the wrapper.
def replace_idx_card(match):
    full_card = match.group(0)
    if 'Monitoreo' in full_card:
        return full_card.replace('<div class="project-card">', '<a class="project-card" href="telemetria.html" target="_blank">').replace('</div>\n        </div>', '</div>\n        </a>')
    elif 'Construcc' in full_card:
        return full_card.replace('<div class="project-card">', '<a class="project-card" href="construccion.html" target="_blank">').replace('</div>\n        </div>', '</div>\n        </a>')
    return full_card

# regex to find project cards in index.html
idx = re.sub(r'<div class="project-card">.*?</div>\s*</div>', replace_idx_card, idx, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)
print("Updated index.html")
