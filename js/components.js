/* ============================================================
   components.js — Injects shared Navbar & Footer into every page
   ============================================================ */

'use strict';

/* ---- SVG Logo Icon ---- */
const logoSVG = `
<svg viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M18 4C10.268 4 4 10.268 4 18s6.268 14 14 14 14-6.268 14-14S25.732 4 18 4z" fill="none"/>
  <path d="M6 22 Q10 14 14 18 Q18 22 22 14 Q26 6 30 14" 
        stroke="#00CFE8" stroke-width="2.5" stroke-linecap="round" fill="none"/>
  <path d="M6 26 Q10 18 14 22 Q18 26 22 18 Q26 10 30 18" 
        stroke="#0077B6" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.7"/>
</svg>`;

/* ---- Navbar HTML ---- */
const navbarHTML = `
<nav class="navbar" role="navigation" aria-label="Navegación principal">
  <div class="container navbar__inner">

    <!-- Logo -->
    <a href="index.html" class="navbar__logo" aria-label="Río Longaví - Inicio">
      <div class="navbar__logo-icon">${logoSVG}</div>
      <div class="navbar__logo-text">
        <span class="navbar__logo-main">Río Longaví</span>
        <span class="navbar__logo-sub">Gestión del Agua</span>
      </div>
    </a>

    <!-- Desktop links -->
    <ul class="navbar__menu" role="list">
      <li><a href="index.html"    class="navbar__link" aria-label="Inicio">Inicio</a></li>
      <li><a href="nosotros.html" class="navbar__link" aria-label="Nosotros">Nosotros</a></li>
      <li><a href="sarcom.html"   class="navbar__link" aria-label="SARCOM">SARCOM</a></li>
      <li><a href="servicios.html" class="navbar__link" aria-label="Servicios">Servicios</a></li>
      <li><a href="proyectos.html" class="navbar__link" aria-label="Proyectos">Proyectos</a></li>
      <li><a href="clientes.html"  class="navbar__link" aria-label="Clientes">Clientes</a></li>
      <li><a href="contacto.html"  class="navbar__link" aria-label="Contacto">Contacto</a></li>
    </ul>

    <!-- Actions -->
    <div class="navbar__actions">
      <button class="theme-toggle" data-theme-toggle aria-label="Cambiar tema">
        <span data-theme-icon>🌙</span>
      </button>
      <button class="navbar__hamburger" aria-label="Abrir menú" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</nav>

<!-- Mobile Menu Overlay -->
<div class="navbar__mobile-menu" role="dialog" aria-label="Menú móvil">
  <a href="index.html"     class="navbar__mobile-link">Inicio</a>
  <a href="nosotros.html"  class="navbar__mobile-link">Nosotros</a>
  <a href="sarcom.html"    class="navbar__mobile-link">SARCOM</a>
  <a href="servicios.html" class="navbar__mobile-link">Servicios</a>
  <a href="proyectos.html" class="navbar__mobile-link">Proyectos</a>
  <a href="clientes.html"  class="navbar__mobile-link">Clientes</a>
  <a href="contacto.html"  class="navbar__mobile-link">Contacto</a>
</div>`;

/* ---- Footer HTML ---- */
const footerHTML = `
<footer class="footer" role="contentinfo">
  <div class="container">
    <div class="footer__grid">

      <!-- Brand -->
      <div class="footer__brand">
        <div class="footer__logo">
          <div style="width:32px;height:32px">${logoSVG}</div>
          <span class="footer__logo-text">Río Longaví</span>
        </div>
        <p class="footer__tagline">
          Innovación y transparencia en la gestión del agua. 
          Soluciones integrales para el desarrollo agrícola y comunitario en el Maule.
        </p>
      </div>

      <!-- Nav links -->
      <div>
        <p class="footer__col-title">Páginas</p>
        <ul class="footer__links" role="list">
          <li><a href="index.html"     class="footer__link">→ Inicio</a></li>
          <li><a href="nosotros.html"  class="footer__link">→ Nosotros</a></li>
          <li><a href="sarcom.html"    class="footer__link">→ SARCOM</a></li>
          <li><a href="servicios.html" class="footer__link">→ Servicios</a></li>
          <li><a href="proyectos.html" class="footer__link">→ Proyectos</a></li>
          <li><a href="clientes.html"  class="footer__link">→ Clientes</a></li>
        </ul>
      </div>

      <!-- Services -->
      <div>
        <p class="footer__col-title">Servicios</p>
        <ul class="footer__links" role="list">
          <li><a href="servicios.html" class="footer__link">→ Telemetría</a></li>
          <li><a href="servicios.html" class="footer__link">→ Construcción</a></li>
          <li><a href="servicios.html" class="footer__link">→ Consultoría</a></li>
          <li><a href="servicios.html" class="footer__link">→ Proyectos</a></li>
          <li><a href="servicios.html" class="footer__link">→ Comunidad</a></li>
        </ul>
      </div>

      <!-- Contact -->
      <div>
        <p class="footer__col-title">Contacto</p>
        <div class="footer__contact-item">
          <span class="footer__contact-icon">✉️</span>
          <span class="footer__contact-text">contacto@riolongavi.cl</span>
        </div>
        <div class="footer__contact-item">
          <span class="footer__contact-icon">📱</span>
          <span class="footer__contact-text">+56 9 XXXX XXXX<br>WhatsApp disponible</span>
        </div>
        <div class="footer__contact-item">
          <span class="footer__contact-icon">📍</span>
          <span class="footer__contact-text">Región del Maule, Chile</span>
        </div>
        <div class="footer__contact-item">
          <span class="footer__contact-icon">🕐</span>
          <span class="footer__contact-text">Lun–Vie: 8:30–18:00 hrs</span>
        </div>
      </div>
    </div>

    <!-- Bottom bar -->
    <div class="footer__bottom">
      <p class="footer__copy">© 2025 Río Longaví. Todos los derechos reservados.</p>
      <div class="footer__social">
        <a href="#" class="footer__social-link" aria-label="Facebook">f</a>
        <a href="#" class="footer__social-link" aria-label="LinkedIn">in</a>
        <a href="#" class="footer__social-link" aria-label="Instagram">ig</a>
      </div>
    </div>
  </div>
</footer>

<!-- Back to Top -->
<button class="back-to-top" aria-label="Volver arriba">↑</button>`;

/* ---- Inject into DOM ---- */
document.addEventListener('DOMContentLoaded', () => {
  // Navbar
  const navPlaceholder = document.getElementById('navbar-placeholder');
  if (navPlaceholder) {
    navPlaceholder.outerHTML = navbarHTML;
  }

  // Footer
  const footerPlaceholder = document.getElementById('footer-placeholder');
  if (footerPlaceholder) {
    footerPlaceholder.outerHTML = footerHTML;
  }
});
