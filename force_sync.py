import os

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'a', encoding='utf-8') as file:
            file.write('\n<!-- force sync -->\n')
