import os
import re

new_projects = [
    {
        "id": "proyecto-asesoria",
        "title": "Asesoría a organizaciones de usuarios de aguas",
        "cat": "Administración de canales",
        "img": "Recursos/Proyectos/Compromiso.webp",
        "old_href": "consultoria.html",
        "img_alt": "Asesoría a organizaciones de usuarios de aguas" # to find in html
    },
    {
        "id": "proyecto-la-puntilla",
        "title": "Canal derivado Castro la Puntilla, Longaví",
        "cat": "Construcción",
        "img": "Recursos/la puntilla 1.jpeg",
        "old_href": "construccion.html",
        "img_alt": "Canal derivado Castro la Puntilla"
    },
    {
        "id": "proyecto-vega-ancoa",
        "title": "Canal vecinal sector Vega Ancoa, Linares",
        "cat": "Construcción",
        "img": "Recursos/la puntilla 2.jpeg",
        "old_href": "construccion.html",
        "img_alt": "Canal vecinal sector Vega Ancoa"
    },
    {
        "id": "proyecto-el-carmen",
        "title": "Canal El Carmen Unión, Piguchén, Retiro",
        "cat": "Construcción",
        "img": "Recursos/la puntilla 3.jpeg",
        "old_href": "construccion.html",
        "img_alt": "Canal El Carmen Unión"
    }
]

# 1. Create individual pages
with open('proyecto-yiyahue.html', 'r', encoding='utf-8') as f:
    template = f.read()

for p in new_projects:
    html = template
    # Update title
    html = re.sub(r'<title>.*?</title>', f'<title>{p["title"]} — Rio Longavi</title>', html)
    # Update H1
    html = re.sub(r'<h1>.*?</h1>', f'<h1>{p["title"]}</h1>', html)
    # Update breadcrumb
    html = re.sub(r'<span class="cur">.*?</span>', f'<span class="cur">{p["title"]}</span>', html)
    # Update category (eyebrow)
    html = re.sub(r'<div class="eyebrow">.*?</div>', f'<div class="eyebrow">{p["cat"]}</div>', html)
    # Update h3 title
    html = re.sub(r'<h3 style="font-size:22px;margin-bottom:16px;">.*?</h3>', f'<h3 style="font-size:22px;margin-bottom:16px;">{p["title"]}</h3>', html)
    # Update hero image
    html = re.sub(r'background-image: linear-gradient\(.*?\), url\(\'.*?\'\);', f'background-image: linear-gradient(180deg, rgba(7,27,46,.55), rgba(7,27,46,.88)), url(\'{p["img"]}\');', html)
    # Update carousel track to only include the main image
    new_track = f'\n          <img src="{p["img"]}" alt="Vista 1 del proyecto" class="media-img" loading="lazy">\n        '
    html = re.sub(r'<div class="carousel-track">.*?</div>', f'<div class="carousel-track">{new_track}</div>', html, flags=re.DOTALL)
    # Update dots to only have 1 dot
    html = re.sub(r'<div class="dots">.*?</div>', f'<div class="dots"><span class="active" data-slide="0"></span></div>', html, flags=re.DOTALL)
    
    with open(f"{p['id']}.html", 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created {p['id']}.html")

# 2. Update proyectos.html links
with open('proyectos.html', 'r', encoding='utf-8') as f:
    proyectos_html = f.read()

for p in new_projects:
    # Instead of complicated regex, replace using standard string manipulation
    # Find the chunk <a class="project-card" ...> that contains p["img"] and replace its href
    parts = proyectos_html.split('<a class="project-card"')
    new_parts = [parts[0]]
    for part in parts[1:]:
        if p["img"] in part or p["img_alt"] in part: # Use the image source or alt text to identify the right block
            # This is the block, we need to replace href="construccion.html" (or consultoria) with our new id
            part = re.sub(r'href="' + p["old_href"] + r'"', f'href="{p["id"]}.html"', part, count=1)
        new_parts.append(part)
    proyectos_html = '<a class="project-card"'.join(new_parts)

with open('proyectos.html', 'w', encoding='utf-8') as f:
    f.write(proyectos_html)
print("Updated proyectos.html links")
