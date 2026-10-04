(() => {
  const leise = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Karte: auf iPhone und iPad Apple Karten, sonst Google Maps */
  if (/iPhone|iPad|iPod/.test(navigator.userAgent)) document.querySelectorAll('.k-karte').forEach(k => k.href = 'https://maps.apple.com/?q=Ulm');

  /* E-Mail: Mailprogramm öffnen UND Adresse kopieren – hilft, wenn am Gerät kein Mailprogramm eingerichtet ist */
  document.querySelectorAll('.k-liste a[href^="mailto:"]').forEach(m => m.addEventListener('click', () => {
    const was = m.closest('li').querySelector('.k-was'), alt = was.dataset.alt || (was.dataset.alt = was.textContent);
    const zeige = () => { was.textContent = alt + ' · Adresse kopiert'; clearTimeout(was._t); was._t = setTimeout(() => was.textContent = alt, 3000); };
    if (navigator.clipboard) navigator.clipboard.writeText(m.textContent.trim()).then(zeige, () => {});
  }));

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
  const bild = document.querySelector('.h-bild'), hausMod = document.querySelector('.haus-mod');
  const dIcon = detail.querySelector('.k-icon'), dTitel = detail.querySelector('h3'), dText = detail.querySelector('p');
  document.querySelectorAll('.haus-haupt > path, .haus-haupt > circle').forEach((el, i) => { el.style.setProperty('--l', Math.ceil(el.getTotalLength()) + 1); el.style.setProperty('--i', i); });
  document.querySelectorAll('.haus-haupt g').forEach((g, i) => g.style.setProperty('--i', i));
  const teile = [...document.querySelectorAll('.haus g[data-k]')];
  let aktArt = 'aussen', selbst = false, autoT = null;
  const waehle = (b, vonHand) => {
    if (vonHand) { selbst = true; clearInterval(autoT); }
    wahl.forEach(w => { const an = w === b; w.classList.toggle('aktiv', an); w._punkt.classList.toggle('aktiv', an); });
    teile.forEach(g => g.classList.toggle('aktiv', g.dataset.k === b.dataset.k));
    /* weicher Wechsel: alter Text blendet kurz aus, neuer blendet ein */
    const setze = () => {
      dIcon.innerHTML = b.querySelector('.l-icon').innerHTML;
      dTitel.textContent = b.querySelector('.l-name').textContent; dText.textContent = b.dataset.text;
      detail.classList.remove('raus', 'neu'); void detail.offsetWidth; detail.classList.add('neu');
    };
    clearTimeout(detail._t);
    if (leise || !dTitel.textContent) setze();
    else if (dTitel.textContent !== b.querySelector('.l-name').textContent) { detail.classList.remove('neu'); detail.classList.add('raus'); detail._t = setTimeout(setze, 140); }
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
    /* Modernisierung hat ein eigenes Bild: Ablauf neu starten, Punkte erst zeigen, wenn das sanierte Haus steht */
    const istMod = art === 'mod'; bild.classList.toggle('mod', istMod);
    clearTimeout(bild._t); hausMod.classList.remove('lauf');
    wahl.forEach(b => b._punkt.classList.toggle('spaet', istMod && b.dataset.art === 'mod' && !leise));
    if (istMod && !leise) { void hausMod.getBoundingClientRect(); hausMod.classList.add('lauf'); bild._t = setTimeout(() => wahl.forEach(b => b._punkt.classList.remove('spaet')), 4500); }
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
  const logos = [...document.querySelectorAll('.kopf .logo-svg')];
  const gross = [...document.querySelectorAll('.gross-logo path')].map(el => ({ el, y: 0, v: 0, w: 0 })); let gZiel = 0, gT = 0; const gVerlauf = []; let letzterSchub = 0;

  /* Scroll-Effekte: Kopf, Foto-Versatz, Zeitstrahl */
  const heldBild = document.querySelector('.held-bild'), schritte = document.querySelector('.schritte'), sLi = [...schritte.children];
  const scrollFx = () => {
    kopf.classList.toggle('schatten', scrollY > 10);
    if (!leise) {
      if (scrollY < innerHeight) heldBild.style.setProperty('--py', (scrollY * .22).toFixed(1) + 'px');
    }
  };
  /* Praxis-Liste: Punkte haken sich nacheinander grün ab */
  document.querySelectorAll('[data-nacheinander]').forEach(ul => {
    const li = [...ul.children];
    if (leise) return li.forEach(l => l.classList.add('an'));
    new IntersectionObserver((es, io) => { if (!es[0].isIntersecting) return; io.disconnect(); li.forEach((l, i) => setTimeout(() => l.classList.add('an'), 700 + i * 480)); }, { threshold: .4 }).observe(ul);
  });

  /* Ablauf: Zahl erscheint, wird zum grünen Haken, Linie läuft zum nächsten Schritt – einer nach dem anderen */
  if (leise) { sLi.forEach(li => li.classList.add('fertig')); schritte.style.setProperty('--fuell', 1); }
  else new IntersectionObserver((es, io) => {
    if (!es[0].isIntersecting) return; io.disconnect();
    sLi.forEach((li, i) => {
      const t = 400 + i * 1250;
      setTimeout(() => li.classList.add('zahl'), t);
      setTimeout(() => { li.classList.remove('zahl'); li.classList.add('fertig'); }, t + 700);
      setTimeout(() => schritte.style.setProperty('--fuell', i < sLi.length - 1 ? ((sLi[i + 1].offsetLeft + 28) / schritte.offsetWidth).toFixed(3) : 1), t + 820);
    });
  }, { threshold: .5 }).observe(schritte);
  scrollFx();
  if (leise) addEventListener('scroll', scrollFx, { passive: true });

  if (!leise) {
    /* butterweiches Scrollen (Lenis) – läuft im selben Takt wie alle Scroll-Effekte */
    const lenis = window.Lenis ? new Lenis({ lerp: .085, smoothWheel: true, wheelMultiplier: .9 }) : null;
    if (lenis) document.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
      const z = document.querySelector(a.getAttribute('href')); if (!z) return;
      e.preventDefault(); lenis.scrollTo(z, { offset: z.id === 'start' ? 0 : -70, duration: 1.4 });
    }));
    const lauf = t => {
      requestAnimationFrame(lauf);
      if (lenis) lenis.raf(t);
      const d = scrollY - letztesY; if (d) scrollFx(); letztesY = scrollY;
      schwung += (Math.min(40, Math.abs(d)) - schwung) * .1;
      /* Logo läuft mit: Buchstaben federn beim Scrollen nacheinander nach */
      const schub = Math.round(Math.max(-150, Math.min(150, -d * 9)) / 15) * 15;
      if (schub !== letzterSchub) { logos.forEach(l => l.style.setProperty('--schub', schub)); letzterSchub = schub; }
      /* großes Logo: Buchstaben wippen beim Scrollen nach – jeder mit eigener Feder, zeitversetzt wie eine Welle */
      if (gross.length && scrollY < innerHeight * 1.2) {
        const schritte = Math.max(1, Math.min(4, Math.round((t - (gT || t - 8.33)) / 8.33))); gT = t;
        gZiel += (Math.max(-150, Math.min(150, -d * 9)) - gZiel) * .2;
        gVerlauf.push([t, gZiel]); while (gVerlauf.length > 2 && gVerlauf[1][0] < t - 400) gVerlauf.shift();
        gross.forEach((g, i) => {
          const zeit = t - i * 45; let ziel = gVerlauf[0][1];
          for (const [zt, zw] of gVerlauf) { if (zt > zeit) break; ziel = zw; }
          for (let k = 0; k < schritte; k++) { g.v = (g.v + (ziel - g.y) * .05) * .86; g.y += g.v; }
          const w = Math.abs(g.y) < .05 && Math.abs(g.v) < .05 ? 0 : g.y;
          if (w !== g.w) { g.el.style.translate = w ? `0 ${w.toFixed(2)}px` : ''; g.w = w; }
        });
      }
      reihen.forEach(r => {
        if (!r.halb) return;
        r.x += r.tempo * (.35 + schwung * .25);
        if (r.x <= -r.halb) r.x += r.halb; else if (r.x >= 0) r.x -= r.halb;
        r.el.style.transform = `translate3d(${r.x.toFixed(2)}px,0,0)`;
      });
    };
    requestAnimationFrame(lauf);
  }
})();
