import os, re
with open('contacto.html', 'r', encoding='utf-8') as file:
    content = file.read()

content = re.sub(
    r'<div class="map-placeholder mt-16">.*?</div>',
    '<div class="mt-16" style="border-radius: var(--radius-m); overflow: hidden; height: 240px; border: 1px solid var(--line);"><iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?q=Dieciocho%20560%2C%20Parral%2C%20Chile&t=&z=15&ie=UTF8&iwloc=&output=embed"></iframe></div>',
    content,
    flags=re.DOTALL
)

with open('contacto.html', 'w', encoding='utf-8') as file:
    file.write(content)
