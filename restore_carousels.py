import re

updates = {
    'proyecto-la-suiza.html': {
        'images': [
            'Recursos/Fotos_Proyectos/La%20Suiza%20.webp',
            'Recursos/Proyectos/proyecto-la-suiza-extra-2.webp',
            'Recursos/Proyectos/proyecto-la-suiza-extra-3.webp',
            'Recursos/Proyectos/proyecto-la-suiza-extra-4.webp'
        ]
    },
    'proyecto-la-cuarta.html': {
        'images': [
            'Recursos/Fotos_Proyectos/Mesam%C3%A1vida%2C%20achibueno.webp',
            'Recursos/Proyectos/proyecto-la-cuarta-extra-1.webp',
            'Recursos/Proyectos/proyecto-la-cuarta-extra-2.webp',
            'Recursos/Proyectos/proyecto-la-cuarta-extra-3.webp'
        ]
    },
    'proyecto-molinos-nogales.html': {
        'images': [
            'Recursos/Fotos_Proyectos/Molino%2C%20nogales.webp',
            'Recursos/Proyectos/proyecto-molinos-nogales-extra-1.webp',
            'Recursos/Proyectos/proyecto-molinos-nogales-extra-2.webp'
        ]
    }
}

for filename, data in updates.items():
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Build new track
    track_html = '\n'
    for i, src in enumerate(data['images']):
        track_html += f'          <img src="{src}" alt="Vista {i+1} del proyecto" class="media-img" loading="lazy">\n'
    track_html += '        '
    
    html = re.sub(r'<div class="carousel-track">.*?</div>', f'<div class="carousel-track">{track_html}</div>', html, flags=re.DOTALL)
    
    # Build new dots
    dots_html = ''
    for i in range(len(data['images'])):
        active = ' class="active"' if i == 0 else ''
        dots_html += f'<span{active} data-slide="{i}"></span>'
        
    html = re.sub(r'<div class="dots">.*?</div>', f'<div class="dots">{dots_html}</div>', html, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Updated {filename}")
