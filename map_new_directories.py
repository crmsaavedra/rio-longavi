import os
import re
import urllib.parse

project_mapping = {
    'proyecto-asesoria.html': {
        'folder': 'Recursos/Fotos_Proyectos/',
        'files': ['Administracion de Ouas.jpeg']
    },
    'proyecto-la-puntilla.html': {
        'folder': 'Recursos/Fotos_Proyectos/Castro La Puntilla/'
    },
    'proyecto-el-carmen.html': {
        'folder': 'Recursos/Fotos_Proyectos/El Carmen Unión/'
    },
    'proyecto-empresa-porvenir.html': {
        'folder': 'Recursos/Fotos_Proyectos/Empresa Porvenir/'
    },
    'proyecto-meladito.html': {
        'folder': 'Recursos/Fotos_Proyectos/Meladito/'
    },
    'proyecto-san-ignacio.html': {
        'folder': 'Recursos/Fotos_Proyectos/San Ignacio/'
    },
    'proyecto-la-mina.html': {
        'folder': 'Recursos/Fotos_Proyectos/Unificado La Mina/'
    },
    'proyecto-vega-ancoa.html': {
        'folder': 'Recursos/Fotos_Proyectos/Vega Ancoa/'
    },
    'proyecto-yiyahue.html': {
        'folder': 'Recursos/Fotos_Proyectos/Yiyahue/'
    }
}

thumbnail_updates = {}

for html_file, data in project_mapping.items():
    folder_path = data['folder']
    
    if 'files' in data:
        images = data['files']
    else:
        if not os.path.exists(folder_path):
            print(f"Directory not found: {folder_path}")
            continue
        images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
        images.sort() # Ensure consistent ordering
        
    if not images:
        print(f"No images found for {html_file}")
        continue
        
    print(f"Updating {html_file} with {len(images)} images.")
    
    # Store first image for thumbnail updates
    # We must URL encode the paths because they have spaces/accents
    first_image_path = folder_path + images[0]
    encoded_first_image_path = urllib.parse.quote(first_image_path)
    thumbnail_updates[html_file] = encoded_first_image_path
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Build track
    track_html = '\n'
    for i, img in enumerate(images):
        img_path = folder_path + img
        encoded_path = urllib.parse.quote(img_path)
        track_html += f'          <img src="{encoded_path}" alt="Vista {i+1} del proyecto" class="media-img" loading="lazy">\n'
    track_html += '        '
    
    html = re.sub(r'<div class="carousel-track">.*?</div>', f'<div class="carousel-track">{track_html}</div>', html, flags=re.DOTALL)
    
    # Build dots
    dots_html = ''
    for i in range(len(images)):
        active = ' class="active"' if i == 0 else ''
        dots_html += f'<span{active} data-slide="{i}"></span>'
    
    html = re.sub(r'<div class="dots">.*?</div>', f'<div class="dots">{dots_html}</div>', html, flags=re.DOTALL)
    
    # Optionally update hero image to first image if requested (or keep it as is, but it's probably better to update it since old ones were deleted)
    # The old ones were deleted so we MUST update the hero image
    html = re.sub(r'background-image: linear-gradient\(.*?\), url\(\'.*?\'\);', f'background-image: linear-gradient(180deg, rgba(7,27,46,.55), rgba(7,27,46,.88)), url(\'{encoded_first_image_path}\');', html)

    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)


# Now update index.html and proyectos.html thumbnails
print("Updating thumbnails...")
for index_file in ['index.html', 'proyectos.html']:
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for html_file, thumb_path in thumbnail_updates.items():
        # Find the block for this html_file and replace its image src
        parts = content.split(f'href="{html_file}"')
        if len(parts) > 1:
            # We found the link, the image is in the next part
            next_part = parts[1]
            # Replace the first src="..." in this part
            parts[1] = re.sub(r'src="[^"]+"', f'src="{thumb_path}"', next_part, count=1)
            content = f'href="{html_file}"'.join(parts)
            
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Done.")
