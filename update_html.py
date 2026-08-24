import re
import os

def load_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def save_file(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

# index.html
text = load_file('index.html')
text = text.replace('Ingeniería hídrica · Cuenca del Maule', 'Río Longaví · Maule, Chile')
text = text.replace('Innovación y <span class="accent">transparencia</span><br>en la gestión del agua', 'Innovación y <span class="accent">Exactitud</span><br>en la Gestión del Agua')
text = text.replace('Diseñamos, construimos y monitoreamos la infraestructura hídrica que necesitan las juntas de vigilancia y comunidades de regantes del Río Longaví.', 'Soluciones integrales en telemetría, ingeniería y administración para el desarrollo agrícola y comunitario.')
text = text.replace('Ver servicios', 'Ver Servicios')
text = text.replace('<span><b>500 km</b> de canales monitoreados</span>', '<span><b>30 km</b> de canales</span>')
text = text.replace('<span><b>34</b> proyectos ejecutados</span>', '<span><b>monitoreo</b> 24/7</span>')
text = text.replace('<span><b>15</b> juntas de vigilancia asesoradas</span>', '<span><b>21</b> años de experiencia</span>')
text = text.replace('<span><b>30%</b> reducción en pérdidas de agua</span>', '<span><b>6</b> comunidades administradas</span>')

text = text.replace('<div class="eyebrow">Nuestro sello</div>', '<div class="eyebrow">Quiénes Somos</div>')
text = text.replace('Ingeniería con compromiso social', 'Ingeniería con Compromiso Social')
text = text.replace('Somos una empresa multidisciplinaria del Maule con más de una década de experiencia acompañando a canalistas, regantes e instituciones en la modernización de su gestión hídrica.', 'Somos una empresa dedicada a optimizar el recurso hídrico a través de tecnología avanzada y gestión administrativa eficiente. Con más de 20 años de experiencia, unimos la ingeniería con el compromiso social agrícola.')

text = text.replace('Orientación social', '🎯 Nuestra Misión')
text = text.replace('Trabajo cercano con comunidades y organizaciones de usuarios de agua.', 'Contribuir a mejorar la calidad de vida de los asociados a través de la profesionalización en el uso de los recursos económicos, humanos e hídricos.')

text = text.replace('Orientación técnica', '🔭 Nuestra Visión')
text = text.replace('Soluciones de ingeniería rigurosas, medibles y sostenibles en el tiempo.', 'Ser la empresa consultora y constructora estable, confiable, cercana y reconocida por clientes y regantes asociados para la ejecución de proyectos de riego, como infraestructura hidráulica y monitoreo de caudales.')

text = text.replace('<div class="eyebrow">Lo que hacemos</div>', '<div class="eyebrow">Nuestros Servicios</div>')
text = text.replace('<h2 class="section-title">Soluciones integrales para el agua</h2>', '<h2 class="section-title">Soluciones Integrales para el Agua</h2>')
text = text.replace('Un ecosistema completo de servicios, desde tecnología de monitoreo hasta asesoría legal y capacitación comunitaria.', 'Ofrecemos un ecosistema completo de servicios para la gestión eficiente del recurso hídrico.')

text = text.replace('<h4>Telemetría</h4>', '<h4>📡 Servicio 03: Telemetría</h4>')
text = text.replace('Sensores ultrasónicos y transmisión de datos GPRS/satelital en tiempo real.', 'Instalación de sensores ultrasónicos y transmisión de datos vía GPRS/Satélite para monitoreo continuo de caudales y niveles.')

text = text.replace('<h4>Construcción</h4>', '<h4>🏗️ Servicio 02: Construcción</h4>')
text = text.replace('Obras civiles, revestimiento de canales y marcos de partida.', 'Obras civiles: revestimiento de canales, entubamiento, canal abovedado y marcos partidores. Infraestructura hidráulica de alta calidad para recuperar pérdidas de agua.')

text = text.replace('<h4>Consultoría</h4>', '<h4>⚖️ Servicio 04: Consultoría</h4>')
text = text.replace('Asesoría legal y técnica para juntas de vigilancia y comunidades.', 'Asesoría legal y técnica para juntas de vigilancia, comunidades de usuarios de aguas. Cumplimiento normativo y gestión documental. Estudios y elaboración de riego.')

text = text.replace('<h4>Proyectos</h4>', '<h4>📐 Servicio 01: Proyectos</h4>')
text = text.replace('Ingeniería de riego y manejo de recursos hídricos de principio a fin.', 'Diseño de ingeniería hidráulica a medida. Soluciones de riego eficientes y sostenibles adaptadas a cada territorio.')

save_file('index.html', text)
print("Updated index.html")
