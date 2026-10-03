(() => {
  const leise = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Kopf: Schatten beim Scrollen, Menü am Handy */
  const kopf = document.querySelector('.kopf'), knopf = document.querySelector('.menue-knopf'), nav = document.querySelector('.nav');
  const schatten = () => kopf.classList.toggle('schatten', scrollY > 10);
  addEventListener('scroll', schatten, { passive: true }); schatten();
  const menue = auf => { nav.classList.toggle('offen', auf); knopf.setAttribute('aria-expanded', auf); };
  knopf.addEventListener('click', () => menue(!nav.classList.contains('offen')));
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => menue(false)));

  /* Einblenden beim Scrollen (Karten leicht versetzt) */
  document.querySelectorAll('.karte').forEach((k, i) => k.style.setProperty('--v', (i % 3) * .08 + 's'));
  const auf = [...document.querySelectorAll('.auf')];
  if (leise) auf.forEach(e => e.classList.add('da'));
  else {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('da'); io.unobserve(e.target); } }), { threshold: .12, rootMargin: '0px 0px -6% 0px' });
    auf.forEach(e => io.observe(e));
  }

  /* Leistungen: zwei Reiter */
  const reiter = [...document.querySelectorAll('.reiter button')], karten = [...document.querySelectorAll('.karte')];
  const zeige = art => {
    reiter.forEach(b => { const an = b.dataset.art === art; b.classList.toggle('aktiv', an); b.setAttribute('aria-selected', an); });
    let i = 0;
    karten.forEach(k => {
      const an = k.dataset.art === art; k.classList.toggle('aus', !an);
      if (an && !leise) { k.style.setProperty('--v', (i++ % 3) * .07 + 's'); k.classList.remove('da'); void k.offsetWidth; k.classList.add('da'); }
    });
  };
  reiter.forEach(b => b.addEventListener('click', () => zeige(b.dataset.art)));
  karten.forEach(k => k.classList.toggle('aus', k.dataset.art !== 'aussen'));
})();
