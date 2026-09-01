import re
import os

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    idx = f.read()

def replace_idx_card(match):
    full_card = match.group(0)
    if 'Monitoreo' in full_card:
        return full_card.replace('<div class="project-card">', '<a class="project-card" href="telemetria.html" target="_blank" style="display:block;color:inherit;text-decoration:none;">').replace('</div>\n        </div>', '</div>\n        </a>')
    elif 'Construcc' in full_card:
        return full_card.replace('<div class="project-card">', '<a class="project-card" href="construccion.html" target="_blank" style="display:block;color:inherit;text-decoration:none;">').replace('</div>\n        </div>', '</div>\n        </a>')
    return full_card

idx = re.sub(r'<div class="project-card">.*?</div>\s*</div>', replace_idx_card, idx, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

print("Updated index.html securely")
