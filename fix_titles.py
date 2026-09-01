import os
import glob
import re

for filepath in glob.glob('*.html'):
    # Let's read with utf-8 first.
    # If it fails, read with iso-8859-1 (ansi).
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='iso-8859-1') as f:
            content = f.read()

    # Replace "Río Longaví" with "Rio Longavi" in title tag specifically
    # And we'll just remove all accents from the <title> tag.
    def remove_accents_title(match):
        title = match.group(0)
        title = title.replace('Río Longaví', 'Rio Longavi')
        title = title.replace('Ro Longav', 'Rio Longavi') # in case of ansi corruption
        title = title.replace('Ro Longav', 'Rio Longavi') # in case of empty stripping
        title = title.replace('Innovación', 'Innovacion')
        title = title.replace('gestión', 'gestion')
        title = title.replace('Construcción', 'Construccion')
        title = title.replace('Consultoría', 'Consultoria')
        title = title.replace('Telemetría', 'Telemetria')
        title = title.replace('Tecnología', 'Tecnologia')
        title = title.replace('tecnología', 'tecnologia')
        title = title.replace('agrícola', 'agricola')
        return title

    content = re.sub(r'<title>.*?</title>', remove_accents_title, content, flags=re.DOTALL)
    
    # Check floating badge in servicios.html
    if 'servicios.html' in filepath:
        if 'floating-badge' not in content:
            content = content.replace('</body>', '<div class="floating-badge">Competitivo en el mercado</div>\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Titles cleaned and badge added to servicios.html")
