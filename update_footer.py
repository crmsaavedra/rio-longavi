import os
import glob

def load_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def save_file(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

files = ['index.html', 'nosotros.html', 'sarcom.html', 'servicios.html', 'proyectos.html', 'clientes.html', 'contacto.html']

for file in files:
    text = load_file(file)
    text = text.replace('Innovación y transparencia en la gestión del agua. Soluciones integrales para el desarrollo agrícola y comunitario en el Maule.', 'Innovación y transparencia en la gestión del agua. Soluciones integrales para el desarrollo agrícola.')
    text = text.replace('+569 7217 4331', '+56 9 72174351')
    text = text.replace('Dieciocho 560, Parral', 'Región del Maule, Chile')
    save_file(file, text)
    print(f"Updated footer in {file}")

