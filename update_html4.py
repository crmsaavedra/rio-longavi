import os

def load_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def save_file(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

text = load_file('sarcom.html')
text = text.replace('Sistema de alerta y registro de canales', 'Sistema que mide derechos de acciones de aguas con tecnología de vanguardia.')
text = text.replace('Tecnología de monitoreo hídrico pensada para el Río Longaví y sus comunidades de regantes.', 'Tecnología de monitoreo hídrico.')
text = text.replace('Transmisión GPRS/satélite', '🛰️ Transmisión')
text = text.replace('Conectividad robusta incluso en zonas remotas de la cuenca del Río Longaví.', 'Conectividad robusta.')
text = text.replace('Sensores ultrasónicos', '📏 Sensores Ultrasónicos')
text = text.replace('Medición de caudal sin contacto con el agua, alta durabilidad y precisión.', 'Medición de caudal sin contacto con el agua, alta durabilidad y precisión.')
text = text.replace('Actualización continua', '🔄 Actualización Continua')
text = text.replace('Datos actualizados cada 30 minutos con registro histórico accesible en todo momento.', 'Datos actualizados cada 30 minutos con registro histórico accesible en todo momento.')
text = text.replace('Energía solar', '⚡ Energía Solar')
text = text.replace('Estaciones alimentadas con paneles solares para operación autónoma y sostenible.', 'Estaciones alimentadas con paneles solares para operación autónoma y sostenible.')
text = text.replace('<div class="eyebrow">Descubre</div>', '<div class="eyebrow">Tiempo Real</div>')
text = text.replace('<h2 class="section-title">Sobre SARCOM</h2>', '<h2 class="section-title">¿Qué es SARCOM?</h2>')
text = text.replace('<div class="eyebrow">¿Qué es SARCOM?</div>', '<div class="eyebrow">Sistema Activo</div>')
save_file('sarcom.html', text)
print("Updated sarcom.html")
