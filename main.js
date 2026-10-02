(() => {
  const leise = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const gross = matchMedia('(min-width: 901px)');
  const maus = matchMedia('(hover: hover) and (pointer: fine)').matches;

  // Kopfzeile
  const kopf = document.querySelector('.kopf');
  const linie = () => kopf.classList.toggle('gescrollt', scrollY > 10);
  addEventListener('scroll', linie, { passive: true }); linie();

  // Handy-Menü
  const btn = document.querySelector('.menu-btn'), nav = document.querySelector('.nav');
  btn.addEventListener('click', () => {
    const auf = nav.classList.toggle('offen');
    btn.setAttribute('aria-expanded', auf); btn.setAttribute('aria-label', auf ? 'Menü schließen' : 'Menü öffnen');
  });
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => { nav.classList.remove('offen'); btn.setAttribute('aria-expanded', 'false'); }));

  // Leistungen aufklappen
  document.querySelectorAll('.zeile-kopf').forEach(k => k.addEventListener('click', () => {
    const li = k.parentElement, auf = !li.classList.contains('offen');
    document.querySelectorAll('.zeile-l.offen').forEach(o => { o.classList.remove('offen'); o.querySelector('.zeile-kopf').setAttribute('aria-expanded', 'false'); });
    if (auf) { li.classList.add('offen'); k.setAttribute('aria-expanded', 'true'); }
    if (window.ScrollTrigger) setTimeout(() => ScrollTrigger.refresh(), 650);
  }));

  // Statement in Wörter teilen
  const satz = document.querySelector('[data-woerter]');
  if (satz) satz.innerHTML = satz.textContent.trim().split(/\s+/).map(w => `<span class="w">${w}</span>`).join(' ');

  if (leise || !window.gsap || !window.ScrollTrigger) {
    document.querySelectorAll('.satz .w').forEach(w => w.style.opacity = 1);
    return;
  }
  gsap.registerPlugin(ScrollTrigger);

  // Weiches Scrollen
  if (window.Lenis) {
    const lenis = new Lenis({ duration: 1.1, smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(t => lenis.raf(t * 1000)); gsap.ticker.lagSmoothing(0);
    document.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
      const id = a.getAttribute('href'); if (id.length < 2) return;
      const ziel = document.querySelector(id); if (!ziel) return;
      e.preventDefault(); lenis.scrollTo(ziel, { offset: -70 });
    }));
  }

  // Hero: Zeilen gleiten herein
  gsap.from('.titel .z > span', { yPercent: 110, duration: 1.3, ease: 'expo.out', stagger: .12, delay: .1 });
  gsap.from(['.meta', '.hero-text', '.rund-btn'], { opacity: 0, y: 20, duration: 1, ease: 'expo.out', stagger: .08, delay: .5 });

  // Breitbild öffnet sich beim Scrollen – bis zur Inhaltsbreite, nicht ganz an den Rand
  const randPx = () => parseFloat(getComputedStyle(document.querySelector('.hero .rand')).paddingLeft) || 24;
  const ende = () => Math.max(randPx() * .5, (innerWidth - 1120) / 2);
  gsap.fromTo('.breitbild-in', { clipPath: () => `inset(0 ${ende() + innerWidth * .06}px round 10px)` }, {
    clipPath: () => `inset(0 ${ende()}px round 10px)`, ease: 'none',
    scrollTrigger: { trigger: '.breitbild', start: 'top 85%', end: 'top 20%', scrub: true, invalidateOnRefresh: true }
  });
  gsap.to('.breitbild img', { scale: 1, ease: 'none', scrollTrigger: { trigger: '.breitbild', start: 'top bottom', end: 'bottom top', scrub: true } });

  // Statement füllt sich Wort für Wort
  gsap.to('.satz .w', { opacity: 1, ease: 'none', stagger: .1,
    scrollTrigger: { trigger: '.statement', start: 'top 70%', end: 'bottom 60%', scrub: true } });

  // Überschriften und Zeilen einblenden
  gsap.utils.toArray('.abschnitt-kopf, .zeile-l, .schritt, .kontakt .riesig span, .kontakt-raster').forEach(el => {
    gsap.from(el, { y: 40, opacity: 0, duration: 1.1, ease: 'expo.out', scrollTrigger: { trigger: el, start: 'top 90%' } });
  });

  // Ablauf: Linie füllt sich
  gsap.to('.fortschritt span', { scaleX: 1, ease: 'none', scrollTrigger: { trigger: '.schritte', start: 'top 80%', end: 'bottom 55%', scrub: true } });

  // Praxisbeispiel seitlich (nur großer Bildschirm) + Zahlen hochzählen
  const zaehlen = el => { const ziel = +el.dataset.zaehle, o = { v: 0 };
    gsap.to(o, { v: ziel, duration: 1.6, ease: 'expo.out', onUpdate: () => el.textContent = Math.round(o.v).toLocaleString('de-DE') }); };
  const mm = gsap.matchMedia();
  mm.add('(min-width: 901px)', () => {
    const spur = document.querySelector('.spur');
    const weg = () => spur.scrollWidth - innerWidth;
    const horiz = gsap.to(spur, { x: () => -weg(), ease: 'none',
      scrollTrigger: { trigger: '.praxis', pin: '.praxis-pin', start: 'top top', end: () => '+=' + weg(), scrub: 1, invalidateOnRefresh: true } });
    document.querySelectorAll('[data-zaehle]').forEach(el => ScrollTrigger.create({ trigger: el, containerAnimation: horiz, start: 'left 85%', once: true, onEnter: () => zaehlen(el) }));
  });
  mm.add('(max-width: 900px)', () => {
    document.querySelectorAll('[data-zaehle]').forEach(el => ScrollTrigger.create({ trigger: el, start: 'top 85%', once: true, onEnter: () => zaehlen(el) }));
  });

  // Magnetischer Rund-Button
  const rb = document.querySelector('.rund-btn');
  if (rb && maus) {
    rb.addEventListener('pointermove', e => { const r = rb.getBoundingClientRect(); gsap.to(rb, { x: (e.clientX - r.left - r.width / 2) * .3, y: (e.clientY - r.top - r.height / 2) * .3, duration: .5, ease: 'power3.out' }); });
    rb.addEventListener('pointerleave', () => gsap.to(rb, { x: 0, y: 0, duration: .8, ease: 'elastic.out(1,.4)' }));
  }

  addEventListener('load', () => ScrollTrigger.refresh());
})();
