(() => {
  const leise = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const kopf = document.querySelector('.kopf'), knopf = document.querySelector('.menue-knopf'), nav = document.querySelector('.nav');
  const menue = auf => { nav.classList.toggle('offen', auf); knopf.setAttribute('aria-expanded', auf); };
  knopf.addEventListener('click', () => menue(!nav.classList.contains('offen')));

  /* Überschrift: Wörter schieben sich einzeln hoch */
  document.querySelectorAll('[data-worte]').forEach(h => {
    const worte = h.textContent.split(/\s+/); h.textContent = '';
    worte.forEach((t, n) => { const w = document.createElement('span'); w.className = 'w'; const i = document.createElement('span'); i.textContent = t; i.style.setProperty('--n', n); w.append(i); h.append(w, ' '); });
  });

  /* Einblenden beim Scrollen */
  const auf = [...document.querySelectorAll('.auf')];
  if (leise) auf.forEach(e => e.classList.add('da'));
  else { const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('da'); io.unobserve(e.target); } }), { threshold: .12, rootMargin: '0px 0px -6% 0px' }); auf.forEach(e => io.observe(e)); }

  /* weiches Scrollen, Kopf-Linie, Logo federt mit */
  const logos = [...document.querySelectorAll('.logo-svg')]; let letztesY = scrollY, letzterSchub = 0;
  const lenis = !leise && window.Lenis ? new Lenis({ lerp: .085, smoothWheel: true, wheelMultiplier: .9 }) : null;
  const lauf = t => {
    requestAnimationFrame(lauf);
    if (lenis) lenis.raf(t);
    const d = scrollY - letztesY; letztesY = scrollY;
    kopf.classList.toggle('schatten', scrollY > 10);
    const schub = Math.round(Math.max(-150, Math.min(150, -d * 9)) / 15) * 15;
    if (schub !== letzterSchub) { logos.forEach(l => l.style.setProperty('--schub', schub)); letzterSchub = schub; }
  };
  requestAnimationFrame(lauf);
})();
