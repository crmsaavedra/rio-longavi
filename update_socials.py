import glob
import os
import re

html_files = glob.glob('*.html')

fb_link = 'https://www.facebook.com/riolongavi?locale=es_LA'
ln_link = 'https://www.linkedin.com/in/r%C3%ADo-longav%C3%AD-chile-b4325b403?utm_source=share_via&utm_content=profile&utm_medium=member_android'
ig_link = 'https://www.instagram.com/riolongavi'

for file in html_files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # We only want to replace the href="#" if it's next to the aria-label for socials.
    content = content.replace('href="#" aria-label="Facebook"', f'href="{fb_link}" target="_blank" aria-label="Facebook"')
    content = content.replace('href="#" aria-label="LinkedIn"', f'href="{ln_link}" target="_blank" aria-label="LinkedIn"')
    content = content.replace('href="#" aria-label="Instagram"', f'href="{ig_link}" target="_blank" aria-label="Instagram"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated social links.")
