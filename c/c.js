(() => {
  const leise = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const mobil = () => innerWidth <= 900;
  const teile = [...document.querySelectorAll('.teil')];
  const navLinks = [...document.querySelectorAll('.nav a')];
  const balken = document.querySelector('.fortschritt span');
  const markeNr = document.querySelector('.marke-nr'), markeWort = document.querySelector('.marke-wort');
  const schein = document.querySelector('.schein');

  /* ---------- Entschlüsseln (Decode) ---------- */
  const zeichen = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/·+';
  const decode = (el, text) => {
    text = text ?? el.dataset.ziel ?? el.textContent;
    el.dataset.ziel = text;
    if (leise) { el.textContent = text; return; }
    const dauer = 650, start = performance.now();
    cancelAnimationFrame(el._raf);
    const tick = t => {
      const p = Math.min(1, (t - start) / dauer), fertig = Math.floor(p * text.length);
      el.textContent = text.split('').map((c, i) => i < fertig || c === ' ' ? c : zeichen[(Math.random() * zeichen.length) | 0]).join('');
      if (p < 1) el._raf = requestAnimationFrame(tick);
    };
    el._raf = requestAnimationFrame(tick);
  };
  const decIO = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { decode(e.target); decIO.unobserve(e.target); } }), { threshold: .6 });
  document.querySelectorAll('[data-decode]').forEach(el => { el.dataset.ziel = el.textContent; decIO.observe(el); });

  /* Einblend-Reihenfolge je Abschnitt */
  teile.forEach(t => t.querySelectorAll('.auf').forEach((el, i) => el.style.setProperty('--i', i)));

  /* ---------- Partikelfeld (ganzer Bildschirm) ---------- */
  const cv = document.getElementById('feld'), ctx = cv.getContext('2d');
  const formen = {
    haus: { d: 'M3 10.5 12 3l9 7.5M5.5 9v11h13V9M9.5 20v-6h5v6' },
    pin: { d: 'M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z', kreis: [12, 9.5, 2.6] },
    haken: { d: 'M7.5 12.5l3 3 6-6.5', kreis: [12, 12, 9] },
    telefon: { d: 'M5 3.5h3.2l1.8 4.6-2.4 1.5a11 11 0 0 0 6.8 6.8l1.5-2.4 4.6 1.8v3.2a2 2 0 0 1-2 2A16.5 16.5 0 0 1 3 5.5a2 2 0 0 1 2-2z' },
    /* Leistungen 01–06 */
    l0: { d: 'M11 12l8-8M16 7l2 2M14 9l2 2', kreis: [8, 15, 4] },
    l1: { d: 'M14.7 6.3a4 4 0 0 0-5.4 5.2L3.5 17.3a1.8 1.8 0 0 0 2.6 2.6l5.8-5.8a4 4 0 0 0 5.2-5.4l-2.6 2.6-2.4-.4-.4-2.4z' },
    l2: { d: 'M12 21c4 0 6.5-2.6 6.5-6.2 0-3.4-2.4-5.6-3.6-8.3-.5 1.8-1.4 3-2.6 3.6C12.5 7 11.2 4.6 9 3c.3 3-1.6 5-2.9 6.8A7 7 0 0 0 5.5 14.8C5.5 18.4 8 21 12 21z' },
    l3: { d: 'M12 2v20M4.2 6.5l15.6 11M19.8 6.5 4.2 17.5M9.5 3.5 12 6l2.5-2.5M9.5 20.5 12 18l2.5 2.5' },
    l4: { d: 'M3 20c.4-3.6 2.9-5.6 6-5.6s5.6 2 6 5.6M16 4.9a3.2 3.2 0 0 1 0 6.2M17.5 14.6c2 .6 3.3 2.3 3.5 5.4', kreis: [9, 8, 3.2] },
    l5: { d: 'M6 16.5V11a6 6 0 1 1 12 0v5.5l1.5 2h-15zM10 21h4' }
  };
  let W = 0, H = 0, dpr = 1, P = [], punkte = {}, aktiveForm = 'haus', wirbelStart = -9999;
  const maus = { x: -9999, y: -9999 };
  const anker = { x: .73, y: .52, g: 300, a: 0 }, ziel = { x: .73, y: .52, g: 300, a: 1 };

  /* Form abtasten -> Punkte in Einheiten von -0.5 bis 0.5 */
  const probe = (f, n) => {
    const G = 360, c = document.createElement('canvas'); c.width = c.height = G;
    const g = c.getContext('2d'), s = G / 26;
    g.translate(G / 2 - 12 * s, G / 2 - 12 * s); g.scale(s, s);
    g.lineWidth = 1.2; g.lineCap = g.lineJoin = 'round';
    g.stroke(new Path2D(f.d));
    if (f.kreis) { g.beginPath(); g.arc(f.kreis[0], f.kreis[1], f.kreis[2], 0, Math.PI * 2); g.stroke(); }
    const daten = g.getImageData(0, 0, G, G).data, pts = [];
    for (let y = 0; y < G; y += 3) for (let x = 0; x < G; x += 3) if (daten[(y * G + x) * 4 + 3] > 120) pts.push([x, y]);
    return Array.from({ length: n }, () => { const q = pts[(Math.random() * pts.length) | 0]; return [(q[0] + Math.random() * 2 - 1) / G - .5, (q[1] + Math.random() * 2 - 1) / G - .5]; });
  };

  const setzeForm = (k, still) => {
    const z = punkte[k]; if (!z) return;
    const neu = k !== aktiveForm; aktiveForm = k;
    const reihe = [...z].sort(() => Math.random() - .5);
    let i = 0;
    for (const p of P) { if (p.staub) continue; p.bx = reihe[i][0]; p.by = reihe[i][1]; i++; }
    if (!still && neu && !leise) wirbelStart = performance.now();
  };
  const setzeAnker = t => {
    if (!t) return;
    if (mobil()) { ziel.x = .5; ziel.y = .4; ziel.g = Math.min(W * .8, H * .44); ziel.a = t.id === 'start' ? .34 : .2; }
    else { ziel.x = +t.dataset.x || .5; ziel.y = +t.dataset.y || .52; ziel.g = Math.min(W * .36, H * .6) * (+t.dataset.g || 1); ziel.a = +t.dataset.a || 1; }
    schein.style.setProperty('--sx', ((ziel.x - .5) * 90).toFixed(1) + 'vw');
  };

  let aktuell = teile[0];
  const groesse = () => {
    dpr = Math.min(2, devicePixelRatio || 1); W = innerWidth; H = innerHeight;
    cv.width = W * dpr; cv.height = H * dpr;
    const nForm = mobil() ? 520 : 900, nStaub = mobil() ? 110 : 240;
    if (P.length !== nForm + nStaub) {
      for (const k in formen) punkte[k] = probe(formen[k], nForm);
      P = Array.from({ length: nForm + nStaub }, (_, i) => {
        const staub = i >= nForm;
        return { staub, x: Math.random() * W, y: Math.random() * H, vx: 0, vy: 0, bx: 0, by: 0, bz: (Math.random() - .5) * .14,
          dx: (Math.random() - .5) * .16, dy: -.04 - Math.random() * .12,
          gold: staub ? i % 5 === 0 : i % 8 === 0, s: staub ? .5 + Math.random() * .8 : .8 + Math.random() * .9, ph: Math.random() * 6.28 };
      });
      setzeForm(aktiveForm, true);
    }
    setzeAnker(aktuell);
  };
  groesse();
  addEventListener('resize', () => { clearTimeout(groesse._t); groesse._t = setTimeout(groesse, 150); });
  addEventListener('pointermove', e => { if (e.pointerType === 'mouse') { maus.x = e.clientX; maus.y = e.clientY; } }, { passive: true });
  document.addEventListener('pointerleave', () => { maus.x = maus.y = -9999; });

  const lauf = t => {
    requestAnimationFrame(lauf);
    if (document.hidden) return;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, H);
    const f = leise ? 1 : .055;
    anker.x += (ziel.x - anker.x) * f; anker.y += (ziel.y - anker.y) * f; anker.g += (ziel.g - anker.g) * f; anker.a += (ziel.a - anker.a) * f;
    const mx = anker.x * W, my = anker.y * H;
    /* leichte Drehung um die Hochachse -> räumlicher Eindruck */
    const dreh = leise ? 0 : Math.sin(t * .00045) * .5, co = Math.cos(dreh), si = Math.sin(dreh);
    const wr = Math.max(0, 1 - (t - wirbelStart) / 950), w = wr * wr * (3 - 2 * wr);
    for (const p of P) {
      if (p.staub) {
        if (!leise) { p.x += p.dx; p.y += p.dy; if (p.y < -5) { p.y = H + 5; p.x = Math.random() * W; } if (p.x < -5) p.x = W + 5; else if (p.x > W + 5) p.x = -5; }
        ctx.globalAlpha = (.16 + .14 * Math.sin(t * .0012 + p.ph)) * (mobil() ? .7 : 1);
      } else {
        const tx = mx + (p.bx * co + p.bz * si) * anker.g + Math.sin(t * .0011 + p.ph) * 1.3;
        const ty = my + p.by * anker.g + Math.cos(t * .0013 + p.ph) * 1.3;
        if (leise) { p.x = tx; p.y = ty; }
        else {
          const zug = .04 * (1 - w * .8);
          let ax = (tx - p.x) * zug, ay = (ty - p.y) * zug;
          if (w > 0) { const rx = p.x - mx, ry = p.y - my, r = Math.sqrt(rx * rx + ry * ry) || 1, k = w * (1.2 + p.s * .5); ax += -ry / r * k + rx / r * w * .12; ay += rx / r * k + ry / r * w * .12; }
          const dx = p.x - maus.x, dy = p.y - maus.y, d2 = dx * dx + dy * dy;
          if (d2 < 6400) { const d = Math.sqrt(d2) || 1, k = (80 - d) / 80 * 2.2; ax += dx / d * k; ay += dy / d * k; }
          p.vx = (p.vx + ax) * .86; p.vy = (p.vy + ay) * .86; p.x += p.vx; p.y += p.vy;
        }
        ctx.globalAlpha = anker.a * (p.gold ? .95 : .78);
      }
      ctx.fillStyle = p.gold ? '#D6B068' : '#ECE6DA';
      ctx.beginPath(); ctx.arc(p.x, p.y, p.gold ? p.s * 1.25 : p.s, 0, 6.283); ctx.fill();
    }
    ctx.globalAlpha = 1;
  };
  requestAnimationFrame(lauf);

  /* ---------- Weiches Scrollen ---------- */
  if (!leise && window.Lenis) {
    const lenis = new Lenis({ duration: 1.1, smoothWheel: true });
    const raf = t => { lenis.raf(t); requestAnimationFrame(raf); }; requestAnimationFrame(raf);
    document.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
      const z = document.querySelector(a.getAttribute('href')); if (!z) return;
      e.preventDefault(); lenis.scrollTo(z, { offset: z.id === 'start' ? 0 : -40 });
    }));
  }

  /* ---------- Leistungen: Auswahl ---------- */
  const pillen = [...document.querySelectorAll('.w-pille')];
  const dNr = document.querySelector('.d-nr'), dTitel = document.querySelector('.d-titel'), dText = document.querySelector('.d-text'), dLauf = document.querySelector('.d-lauf');
  const TAKT = 3600; let gewaehlt = 0, autoT = null, selbst = false;
  dLauf.style.setProperty('--takt', TAKT + 'ms');
  const name = b => b.lastChild.textContent.trim();
  const waehle = (i, vonHand) => {
    if (vonHand) { selbst = true; clearInterval(autoT); autoT = null; dLauf.classList.remove('laeuft'); }
    if (i === gewaehlt && vonHand) return;
    gewaehlt = i;
    pillen.forEach((b, j) => { b.classList.toggle('aktiv', j === i); b.setAttribute('aria-selected', j === i); });
    dNr.textContent = String(i + 1).padStart(2, '0') + ' / 06';
    decode(dTitel, name(pillen[i]));
    dText.classList.add('weg'); setTimeout(() => { dText.textContent = pillen[i].dataset.text; dText.classList.remove('weg'); }, leise ? 0 : 220);
    if (aktuell && aktuell.id === 'leistungen') setzeForm('l' + i);
    if (!vonHand) { dLauf.classList.remove('laeuft'); void dLauf.offsetWidth; dLauf.classList.add('laeuft'); }
  };
  pillen.forEach((b, i) => {
    b.addEventListener('click', () => waehle(i, true));
    b.addEventListener('pointerenter', e => { if (e.pointerType === 'mouse') waehle(i, true); });
    b.addEventListener('focus', () => waehle(i, true));
  });
  const auto = an => {
    clearInterval(autoT); autoT = null; dLauf.classList.remove('laeuft');
    if (!an || selbst || leise) return;
    void dLauf.offsetWidth; dLauf.classList.add('laeuft');
    autoT = setInterval(() => waehle((gewaehlt + 1) % pillen.length, false), TAKT);
  };

  /* ---------- Abschnitt aktiv ---------- */
  const zeige = t => {
    if (aktuell === t && t._gezeigt) return; aktuell = t; t._gezeigt = true;
    navLinks.forEach(l => l.classList.toggle('aktiv', l.dataset.ziel === t.id));
    setzeAnker(t);
    setzeForm(t.id === 'leistungen' ? 'l' + gewaehlt : t.dataset.form);
    markeNr.textContent = t.dataset.nr; decode(markeWort, t.dataset.wort);
    auto(t.id === 'leistungen');
  };
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('da'); zeige(e.target); } }), { rootMargin: '-45% 0px -45% 0px' });
  teile.forEach(t => io.observe(t));
  const sofort = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) e.target.classList.add('da'); }), { threshold: .12 });
  teile.forEach(t => sofort.observe(t));
  if (leise) teile.forEach(t => t.classList.add('da'));

  /* ---------- Kacheln neigen ---------- */
  if (!leise && matchMedia('(hover: hover) and (pointer: fine)').matches) {
    document.querySelectorAll('[data-tilt]').forEach(k => {
      k.addEventListener('pointermove', e => {
        const r = k.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        k.style.setProperty('--ry', ((x - .5) * 14).toFixed(2) + 'deg'); k.style.setProperty('--rx', ((.5 - y) * 12).toFixed(2) + 'deg');
        k.style.setProperty('--mx', (x * 100).toFixed(1) + '%'); k.style.setProperty('--my', (y * 100).toFixed(1) + '%');
      });
      k.addEventListener('pointerleave', () => { k.style.setProperty('--rx', '0deg'); k.style.setProperty('--ry', '0deg'); });
    });
  }

  /* ---------- Zahlen, Foto-Parallax, Zeitstrahl, Fortschritt ---------- */
  const zIO = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return; zIO.unobserve(e.target);
    const el = e.target, z = +el.dataset.zaehle, t0 = performance.now(), d = 1400;
    if (leise) return;
    const f = t => { const p = Math.min(1, (t - t0) / d), w = 1 - Math.pow(1 - p, 4); el.textContent = Math.round(z * w).toLocaleString('de-DE'); if (p < 1) requestAnimationFrame(f); };
    requestAnimationFrame(f);
  }), { threshold: .8 });
  document.querySelectorAll('[data-zaehle]').forEach(el => zIO.observe(el));

  const foto = document.querySelector('[data-parallax]'), schritte = document.querySelector('.schritte'), sLi = [...schritte.children];
  const scrollFx = () => {
    if (foto && !leise) { const r = foto.getBoundingClientRect(), m = (r.top + r.height / 2 - innerHeight / 2) / innerHeight; foto.style.setProperty('--py', (m * -30).toFixed(1) + 'px'); }
    const r = schritte.getBoundingClientRect(), p = leise ? 1 : Math.min(1, Math.max(0, (innerHeight * .72 - r.top) / r.height));
    schritte.style.setProperty('--fuell', p.toFixed(3));
    sLi.forEach((li, i) => li.classList.toggle('an', p >= i / (sLi.length - 1) - .04));
    const max = document.documentElement.scrollHeight - innerHeight;
    balken.style.transform = `scaleX(${max > 0 ? scrollY / max : 0})`;
    if (max > 0 && scrollY >= max - 4) { const l = teile[teile.length - 1]; l.classList.add('da'); zeige(l); }
  };
  addEventListener('scroll', scrollFx, { passive: true }); scrollFx();
  zeige(teile[0]);
})();
