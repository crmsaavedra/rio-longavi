import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try replacing plain style.css with a versioned one
    # If it already has ?v=, we can increment it, but let's just use ?v=2
    if 'css/style.css"' in content:
        content = content.replace('css/style.css"', 'css/style.css?v=2"')
    elif 'css/style.css?v=2"' in content:
        content = content.replace('css/style.css?v=2"', 'css/style.css?v=3"')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated CSS version tags to force cache refresh.")
