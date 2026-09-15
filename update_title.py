import os

# Files to update
files = ['proyectos.html', 'proyecto-la-mina.html']

old_title = "Revestimiento Canal unificado La Mina Nogales-Molino"
new_title = "Abovedamiento bocatoma Canal unificado Canales Nogales y Molino"

old_alt = 'alt="Revestimiento Canal unificado La Mina"'
new_alt = 'alt="Abovedamiento bocatoma Canal unificado Canales Nogales y Molino"'

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace titles
    content = content.replace(old_title, new_title)
    
    # Replace alts
    content = content.replace(old_alt, new_alt)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Title updated successfully.")
