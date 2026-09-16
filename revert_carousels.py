import re

reverts = {
    'proyecto-la-cuarta.html': 'Recursos/Fotos_Proyectos/Mesam%C3%A1vida%2C%20achibueno.webp',
    'proyecto-molinos-nogales.html': 'Recursos/Fotos_Proyectos/Molino%2C%20nogales.webp'
}

for filename, img in reverts.items():
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Track with only the main image
    track_html = f'\n          <img src="{img}" alt="Vista 1 del proyecto" class="media-img" loading="lazy">\n        '
    html = re.sub(r'<div class="carousel-track">.*?</div>', f'<div class="carousel-track">{track_html}</div>', html, flags=re.DOTALL)
    
    # Dots with only 1 dot
    dots_html = '<span class="active" data-slide="0"></span>'
    html = re.sub(r'<div class="dots">.*?</div>', f'<div class="dots">{dots_html}</div>', html, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Reverted La Cuarta and Molinos Nogales")
