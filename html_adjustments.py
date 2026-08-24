import os
import re

# --- 1. index.html ---
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Rio Longavi logo in SARCOM section with SARCOM logo
content = re.sub(
    r'<div class="flex center" style="justify-content:center;gap:10px;margin-bottom:18px;">\s*<img src="Recursos/logo-blanco.svg" alt="SARCOM" class="logo-img-sm">\s*<span style=".*?">SARCOM</span>\s*</div>',
    r'<div class="flex center" style="justify-content:center;margin-bottom:18px;">\n        <img src="Recursos/SARCOM/Logotipo principal_Blanco.png" alt="SARCOM" style="height:48px;width:auto;">\n      </div>',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


# --- 2. sarcom.html ---
with open('sarcom.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove 'Más información' links
content = re.sub(r'<a class="more".*?>.*?</a>\s*', '', content)

# Remove the 'Columna de agua' or 'Nivel freático' tile in the grid if they meant that
# Just to be safe, I will change grid-4 to grid-3 and remove the 3rd tile (Columna de agua / Nivel)
content = content.replace('grid-4', 'grid-3')
content = re.sub(r'<div class="metric-tile">\s*<div class="val">150 m</div>\s*<div class="lbl">Columna de agua</div>\s*<div class="flowline"></div>\s*</div>', '', content)

# Remove the entire chart section
content = re.sub(r'<section class="section">\s*<div class="wrap">\s*<div class="chart-wrap" style="max-width:900px;margin:0 auto;">.*?</div>\s*</div>\s*</section>', '', content, flags=re.DOTALL)

with open('sarcom.html', 'w', encoding='utf-8') as f:
    f.write(content)


# --- 3. nosotros.html ---
with open('nosotros.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the black numbers from the objectives
content = re.sub(r'<div class="num">0[123]</div>', '', content)

with open('nosotros.html', 'w', encoding='utf-8') as f:
    f.write(content)


# --- 4. servicios.html ---
with open('servicios.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the black ticks from the check-lists
content = re.sub(r'<svg viewBox="0 0 24 24" fill="none"><path d="M4 12l5 5L20 6" stroke="currentColor" stroke-width="2"/></svg>', '', content)
# It seems they also have a literal 'V ' or 'V' character if the subagent put them?
# Let's check what the subagent put. The subagent extracted "V Asesoría legal" from the text.
content = re.sub(r'<li>\s*V\s*', '<li>', content)

with open('servicios.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML adjustments applied.")
