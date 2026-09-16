import os
import glob
from PIL import Image
import subprocess
import re
import urllib.parse

# Increase limit to allow the 200MP images
Image.MAX_IMAGE_PIXELS = None

base_dir = 'Recursos/Fotos_Proyectos/San Ignacio'
html_files = glob.glob('*.html')

converted_files = {}
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            old_path = os.path.join(root, file)
            name, ext = os.path.splitext(file)
            new_file = name + '.webp'
            new_path = os.path.join(root, new_file)
            
            try:
                print(f"Processing {old_path}...")
                with Image.open(old_path) as img:
                    if img.mode in ('RGBA', 'P'):
                        img = img.convert('RGB')
                        
                    max_size = 1920
                    if img.width > max_size or img.height > max_size:
                        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                        
                    img.save(new_path, 'webp', quality=80)
                    
                subprocess.run(['git', 'add', new_path], check=True)
                subprocess.run(['git', 'rm', '-f', old_path], check=True)
                
                old_rel = old_path.replace('\\', '/')
                new_rel = new_path.replace('\\', '/')
                converted_files[old_rel] = new_rel
                print(f"Converted {old_rel} -> {new_rel}")
            except Exception as e:
                print(f"Failed to process {old_path}: {e}")

print("Updating HTML files...")
for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    for old_rel, new_rel in converted_files.items():
        old_url = urllib.parse.quote(old_rel)
        new_url = urllib.parse.quote(new_rel)
        html = html.replace(old_url, new_url)
        html = html.replace(old_rel, new_rel)
        
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("All done!")
