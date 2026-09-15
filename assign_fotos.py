import os
import re
import urllib.parse

# 1. Create missing project pages (Meladito, La Mina)
template_path = 'proyecto-yiyahue.html' # Use an existing one as template
with open(template_path, 'r', encoding='utf-8') as f:
    template_html = f.read()

new_projects = [
    {
        "id": "proyecto-meladito",
        "title": "Revestimiento Canal Meladito, Longaví",
        "cat": "Construcción"
    },
    {
        "id": "proyecto-la-mina",
        "title": "Revestimiento Canal unificado La Mina Nogales-Molino",
        "cat": "Construcción"
    }
]

for p in new_projects:
    if not os.path.exists(f"{p['id']}.html"):
        html = template_html
        html = re.sub(r'<title>.*?</title>', f'<title>{p["title"]} — Rio Longavi</title>', html)
        html = re.sub(r'<h1>.*?</h1>', f'<h1>{p["title"]}</h1>', html)
        html = re.sub(r'<span class="cur">.*?</span>', f'<span class="cur">{p["title"]}</span>', html)
        html = re.sub(r'<div class="eyebrow">.*?</div>', f'<div class="eyebrow">{p["cat"]}</div>', html)
        html = re.sub(r'<h3 style="font-size:22px;margin-bottom:16px;">.*?</h3>', f'<h3 style="font-size:22px;margin-bottom:16px;">{p["title"]}</h3>', html)
        with open(f"{p['id']}.html", 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Created {p['id']}.html")

# 2. Link them in proyectos.html
with open('proyectos.html', 'r', encoding='utf-8') as f:
    proyectos_html = f.read()

# Replace href for Meladito
proyectos_html = re.sub(
    r'(<a class="project-card" data-cat="construccion" href=")(construccion\.html)(" target="_blank">\s*<div class="media ratio-4-3"><img src="Recursos/Proyectos/proyecto-7\.webp" alt="Revestimiento Canal Meladito")',
    r'\1proyecto-meladito.html\3',
    proyectos_html
)

# Replace href for La Mina
proyectos_html = re.sub(
    r'(<a class="project-card" data-cat="construccion" href=")(construccion\.html)(" target="_blank">\s*<div class="media ratio-4-3"><img src="Recursos/Proyectos/proyecto-9\.webp" alt="Revestimiento Canal unificado La Mina")',
    r'\1proyecto-la-mina.html\3',
    proyectos_html
)

with open('proyectos.html', 'w', encoding='utf-8') as f:
    f.write(proyectos_html)

# 3. Update carousels for all 8 projects
mapping = {
    'proyecto-la-suiza': ['La Suiza .webp'],
    'proyecto-la-cuarta': ['Mesamávida, achibueno.webp'],
    'proyecto-molinos-nogales': ['Molino, nogales.webp'],
    'proyecto-empresa-porvenir': ['Pozo en sector San Ign, telemetría.webp'],
    'proyecto-san-ignacio': ['Pozo en sector San Ignacio, telemetría.webp', 'San Ignacio, telemetría en pozo automática.webp', 'San Ignacio, telemetría pozo automático.webp'],
    'proyecto-yiyahue': ['Canal Yiyahue.webp'],
    'proyecto-meladito': ['Canal Meladito.webp'],
    'proyecto-la-mina': ['La Mina_01.webp', 'La Mina_02.webp', 'La Mina_03.webp', 'La Mina_04.webp']
}

for proj_id, imgs in mapping.items():
    html_file = f"{proj_id}.html"
    if not os.path.exists(html_file):
        continue
        
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace the carousel track
    track_pattern = r'<div class="carousel-track">(.*?)</div>'
    
    new_track = '\n'
    for i, img_name in enumerate(imgs):
        # URL encode the filename to handle spaces and accents
        encoded_name = urllib.parse.quote(img_name)
        src = f"Recursos/Fotos_Proyectos/{encoded_name}"
        new_track += f'          <img src="{src}" alt="Vista {i+1} del proyecto" class="media-img" loading="lazy">\n'
    new_track += '        '
        
    html = re.sub(track_pattern, f'<div class="carousel-track">{new_track}</div>', html, flags=re.DOTALL)
    
    # Update dots
    dots_pattern = r'<div class="dots">(.*?)</div>'
    new_dots = ''
    for i in range(len(imgs)):
        active = ' class="active"' if i == 0 else ''
        new_dots += f'<span{active} data-slide="{i}"></span>'
    html = re.sub(dots_pattern, f'<div class="dots">{new_dots}</div>', html, flags=re.DOTALL)
    
    # Update hero BG to the first image of the project
    if imgs:
        encoded_name = urllib.parse.quote(imgs[0])
        hero_src = f"Recursos/Fotos_Proyectos/{encoded_name}"
        html = re.sub(r'background-image: linear-gradient\(.*?\), url\(\'.*?\'\);', f'background-image: linear-gradient(180deg, rgba(7,27,46,.55), rgba(7,27,46,.88)), url(\'{hero_src}\');', html)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated carousel and hero for {proj_id}.html")

print("All done!")
