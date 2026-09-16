import re

with open('proyectos.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The card to replace:
# <a class="project-card" data-cat="telemetria" href="telemetria.html">
#         <div class="media ratio-4-3"><img src="Recursos/Proyectos/proyecto-3.webp" alt="Canal unificado Molinos – Nogales" class="media-img" loading="lazy"><span class="tag">Monitoreo</span></div>
#         <div class="body"><div class="cat">Monitoreo</div><h4>Canal unificado Molinos – Nogales, Santa Delfina, Retiro</h4></div>
# </a>

# Let's replace the link and the image
html = re.sub(
    r'<a class="project-card" data-cat="telemetria" href="telemetria\.html">\s*<div class="media ratio-4-3"><img src="Recursos/Proyectos/proyecto-3\.webp"',
    r'<a class="project-card" data-cat="telemetria" href="proyecto-molinos-nogales.html">\n        <div class="media ratio-4-3"><img src="Recursos/Fotos_Proyectos/Molino%2C%20nogales.webp"',
    html
)

with open('proyectos.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated Molinos in proyectos.html")
