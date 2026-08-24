import os

def load_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def save_file(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

# nosotros.html
text = load_file('nosotros.html')
text = text.replace('Nuestra historia', 'Quiénes Somos')
text = text.replace('Comprometidos con el agua y las personas', 'Comprometidos con el Agua y las Personas')
text = text.replace('Somos una empresa multidisciplinaria del Maule, con años de experiencia acompañando a comunidades de regantes y juntas de vigilancia. Combinamos ingeniería, tecnología y compromiso social para hacer del agua un recurso gestionado con transparencia.', 'Somos una empresa dedicada a optimizar el recurso hídrico a través de tecnología avanzada y gestión administrativa eficiente. Con años de experiencia en el Maule, unimos la ingeniería con el compromiso social, siendo aliados estratégicos de regantes, comunidades y juntas de vigilancia en la cuenca del Río Longaví.')
text = text.replace('Ser una empresa que contribuye a mejorar la calidad de vida de sus asociados, a través de la profesionalización y la optimización en el uso de los recursos hídricos.', 'Contribuir a mejorar la calidad de vida de los asociados a través de la profesionalización en el uso de los recursos económicos, humanos e hídricos.')
text = text.replace('Ser una empresa consultora y constructora reconocida, confiable y con presencia permanente por sus clientes y regantes asociados al Río Longaví por su nivel de materialización de sus proyectos, orientación al desarrollo territorial y a las personas.', 'Ser la empresa consultora y constructora estable, confiable, cercana y reconocida por clientes y regantes asociados para la ejecución de proyectos de riego, como infraestructura hidráulica y monitoreo de caudales.')
text = text.replace('Horizonte', 'Resumen Ejecutivo')
text = text.replace('Nuestra visión de largo plazo', 'Nuestra Visión de Largo Plazo')
text = text.replace('Ser una empresa comprometida a nivel regional, nacional e internacional como una compañía que apunta al desarrollo de servicios de valor asociado al buen uso de los recursos hídricos, productivos, económicamente rentables y transversales al desarrollo de la geografía e influencia del Río Longaví.', 'Ser una empresa reconocida regional, nacional e internacionalmente, como una compañía que contribuye a mejorar la calidad de vida de sus asociados por medio del desarrollo de servicios de alta calidad y valor agregado, generados a partir de la optimización del buen uso de los recursos hídricos, humanos y productivos.')
text = text.replace('Servicio confiable', '01')
text = text.replace('Proveer a la compañía una cultura de servicio confiable para la administración, manejo y operación de los recursos hídricos superficiales.', 'Posicionar la compañía ante sus clientes como un aliado estratégico para la administración, manejo y operación de los recursos hídricos superficiales y subterráneos.')
text = text.replace('Infraestructura hídrica', '02')
text = text.replace('Posicionar a la compañía como una constructora confiable en la construcción de las obras hidráulicas, garantizando su durabilidad.', 'Posicionar la compañía ante sus clientes como un aliado estratégico para la construcción de las obras hidráulicas, que permitan recuperar las pérdidas de agua.')
text = text.replace('Consultoría especializada', '03')
text = text.replace('Consolidar el financiamiento de la compañía con el fin de mantener los programas de servicios propuestos a clientes y asociados.', 'Consolidar financieramente la compañía, con el fin de desarrollar los programas de servicios propuestos para nuestros clientes y asociados.')
save_file('nosotros.html', text)
print("Updated nosotros.html")
