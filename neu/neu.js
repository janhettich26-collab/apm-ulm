(() => {
  const leise = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const teile = [...document.querySelectorAll('.teil')];
  const links = [...document.querySelectorAll('.toc a')];
  const balken = document.querySelector('.fortschritt span');
  const plabel = document.querySelector('.partikel-label');

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
  document.querySelectorAll('[data-decode]').forEach(el => { el.dataset.ziel = el.textContent; if (el !== plabel) decIO.observe(el); });

  /* ---------- Partikel ---------- */
  const cv = document.getElementById('partikel');
  const formen = {
    haus: { d: 'M3 10.5 12 3l9 7.5M5.5 9v11h13V9M9.5 20v-6h5v6' },
    werkzeug: { d: 'M14.7 6.3a4 4 0 0 0-5.4 5.2L3.5 17.3a1.8 1.8 0 0 0 2.6 2.6l5.8-5.8a4 4 0 0 0 5.2-5.4l-2.6 2.6-2.4-.4-.4-2.4z' },
    pin: { d: 'M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z', kreis: [12, 9.5, 2.6] },
    haken: { d: 'M7.5 12.5l3 3 6-6.5', kreis: [12, 12, 9] },
    telefon: { d: 'M5 3.5h3.2l1.8 4.6-2.4 1.5a11 11 0 0 0 6.8 6.8l1.5-2.4 4.6 1.8v3.2a2 2 0 0 1-2 2A16.5 16.5 0 0 1 3 5.5a2 2 0 0 1 2-2z' }
  };
  let P = [], W = 0, H = 0, dpr = 1, ziele = {}, maus = { x: -9999, y: -9999 }, aktiveForm = 'haus';
  const N = 760;

  const probe = (f, groesse) => {
    const c = document.createElement('canvas'); c.width = c.height = groesse;
    const g = c.getContext('2d'), s = groesse / 26;
    g.translate(groesse / 2 - 12 * s, groesse / 2 - 12 * s); g.scale(s, s);
    g.lineWidth = 1.25; g.lineCap = g.lineJoin = 'round'; g.strokeStyle = '#000';
    g.stroke(new Path2D(f.d));
    if (f.kreis) { g.beginPath(); g.arc(f.kreis[0], f.kreis[1], f.kreis[2], 0, Math.PI * 2); g.stroke(); }
    const daten = g.getImageData(0, 0, groesse, groesse).data, pts = [];
    for (let y = 0; y < groesse; y += 3) for (let x = 0; x < groesse; x += 3) if (daten[(y * groesse + x) * 4 + 3] > 120) pts.push([x, y]);
    const out = [];
    for (let i = 0; i < N; i++) { const q = pts[(Math.random() * pts.length) | 0]; out.push([q[0] + (Math.random() - .5) * 2, q[1] + (Math.random() - .5) * 2]); }
    return out;
  };

  const groesse = () => {
    if (!cv) return;
    const r = cv.getBoundingClientRect(); dpr = Math.min(2, devicePixelRatio || 1);
    W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr;
    const seite = Math.min(W, H) * .92;
    for (const k in formen) {
      const roh = probe(formen[k], 360), f = seite / 360, ox = (W - seite) / 2, oy = (H - seite) / 2 - 8;
      ziele[k] = roh.map(([x, y]) => [ox + x * f, oy + y * f]);
    }
    if (!P.length) P = Array.from({ length: N }, (_, i) => ({ x: Math.random() * W, y: Math.random() * H, vx: 0, vy: 0, gold: i % 9 === 0, s: .8 + Math.random() * .9, ph: Math.random() * 6.28 }));
    setzeForm(aktiveForm, true);
  };
  const setzeForm = (k, still) => {
    aktiveForm = k; const z = ziele[k]; if (!z) return;
    const reihen = [...z].sort(() => Math.random() - .5);
    P.forEach((p, i) => { p.tx = reihen[i][0]; p.ty = reihen[i][1]; if (!still) { p.vx += (Math.random() - .5) * 6; p.vy += (Math.random() - .5) * 6; } });
  };

  if (cv) {
    const ctx = cv.getContext('2d');
    groesse(); addEventListener('resize', () => { clearTimeout(groesse._t); groesse._t = setTimeout(groesse, 150); });
    cv.addEventListener('pointermove', e => { const r = cv.getBoundingClientRect(); maus.x = e.clientX - r.left; maus.y = e.clientY - r.top; });
    cv.addEventListener('pointerleave', () => { maus.x = maus.y = -9999; });
    let sichtbar = true;
    new IntersectionObserver(es => { sichtbar = es[0].isIntersecting; }).observe(cv);
    const lauf = t => {
      requestAnimationFrame(lauf);
      if (!sichtbar) return;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, H);
      for (const p of P) {
        const wx = Math.sin(t * .0011 + p.ph) * 1.4, wy = Math.cos(t * .0013 + p.ph) * 1.4;
        let ax = (p.tx + wx - p.x) * .035, ay = (p.ty + wy - p.y) * .035;
        const dx = p.x - maus.x, dy = p.y - maus.y, d2 = dx * dx + dy * dy;
        if (d2 < 4900) { const d = Math.sqrt(d2) || 1, k = (70 - d) / 70 * 2.2; ax += dx / d * k; ay += dy / d * k; }
        p.vx = (p.vx + ax) * .86; p.vy = (p.vy + ay) * .86;
        if (leise) { p.x = p.tx; p.y = p.ty; } else { p.x += p.vx; p.y += p.vy; }
        ctx.beginPath(); ctx.arc(p.x, p.y, p.gold ? p.s * 1.25 : p.s, 0, 6.283);
        ctx.fillStyle = p.gold ? 'rgba(214,176,104,.95)' : 'rgba(236,230,218,.82)'; ctx.fill();
      }
    };
    requestAnimationFrame(lauf);
  }

  /* ---------- Weiches Scrollen ---------- */
  if (!leise && window.Lenis) {
    const lenis = new Lenis({ duration: 1.1, smoothWheel: true });
    const raf = t => { lenis.raf(t); requestAnimationFrame(raf); }; requestAnimationFrame(raf);
    document.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
      const z = document.querySelector(a.getAttribute('href')); if (!z) return;
      e.preventDefault(); lenis.scrollTo(z, { offset: -70 });
    }));
  }

  /* ---------- Abschnitt aktiv ---------- */
  let aktuell = null;
  const zeige = t => {
    if (aktuell === t) return; aktuell = t;
    links.forEach(l => l.classList.toggle('aktiv', l.dataset.ziel === t.id));
    if (t.dataset.form && ziele[t.dataset.form]) setzeForm(t.dataset.form);
    if (plabel && t.dataset.wort) decode(plabel, t.dataset.wort);
  };
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('da'); zeige(e.target); } }), { rootMargin: '-45% 0px -45% 0px' });
  teile.forEach(t => io.observe(t));
  const sofort = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) e.target.classList.add('da'); }), { threshold: .15 });
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


  /* ---------- Zahlen, Foto-Parallax, Ablauf-Linie ---------- */
  const zIO = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return; zIO.unobserve(e.target);
    const el = e.target, ziel = +el.dataset.zaehle, t0 = performance.now(), d = 1400;
    if (leise) return;
    const f = t => { const p = Math.min(1, (t - t0) / d), w = 1 - Math.pow(1 - p, 4); el.textContent = Math.round(ziel * w).toLocaleString('de-DE'); if (p < 1) requestAnimationFrame(f); };
    requestAnimationFrame(f);
  }), { threshold: .8 });
  document.querySelectorAll('[data-zaehle]').forEach(el => zIO.observe(el));
  const foto = document.querySelector('[data-parallax]'), schritte = document.querySelector('.schritte');
  const scrollFx = () => {
    if (foto && !leise) { const r = foto.getBoundingClientRect(), m = (r.top + r.height / 2 - innerHeight / 2) / innerHeight; foto.style.setProperty('--py', (m * -30).toFixed(1) + 'px'); }
    if (schritte) { const r = schritte.getBoundingClientRect(), p = Math.min(1, Math.max(0, (innerHeight * .85 - r.top) / (r.height + innerHeight * .25))); schritte.style.setProperty('--fuell', p.toFixed(3)); }
  };
  addEventListener('scroll', scrollFx, { passive: true }); scrollFx();

  /* ---------- Fortschritt ---------- */
  const fort = () => { const max = document.documentElement.scrollHeight - innerHeight; balken.style.transform = `scaleX(${max > 0 ? scrollY / max : 0})`;
    if (max > 0 && scrollY >= max - 4) { const l = teile[teile.length - 1]; l.classList.add('da'); zeige(l); } };
  addEventListener('scroll', fort, { passive: true }); fort();
})();
