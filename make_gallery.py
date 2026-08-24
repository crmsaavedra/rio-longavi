import os
html = '<html><body>'
path = r'C:\Users\crism\Desktop\Proyectos\riolongavi\Recursos\Imagenes varias'
for f in os.listdir(path):
    if f.endswith('.jpeg') or f.endswith('.jpg'):
        html += f'<div style="display:inline-block; margin:10px;"><img src="Recursos/Imagenes varias/{f}" height="200"><br>{f}</div>\n'
html += '</body></html>'
with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(html)
