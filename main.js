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

  // Ablauf: Linie füllt sich beim Scrollen
  const schritte = document.querySelector('.schritte');
  if (schritte && !leise) {
    const fuellen = () => {
      const r = schritte.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, (innerHeight * 0.85 - r.top) / (r.height + innerHeight * 0.35)));
      schritte.style.setProperty('--fortschritt', (p * 100).toFixed(1) + '%');
    };
    addEventListener('scroll', fuellen, { passive: true }); fuellen();
  } else if (schritte) {
    schritte.style.setProperty('--fortschritt', '100%');
  }
})();
