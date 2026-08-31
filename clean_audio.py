import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace from <audio id="entrevista-audio" up to the </div></div></div></section> block
content = re.sub(
    r'\s*<audio id="entrevista-audio"[\s\S]*?<div class="audio-controls">[\s\S]*?</div>\s*</div>\s*</div>\s*</section>',
    '\n  </div>\n</section>',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Audio remnant removed.")
