import re

new_logo_row = '''<div class="logo-row">
      <div class="logo-tile"><img src="Recursos/Logos clientes/cliente-1.webp" alt="Sur Río Ñuble" loading="lazy"></div>
      <div class="logo-tile"><img src="Recursos/Logos clientes/cliente-2.webp" alt="Embalse Digua" loading="lazy"></div>
      <div class="logo-tile"><img src="Recursos/Logos clientes/cliente-3.webp" alt="Junta de Vigilancia Río Longaví" loading="lazy"></div>
      <div class="logo-tile"><img src="Recursos/Logos clientes/cliente-achibueno.webp" alt="Río Achibueno" loading="lazy"></div>
      <div class="logo-tile"><img src="Recursos/Logos clientes/cliente-sitma.webp" alt="SITMA" loading="lazy"></div>
    </div>'''

for file_name in ['index.html', 'clientes.html']:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = re.sub(r'<div class="logo-row">.*?</div>\s*</div>\s*(?:</section>|\n)', new_logo_row + '\n  </div>\n</section>\n', content, flags=re.DOTALL)
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated HTML files.")
