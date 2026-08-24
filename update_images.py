import os
import re

# --- 1. nosotros.html ---
with open('nosotros.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace first occurrence of Compromiso.webp with Sobre nosotros.webp
content = content.replace('Recursos/Compromiso.webp', 'Recursos/Sobre nosotros.webp', 1)
# Replace second occurrence of Compromiso.webp with Misin.webp
content = content.replace('Recursos/Compromiso.webp', 'Recursos/Misión.webp', 1)

with open('nosotros.html', 'w', encoding='utf-8') as f:
    f.write(content)

# --- 2. proyectos.html ---
with open('proyectos.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change image for "Canal interno en sector San Ignacio, Retiro" (proyecto-4.webp) to San Ignacio, telemetra pozo automtico.webp
content = content.replace('Recursos/Proyectos/proyecto-4.webp', 'Recursos/Proyectos/San Ignacio, telemetría pozo automático.webp')

# Add 3 new projects under "Construccin"
# 1. Canal derivado Castro la Puntilla, Longav (la puntilla 1.jpeg) -> wait, maybe .webp exists? I'll use the .jpeg for now
# 2. Canal vecinal sector Vega Ancoa, Linares (la puntilla 2.jpeg)
# 3. Canal El Carmen Unin, Piguchn, Retiro (la puntilla 3.jpeg)

new_projects = '''
      <a class="project-card" data-cat="construccion" href="ficha-proyecto.html">
        <div class="media ratio-4-3"><img src="Recursos/la puntilla 1.jpeg" alt="Canal derivado Castro la Puntilla" class="media-img" loading="lazy"><span class="tag">Construcción</span></div>
        <div class="body"><div class="cat">Construcción</div><h4>Canal derivado Castro la Puntilla, Longaví</h4></div>
      </a>
      <a class="project-card" data-cat="construccion" href="ficha-proyecto.html">
        <div class="media ratio-4-3"><img src="Recursos/la puntilla 2.jpeg" alt="Canal vecinal sector Vega Ancoa" class="media-img" loading="lazy"><span class="tag">Construcción</span></div>
        <div class="body"><div class="cat">Construcción</div><h4>Canal vecinal sector Vega Ancoa, Linares</h4></div>
      </a>
      <a class="project-card" data-cat="construccion" href="ficha-proyecto.html">
        <div class="media ratio-4-3"><img src="Recursos/la puntilla 3.jpeg" alt="Canal El Carmen Unión" class="media-img" loading="lazy"><span class="tag">Construcción</span></div>
        <div class="body"><div class="cat">Construcción</div><h4>Canal El Carmen Unión, Piguchén, Retiro</h4></div>
      </a>
'''

# Find the end of the project grid and insert the new projects
content = content.replace('    </div>\n  </div>', new_projects + '    </div>\n  </div>')

with open('proyectos.html', 'w', encoding='utf-8') as f:
    f.write(content)

# --- 3. style.css (fix avatar cutoff) ---
with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write('\n.avatar img { object-position: top; }\n')

print("Images and projects updated.")
