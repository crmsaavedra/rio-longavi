import os

def load_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def save_file(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

# ====== servicios.html ======
text = load_file('servicios.html')
text = text.replace('Lo que hacemos', 'Lo Que Hacemos')
text = text.replace('Soluciones integrales para la gestión del agua', 'Soluciones Integrales para la Gestión del Agua')
text = text.replace('Ofrecemos un ecosistema completo de servicios diseñados para cubrir todas las necesidades de gestión hídrica: desde la instalación de tecnología de punta hasta la asesoría legal y la capacitación comunitaria.', 'Ofrecemos un ecosistema completo de servicios diseñados para cubrir todas las necesidades de gestión hídrica: desde la instalación de tecnología de punta, asesoría legal y ejecución de obras civiles.')

text = text.replace('Servicio 01', '📡 Servicio 01')
text = text.replace('Instalación de sensores ultrasónicos y transmisión de datos GPRS/satelital. Nuestro sistema de telemetría permite el monitoreo continuo y remoto de caudales, niveles freáticos y volúmenes de agua sobre toda la red de canales, con visualización en tiempo real en nuestra plataforma SARCOM.', 'Instalación de sensores ultrasónicos y transmisión de datos. Nuestro sistema de telemetría permite el monitoreo continuo y remoto de caudales, niveles freáticos y volúmenes de agua en toda la red de canales. Compatible con nuestra plataforma SARCOM para visualización cada 30 minutos.')
text = text.replace('Sensores ultrasónicos de largo alcance', '✓ Sensores ultrasónicos de largo alcance')
text = text.replace('Transmisión GPRS y satelital', '✓ Transmisión')
text = text.replace('Estaciones con energía solar autónoma', '✓ Estaciones con energía solar autónoma')
text = text.replace('Integración con plataforma SARCOM', '✓ Integración con plataforma SARCOM')
text = text.replace('Cotiza aquí', 'Cotiza Aquí ↗')

text = text.replace('Servicio 02', '🏗️ Servicio 02')
text = text.replace('Obras civiles, revestimiento de canales y marcos de partida. Ejecutamos proyectos de infraestructura hídrica que permiten recuperar las pérdidas de agua, mejorar la eficiencia de conducción y garantizar la durabilidad de las obras en el tiempo.', 'Obras civiles, revestimiento de canales y marcos de partida. Ejecutamos proyectos de infraestructura hidráulica que permiten recuperar las pérdidas de agua, mejorar la eficiencia de conducción y garantizar la durabilidad de las obras en el tiempo.')
text = text.replace('Revestimiento de canales en hormigón', '✓ Revestimiento de canales en hormigón')
text = text.replace('Construcción de marcos de partida', '✓ Construcción de marcos de partida')
text = text.replace('Compuertas automatizadas', '✓ Compuertas automatizadas')
text = text.replace('Supervisión técnica profesional', '✓ Supervisión técnica profesional')

text = text.replace('Servicio 03', '⚖️ Servicio 03')
text = text.replace('Asesoría legal y técnica para juntas de vigilancia y comunidades. Apoyamos a organizaciones de usuarios de agua en la elaboración de estatutos, catastros y en la resolución de conflictos hídricos.', 'Asesoría legal y técnica para juntas de vigilancia y comunidades. Apoyamos a las organizaciones de usuarios de agua en el cumplimiento de sus obligaciones legales, la elaboración de estatutos, catastros de usuarios y la resolución de conflictos hídricos.')
text = text.replace('Asesoría legal hídrica', '✓ Asesoría legal hídrica')
text = text.replace('Catastros de usuarios de agua', '✓ Catastros de usuarios de agua')
text = text.replace('Elaboración de actas y estatutos', '✓ Elaboración de actas y estatutos')
text = text.replace('Resolución de conflictos hídricos', '✓ Mediación de conflictos hídricos')

text = text.replace('Servicio 04', '📐 Servicio 04')
text = text.replace('Diseño de ingeniería hidráulica a medida. Desarrollamos proyectos integrales de riego y manejo de recursos hídricos, desde el estudio de factibilidad y diseño hasta la ejecución y puesta en marcha a nivel predial y territorial.', 'Diseño de ingeniería hidráulica a medida. Desarrollamos proyectos integrales de riego y manejo de recursos hídricos, desde el estudio de factibilidad y diseño hasta la ejecución y puesta en marcha, adaptados a cada realidad territorial.')
text = text.replace('Diseño hidráulico especializado', '✓ Diseño hidráulico especializado')
text = text.replace('Estudios de factibilidad', '✓ Estudios de factibilidad')
text = text.replace('Gestión de permisos y expedientes', '✓ Gestión de permisos y expedientes')
text = text.replace('Supervisión de obra', '✓ Supervisión de obra')

text = text.replace('¿Qué servicio necesitas?', '¿Qué servicio necesitas?')
text = text.replace('Cuéntanos tu proyecto y te prepararemos una propuesta a medida.', 'Cuéntanos tu proyecto y te preparamos una propuesta a medida.')
text = text.replace('Solicitar cotización', 'Contactar ahora')
save_file('servicios.html', text)
print("Updated servicios.html")

# ====== proyectos.html ======
text = load_file('proyectos.html')
text = text.replace('Más de 500 km de canales monitoreados  ·  Reducción del 30% en pérdidas de agua', 'Más de 30 km de canales monitoreados  ·  Reducción del 30% en pérdidas de agua')
text = text.replace('Galería de proyectos', 'Galería de Proyectos')
text = text.replace('Cada proyecto representa un paso hacia la gestión eficiente y transparente del agua en el Maule.', 'Cada proyecto representa un paso hacia la gestión eficiente y transparente del agua en el Maule.')
text = text.replace('¿Tu próximo proyecto?', '¿Tu próximo proyecto?')
text = text.replace('Hagamos algo juntos', 'Hagamos algo juntos')
text = text.replace('Solicitar cotización', 'Solicitar cotización')
save_file('proyectos.html', text)
print("Updated proyectos.html")

# ====== clientes.html ======
text = load_file('clientes.html')
text = text.replace('Quienes confían en nosotros', 'Quienes Confían en Nosotros')
text = text.replace('Trabajamos con las principales juntas de vigilancia, asociaciones de canalistas y comunidades de regantes del Maule y Ñuble.', 'Trabajamos con juntas de vigilancia, asociaciones y comunidades de usuarios de aguas y empresas relacionadas con el rubro.')
text = text.replace('Lo que dicen nuestros clientes', 'Lo Que Dicen Nuestros Clientes')

text = text.replace('Para los regantes es bastante más cómodo, hay una empresa que maneja, sabe y entiende qué se debe hacer con los canales y eso te da tranquilidad y te alivia la carga de estar preocupado.', 'Para los regantes es bastante más cómodo, hay una empresa que maneja, sabe y entiende qué se debe hacer con los canales.')
text = text.replace('Matías Rivera, Canal Villa Rosa - Parral', 'Matías Rivera, Presidente del canal Villa Rosa - Parral.')

text = text.replace('Estamos muy satisfechos, el trabajo y servicio para mí ha sido muy bueno. Les recomiendo 100%, es una empresa seria y grande que conoce el riego.', 'Estamos muy satisfechos, el trabajo y servicio para mí ha sido muy bueno. Les recomiendo, es una empresa seria y grande que conoce el riego.')
text = text.replace('Óscar Sermini, Productor de fardos, Retiro', 'Óscar Sermini; productor de fardos de Retiro')

text = text.replace('Llevamos más de 15 años en los que hemos tenido muy buena experiencia entregando la administración de nuestro canal a la empresa Río Longaví. Administran Canal San Ignacio, Molino y Nogales Membrillo con total transparencia.', 'Llevamos más de 15 años en los que hemos tenido muy buena experiencia entregando la administración de nuestro canal a la empresa Río Longaví, con Canal San Ignacio, Molino y Nogales Membrillo.')
text = text.replace('Emilio Sarah, Empresario agrícola, Retiro - Parral', 'Emilio Sarah; empresario Retiro – Parral.')

text = text.replace('Únete a nuestros clientes', 'Únete a Nuestros Clientes')
text = text.replace('¿Eres la próxima historia de éxito?', '¿Eres la próxima historia de éxito?')
text = text.replace('Trabajemos juntos', 'Trabajemos juntos')
save_file('clientes.html', text)
print("Updated clientes.html")

# ====== contacto.html ======
text = load_file('contacto.html')
text = text.replace('¿Cómo podemos ayudarte?', '¿Cómo Podemos Ayudarte?')
text = text.replace('Cuéntanos sobre tu proyecto o necesidades de gestión hídrica y te prepararemos una propuesta personalizada.', 'Cuéntanos sobre tu proyecto y te prepararemos una propuesta personalizada.')
text = text.replace('Información de contacto', 'Información de Contacto')
text = text.replace('Correo electrónico', '✉️ Correo Electrónico')
text = text.replace('Teléfono / WhatsApp', '📱 Teléfono / WhatsApp')
text = text.replace('Dirección', '📍 Dirección')
text = text.replace('Dieciocho 560, Parral', 'Dieciocho #560; Parral.')
text = text.replace('Horario de atención', '🕐 Horario de Atención')
text = text.replace('Lunes a Viernes', 'Lunes a Viernes')
text = text.replace('9:00 — 17:30 hrs', '9:00 — 17:30 hrs')

text = text.replace('Cotiza con nosotros', 'Cotiza con Nosotros')
text = text.replace('Completa el formulario a continuación y te responderemos en menos de 24 horas hábiles.', 'Completa el formulario y te responderemos en menos de 24 horas hábiles.')

text = text.replace('¿Tienes dudas?', '¿Tienes Dudas?')
text = text.replace('¿Qué zona geográfica cubren sus servicios?', '¿Qué zona geográfica cubren sus servicios?')
text = text.replace('Nuestra área de operación principal es en la Región del Maule y Ñuble. Sin embargo, también atendemos proyectos en otras cuencas y regiones de Chile según disponibilidad y factibilidad técnica.', 'Nuestra área de operación principal es en la Región del Maule y Ñuble. Sin embargo, también atendemos proyectos en otras cuencas, según disponibilidad.')
save_file('contacto.html', text)
print("Updated contacto.html")

