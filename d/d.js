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

  /* Leistungen am Haus: Punkte anklicken, zwei Reiter, läuft von selbst durch bis man klickt */
  const reiter = [...document.querySelectorAll('.reiter button')], wahl = [...document.querySelectorAll('.h-wahl')];
  const buehne = document.querySelector('.h-buehne'), punkteBox = document.querySelector('.h-punkte'), detail = document.querySelector('.h-detail');
  const dIcon = detail.querySelector('.k-icon'), dTitel = detail.querySelector('h3'), dText = detail.querySelector('p');
  document.querySelectorAll('.haus path, .haus circle').forEach((el, i) => { el.style.setProperty('--l', Math.ceil(el.getTotalLength()) + 1); el.style.setProperty('--i', i); });
  const teile = [...document.querySelectorAll('.haus g[data-k]')];
  let aktArt = 'aussen', selbst = false, autoT = null;
  const waehle = (b, vonHand) => {
    if (vonHand) { selbst = true; clearInterval(autoT); }
    wahl.forEach(w => { const an = w === b; w.classList.toggle('aktiv', an); w._punkt.classList.toggle('aktiv', an); });
    teile.forEach(g => g.classList.toggle('aktiv', g.dataset.k === b.dataset.k));
    dIcon.innerHTML = b.querySelector('.l-icon').innerHTML;
    dTitel.textContent = b.querySelector('.l-name').textContent; dText.textContent = b.dataset.text;
    detail.classList.remove('neu'); void detail.offsetWidth; detail.classList.add('neu');
  };
  wahl.forEach(b => {
    const p = document.createElement('button'); p.className = 'h-punkt'; p.type = 'button';
    p.setAttribute('aria-label', b.querySelector('.l-name').textContent);
    p.style.left = ((+b.dataset.x + 60) / 760 * 100) + '%'; p.style.top = (b.dataset.y / 480 * 100) + '%';
    punkteBox.append(p); b._punkt = p;
    b.addEventListener('click', () => waehle(b, true)); p.addEventListener('click', () => waehle(b, true));
    p.addEventListener('pointerenter', e => { if (e.pointerType === 'mouse') waehle(b, true); });
  });
  const zeige = art => {
    aktArt = art;
    reiter.forEach(b => { const an = b.dataset.art === art; b.classList.toggle('aktiv', an); b.setAttribute('aria-selected', an); });
    let i = 0;
    wahl.forEach(b => { const an = b.dataset.art === art; b.parentElement.classList.toggle('aus', !an); b._punkt.classList.toggle('aus', !an); if (an) b._punkt.style.setProperty('--i', i++); });
    waehle(wahl.find(b => b.dataset.art === art), false);
  };
  reiter.forEach(b => b.addEventListener('click', () => { selbst = true; clearInterval(autoT); zeige(b.dataset.art); }));
  zeige('aussen');
  if (!leise) new IntersectionObserver(es => {
    clearInterval(autoT);
    if (!es[0].isIntersecting || selbst) return;
    autoT = setInterval(() => { const l = wahl.filter(b => b.dataset.art === aktArt), n = l[(l.findIndex(b => b.classList.contains('aktiv')) + 1) % l.length]; waehle(n, false); }, 3200);
  }, { threshold: .35 }).observe(buehne);

  /* Laufband: zwei Reihen gegenläufig, Scrollen gibt Schwung */
  const reihen = [...document.querySelectorAll('.lb-reihe')].map(el => ({ el, x: 0, tempo: +el.dataset.tempo, halb: 0 }));
  const messen = () => reihen.forEach(r => { r.halb = r.el.scrollWidth / 2; if (r.tempo > 0 && r.x === 0) r.x = -r.halb; });
  messen(); addEventListener('resize', messen);
  if (document.fonts) document.fonts.ready.then(messen);
  let letztesY = scrollY, schwung = 0;
  const logos = [...document.querySelectorAll('.logo-svg')]; let letzterSchub = 0;

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
      /* Logo läuft mit: Buchstaben federn beim Scrollen nacheinander nach */
      const schub = Math.round(Math.max(-150, Math.min(150, -d * 9)));
      if (schub !== letzterSchub) { logos.forEach(l => l.style.setProperty('--schub', schub)); letzterSchub = schub; }
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
