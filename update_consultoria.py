import re

file = 'consultoria.html'
with open(file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the carousel track
track_pattern = r'<div class="carousel-track">.*?</div>'
new_track = '''<div class="carousel-track">
          <img src="Recursos/Consultoria.webp" alt="Vista 1 del proyecto" class="media-img" loading="lazy">
        </div>'''
html = re.sub(track_pattern, new_track, html, flags=re.DOTALL)

# Replace the dots
dots_pattern = r'<div class="dots">.*?</div>'
new_dots = '<div class="dots"><span class="active" data-slide="0"></span></div>'
html = re.sub(dots_pattern, new_dots, html, flags=re.DOTALL)

with open(file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated consultoria.html")
