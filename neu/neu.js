(() => {
  const leise = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const teile = [...document.querySelectorAll('.teil')];
  const bilder = [...document.querySelectorAll('.bild')];
  const zaehler = document.querySelector('.zaehler b');
  const bildtext = document.querySelector('.bildtext');
  const balken = document.querySelector('.fortschritt span');

  // Weiches Scrollen
  let lenis = null;
  if (!leise && window.Lenis) {
    lenis = new Lenis({ duration: 1.05, smoothWheel: true });
    const raf = t => { lenis.raf(t); requestAnimationFrame(raf); }; requestAnimationFrame(raf);
    document.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
      const z = document.querySelector(a.getAttribute('href')); if (!z) return;
      e.preventDefault(); lenis.scrollTo(z, { offset: -60 });
    }));
  }

  // Abschnitt aktiv -> Bild wechseln
  const zeige = t => {
    const name = t.dataset.bild, i = teile.indexOf(t);
    bilder.forEach(b => b.classList.toggle('aktiv', b.dataset.name === name));
    zaehler.textContent = String(i + 1).padStart(2, '0');
    bildtext.style.opacity = 0;
    setTimeout(() => { bildtext.textContent = t.dataset.text; bildtext.style.opacity = 1; }, 200);
  };
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('da'); zeige(e.target); }
  }), { rootMargin: '-45% 0px -45% 0px' });
  teile.forEach(t => io.observe(t));

  // Einblenden auch für Teile, die beim Laden sichtbar sind
  const sofort = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) e.target.classList.add('da'); }), { threshold: .15 });
  teile.forEach(t => sofort.observe(t));
  if (leise) teile.forEach(t => t.classList.add('da'));

  // Fortschrittsbalken
  const fort = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    balken.style.transform = `scaleX(${max > 0 ? scrollY / max : 0})`;
  };
  addEventListener('scroll', fort, { passive: true }); fort();
})();
