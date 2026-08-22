import os, re
for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # In contact cards
        content = content.replace('<p>contacto@riolongavi.cl</p>', '<p><a href="mailto:contacto@riolongavi.cl" style="color: inherit; text-decoration: none; border-bottom: 1px solid rgba(0,0,0,0.2); padding-bottom: 1px;">contacto@riolongavi.cl</a></p>')
        
        # In footers
        content = re.sub(
            r'</svg>contacto@riolongavi\.cl</li>', 
            r'</svg><a href="mailto:contacto@riolongavi.cl" style="color: inherit; text-decoration: none;">contacto@riolongavi.cl</a></li>', 
            content
        )
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
