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

  /* Zahlen zählen hoch */
  const zIO = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return; zIO.unobserve(e.target);
    const el = e.target, z = +el.dataset.zaehle, t0 = performance.now(), d = 1300;
    if (leise) return;
    const f = t => { const p = Math.min(1, (t - t0) / d), w = 1 - Math.pow(1 - p, 4); el.textContent = Math.round(z * w); if (p < 1) requestAnimationFrame(f); };
    requestAnimationFrame(f);
  }), { threshold: .8 });
  document.querySelectorAll('[data-zaehle]').forEach(el => zIO.observe(el));

  /* Leistungen filtern */
  const knoepfe = [...document.querySelectorAll('.filter button')], karten = [...document.querySelectorAll('.karte')];
  knoepfe.forEach(b => b.addEventListener('click', () => {
    knoepfe.forEach(x => x.classList.toggle('aktiv', x === b));
    const f = b.dataset.filter;
    karten.forEach(k => { k.classList.toggle('aus', f !== 'alle' && k.dataset.art !== f); k.classList.add('da'); });
  }));
})();
