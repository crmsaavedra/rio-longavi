import re

updates = {
    'proyecto-la-cuarta.html': 'Recursos/Fotos_Proyectos/Mesam%C3%A1vida%2C%20achibueno.webp'
}

for filename, img in updates.items():
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = re.sub(
        r'(<div class="carousel-track">\s*<img src=")[^"]+(")',
        rf'\g<1>{img}\g<2>',
        html,
        count=1
    )
    
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
