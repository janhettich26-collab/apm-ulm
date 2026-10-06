# Druckvorlagen APM Ulm – erzeugt alle Druckdateien (Jan 06.10.2026)
# Aufruf: python3 bau_druck.py  -> HTML in _bau/, danach druck.mjs rendert PDF + Vorschau
import os, re, json, html, segno
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

H = os.path.expanduser
NAVY, GRAU, HELL, LINIE, GRUEN = '#1C2840', '#566078', '#8C94A6', '#C9CDD6', '#2F8F5B'
BAU = H('~/Websites/apm-ulm-v2/druck/_bau')
OUT = H('~/Desktop/2026-10-06_Druckvorlagen_APM-Ulm_Paket_V1')
TEL, TEL_INT = '0170 5810174', '+49 170 5810174'
MAIL, INFO, WEB = 'emre.altun@apm-ulm.de', 'info@apm-ulm.de', 'www.apm-ulm.de'
NAME, ROLLE, STR, ORT = 'Emre Altun', 'Inhaber', 'Weinbergweg 81', '89075 Ulm'
FIRMA, UST = 'apm ulm – altun property management', 'DE364898141'
SUB = 'altun property management'

# Leistungen + Symbole direkt aus der Webseite (eine Quelle)
_src = open(H('~/Websites/apm-ulm-v2/d/_bau.py'), encoding='utf-8').read()
_ns = {}; exec(_src[_src.index('\nI = {'):_src.index('\nMOD = [')] + _src[_src.index('\nMOD = ['):_src.index(']\n', _src.index('\nMOD = ['))+2], _ns)
I, AUSSEN, TECHNIK, MOD = _ns['I'], _ns['AUSSEN'], _ns['TECHNIK'], _ns['MOD']

# ---------- Logo (Vektor, alles Pfade) ----------
_logo = open(H('~/Desktop/H-KIOS/18_Marketing/APM-Ulm_Website/2026-10-03_Logo_APM-Ulm_Paket_V1/01_Logo_Grunddateien/Logo_APM-Ulm_Navy_Vektor_fuer-Druckerei.svg')).read()
LOGO_IN = _logo[_logo.index('>') + 1:_logo.rindex('</svg>')]
LX, LY, LW, LH = 120.0, 120.0, 1184.09, 337.44

FONT = {'r': TTFont('/System/Library/Fonts/Supplemental/Verdana.ttf'),
        'b': TTFont('/System/Library/Fonts/Supplemental/Verdana Bold.ttf')}

def tbreite(t, size, w='r', sp=0):
    f = FONT[w]; cm = f.getBestCmap(); s = size / f['head'].unitsPerEm
    return sum(f['hmtx'][cm[ord(c)]][0] * s for c in t) + sp * (len(t) - 1)

def tpfad(t, size, x, y, w='r', sp=0, anker='start', fit=None):
    """Text als Pfad (Schrift in Kurven) – fuer Folie, Stempel, Textil."""
    f = FONT[w]; gs = f.getGlyphSet(); cm = f.getBestCmap(); s = size / f['head'].unitsPerEm
    nat = tbreite(t, size, w)
    if fit: sp = (fit - nat) / (len(t) - 1)
    tot = nat + sp * (len(t) - 1)
    x -= tot / 2 if anker == 'middle' else (tot if anker == 'end' else 0)
    pen = SVGPathPen(gs, ntos=lambda v: ('%.2f' % v).rstrip('0').rstrip('.'))
    for c in t:
        g = cm[ord(c)]; gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, y)))
        x += f['hmtx'][g][0] * s + sp
    return pen.getCommands()

SUB_GR, SUB_BASIS = LW * 0.05, LY + LW * 0.385   # Unterzeile: Groesse + Grundlinie (wie Jans Vorlage)
def logo(farbe=NAVY, sub=True, extra=''):
    """SVG-Logo; sub=True mit 'altun property management' ueber volle Breite."""
    g = f'<g fill="{farbe}">{LOGO_IN}</g>'
    h = LH
    if sub:
        g += f'<path fill="{farbe}" d="{tpfad(SUB, SUB_GR, LX, SUB_BASIS, fit=LW)}"/>'
        h = SUB_BASIS + SUB_GR * 0.27 - LY
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{LX} {LY} {LW} {h:.2f}" {extra}>{g}</svg>', LW / h

def qr(farbe=NAVY, url='https://www.apm-ulm.de'):
    q = segno.make(url, error='m'); d = []
    for y, row in enumerate(q.matrix_iter(border=0)):
        for x, v in enumerate(row):
            if v: d.append(f'M{x} {y}h1v1h-1z')
    n = q.symbol_size(border=0)[0]
    return f'<svg viewBox="0 0 {n} {n}" shape-rendering="crispEdges"><path fill="{farbe}" d="{"".join(d)}"/></svg>'

K = {  # Kontakt-Symbole (wie Webseite)
 'tel': '<path d="M5 3.5h3.2l1.8 4.6-2.4 1.5a11 11 0 0 0 6.8 6.8l1.5-2.4 4.6 1.8v3.2a2 2 0 0 1-2 2A16.5 16.5 0 0 1 3 5.5a2 2 0 0 1 2-2z"/>',
 'mail': '<path d="M3.5 6h17v12h-17z"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/>',
 'web': '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.6 2.6 3.8 5.4 3.8 8.5s-1.2 5.9-3.8 8.5c-2.6-2.6-3.8-5.4-3.8-8.5s1.2-5.9 3.8-8.5z"/>',
 'ort': '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
}
def sym(d, farbe=NAVY, sw=1.5, cls='sym'):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="{farbe}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'

VORTEILE = [
 ('Ein Ansprechpartner', 'Ein fester Kontakt für alles rund um Ihr Gebäude – ohne Weiterleiten, ohne Warteschleife.',
  '<path d="M10 70h100"/><circle cx="60" cy="31" r="11"/><path d="M38 70c1-14 10-22 22-22s21 8 22 22"/><path class="g" d="M80 10h22v15H91l-6 6v-6h-5z"/><path class="g" d="M85 15.5h12M85 20h8"/>'),
 ('Vor Ort statt Hotline', 'Wir kennen Ihr Gebäude, weil wir regelmäßig drin sind.',
  '<path d="M10 70h100"/><path d="M22 70V28h36v42"/><path d="M30 38h7M43 38h7M30 49h7M43 49h7M36 70V60h8v10"/><path class="g" d="M86 64s-15-13-15-26a15 15 0 0 1 30 0c0 13-15 26-15 26z"/><circle class="g" cx="86" cy="38" r="5"/>'),
 ('Alles dokumentiert', 'Prüfungen, Wartungen und Mängel nachvollziehbar festgehalten.',
  '<path d="M38 16h44v56H38z"/><path d="M50 11h20v10H50z"/><path class="g" d="M46 34l4 4 7-8"/><path d="M63 34h12"/><path class="g" d="M46 47l4 4 7-8"/><path d="M63 47h12"/><path class="g" d="M46 60l4 4 7-8"/><path d="M63 60h12"/>'),
]
def vbild(d):
    return f'<svg class="vb" viewBox="0 0 120 80" fill="none" stroke="{NAVY}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'
SCHRITTE = [('Begehung', 'Technik, Flächen und Prüfpflichten gemeinsam ansehen.'),
            ('Objektakte', 'Anlagen, Fristen und Ansprechpartner an einem Ort.'),
            ('Laufender Betrieb', 'Feste Rundgänge, schnelle Reaktion, Fachfirmen im Griff.'),
            ('Kurzer Bericht', 'Was erledigt ist, was geplant ist, was ansteht.')]
BEREICHE = [('Infrastrukturelles Management', AUSSEN), ('Technisches Management', TECHNIK), ('Gebäudemodernisierung', MOD)]

BASIS_CSS = f'''*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{font-family:Verdana,sans-serif;color:{NAVY};-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.seite{{position:relative;overflow:hidden}} .seite+.seite{{break-before:page}}
svg{{display:block}} .abs{{position:absolute}}
.g{{stroke:{GRUEN}}}
'''
JOBS = []
def seiten(datei, w, h, inhalt, css='', vorschau=None, prevbg=None, ziel_dir='', bleed=0, notiz=''):
    """Eine Druckdatei: inhalt = Liste von HTML je Seite. w/h inkl. Beschnitt (mm)."""
    os.makedirs(os.path.join(OUT, ziel_dir), exist_ok=True)
    body = ''.join(f'<div class="seite" style="width:{w}mm;height:{h}mm">{s}</div>' for s in inhalt)
    doc = f'<!doctype html><html lang="de"><head><meta charset="utf-8"><style>@page{{size:{w}mm {h}mm;margin:0}}{BASIS_CSS}{css}</style></head><body>{body}</body></html>'
    stamm = re.sub(r'\.pdf$', '', datei)
    hp = os.path.join(BAU, stamm + '.html'); open(hp, 'w', encoding='utf-8').write(doc)
    prev = [os.path.join(BAU, f'{stamm}_v{i}.png') for i in range(len(inhalt))]
    JOBS.append({'html': hp, 'pdf': os.path.join(OUT, ziel_dir, datei), 'w': w, 'h': h, 'prev': prev,
                 'prevbg': prevbg, 'bleed': bleed, 'name': datei, 'dir': ziel_dir, 'notiz': notiz})

def svg_datei(ziel_dir, name, svg, w, h):
    """Reine Vektordatei (SVG) in Endgroesse – fuer Folienplotter/Stick/Stempel."""
    os.makedirs(os.path.join(OUT, ziel_dir), exist_ok=True)
    s = svg.replace('<svg ', f'<svg width="{w}mm" height="{h}mm" ', 1)
    open(os.path.join(OUT, ziel_dir, name), 'w', encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n' + s)

os.makedirs(BAU, exist_ok=True)
B = 3  # Beschnitt mm

# ============ 01 Logo-Grunddateien mit Unterzeile ============
D = '01_Logo_Vektor'
for fn, farbe in [('Navy', NAVY), ('Weiss', '#FFFFFF'), ('Schwarz', '#000000')]:
    s, r = logo(farbe, True)
    svg_datei(D, f'Logo_APM-Ulm_mit-altun-property-management_{fn}_Vektor.svg', s, 200, round(200 / r, 2))
    s2, r2 = logo(farbe, False)
    svg_datei(D, f'Logo_APM-Ulm_ohne-Unterzeile_{fn}_Vektor.svg', s2, 200, round(200 / r2, 2))
s, r = logo(NAVY, True)
seiten('Logo_APM-Ulm_mit-altun-property-management_Navy_Vektor.pdf', 200, round(200 / r, 2), [s], ziel_dir=D)
s, r = logo('#FFFFFF', True)
seiten('Logo_APM-Ulm_mit-altun-property-management_Weiss_Vektor.pdf', 200, round(200 / r, 2), [s], ziel_dir=D, prevbg=NAVY)

# ============ 02 Visitenkarte 85x55 ============
D = '02_Visitenkarte'
VW, VH = 85 + 2 * B, 55 + 2 * B
lg, r = logo('#FFFFFF', True)
vorne = f'<div class="abs" style="inset:0;background:{NAVY}"></div><div class="abs" style="left:{(VW-50)/2}mm;top:{(VH-50/r)/2}mm;width:50mm">{lg}</div>'
lk, rk = logo(NAVY, False)
zeilen = ''.join(f'<div class="kz">{sym(K[k], NAVY, 1.6)}<span>{t}</span></div>' for k, t in
                 [('tel', TEL_INT), ('mail', MAIL), ('web', WEB), ('ort', f'{STR} · {ORT}')])
hinten = f'''<div class="abs" style="right:{B+7}mm;top:{B+7.6}mm;width:21mm">{lk}</div>
<div class="abs" style="left:{B+7}mm;top:{B+6.6}mm"><div class="nm">{NAME}</div><div class="rl">{ROLLE}</div></div>
<div class="abs" style="left:{B+7}mm;top:{B+19.5}mm;width:9mm;height:.3mm;background:{NAVY}"></div>
<div class="abs" style="left:{B+7}mm;top:{B+24}mm">{zeilen}</div>'''
vcss = f'''.nm{{font-weight:700;font-size:10.5pt;letter-spacing:.01em}} .rl{{font-size:6.3pt;color:{GRAU};letter-spacing:.14em;margin-top:1.2mm}}
.kz{{display:flex;align-items:center;gap:2.6mm;font-size:6.6pt;height:4.9mm}} .kz .sym{{width:3mm;height:3mm;flex:none}}'''
seiten('Visitenkarte_Vorder-und-Rueckseite_85x55mm_plus-3mm-Beschnitt_DRUCK.pdf', VW, VH, [vorne, hinten], vcss, ziel_dir=D, bleed=B,
       notiz='Seite 1 = Vorderseite (Logo auf Navy), Seite 2 = Rückseite (Kontakt).')

# ============ 03 Flyer A5 ============
D = '03_Flyer'
def kontaktband(gross=True):
    t = '13pt' if gross else '11pt'
    return f'''<div class="band"><div class="bt">Sprechen wir über Ihr Gebäude</div>
<div class="bk"><span class="btel">{sym(K["tel"], "#fff", 1.6)}{TEL_INT}</span></div>
<div class="bk2"><span>{sym(K["mail"], "#fff", 1.6)}{INFO}</span><span>{sym(K["web"], "#fff", 1.6)}{WEB}</span></div></div>'''
FW, FH = 148 + 2 * B, 210 + 2 * B
lf, rf = logo(NAVY, True)
vort = ''.join(f'<div class="vt">{vbild(d)}<div><h3>{t}</h3><p>{p}</p></div></div>' for t, p, d in VORTEILE)
a5_vorne = f'''<div class="abs" style="left:{B+14}mm;top:{B+15}mm;width:60mm">{lf}</div>
<div class="abs" style="left:{B+14}mm;right:{B+14}mm;top:{B+58}mm">
<h1>Gebäude in Ulm,<br><em>um Ulm und um Ulm herum</em></h1>
<p class="lead">Vom Hausmeisterdienst bis zur Haustechnik: Wir halten Ihre Immobilie in Schuss. Sie sprechen mit einem festen Ansprechpartner, der Ihr Gebäude kennt, weil er selbst regelmäßig vor Ort ist.</p>
<div class="vts">{vort}</div></div>
<div class="abs fuss" style="left:0;right:0;bottom:0;height:{B+38}mm">{kontaktband()}</div>'''
def liste(items, cls='li'):
    return ''.join(f'<div class="{cls}">{sym(I[k], NAVY, 1.5)}<span>{n}</span></div>' for k, n, _ in items)
bereiche = ''.join(f'<div class="ber"><h4>{t}</h4>{liste(l)}</div>' for t, l in BEREICHE)
schr = ''.join(f'<div class="sc"><b>{i+1}</b><h5>{t}</h5><p>{p}</p></div>' for i, (t, p) in enumerate(SCHRITTE))
a5_hinten = f'''<div class="abs" style="left:{B+14}mm;right:{B+14}mm;top:{B+14}mm">
<h2>Alles rund um Ihr Gebäude – <em>aus einer Hand</em></h2>
<div class="bers">{bereiche}</div>
<h2 class="h2b">Vier Schritte bis zum <em>sicheren Betrieb</em></h2>
<div class="scs">{schr}</div></div>
<div class="abs" style="left:{B+14}mm;right:{B+14}mm;bottom:{B+12}mm;display:flex;align-items:flex-end;justify-content:space-between">
<div class="kend"><div class="nm">{NAME}</div><div class="kl">{ROLLE} · {FIRMA}</div><div class="kl">{STR} · {ORT}</div>
<div class="kl"><b>{TEL_INT}</b> · {INFO}</div></div>
<div class="qr">{qr()}<span>{WEB}</span></div></div>'''
fcss = f'''h1{{font-weight:400;font-size:20pt;line-height:1.22;letter-spacing:-.01em}} h1 em,h2 em{{font-style:normal;color:{GRAU}}}
.lead{{font-size:8.6pt;line-height:1.6;color:{GRAU};margin-top:5mm;max-width:112mm}}
.vts{{margin-top:8mm;display:flex;flex-direction:column;gap:4.2mm}} .vt{{display:flex;gap:5mm;align-items:center}}
.vb{{width:21mm;height:14mm;flex:none}} .vt h3{{font-size:9pt;font-weight:700}} .vt p{{font-size:7.6pt;color:{GRAU};line-height:1.5;margin-top:.8mm}}
.band{{position:absolute;inset:0;background:{NAVY};color:#fff;padding:7.5mm {B+14}mm 0}}
.bt{{font-size:7.4pt;letter-spacing:.14em;color:#C9D0DE}} .bk{{margin-top:2.6mm;font-size:15pt;font-weight:700}}
.band .sym{{width:4.2mm;height:4.2mm;display:inline-block;vertical-align:-.7mm;margin-right:2.4mm}}
.bk2{{margin-top:2.6mm;font-size:8.2pt;display:flex;gap:9mm}} .bk2 .sym{{width:3.4mm;height:3.4mm}}
h2{{font-weight:400;font-size:14pt;line-height:1.25}} .h2b{{margin-top:8mm}}
.bers{{display:grid;grid-template-columns:1fr 1fr;gap:5mm 7mm;margin-top:6mm}} .ber:first-child{{grid-row:span 2}}
.ber h4{{font-size:7.6pt;font-weight:700;letter-spacing:.02em;padding-bottom:1.6mm;margin-bottom:1.6mm;border-bottom:.25mm solid {NAVY}}}
.li{{display:flex;align-items:center;gap:2.4mm;font-size:7.6pt;height:5.4mm}} .li .sym{{width:3.6mm;height:3.6mm;flex:none}}
.scs{{display:grid;grid-template-columns:repeat(4,1fr);gap:3.5mm;margin-top:5mm}}
.sc b{{display:flex;width:6.5mm;height:6.5mm;border:.3mm solid {NAVY};border-radius:50%;align-items:center;justify-content:center;font-size:7.5pt}}
.sc h5{{font-size:7.4pt;margin-top:2mm}} .sc p{{font-size:6.5pt;color:{GRAU};line-height:1.45;margin-top:.8mm}}
.nm{{font-weight:700;font-size:9.5pt}} .kl{{font-size:7pt;color:{GRAU};margin-top:1.1mm}} .kl b{{color:{NAVY}}}
.qr{{width:20mm;text-align:center;font-size:5.6pt;color:{GRAU}}} .qr svg{{width:20mm;height:20mm;margin-bottom:1.4mm}}'''
seiten('Flyer_A5_148x210mm_beidseitig_plus-3mm-Beschnitt_DRUCK.pdf', FW, FH, [a5_vorne, a5_hinten], fcss, ziel_dir=D, bleed=B,
       notiz='Seite 1 = Vorderseite, Seite 2 = Rückseite.')

# ---- DIN lang 99x210 ----
LW_, LH_ = 99 + 2 * B, 210 + 2 * B
vort2 = ''.join(f'<div class="vt">{vbild(d)}<div><h3>{t}</h3><p>{p}</p></div></div>' for t, p, d in VORTEILE)
dl_vorne = f'''<div class="abs" style="left:{B+10}mm;top:{B+14}mm;width:52mm">{lf}</div>
<div class="abs" style="left:{B+10}mm;right:{B+10}mm;top:{B+50}mm">
<h1>Gebäude in Ulm,<br><em>um Ulm und um Ulm herum</em></h1>
<p class="lead">Vom Hausmeisterdienst bis zur Haustechnik – mit einem festen Ansprechpartner, der Ihr Gebäude kennt.</p>
<div class="vts">{vort2}</div></div>
<div class="abs" style="left:0;right:0;bottom:0;height:{B+36}mm">{kontaktband(False)}</div>'''
bereiche2 = ''.join(f'<div class="ber"><h4>{t}</h4>{liste(l)}</div>' for t, l in BEREICHE)
dl_hinten = f'''<div class="abs" style="left:{B+10}mm;right:{B+10}mm;top:{B+12}mm">
<h2>Unsere <em>Leistungen</em></h2><div class="bers1">{bereiche2}</div></div>
<div class="abs" style="left:{B+10}mm;right:{B+10}mm;bottom:{B+10}mm;display:flex;align-items:flex-end;justify-content:space-between">
<div class="kend"><div class="nm">{NAME}</div><div class="kl"><b>{TEL_INT}</b></div><div class="kl">{INFO}</div></div>
<div class="qr" style="width:17mm">{qr()}<span>{WEB}</span></div></div>'''
dcss = fcss + f'''h1{{font-size:15pt}} .lead{{font-size:7.8pt;margin-top:4mm}} .vts{{margin-top:7mm;gap:4.5mm}}
.vt{{flex-direction:column;align-items:flex-start;gap:1.8mm}} .vb{{width:16mm;height:10.7mm}}
.band{{padding:6.5mm {B+10}mm 0}} .bk{{font-size:13pt}} .bk2{{flex-direction:column;gap:1.4mm;margin-top:2.2mm}}
h2{{font-size:13pt}} .bers1{{margin-top:4mm;display:flex;flex-direction:column;gap:3.6mm}}
.li{{height:4.75mm;font-size:7.2pt}} .qr svg{{width:17mm;height:17mm}}'''
seiten('Flyer_DIN-lang_99x210mm_beidseitig_plus-3mm-Beschnitt_DRUCK.pdf', LW_, LH_, [dl_vorne, dl_hinten], dcss, ziel_dir=D, bleed=B,
       notiz='Briefkasten-/Auslageformat. Seite 1 vorne, Seite 2 hinten.')

# ============ 04 Autoaufkleber (Folienplot = einfarbig, Schrift in Kurven) ============
D = '04_Auto-Beschriftung'
def nur_svg(inhalt, w, h):  # Vektor in mm-Koordinaten
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{inhalt}</svg>'
def logo_g(farbe, x, y, breite, sub=True):
    s, r = logo(farbe, sub)
    inner = s[s.index('>') + 1:s.rindex('</svg>')]
    sc = breite / LW
    return f'<g transform="translate({x} {y}) scale({sc}) translate({-LX} {-LY})">{inner}</g>', breite / r

for farbe, fn, bg in [('#FFFFFF', 'Weiss', '#3A3F47'), (NAVY, 'Navy', '#E9EBEF')]:
    # a) Logo fuer Fahrer-/Beifahrertuer
    for cm in (30, 45, 60):
        w = cm * 10; g, h = logo_g(farbe, 0, 0, w)
        svg = nur_svg(g, w, round(h, 1))
        nm = f'Aufkleber_Logo_Tuer_{cm}cm-breit_{fn}_Folie'
        svg_datei(D, nm + '.svg', svg, w, round(h, 1))
        seiten(nm + '.pdf', w, round(h, 1), [svg], ziel_dir=D, prevbg=bg)
    # b) komplette Seitenbeschriftung (Transporter): Logo + Leistungen + Telefon + Web
    for cm in (80, 100):
        w = cm * 10; lb = w * 0.62; g, h = logo_g(farbe, 0, 0, lb)
        y = h + w * 0.105; z1 = 'Hausmeisterdienst  ·  Haustechnik  ·  Modernisierung'
        p1 = tpfad(z1, w * 0.032, 0, y, fit=None)
        y2 = y + w * 0.085; p2 = tpfad(TEL, w * 0.068, 0, y2, 'b')
        y3 = y2 + w * 0.06; p3 = tpfad(WEB, w * 0.04, 0, y3)
        hh = round(y3 + w * 0.012, 1)
        svg = nur_svg(g + f'<path fill="{farbe}" d="{p1}{p2}{p3}"/>', w, hh)
        nm = f'Aufkleber_Seitenbeschriftung_Transporter_{cm}cm-breit_{fn}_Folie'
        svg_datei(D, nm + '.svg', svg, w, hh)
        seiten(nm + '.pdf', w, hh, [svg], ziel_dir=D, prevbg=bg)
    # c) Heckscheibe einzeilig
    for cm in (60, 80, 100):
        w = cm * 10; z = f'{WEB}   ·   {TEL}'
        size = w / (tbreite(z, 1) ); hh = round(size * 1.0, 1)
        p = tpfad(z, size, 0, size * 0.76)
        svg = nur_svg(f'<path fill="{farbe}" d="{p}"/>', w, hh)
        nm = f'Aufkleber_Heckscheibe_{cm}cm-breit_{fn}_Folie'
        svg_datei(D, nm + '.svg', svg, w, hh)
        seiten(nm + '.pdf', w, hh, [svg], ziel_dir=D, prevbg=bg)

# d) Magnetschild (gedruckt, abnehmbar) 50x30 und 60x40
for (mw, mh) in ((500, 300), (600, 400)):
    W2, H2 = mw + 2 * B, mh + 2 * B
    lb = mw * 0.5; s, r = logo('#FFFFFF', True)
    inhalt = f'''<div class="abs" style="inset:0;background:{NAVY}"></div>
<div class="abs" style="left:{B+mw*0.08}mm;top:{B+mh*0.1}mm;color:#fff;white-space:nowrap">
<div style="width:{lb}mm">{s}</div>
<div style="font-size:{mw*0.025}mm;color:#C9D0DE;letter-spacing:.04em;margin-top:{mh*0.075}mm">Hausmeisterdienst · Haustechnik · Modernisierung</div>
<div style="font-size:{mw*0.08}mm;font-weight:700;margin-top:{mh*0.035}mm;line-height:1.1">{TEL}</div>
<div style="font-size:{mw*0.042}mm;margin-top:{mh*0.015}mm">{WEB}</div></div>'''
    seiten(f'Magnetschild_Auto_{mw//10}x{mh//10}cm_plus-3mm-Beschnitt_DRUCK.pdf', W2, H2, [inhalt], ziel_dir=D, bleed=B)

# ============ 05 Stempel (schwarz, Kurven, Originalgroesse) ============
D = '05_Stempel'
for typ, w, h, zeilen_ in [
    ('Trodat-Printy-4912_47x18mm', 47, 18, [f'{NAME} · {STR} · {ORT}', f'Tel. {TEL} · {INFO}']),
    ('Trodat-Printy-4913_58x22mm', 58, 22, [f'{NAME} · {STR} · {ORT}', f'Tel. {TEL} · {INFO}', f'{WEB} · USt-IdNr. {UST}']),
    ('Trodat-Printy-4915_70x25mm', 70, 25, [f'{NAME} · {STR} · {ORT}', f'Tel. {TEL} · {INFO}', f'{WEB} · USt-IdNr. {UST}'])]:
    rand = 1.6; n = len(zeilen_)
    lh = h * (0.30 if n == 3 else 0.36); lbw = lh * LW / LH
    g, _ = logo_g('#000', round((w - lbw) / 2, 2), rand, lbw, sub=False)
    size = min((w - 2 * rand) / max(tbreite(z, 1) for z in zeilen_), h * 0.105)
    rest = h - rand - (rand + lh); step = rest / n
    pf = ''.join(tpfad(z, size, w / 2, rand + lh + step * (i + 0.5) + size * 0.42, anker='middle') for i, z in enumerate(zeilen_))
    svg = nur_svg(g + f'<path fill="#000" d="{pf}"/>', w, h)
    svg_datei(D, f'Stempel_{typ}_Schwarz_Originalgroesse.svg', svg, w, h)
    seiten(f'Stempel_{typ}_Schwarz_Originalgroesse.pdf', w, h, [svg], ziel_dir=D)

# ============ 06 Briefpapier A4 (DIN 5008 Form B) ============
D = '06_Briefpapier'
lb_, rb_ = logo(NAVY, True)
def brief(b=0):
    return f'''<div class="abs" style="right:{b+20}mm;top:{b+14}mm;width:56mm">{lb_}</div>
<div class="abs abs1" style="left:{b+20}mm;top:{b+47}mm">{FIRMA.replace(" – "," · ")} · {STR} · {ORT}</div>
<div class="abs fm" style="left:{b+4}mm;top:{b+105}mm"></div><div class="abs fm" style="left:{b+4}mm;top:{b+210}mm"></div>
<div class="abs fm lm" style="left:{b+4}mm;top:{b+148.5}mm"></div>
<div class="abs fz" style="left:{b+20}mm;right:{b+20}mm;bottom:{b+10}mm">
<div><b>{FIRMA}</b><br>Inhaber {NAME}<br>{STR} · {ORT}</div>
<div>Telefon {TEL_INT}<br>{INFO}<br>{WEB}</div>
<div>USt-IdNr. {UST}</div></div>'''
bcss = f'''.abs1{{font-size:6.6pt;color:{GRAU};letter-spacing:.02em}} .fm{{width:5mm;height:.25mm;background:{HELL}}} .lm{{width:7mm}}
.fz{{display:flex;justify-content:space-between;gap:6mm;font-size:6.6pt;line-height:1.6;color:{GRAU};border-top:.2mm solid {LINIE};padding-top:3mm}}
.fz b{{color:{NAVY};font-weight:400}}'''
seiten('Briefpapier_A4_DIN-5008_plus-3mm-Beschnitt_DRUCKEREI.pdf', 216, 303, [brief(B)], bcss, ziel_dir=D, bleed=B,
       notiz='Für die Druckerei (Vordruck auf 90–100 g Papier).')
seiten('Briefpapier_A4_zum-Selbstausdrucken.pdf', 210, 297, [brief(0)], bcss, ziel_dir=D)

# ============ 07 Aushang im Treppenhaus A4 ============
D = '07_Aushang_Treppenhaus'
aus = f'''<div class="abs" style="left:20mm;top:18mm;width:62mm">{lb_}</div>
<div class="abs" style="left:20mm;right:20mm;top:62mm">
<h1>Ihr Ansprechpartner<br><em>für dieses Gebäude</em></h1>
<p class="lead">Bei Schäden, Störungen oder Fragen rund ums Haus erreichen Sie uns direkt – wir kümmern uns.</p>
<div class="gross"><div class="nm">{NAME}</div>
<div class="tl">{sym(K["tel"], NAVY, 1.4)}{TEL_INT}</div>
<div class="ml">{sym(K["mail"], NAVY, 1.4)}{INFO}</div></div>
<div class="feld"><span>Objekt</span><i></i></div><div class="feld"><span>Regelmäßig vor Ort</span><i></i></div><div class="feld"><span>Hinweis</span><i></i></div>
</div>
<div class="abs not" style="left:20mm;bottom:20mm">Im Notfall zuerst: <b>Feuerwehr und Rettungsdienst 112</b> · <b>Polizei 110</b></div>
<div class="abs qr" style="right:20mm;bottom:17mm;width:26mm">{qr()}<span>{WEB}</span></div>'''
acss = f'''h1{{font-weight:400;font-size:28pt;line-height:1.18}} h1 em{{font-style:normal;color:{GRAU}}}
.lead{{font-size:11pt;line-height:1.6;color:{GRAU};margin-top:7mm;max-width:150mm}}
.gross{{margin-top:14mm}} .nm{{font-size:15pt;font-weight:700}} .tl{{font-size:26pt;font-weight:700;margin-top:4mm}} .ml{{font-size:13pt;margin-top:3mm}}
.sym{{display:inline-block;vertical-align:-1mm;margin-right:4mm}} .tl .sym{{width:9mm;height:9mm}} .ml .sym{{width:6mm;height:6mm}}
.feld{{display:flex;align-items:flex-end;gap:5mm;margin-top:11mm;font-size:9.5pt;color:{GRAU}}} .feld:first-of-type{{margin-top:18mm}}
.feld span{{width:42mm}} .feld i{{flex:1;border-bottom:.25mm solid {LINIE};height:6mm}}
.not{{font-size:9pt;color:{GRAU};max-width:120mm;line-height:1.6}} .not b{{color:{NAVY}}}
.qr{{text-align:center;font-size:7pt;color:{GRAU}}} .qr svg{{width:26mm;height:26mm;margin-bottom:2mm}}'''
seiten('Aushang_Treppenhaus_A4_Ansprechpartner_zum-Ausdrucken.pdf', 210, 297, [aus], acss, ziel_dir=D,
       notiz='Felder Objekt/Vor Ort/Hinweis von Hand ausfüllen.')

# ============ 08 Aufkleber fuer Technikraeume ============
D = '08_Aufkleber_Technik'
TW, TH = 70 + 2 * B, 35 + 2 * B
lt, _ = logo(NAVY, True)
tech = f'''<div class="abs" style="left:{B+4.5}mm;top:{B+4.5}mm;width:30mm">{lt}</div>
<div class="abs" style="left:{B+4.5}mm;bottom:{B+4.2}mm"><div class="t1">Störung oder Schaden? Bitte melden:</div><div class="t2">{TEL}</div></div>
<div class="abs qr" style="right:{B+4.5}mm;top:{B+4.5}mm;width:17mm">{qr()}<span>{WEB}</span></div>'''
tcss = f'''.t1{{font-size:5.4pt;color:{GRAU}}} .t2{{font-size:11.5pt;font-weight:700;margin-top:.8mm}}
.qr{{text-align:center;font-size:4.2pt;color:{GRAU}}} .qr svg{{width:17mm;height:17mm;margin-bottom:1mm}}'''
seiten('Aufkleber_Technikraum_Stoerung-melden_70x35mm_plus-3mm-Beschnitt_DRUCK.pdf', TW, TH, [tech], tcss, ziel_dir=D, bleed=B)
WW, WH = 60 + 2 * B, 40 + 2 * B
lw_, _ = logo('#FFFFFF', False)
wart = f'''<div class="abs" style="left:0;right:0;top:0;height:{B+10}mm;background:{NAVY}"></div>
<div class="abs" style="left:{B+4}mm;top:{B+2.6}mm;width:15mm">{lw_}</div>
<div class="abs wt" style="right:{B+4}mm;top:{B+3.6}mm">Wartungsnachweis</div>
<div class="abs" style="left:{B+4}mm;right:{B+4}mm;top:{B+13}mm">
{''.join(f'<div class="wf"><span>{t}</span><i></i></div>' for t in ('Anlage','Letzte Wartung','Nächste Wartung','Zeichen'))}</div>'''
wcss = f'''.wt{{color:#fff;font-size:6.4pt;letter-spacing:.12em}} .wf{{display:flex;align-items:flex-end;gap:2mm;height:6.2mm;font-size:5.6pt;color:{GRAU}}}
.wf span{{width:19mm}} .wf i{{flex:1;border-bottom:.2mm solid {HELL};height:4mm}}'''
seiten('Aufkleber_Wartungsnachweis_beschreibbar_60x40mm_plus-3mm-Beschnitt_DRUCK.pdf', WW, WH, [wart], wcss, ziel_dir=D, bleed=B)

# ============ 09 Arbeitskleidung ============
D = '09_Arbeitskleidung'
for farbe, fn, bg in [('#FFFFFF', 'Weiss-fuer-dunkle-Kleidung', NAVY), (NAVY, 'Navy-fuer-helle-Kleidung', '#E9EBEF')]:
    g, h = logo_g(farbe, 0, 0, 90); svg = nur_svg(g, 90, round(h, 1))
    nm = f'Textil_Brust-links_9cm_mit-Unterzeile_{fn}'
    svg_datei(D, nm + '.svg', svg, 90, round(h, 1)); seiten(nm + '.pdf', 90, round(h, 1), [svg], ziel_dir=D, prevbg=bg)
    g, h = logo_g(farbe, 0, 0, 90, sub=False); svg = nur_svg(g, 90, round(h, 1))
    nm = f'Textil_Brust-links_9cm_ohne-Unterzeile_fuer-Stick_{fn}'
    svg_datei(D, nm + '.svg', svg, 90, round(h, 1)); seiten(nm + '.pdf', 90, round(h, 1), [svg], ziel_dir=D, prevbg=bg)
    g, h = logo_g(farbe, 0, 0, 280); y = h + 280 * 0.12
    p = tpfad(WEB, 280 * 0.07, 140, y, anker='middle'); hh = round(y + 4, 1)
    svg = nur_svg(g + f'<path fill="{farbe}" d="{p}"/>', 280, hh)
    nm = f'Textil_Ruecken_28cm_mit-Webadresse_{fn}'
    svg_datei(D, nm + '.svg', svg, 280, hh); seiten(nm + '.pdf', 280, hh, [svg], ziel_dir=D, prevbg=bg)

# ============ 10 Banner 200x100 ============
D = '10_Banner_Bauzaun'
s, r = logo('#FFFFFF', True)
ban = f'''<div class="abs" style="inset:0;background:{NAVY}"></div>
<div class="abs" style="left:120mm;top:120mm;width:900mm">{s}</div>
<div class="abs" style="left:120mm;bottom:130mm;color:#fff">
<div style="font-size:52mm;color:#C9D0DE;letter-spacing:.04em">Hausmeisterdienst · Haustechnik · Modernisierung</div>
<div style="font-size:150mm;font-weight:700;margin-top:30mm;line-height:1">{TEL}</div>
<div style="font-size:72mm;margin-top:26mm">{WEB}</div></div>'''
seiten('Banner_Bauzaun-Geruest_200x100cm_Endformat_DRUCK.pdf', 2000, 1000, [ban], ziel_dir=D,
       notiz='Endformat ohne Beschnitt; Ösen-Rand 5 cm ist frei.')

# ============ Signatur-Logo (PNG fuer E-Mail) ============
s, r = logo(NAVY, True)
open(os.path.join(BAU, 'signatur_logo.html'), 'w').write(
    f'<!doctype html><html><head><style>html,body{{margin:0;background:transparent}} svg{{display:block;width:600px}}</style></head><body>{s}</body></html>')

json.dump(JOBS, open(os.path.join(BAU, 'jobs.json'), 'w'), ensure_ascii=False, indent=1)
print(len(JOBS), 'Druckdateien vorbereitet')
