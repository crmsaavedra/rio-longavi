import re

files = ['index.html', 'proyectos.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace target="_blank" specifically in the project-card links
    # Just remove target="_blank" from anywhere it appears in <a class="project-card" ... >
    # Actually, simpler: replace ' target="_blank"' with '' globally, but let's be safe.
    
    # We can just do a regex sub for target="_blank" if it's an a tag
    # Actually, if we just remove ' target="_blank"' from the whole file it might affect other links?
    # Let's check if there are other target="_blank" links (like external social media or whatsapp).
    # It's safer to only remove it from `<a class="project-card" ...>`
    
    def remove_target(match):
        tag = match.group(0)
        return tag.replace(' target="_blank"', '')

    content = re.sub(r'<a[^>]*class="project-card"[^>]*>', remove_target, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Removed target='_blank' from project cards.")
