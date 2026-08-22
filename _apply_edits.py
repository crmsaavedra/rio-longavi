import pathlib

f = pathlib.Path(r"c:\Users\crism\Desktop\Proyectos\riolongavi\servicios.html")
c = f.read_text(encoding="utf-8")

# 1. Replace SVG logo with img (both header and footer)
old_svg = '<svg width="30" height="30" viewBox="0 0 30 30" fill="none"><path d="M4 20c4-6 8-6 11-2s7 4 11-2" stroke="#3cc0ea" stroke-width="2" stroke-linecap="round"/><path d="M4 14c4-6 8-6 11-2s7 4 11-2" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/></svg>'
new_img = '<img src="Recursos/logo-blanco.png" alt="Río Longaví" class="logo-img">'
c = c.replace(old_svg, new_img)

# 2. Page hero background
c = c.replace(
    '<div class="page-hero">',
    """<div class="page-hero" style="background-image: linear-gradient(180deg, rgba(7,27,46,.55), rgba(7,27,46,.88)), url('Recursos/Servicios.webp');">"""
)

# 3. Telemetría
c = c.replace(
    '<div class="service-media media ratio-4-3"><span class="tag">Recursos / Telemetria.webp</span></div>',
    '<div class="service-media media ratio-4-3"><img src="Recursos/Telemetria.webp" alt="Servicio de telemetría hídrica" class="media-img" loading="lazy"></div>'
)

# 4. Construcción
c = c.replace(
    '<div class="service-media media ratio-4-3"><span class="tag">Recursos / construcción.webp</span></div>',
    '<div class="service-media media ratio-4-3"><img src="Recursos/construcción.webp" alt="Servicio de construcción hídrica" class="media-img" loading="lazy"></div>'
)

# 5. Consultoría
c = c.replace(
    '<div class="service-media media ratio-4-3"><span class="tag">Recursos / Consultoria.webp</span></div>',
    '<div class="service-media media ratio-4-3"><img src="Recursos/Consultoria.webp" alt="Servicio de consultoría" class="media-img" loading="lazy"></div>'
)

# 6. Proyectos
c = c.replace(
    '<div class="service-media media ratio-4-3"><span class="tag">Recursos / Proyectos.webp</span></div>',
    '<div class="service-media media ratio-4-3"><img src="Recursos/Proyectos.webp" alt="Servicio de proyectos" class="media-img" loading="lazy"></div>'
)

# 7. Comunidad
c = c.replace(
    '<div class="service-media media ratio-4-3"><span class="tag">Recursos / comunidad.webp</span></div>',
    '<div class="service-media media ratio-4-3"><img src="Recursos/comunidad.webp" alt="Servicio comunitario" class="media-img" loading="lazy"></div>'
)

# 8. CTA band
c = c.replace(
    '<div class="cta-band">',
    """<div class="cta-band" style="background-image: linear-gradient(180deg, rgba(7,27,46,.8), rgba(7,27,46,.92)), url('Recursos/Imagen de footer.webp');">"""
)

f.write_text(c, encoding="utf-8")
print("All edits applied successfully.")
