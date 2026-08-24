import os

def load_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def save_file(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

text = load_file('index.html')

# Index SARCOM teaser
text = text.replace('SARCOM teaser', 'Plataforma de Telemetría')
text = text.replace('Sistema de alerta y registro de canales', '¿Qué es SARCOM?')
text = text.replace('Tecnología de monitoreo hídrico pensada para el Río Longaví y sus comunidades de regantes.', 'Sistema que mide derechos de aprovechamientos de agua con tecnología de vanguardia<br>Control total de tus recursos hídricos.')
text = text.replace('Transmisión GPRS/satélite', 'Control Total')
text = text.replace('Conectividad robusta en zonas remotas de la cuenca.', 'Monitoreo de caudales 24/7 con acceso en tiempo real desde cualquier dispositivo.')
text = text.replace('Sensores ultrasónicos', 'Normativa')
text = text.replace('Medición de caudal sin contacto, precisa y duradera.', 'Cumplimiento del Decreto 53 y Resolución 1238 de la Dirección General de Aguas.')
text = text.replace('Actualización continua', 'Hardware robusto')
text = text.replace('Datos históricos accesibles cada 30 minutos.', 'Notificaciones inmediatas ante variaciones críticas en caudales y niveles freáticos.')
text = text.replace('Descubre SARCOM', 'Ver datos en tiempo real')

# Index - Administración de Canales
text = text.replace('Operación continua', 'Gestión Integral')
text = text.replace('Distribución y turnos', '💰 Gestión Contable y Financiera')
text = text.replace('Programación y control del reparto de agua entre usuarios.', 'Manejo transparente de cuotas y presupuestos anuales con rendición de cuentas detallada.')
text = text.replace('Monitoreo permanente', '⚙️ Gestión Operativa')
text = text.replace('Supervisión remota de niveles, caudales y estado de obras.', 'Coordinación de celadores, limpieza de canales y mantenimiento preventivo programado.')
text = text.replace('Mantención de infraestructura', '📋 Gestión Administrativa')
text = text.replace('Cuidado preventivo y correctivo de canales y compuertas.', 'Elaboración de actas y cumplimiento legal de normativas vigentes.')
text = text.replace('<p class="section-sub">Gestión operativa continua de canales y sistemas de distribución.</p>', '<p class="section-sub">Gestión completa, transparente y eficiente de sus recursos hídricos.</p>')

# Index - Proyectos Destacados
text = text.replace('Cada proyecto representa un paso hacia la gestión eficiente y transparente del agua en el Maule.', 'Más de 30 km de construcción de canales y una reducción significativa en pérdidas de agua.')

save_file('index.html', text)
print("Updated index.html additional parts")
