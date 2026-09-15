import os
import glob
from PIL import Image
try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    print("pillow_heif not available. HEIC files might fail.")

folders = {
    'Achibueno': 'proyecto-la-cuarta',
    'La Suiza': 'proyecto-la-suiza',
    'Molino Nogales': 'proyecto-molinos-nogales'
}

base_dir = 'Recursos'
dest_dir = 'Recursos/Proyectos'

def process_image(img_path, dest_name):
    try:
        img = Image.open(img_path)
        # Convert to RGB in case it's RGBA or something
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Resize if too large
        max_size = (1920, 1080)
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        dest_path = os.path.join(dest_dir, dest_name)
        img.save(dest_path, 'WEBP', quality=85)
        print(f"Processed: {img_path} -> {dest_path}")
        return True
    except Exception as e:
        print(f"Error processing {img_path}: {e}")
        return False

# Keep track of generated images for each project to update HTML
project_images = {v: [] for v in folders.values()}

# Always keep the original first image if possible, but let's just replace the whole carousel with the new ones + the old one.
# Actually, the user wants to "sumar más foto" (add more photos). So we append them.

for folder, proj_id in folders.items():
    folder_path = os.path.join(base_dir, folder)
    if not os.path.exists(folder_path):
        continue
        
    idx = 1
    for filename in os.listdir(folder_path):
        ext = filename.lower().split('.')[-1]
        if ext in ['heic', 'jpg', 'jpeg', 'png', 'webp']:
            img_path = os.path.join(folder_path, filename)
            dest_name = f"{proj_id}-extra-{idx}.webp"
            if process_image(img_path, dest_name):
                project_images[proj_id].append(f"Recursos/Proyectos/{dest_name}")
                idx += 1

# Now update the HTML files
import re

for proj_id, imgs in project_images.items():
    if not imgs:
        continue
        
    html_file = f"{proj_id}.html"
    if not os.path.exists(html_file):
        continue
        
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Find the carousel track
    # <div class="carousel-track">
    #   <img src="..." alt="..." ...>
    #   ...
    # </div>
    
    # Let's extract the first image so we don't lose it
    track_pattern = r'<div class="carousel-track">(.*?)</div>'
    match = re.search(track_pattern, html, flags=re.DOTALL)
    if match:
        old_track = match.group(1)
        # Find the first img in the track
        first_img = re.search(r'<img src="([^"]+)"', old_track)
        first_img_src = first_img.group(1) if first_img else None
        
        # Build new track
        new_track = '\n'
        slides = []
        if first_img_src:
            slides.append(first_img_src)
        slides.extend(imgs)
        
        # Remove duplicates if any
        seen = set()
        unique_slides = []
        for s in slides:
            if s not in seen:
                unique_slides.append(s)
                seen.add(s)
        
        for i, src in enumerate(unique_slides):
            new_track += f'          <img src="{src}" alt="Vista {i+1} del proyecto" class="media-img" loading="lazy">\n'
            
        new_html = html[:match.start(1)] + new_track + html[match.end(1):]
        
        # Also need to update the dots
        # <div class="dots"><span class="active" data-slide="0"></span>...</div>
        dots_pattern = r'<div class="dots">(.*?)</div>'
        dots_match = re.search(dots_pattern, new_html, flags=re.DOTALL)
        if dots_match:
            new_dots = ''
            for i in range(len(unique_slides)):
                active = ' class="active"' if i == 0 else ''
                new_dots += f'<span{active} data-slide="{i}"></span>'
            new_html = new_html[:dots_match.start(1)] + new_dots + new_html[dots_match.end(1):]
            
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated HTML for {proj_id}")

