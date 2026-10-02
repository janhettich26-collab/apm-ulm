(() => {
  const leise = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Einblenden beim Scrollen
  const els = document.querySelectorAll('.reveal');
  if (leise || !('IntersectionObserver' in window)) {
    els.forEach(e => e.classList.add('sichtbar'));
  } else {
    const io = new IntersectionObserver(eintraege => {
      eintraege.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('sichtbar'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    els.forEach(e => {
      const r = e.getBoundingClientRect();
      if (r.top < innerHeight && r.bottom > 0) e.classList.add('sichtbar'); else io.observe(e);
    });
  }

  // Kopfzeile: Linie nach dem Scrollen
  const kopf = document.querySelector('.kopf');
  const linie = () => kopf.classList.toggle('gescrollt', scrollY > 8);
  addEventListener('scroll', linie, { passive: true }); linie();

  // Menü am Handy
  const btn = document.querySelector('.menu-btn');
  const nav = document.querySelector('.nav');
  btn.addEventListener('click', () => {
    const auf = nav.classList.toggle('offen');
    btn.setAttribute('aria-expanded', auf);
    btn.setAttribute('aria-label', auf ? 'Menü schließen' : 'Menü öffnen');
  });
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    nav.classList.remove('offen'); btn.setAttribute('aria-expanded', 'false');
  }));

  // Kacheln neigen sich leicht zur Maus (nur mit Maus, nicht bei "weniger Bewegung")
  if (!leise && matchMedia('(hover: hover) and (pointer: fine)').matches) {
    document.querySelectorAll('[data-tilt]').forEach(k => {
      k.addEventListener('pointermove', e => {
        const r = k.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        k.style.setProperty('--ry', ((x - .5) * 6).toFixed(2) + 'deg');
        k.style.setProperty('--rx', ((.5 - y) * 6).toFixed(2) + 'deg');
        k.style.setProperty('--mx', (x * 100).toFixed(1) + '%');
        k.style.setProperty('--my', (y * 100).toFixed(1) + '%');
      });
      k.addEventListener('pointerleave', () => { k.style.setProperty('--rx', '0deg'); k.style.setProperty('--ry', '0deg'); });
    });
  }
})();
