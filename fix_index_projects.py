import os
import re

index_path = 'index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace San Ignacio in index.html
content = content.replace(
    '<div class="media ratio-4-3"><img src="Recursos/Proyectos/proyecto-4.webp" alt="Canal interno San Ignacio" class="media-img" loading="lazy"><span class="tag">Monitoreo</span></div>',
    '<div class="media ratio-4-3"><img src="Recursos/Proyectos/proyecto-pozo.jpeg" alt="Canal interno San Ignacio" class="media-img" loading="lazy"><span class="tag">Monitoreo</span></div>'
)
content = content.replace(
    '<div class="body"><div class="cat">Monitoreo</div><h4>Canal interno en sector San Ignacio, Retiro</h4></div>',
    '<div class="body"><div class="cat">Monitoreo de pozos</div><h4>Pozo agrícola San Ignacio, Retiro</h4></div>'
)

# Replace La Tercera in index.html
content = content.replace(
    '<div class="media ratio-4-3"><img src="Recursos/Proyectos/proyecto-5.webp" alt="Canal interno La Tercera" class="media-img" loading="lazy"><span class="tag">Monitoreo</span></div>',
    '<div class="media ratio-4-3"><img src="Recursos/Proyectos/Pozo en sector San Ign, telemetría.webp" alt="Monitoreo de pozo" class="media-img" loading="lazy"><span class="tag">Monitoreo</span></div>'
)
content = content.replace(
    '<div class="body"><div class="cat">Monitoreo</div><h4>Canal interno en sector La Tercera, Longaví</h4></div>',
    '<div class="body"><div class="cat">Monitoreo de pozos</div><h4>Empresa Porvenir, sector La Tercera, Longaví</h4></div>'
)

# Fix encoding issue just in case Longaví was mangled in read
content = content.replace('Longav', 'Longaví')
content = content.replace('Construccin', 'Construcción')
content = content.replace('Mesamvida', 'Mesamávida')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html projects")
