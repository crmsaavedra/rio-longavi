/* ============================================================
   RÍO LONGAVÍ — Global JavaScript (ES6+ Vanilla)
   ============================================================ */

'use strict';

/* --- Helpers --- */
const qs  = (sel, ctx = document) => ctx.querySelector(sel);
const qsa = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

/* ============================================================
   1. THEME (Light / Dark)
   ============================================================ */
const ThemeManager = (() => {
  const KEY = 'rl-theme';
  const root = document.documentElement;

  const apply = (theme) => {
    root.setAttribute('data-theme', theme);
    localStorage.setItem(KEY, theme);
    // Update toggle icons
    qsa('[data-theme-icon]').forEach(el => {
      el.textContent = theme === 'dark' ? '☀️' : '🌙';
    });
    qsa('[data-theme-label]').forEach(el => {
      el.textContent = theme === 'dark' ? 'Modo Claro' : 'Modo Oscuro';
    });
  };

  const toggle = () => {
    const current = root.getAttribute('data-theme') || 'light';
    apply(current === 'dark' ? 'light' : 'dark');
  };

  const init = () => {
    // Check saved preference, then system preference
    const saved = localStorage.getItem(KEY);
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    apply(saved || (prefersDark ? 'dark' : 'light'));

    // Wire toggles
    qsa('[data-theme-toggle]').forEach(btn => {
      btn.addEventListener('click', toggle);
    });
  };

  return { init, toggle };
})();

/* ============================================================
   2. NAVBAR
   ============================================================ */
const Navbar = (() => {
  const init = () => {
    const navbar = qs('.navbar');
    if (!navbar) return;

    const hamburger = qs('.navbar__hamburger');
    const mobileMenu = qs('.navbar__mobile-menu');

    // Scrolled state
    const onScroll = () => {
      navbar.classList.toggle('navbar--scrolled', window.scrollY > 40);
      BackToTop.toggle(window.scrollY > 400);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // Mobile menu toggle
    if (hamburger && mobileMenu) {
      hamburger.addEventListener('click', () => {
        const open = hamburger.classList.toggle('is-open');
        mobileMenu.classList.toggle('is-open', open);
        document.body.style.overflow = open ? 'hidden' : '';
      });

      // Close on link click
      qsa('.navbar__mobile-link', mobileMenu).forEach(link => {
        link.addEventListener('click', () => {
          hamburger.classList.remove('is-open');
          mobileMenu.classList.remove('is-open');
          document.body.style.overflow = '';
        });
      });
    }

    // Active link
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    qsa('.navbar__link, .navbar__mobile-link').forEach(link => {
      const href = link.getAttribute('href') || '';
      if (href === currentPath || (currentPath === '' && href === 'index.html')) {
        link.classList.add('is-active');
      }
    });
  };

  return { init };
})();

/* ============================================================
   3. SCROLL REVEAL
   ============================================================ */
const ScrollReveal = (() => {
  const init = () => {
    const targets = qsa('.reveal');
    if (!targets.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });

    targets.forEach(el => observer.observe(el));
  };

  return { init };
})();

/* ============================================================
   4. BACK TO TOP
   ============================================================ */
const BackToTop = (() => {
  let btn = null;

  const toggle = (show) => {
    if (btn) btn.classList.toggle('is-visible', show);
  };

  const init = () => {
    btn = qs('.back-to-top');
    if (!btn) return;
    btn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  };

  return { init, toggle };
})();

/* ============================================================
   5. CONTACT FORM
   ============================================================ */
const ContactForm = (() => {
  const init = () => {
    const forms = qsa('.contact-form__element, .js-contact-form');
    forms.forEach(form => {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const toast = qs('.form-toast', form.closest('.contact-form') || form.parentElement);
        if (toast) {
          toast.style.display = 'block';
          setTimeout(() => { toast.style.display = 'none'; }, 4000);
        }
        form.reset();
      });
    });
  };

  return { init };
})();

/* ============================================================
   6. COUNTER ANIMATION (Stats bar)
   ============================================================ */
const CounterAnimation = (() => {
  const animateCounter = (el) => {
    const target = parseFloat(el.getAttribute('data-target'));
    const duration = 1800;
    const start = performance.now();
    const isFloat = target % 1 !== 0;

    const tick = (now) => {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const ease = 1 - Math.pow(1 - progress, 3); // cubic ease-out
      const value = target * ease;
      el.textContent = isFloat ? value.toFixed(1) : Math.floor(value).toLocaleString('es-CL');
      if (progress < 1) requestAnimationFrame(tick);
    };

    requestAnimationFrame(tick);
  };

  const init = () => {
    const counters = qsa('[data-target]');
    if (!counters.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(el => observer.observe(el));
  };

  return { init };
})();

/* ============================================================
   7. SARCOM CHART (Nivel Freático)
   ============================================================ */
const FreaticChart = (() => {
  const draw = (canvas) => {
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const W = canvas.offsetWidth;
    const H = canvas.offsetHeight;
    canvas.width = W;
    canvas.height = H;

    // Data points (simulated)
    const data = [-97, -94, -93, -97, -100, -98, -99, -100];
    const labels = ['12:50', '1:00', '1:10', '1:20', '1:30', '1:40', '1:50', '2:00'];
    const alertLevel = -99;

    const minY = -101, maxY = -92;
    const padX = 44, padY = 20;
    const plotW = W - padX * 2;
    const plotH = H - padY * 2;

    const toX = (i) => padX + (i / (data.length - 1)) * plotW;
    const toY = (v) => padY + ((v - maxY) / (minY - maxY)) * plotH;

    // Background
    ctx.fillStyle = getComputedStyle(document.documentElement).getPropertyValue('--color-bg-alt') || '#F4F8FB';
    ctx.fillRect(0, 0, W, H);

    // Grid lines
    ctx.strokeStyle = 'rgba(100,140,170,0.2)';
    ctx.lineWidth = 1;
    for (let v = -100; v <= -93; v++) {
      const y = toY(v);
      ctx.beginPath();
      ctx.moveTo(padX, y);
      ctx.lineTo(W - padX, y);
      ctx.stroke();

      // Y labels
      ctx.fillStyle = '#7BAFC8';
      ctx.font = '11px Barlow, sans-serif';
      ctx.textAlign = 'right';
      ctx.fillText(v, padX - 6, y + 4);
    }

    // Alert line
    ctx.strokeStyle = '#E74C3C';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([6, 4]);
    const alertY = toY(alertLevel);
    ctx.beginPath();
    ctx.moveTo(padX, alertY);
    ctx.lineTo(W - padX, alertY);
    ctx.stroke();
    ctx.setLineDash([]);

    // Area fill
    const grad = ctx.createLinearGradient(0, padY, 0, H - padY);
    grad.addColorStop(0, 'rgba(0,119,182,0.25)');
    grad.addColorStop(1, 'rgba(0,119,182,0.02)');
    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.moveTo(toX(0), toY(data[0]));
    data.forEach((v, i) => ctx.lineTo(toX(i), toY(v)));
    ctx.lineTo(toX(data.length - 1), H - padY);
    ctx.lineTo(toX(0), H - padY);
    ctx.closePath();
    ctx.fill();

    // Line
    ctx.strokeStyle = '#0077B6';
    ctx.lineWidth = 2.5;
    ctx.lineJoin = 'round';
    ctx.beginPath();
    ctx.moveTo(toX(0), toY(data[0]));
    data.forEach((v, i) => ctx.lineTo(toX(i), toY(v)));
    ctx.stroke();

    // Dots + X labels
    data.forEach((v, i) => {
      const x = toX(i), y = toY(v);
      ctx.beginPath();
      ctx.arc(x, y, 4, 0, Math.PI * 2);
      ctx.fillStyle = '#0077B6';
      ctx.fill();
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.fillStyle = '#7BAFC8';
      ctx.font = '10px Barlow, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(labels[i], x, H - 4);
    });
  };

  // Animate counters on SARCOM page
  const animateMetric = (el) => {
    if (!el) return;
    const target = parseFloat(el.getAttribute('data-value'));
    if (isNaN(target)) return;
    const suffix = el.getAttribute('data-suffix') || '';
    const duration = 2000;
    const start = performance.now();

    const tick = (now) => {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const ease = 1 - Math.pow(1 - progress, 3);
      const val = target * ease;
      el.textContent = Math.abs(val) < 1 && target !== 0
        ? val.toFixed(2)
        : (target < 0 ? '-' : '') + Math.abs(Math.floor(val)).toLocaleString('es-CL') + suffix;
      if (progress < 1) requestAnimationFrame(tick);
    };

    requestAnimationFrame(tick);
  };

  const init = () => {
    const canvas = qs('#freaticChart');
    if (canvas) {
      draw(canvas);
      window.addEventListener('resize', () => draw(canvas));
      // Redraw on theme toggle
      qsa('[data-theme-toggle]').forEach(btn => {
        btn.addEventListener('click', () => setTimeout(() => draw(canvas), 350));
      });
    }

    // Animate metric values
    qsa('[data-value]').forEach(el => {
      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            animateMetric(entry.target);
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });
      observer.observe(el);
    });
  };

  return { init };
})();

/* ============================================================
   8. PROJECTS GALLERY (hover details)
   ============================================================ */
const ProjectsGallery = (() => {
  const init = () => {
    // Already handled by CSS hover states
    // Could add lightbox here in the future
  };
  return { init };
})();

/* ============================================================
   INIT
   ============================================================ */
document.addEventListener('DOMContentLoaded', () => {
  ThemeManager.init();
  Navbar.init();
  ScrollReveal.init();
  BackToTop.init();
  ContactForm.init();
  CounterAnimation.init();
  FreaticChart.init();
  ProjectsGallery.init();
});
