import re
import urllib.parse

mapping = {
    'proyecto-la-suiza.html': 'La Suiza .webp',
    'proyecto-la-cuarta.html': 'Mesamávida, achibueno.webp',
    'proyecto-molinos-nogales.html': 'Molino, nogales.webp',
    'proyecto-empresa-porvenir.html': 'Pozo en sector San Ign, telemetría.webp',
    'proyecto-san-ignacio.html': 'Pozo en sector San Ignacio, telemetría.webp',
    'proyecto-yiyahue.html': 'Canal Yiyahue.webp',
    'proyecto-meladito.html': 'Canal Meladito.webp',
    'proyecto-la-mina.html': 'La Mina_01.webp'
}

for file in ['index.html', 'proyectos.html']:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    for link, img in mapping.items():
        encoded = urllib.parse.quote(img)
        new_src = f"Recursos/Fotos_Proyectos/{encoded}"
        
        # Regex to find the <img> tag inside the <a href="link">
        pattern = r'(href="' + re.escape(link) + r'".*?<img src=")(.*?)(")'
        html = re.sub(pattern, r'\g<1>' + new_src + r'\3', html, flags=re.DOTALL)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Updated thumbnails in index and proyectos.")
