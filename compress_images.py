import os
import glob
from PIL import Image
import subprocess
import re

base_dir = 'Recursos/Fotos_Proyectos'
html_files = glob.glob('*.html')

# 1. Convert images
converted_files = {} # mapping old relative path to new relative path (not URL encoded)
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            old_path = os.path.join(root, file)
            # Create new webp name
            name, ext = os.path.splitext(file)
            new_file = name + '.webp'
            new_path = os.path.join(root, new_file)
            
            try:
                print(f"Processing {old_path}...")
                with Image.open(old_path) as img:
                    # Convert to RGB if needed
                    if img.mode in ('RGBA', 'P'):
                        img = img.convert('RGB')
                        
                    # Resize if too large
                    max_size = 1920
                    if img.width > max_size or img.height > max_size:
                        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                        
                    # Save as webp
                    img.save(new_path, 'webp', quality=80)
                    
                # Add to git
                subprocess.run(['git', 'add', new_path], check=True)
                # Remove old file from git
                subprocess.run(['git', 'rm', '-f', old_path], check=True)
                
                # Keep track for HTML replacement
                # We need to replace the URL encoded versions in the HTML
                old_rel = old_path.replace('\\', '/')
                new_rel = new_path.replace('\\', '/')
                converted_files[old_rel] = new_rel
                print(f"Converted {old_rel} -> {new_rel}")
            except Exception as e:
                print(f"Failed to process {old_path}: {e}")

# 2. Update HTML files
# We need to URL encode the paths because the HTML uses URL encoding for spaces and accents
import urllib.parse

print("Updating HTML files...")
for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    for old_rel, new_rel in converted_files.items():
        # URL encode both
        old_url = urllib.parse.quote(old_rel)
        new_url = urllib.parse.quote(new_rel)
        
        # Replace
        html = html.replace(old_url, new_url)
        # Also replace unencoded just in case
        html = html.replace(old_rel, new_rel)
        
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("All done!")
