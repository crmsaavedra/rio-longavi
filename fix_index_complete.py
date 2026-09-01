import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# 1. Update San Ignacio
idx = idx.replace(
    '<div class="media ratio-4-3"><img src="Recursos/Proyectos/proyecto-4.webp" alt="Canal interno San Ignacio" class="media-img" loading="lazy"><span class="tag">Monitoreo</span></div>',
    '<div class="media ratio-4-3"><img src="Recursos/Proyectos/proyecto-pozo.jpeg" alt="Canal interno San Ignacio" class="media-img" loading="lazy"><span class="tag">Monitoreo</span></div>'
)
idx = idx.replace(
    '<div class="body"><div class="cat">Monitoreo</div><h4>Canal interno en sector San Ignacio, Retiro</h4></div>',
    '<div class="body"><div class="cat">Monitoreo de pozos</div><h4>Pozo agrícola San Ignacio, Retiro</h4></div>'
)

# 2. Update La Tercera
idx = idx.replace(
    '<div class="media ratio-4-3"><img src="Recursos/Proyectos/proyecto-5.webp" alt="Canal interno La Tercera" class="media-img" loading="lazy"><span class="tag">Monitoreo</span></div>',
    '<div class="media ratio-4-3"><img src="Recursos/Proyectos/Pozo en sector San Ign, telemetría.webp" alt="Monitoreo de pozo" class="media-img" loading="lazy"><span class="tag">Monitoreo</span></div>'
)
idx = idx.replace(
    '<div class="body"><div class="cat">Monitoreo</div><h4>Canal interno en sector La Tercera, Longaví</h4></div>',
    '<div class="body"><div class="cat">Monitoreo de pozos</div><h4>Empresa Porvenir, sector La Tercera, Longaví</h4></div>'
)

# 3. Convert <div class="project-card"> to <a class="project-card">
def replace_idx_card(match):
    full_card = match.group(0)
    if 'Monitoreo' in full_card:
        return full_card.replace('<div class="project-card">', '<a class="project-card" href="telemetria.html" target="_blank" style="display:block;color:inherit;text-decoration:none;">').replace('</div>\n        </div>', '</div>\n        </a>')
    elif 'Construcci' in full_card:
        return full_card.replace('<div class="project-card">', '<a class="project-card" href="construccion.html" target="_blank" style="display:block;color:inherit;text-decoration:none;">').replace('</div>\n        </div>', '</div>\n        </a>')
    return full_card

idx = re.sub(r'<div class="project-card">.*?</div>\s*</div>', replace_idx_card, idx, flags=re.DOTALL)

# 4. Cache bust CSS
idx = idx.replace('css/style.css"', 'css/style.css?v=5"')
idx = idx.replace('css/style.css?v=2"', 'css/style.css?v=5"')
idx = idx.replace('css/style.css?v=3"', 'css/style.css?v=5"')
idx = idx.replace('css/style.css?v=4"', 'css/style.css?v=5"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

print("index.html fully updated!")
