import re
import os

projects = [
    {
        "id": "proyecto-la-suiza",
        "title": "Canal La Suiza, San Clemente",
        "cat": "Monitoreo",
        "img": "Recursos/Proyectos/proyecto-1.webp"
    },
    {
        "id": "proyecto-la-cuarta",
        "title": "Canal La Cuarta Mesamávida, sistema Achibueno, Linares",
        "cat": "Monitoreo",
        "img": "Recursos/Proyectos/proyecto-2.webp"
    },
    {
        "id": "proyecto-molinos-nogales",
        "title": "Canal unificado Molinos–Nogales, Santa Delfina, Retiro",
        "cat": "Monitoreo",
        "img": "Recursos/Proyectos/proyecto-3.webp"
    },
    {
        "id": "proyecto-san-ignacio",
        "title": "Pozo agrícola San Ignacio, Retiro",
        "cat": "Monitoreo de pozos",
        "img": "Recursos/Proyectos/proyecto-pozo.jpeg"
    },
    {
        "id": "proyecto-empresa-porvenir",
        "title": "Empresa Porvenir, sector La Tercera, Longaví",
        "cat": "Monitoreo de pozos",
        "img": "Recursos/Proyectos/Pozo en sector San Ign, telemetría.webp"
    },
    {
        "id": "proyecto-yiyahue",
        "title": "Revestimiento Canal Yiyahue, Parral",
        "cat": "Construcción",
        "img": "Recursos/Proyectos/proyecto-6.webp"
    }
]

with open('ficha-proyecto.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Make the specific pages
for p in projects:
    html = template
    # Title tag
    html = re.sub(r'<title>.*?</title>', f'<title>{p["title"]} — Rio Longavi</title>', html)
    # H1
    html = re.sub(r'<h1>.*?</h1>', f'<h1>{p["title"]}</h1>', html)
    # Breadcrumb
    html = re.sub(r'<span class="cur">.*?</span>', f'<span class="cur">{p["title"]}</span>', html)
    # Hero BG
    html = re.sub(r"url\('Recursos/Proyectos/proyecto-4\.webp'\)", f"url('{p['img']}')", html)
    # Eyebrow
    html = re.sub(r'<div class="eyebrow">.*?</div>', f'<div class="eyebrow">{p["cat"]}</div>', html)
    # H3
    html = re.sub(r'<h3 style="font-size:22px;margin-bottom:16px;">.*?</h3>', f'<h3 style="font-size:22px;margin-bottom:16px;">{p["title"]}</h3>', html)
    # Carousel (just put the main image as the only one for now, or keep the default 4 but make the first one correct)
    
    # We will keep the default 4, but replace the first one with the specific image
    html = re.sub(r'<img src="Recursos/Proyectos/proyecto-4\.webp" alt="Vista 1 del proyecto"', f'<img src="{p["img"]}" alt="Vista 1 del proyecto"', html)
    
    # Let's save it
    with open(f'{p["id"]}.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created {p['id']}.html")

# Update index.html and proyectos.html to link to these new pages
for file_to_update in ['index.html', 'proyectos.html']:
    with open(file_to_update, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will look for <h4>Title</h4> inside the cards and replace the href of the wrapping <a> tag
    # Since we can't easily parse it with simple regex, let's do something specific
    
    for p in projects:
        # Find the a tag that contains this title
        # The block looks like <a class="project-card" href="..." ...> ... <h4>TITLE</h4> ... </a>
        # We can use regex to match the href specifically for the card with this title
        
        # Regex to find the href right before the image that belongs to this title
        # Actually it's simpler:
        # Split by `<a class="project-card"`
        parts = content.split('<a class="project-card"')
        new_parts = [parts[0]]
        for part in parts[1:]:
            if f'<h4>{p["title"]}</h4>' in part:
                # Replace the href in this part
                part = re.sub(r'href=".*?"', f'href="{p["id"]}.html"', part, count=1)
            new_parts.append(part)
        content = '<a class="project-card"'.join(new_parts)
    
    with open(file_to_update, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated links in {file_to_update}")

