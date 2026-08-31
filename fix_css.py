import os

css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Try to remove the line with ?? or the rocket
lines = css.split('\n')
new_lines = []
for line in lines:
    if '.floating-badge::before' in line:
        continue
    new_lines.append(line)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Fixed CSS.")
