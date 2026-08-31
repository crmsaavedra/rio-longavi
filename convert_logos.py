from PIL import Image
import os

files = ['Recursos/Logos clientes/cliente-achibueno.png', 'Recursos/Logos clientes/cliente-sitma.png']
for f in files:
    try:
        img = Image.open(f)
        out = f.replace('.png', '.webp')
        img.save(out, 'WEBP', quality=85)
        os.remove(f)
        print(f"Converted {f} to webp")
    except Exception as e:
        print(f"Error {f}: {e}")
