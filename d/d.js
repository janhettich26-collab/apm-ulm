(() => {
  const leise = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Kopf: Linie beim Scrollen, Menü am Handy */
  const kopf = document.querySelector('.kopf'), knopf = document.querySelector('.menue-knopf'), nav = document.querySelector('.nav');
  const menue = auf => { nav.classList.toggle('offen', auf); knopf.setAttribute('aria-expanded', auf); };
  knopf.addEventListener('click', () => menue(!nav.classList.contains('offen')));
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => menue(false)));

  /* Überschrift: Wörter schieben sich einzeln hoch */
  document.querySelectorAll('[data-worte]').forEach(h => {
    let n = 0;
    const huelle = knoten => [...knoten.childNodes].forEach(k => {
      if (k.nodeType === 3) {
        const f = document.createDocumentFragment();
        k.textContent.split(/(\s+)/).forEach(t => {
          if (!t.trim()) { f.append(t); return; }
          const w = document.createElement('span'); w.className = 'w';
          const i = document.createElement('span'); i.textContent = t; i.style.setProperty('--n', n++);
          w.append(i); f.append(w);
        });
        k.replaceWith(f);
      } else huelle(k);
    });
    huelle(h);
  });

  /* Einblenden beim Scrollen */
  const auf = [...document.querySelectorAll('.auf')];
  if (leise) auf.forEach(e => e.classList.add('da'));
  else {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('da'); io.unobserve(e.target); } }), { threshold: .1, rootMargin: '0px 0px -6% 0px' });
    auf.forEach(e => io.observe(e));
  }

  /* Leistungen: zwei Reiter, Zeilen bauen sich nacheinander auf */
  const reiter = [...document.querySelectorAll('.reiter button')], zeilen = [...document.querySelectorAll('.zeile')];
  const zeige = (art, sofort) => {
    reiter.forEach(b => { const an = b.dataset.art === art; b.classList.toggle('aktiv', an); b.setAttribute('aria-selected', an); });
    let i = 0;
    zeilen.forEach(z => {
      const an = z.dataset.art === art; z.classList.toggle('aus', !an);
      if (!an) return;
      z.style.setProperty('--v', (i++ * .05) + 's');
      if (!sofort && !leise) { z.classList.remove('da'); void z.offsetWidth; z.classList.add('da'); }
    });
  };
  reiter.forEach(b => b.addEventListener('click', () => zeige(b.dataset.art)));
  zeige('aussen', true);

  /* Laufband: zwei Reihen gegenläufig, Scrollen gibt Schwung */
  const reihen = [...document.querySelectorAll('.lb-reihe')].map(el => ({ el, x: 0, tempo: +el.dataset.tempo, halb: 0 }));
  const messen = () => reihen.forEach(r => { r.halb = r.el.scrollWidth / 2; if (r.tempo > 0 && r.x === 0) r.x = -r.halb; });
  messen(); addEventListener('resize', messen);
  if (document.fonts) document.fonts.ready.then(messen);
  let letztesY = scrollY, schwung = 0;

  /* Scroll-Effekte: Kopf, Foto-Versatz, Zeitstrahl */
  const heldBild = document.querySelector('.held-bild'), praxisBild = document.querySelector('.block-bild img'), schritte = document.querySelector('.schritte'), sLi = [...schritte.children];
  const scrollFx = () => {
    kopf.classList.toggle('schatten', scrollY > 10);
    if (!leise) {
      if (scrollY < innerHeight) heldBild.style.setProperty('--py', (scrollY * .22).toFixed(1) + 'px');
      const r = praxisBild.getBoundingClientRect(), m = (r.top + r.height / 2 - innerHeight / 2) / innerHeight;
      praxisBild.style.setProperty('--py', (m * -34).toFixed(1) + 'px');
    }
    const r = schritte.getBoundingClientRect(), p = leise ? 1 : Math.min(1, Math.max(0, (innerHeight * .8 - r.top) / (innerHeight * .45)));
    schritte.style.setProperty('--fuell', p.toFixed(3));
    sLi.forEach((li, i) => li.classList.toggle('an', p >= i / (sLi.length - 1) - .02 && p > 0));
  };
  addEventListener('scroll', scrollFx, { passive: true }); scrollFx();

  if (!leise) {
    const lauf = () => {
      requestAnimationFrame(lauf);
      const d = scrollY - letztesY; letztesY = scrollY;
      schwung += (Math.min(40, Math.abs(d)) - schwung) * .1;
      reihen.forEach(r => {
        if (!r.halb) return;
        r.x += r.tempo * (.35 + schwung * .25);
        if (r.x <= -r.halb) r.x += r.halb; else if (r.x >= 0) r.x -= r.halb;
        r.el.style.transform = `translate3d(${r.x.toFixed(1)}px,0,0)`;
      });
    };
    requestAnimationFrame(lauf);
  }
})();
