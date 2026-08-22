import os
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
c = re.sub(r'<!-- BANNER JUNTA DE VIGILANCIA -->.*?</section>', '''<!-- BANNER JUNTA DE VIGILANCIA -->
<section class="section" style="padding-top:0;">
  <div class="wrap">
    <a href="https://juntariolongavi.cl" target="_blank" rel="noopener" class="banner-link" style="display:block; width:100%; border-radius:16px; overflow:hidden; transition:transform 0.2s; box-shadow:0 12px 30px rgba(0,0,0,0.15);">
      <img src="Recursos/Banner web.webp" alt="Visítanos en juntariolongavi.cl" style="width:100%; height:auto; display:block;">
    </a>
  </div>
</section>''', c, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
