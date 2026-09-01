import re

with open('servicios.html', 'r', encoding='utf-8', errors='ignore') as f:
    servicios = f.read()

with open('ficha-proyecto.html', 'r', encoding='utf-8', errors='ignore') as f:
    ficha = f.read()

def create_page(service_id, title, img_path):
    # Find content in servicios.html
    # Look for <h3>Title</h3> and grab everything until </div>
    pattern = r'<h3>' + service_id + r'</h3>(.*?<ul class="check-list">.*?</ul>)'
    match = re.search(pattern, servicios, re.DOTALL)
    content = match.group(1) if match else "<p>Detalles del servicio.</p>"
    
    html = ficha
    # Title
    html = re.sub(r'<title>.*?</title>', f'<title>{title} — Río Longaví</title>', html)
    # Breadcrumb
    html = html.replace('<span class="cur">Ficha de proyecto</span>', f'<span class="cur">{title}</span>')
    # H1
    html = re.sub(r'<h1>.*?</h1>', f'<h1>{title}</h1>', html)
    # Hero BG
    html = re.sub(r"url\('Recursos/Proyectos/proyecto-4\.webp'\)", f"url('{img_path}')", html)
    # Carousel first img
    html = re.sub(r'<img src="Recursos/Proyectos/proyecto-4\.webp"', f'<img src="{img_path}"', html)
    # Eyebrow
    html = html.replace('<div class="eyebrow">Monitoreo de Pozos</div>', '<div class="eyebrow">Servicios</div>')
    # H3
    html = re.sub(r'<h3 style="font-size:22px;margin-bottom:16px;">.*?</h3>', f'<h3 style="font-size:22px;margin-bottom:16px;">{title}</h3>', html)
    # Content replacement
    # We replace from <h4 style="font-size:13px;...">...</ul>
    desc_pattern = r'<h4 style="font-size:13px;text-transform:uppercase;letter-spacing:\.04em;color:var\(--ink-600\);margin-bottom:12px;">Descripci.*?</h4>.*?</ul>'
    
    new_desc = f'<h4 style="font-size:13px;text-transform:uppercase;letter-spacing:.04em;color:var(--ink-600);margin-bottom:12px;">Descripción del servicio</h4>\n{content}'
    
    html = re.sub(desc_pattern, new_desc, html, flags=re.DOTALL)
    
    # Also replace "Volver a proyectos" with "Volver a servicios"
    html = html.replace('href="proyectos.html"', 'href="servicios.html"').replace('Volver a proyectos', 'Volver a servicios')
    
    # Make sure we don't accidentally break the projects nav link
    # The nav link should point to proyectos.html still for "Proyectos" but wait, the breadcrumb was changed correctly.
    # Oh, wait. I replaced all `href="proyectos.html"`. Let's just fix the breadcrumb and the back button specifically.
    
    return html

pages = [
    ('telemetria.html', 'Telemetr.a', 'Telemetría', 'Recursos/Telemetria.webp'),
    ('construccion.html', 'Construcci.n', 'Construcción', 'Recursos/construcción.webp'),
    ('consultoria.html', 'Consultor.a', 'Consultoría', 'Recursos/Proyectos/proyecto-1.webp') # fallback image
]

for filename, svc_id, title, img in pages:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(create_page(svc_id, title, img))
    print(f"Created {filename}")
