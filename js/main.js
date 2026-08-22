// Río Longaví — comportamiento compartido del sitio
document.addEventListener('DOMContentLoaded', () => {

  // Menú móvil
  const navToggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav');
  if (navToggle && nav) {
    navToggle.addEventListener('click', () => {
      nav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', nav.classList.contains('open'));
    });
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => nav.classList.remove('open')));
  }

  );
  }

  // Acordeón de preguntas frecuentes
  document.querySelectorAll('.faq-item').forEach(item => {
    const q = item.querySelector('.faq-q');
    q && q.addEventListener('click', () => {
      const wasOpen = item.classList.contains('open');
      item.parentElement.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!wasOpen) item.classList.add('open');
    });
  });

  // Filtro de proyectos
  const pills = document.querySelectorAll('.filter-pill');
  const cards = document.querySelectorAll('.project-card');
  pills.forEach(pill => {
    pill.addEventListener('click', () => {
      pills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      const cat = pill.dataset.filter;
      cards.forEach(card => {
        card.style.display = (cat === 'todos' || card.dataset.cat === cat) ? '' : 'none';
      });
    });
  });

  // Generar barras de forma de onda (entrevista)
  document.querySelectorAll('.waveform').forEach(wf => {
    const bars = 46;
    let html = '';
    for (let i = 0; i < bars; i++) {
      const h = 8 + Math.round(Math.abs(Math.sin(i * 0.7)) * 40 + Math.random() * 10);
      html += `<span style="height:${h}px"></span>`;
    }
    wf.innerHTML = html;
  });

  // Reproductor de audio real
  const audioEl = document.getElementById('entrevista-audio');
  const playBtn = document.getElementById('audio-play-btn');
  const progressBar = document.getElementById('audio-progress');
  const progressFill = document.getElementById('audio-progress-fill');
  const timeCurrent = document.getElementById('audio-current');
  const timeDuration = document.getElementById('audio-duration');

  if (audioEl && playBtn) {
    const playIcon = playBtn.querySelector('[data-play]');
    const pauseIcon = playBtn.querySelector('[data-pause]');

    const formatTime = (time) => {
      if (isNaN(time)) return '0:00';
      const m = Math.floor(time / 60);
      const s = Math.floor(time % 60);
      return `${m}:${s.toString().padStart(2, '0')}`;
    };

    audioEl.addEventListener('loadedmetadata', () => {
      timeDuration.textContent = formatTime(audioEl.duration);
    });

    playBtn.addEventListener('click', () => {
      if (audioEl.paused) {
        audioEl.play();
        playIcon.style.display = 'none';
        pauseIcon.style.display = 'block';
      } else {
        audioEl.pause();
        playIcon.style.display = 'block';
        pauseIcon.style.display = 'none';
      }
    });

    audioEl.addEventListener('timeupdate', () => {
      timeCurrent.textContent = formatTime(audioEl.currentTime);
      const percent = (audioEl.currentTime / audioEl.duration) * 100;
      progressFill.style.width = `${percent}%`;
    });

    progressBar.addEventListener('click', (e) => {
      const rect = progressBar.getBoundingClientRect();
      const pos = (e.clientX - rect.left) / rect.width;
      audioEl.currentTime = pos * audioEl.duration;
    });

    audioEl.addEventListener('ended', () => {
      playIcon.style.display = 'block';
      pauseIcon.style.display = 'none';
      progressFill.style.width = '0%';
      audioEl.currentTime = 0;
    });
  }

  // Carrusel de ficha de proyecto
  const track = document.querySelector('.carousel-track');
  const dots = document.querySelectorAll('.dots span[data-slide]');
  if (track && dots.length > 0) {
    dots.forEach(dot => {
      dot.addEventListener('click', () => {
        dots.forEach(d => d.classList.remove('active'));
        dot.classList.add('active');
        const slideIndex = parseInt(dot.getAttribute('data-slide'));
        track.style.transform = `translateX(-${slideIndex * 100}%)`;
      });
    });
  }

  // Simulación de datos en vivo SARCOM (variación leve de los valores)
  const flowVal = document.querySelector('[data-live="flow"]');
  if (flowVal) {
    setInterval(() => {
      const base = -246;
      const jitter = (Math.random() * 6 - 3).toFixed(1);
      flowVal.textContent = (base + parseFloat(jitter)).toFixed(1) + ' l/s';
    }, 2600);
  }

  // Gráfico de nivel freático (SVG simple sin librerías)
  const chart = document.querySelector('#nivel-chart');
  if (chart) {
    const points = [22, 30, 38, 46, 40, 30, 22, 16, 12, 18, 14, 10];
    const w = 640, h = 200, pad = 10;
    const step = (w - pad * 2) / (points.length - 1);
    const max = Math.max(...points), min = Math.min(...points);
    const scaled = points.map(p => h - pad - ((p - min) / (max - min)) * (h - pad * 2));
    const path = scaled.map((y, i) => `${i === 0 ? 'M' : 'L'} ${pad + i * step} ${y}`).join(' ');
    const area = `${path} L ${pad + (points.length - 1) * step} ${h - pad} L ${pad} ${h - pad} Z`;
    const alertY = h - pad - ((14 - min) / (max - min)) * (h - pad * 2);
    chart.innerHTML = `
      <svg viewBox="0 0 ${w} ${h}" width="100%" height="220" preserveAspectRatio="none">
        <defs>
          <linearGradient id="areaFill" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#12a2d6" stop-opacity="0.35"/>
            <stop offset="100%" stop-color="#12a2d6" stop-opacity="0"/>
          </linearGradient>
        </defs>
        <path d="${area}" fill="url(#areaFill)" />
        <path d="${path}" fill="none" stroke="#12a2d6" stroke-width="2.5" />
        <line x1="${pad}" y1="${alertY}" x2="${w-pad}" y2="${alertY}" stroke="#f0a53c" stroke-width="1.5" stroke-dasharray="5 5" />
      </svg>`;
  }
});
