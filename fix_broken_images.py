import re
import urllib.parse

updates = {
    'proyecto-la-suiza.html': 'Recursos/Proyectos/proyecto-1.webp',
    'proyecto-la-cuarta.html': 'Recursos/Proyectos/proyecto-la-cuarta-extra-1.webp',
    'proyecto-molinos-nogales.html': 'Recursos/Proyectos/proyecto-molinos-nogales-extra-1.webp'
}

for filename, img in updates.items():
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Update the first image in the carousel track (or the only image)
    # The first img tag after <div class="carousel-track">
    html = re.sub(
        r'(<div class="carousel-track">\s*<img src=")[^"]+(")',
        rf'\g<1>{img}\g<2>',
        html,
        count=1
    )
    
    # 2. Update the background image in page-hero
    html = re.sub(
        r'background-image: linear-gradient\(.*?\), url\(\'.*?\'\);',
        f'background-image: linear-gradient(180deg, rgba(7,27,46,.55), rgba(7,27,46,.88)), url(\'{img}\');',
        html
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Updated HTML files.")

# Now update index.html and proyectos.html
for index_file in ['index.html', 'proyectos.html']:
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for html_file, img in updates.items():
        parts = content.split(f'href="{html_file}"')
        if len(parts) > 1:
            next_part = parts[1]
            parts[1] = re.sub(r'src="[^"]+"', f'src="{img}"', next_part, count=1)
            content = f'href="{html_file}"'.join(parts)
            
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated thumbnails.")
