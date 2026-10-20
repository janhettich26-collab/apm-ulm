# Ausfuellbare Vorlagen fuer APM Ulm (Jan/Emre 19.10.2026)
#   - Beauftragung (APM beauftragt Handwerker), Vorbild Valon-Auftragsschreiben (nur Aufbau)
#   - Auftragsbestaetigung (APM bestaetigt einen erhaltenen Auftrag)
# Design wie APM-Briefpapier, Fusszeile mit Bank wie Emres Rechnungen.
# Aufruf: python3 bau_auftrag.py [--muster]   (--muster = mit Beispielwerten ins Scratchpad zum Pruefen)
import os, sys, fitz

H = os.path.expanduser
MM = 72 / 25.4
OUT_DIR = H('~/Desktop/APM/08_Vorlagen_Auftraege')
PRUEF = '/private/tmp/claude-501/-Users-jan/1d190980-c514-4fe0-ba0d-7f23c0ee718d/scratchpad/vorlage'
DATEIEN = {'beauftragung': '2026-10-19_Vorlage_APM-Ulm_Beauftragung_ausfuellbar_V4.pdf',
           'bestaetigung': '2026-10-19_Vorlage_APM-Ulm_Auftragsbestaetigung_ausfuellbar_V4.pdf',
           'bestaetigung_apm': '2026-10-19_Vorlage_APM-Ulm_Auftragsbestaetigung_APM-Stil_ausfuellbar_V1.pdf'}
MUSTER = '--muster' in sys.argv
STRICHMAENNCHEN = False  # Spass-Figuren wie auf der Webseite (Jan 19.10.); False = ohne

def rgb(h): return tuple(int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
NAVY, GRAU, HELL, LINIE, GRUEN = rgb('#1C2840'), rgb('#566078'), rgb('#8C94A6'), rgb('#C9CDD6'), rgb('#2F8F5B')
FIRMA, INH, STR, ORT = 'APM Ulm – altun property management', 'Emre Altun', 'Weinbergweg 81', '89075 Ulm'
TEL, MAIL, INFO, WEB = '+49 170 5810174', 'emre.altun@apm-ulm.de', 'info@apm-ulm.de', 'www.apm-ulm.de'
UST, STNR = 'DE364898141', '88103/16902'
BANK, IBAN, BIC = 'Postbank Ndl der Deutsche Bank', 'DE55 6407 0215 0062 5525 00', 'DEUTDESSP14'
LOGO = H('~/Desktop/APM/01_Logo/2026-10-06_Logo_APM-Ulm_mit-altun-property-management/'
         'Logo_APM-Ulm_mit-altun-property-management_Navy_Vektor.pdf')
VR, VB = '/System/Library/Fonts/Supplemental/Verdana.ttf', '/System/Library/Fonts/Supplemental/Verdana Bold.ttf'
FONT = {'r': fitz.Font(fontfile=VR), 'b': fitz.Font(fontfile=VB)}
FN = {'r': 'verd', 'b': 'verdb'}

L, R = 20, 190          # Satzspiegel links/rechts (mm)
BODY, LH = 8.8, 4.55    # Fliesstext pt, Zeilenabstand mm
LBL = 6.8               # Feld-Ueberschriften pt
FELD = 9.5              # Eingabe pt
logo = fitz.open(LOGO)
doc = None

# Beispielwerte (nur --muster), Schluessel = Feldname
BSP = {
    'Datum': '19. Oktober 2026',
    'Empfaenger': 'Muster Hausverwaltung GmbH\nFrau Erika Muster\nIndustriestraße 5\n89079 Ulm',
    'Eigentuemer': 'Muster Immobilien GmbH, Hauptstraße 1, 89073 Ulm',
    'Leistungsort': 'Lise-Meitner-Str. 13, 89081 Ulm / 5146',
    'Auftragsnummer': '2026/0001/01', 'Externe_Auftragsnr': 'APM-2026-014', 'Auftragsart': 'Instandsetzung',
    'Gewerk': 'Beleuchtungsanlagen', 'Angebot_vom': '18.03.2026', 'Angebotsnummer': '103049',
    'Auftrag_vom': '13.04.2026', 'Angebot': '18.03.2026 / 103049',
    'Abrechnungsart': 'Pauschalpreis', 'Betrag': '1.911,27',
    'Leistung': 'Instandsetzung Tiefgarage Beleuchtung.',
    'Vertragsart': 'Werkvertrag VOB', 'Leistungszeitraum': '31.03.2026 – 15.04.2026',
    'Ansprechpartner': 'Hausmeister, Herr Max Beispiel\nTel. +49 160 0000000\nMail: hausmeister@example.de',
    'Rechnungsanschrift': 'Muster Immobilien GmbH\nc/o Muster Hausverwaltung GmbH\nIndustriestraße 5\n89079 Ulm',
    'Leistungsempfaenger': 'Muster Immobilien GmbH\nHauptstraße 1\n89073 Ulm',
    'Rechnung_Mail': 'rechnung@example.de',
}

# ---------- Bausteine ----------
def text(p, x, y, t, size=BODY, w='r', col=NAVY):
    """y = Grundlinie in mm"""
    p.insert_text((x * MM, y * MM), t, fontname=FN[w], fontsize=size, color=col)

def breite(t, size=BODY, w='r'): return FONT[w].text_length(t, fontsize=size) / MM

def absatz(p, y, t, size=BODY, w='r', col=NAVY, x=L, bis=R):
    """Umbruch nach Breite, gibt die Grundlinie der naechsten Zeile zurueck"""
    zeile = ''
    for wort in t.split(' '):
        probe = (zeile + ' ' + wort).strip()
        if breite(probe, size, w) > bis - x and zeile:
            text(p, x, y, zeile, size, w, col); y += LH; zeile = wort
        else:
            zeile = probe
    if zeile: text(p, x, y, zeile, size, w, col); y += LH
    return y

def feld(p, name, x, y, b, h, tip, multi=False, fett=False, wert='', size=FELD):
    """Eingabefeld, (x,y) = obere linke Ecke in mm"""
    wd = fitz.Widget()
    wd.field_type = fitz.PDF_WIDGET_TYPE_TEXT
    wd.field_name = name
    wd.field_label = tip
    wd.rect = fitz.Rect(x * MM, y * MM, (x + b) * MM, (y + h) * MM)
    wd.text_font = 'HeBo' if fett else 'Helv'
    wd.text_fontsize = size
    wd.text_color = NAVY
    wd.border_width = 0
    wd.fill_color = None
    if multi: wd.field_flags |= fitz.PDF_TX_FIELD_IS_MULTILINE
    wd.field_value = BSP.get(name, wert) if MUSTER else wert
    return p.add_widget(wd)

def label(p, x, y, t): text(p, x, y, t, LBL, 'r', GRAU)

def linie(p, y, x0=L, x1=R, col=LINIE, d=0.6):
    p.draw_line((x0 * MM, y * MM), (x1 * MM, y * MM), color=col, width=d)

def zelle(p, x, y, b, lab, name, tip=None):
    label(p, x, y + 4.4, lab)
    feld(p, name, x - 0.4, y + 5.4, b, 5.2, tip or lab)

def maennchen(p, x, y, art='winkt', s=0.36):
    """Strichmaennchen wie auf apm-ulm.de (Kopf r4, Koerper, Arme, Beine); (x,y) = Fusspunkt in mm"""
    if not STRICHMAENNCHEN: return
    P = lambda a, b: fitz.Point((x + a * s) * MM, (y + b * s) * MM)
    sh = p.new_shape()
    sh.draw_circle(P(0, -25), 4 * s * MM)
    wege = [[(0, -21), (0, -10)], [(0, -10), (-2.5, 0)], [(0, -10), (3, 0)]]
    if art == 'winkt':      # ein Arm hoch zum Winken
        wege += [[(0, -18), (6, -12)], [(0, -18), (-7, -21), (-9, -28)]]
    elif art == 'ok':       # haelt einen gruenen Haken hoch
        wege += [[(0, -18), (-6, -12)], [(0, -18), (6, -22), (9, -27)]]
    elif art == 'koffer':   # traegt einen Werkzeugkoffer
        wege += [[(0, -18), (-6, -12)], [(0, -18), (5, -13), (7, -8)]]
    for w in wege:
        sh.draw_polyline([P(*q) for q in w])
    sh.finish(color=NAVY, width=0.7, closePath=False, lineCap=1, lineJoin=1)
    if art == 'koffer':
        sh.draw_rect(fitz.Rect(P(3.5, -8), P(11.5, -2)))
        sh.draw_polyline([P(6, -8), P(6, -9.5), P(9, -9.5), P(9, -8)])
        sh.finish(color=NAVY, width=0.7, closePath=False, lineCap=1, lineJoin=1)
    sh.commit()
    if art == 'ok':
        k = p.new_shape()
        k.draw_circle(P(11, -33), 5.5 * s * MM)
        k.draw_polyline([P(8.4, -33), P(10.3, -31), P(13.8, -35)])
        k.finish(color=GRUEN, width=0.7, closePath=False, lineCap=1, lineJoin=1)
        k.commit()

FUSS = [[(FIRMA.split(' – ')[0], NAVY), ('altun property management', GRAU), (STR, GRAU), (ORT, GRAU)],
        [(f'Telefon {TEL}', GRAU), (f'E-Mail {INFO}', GRAU), (f'Website {WEB}', GRAU)],
        [(f'USt-IdNr. {UST}', GRAU), (f'Steuer-Nr. {STNR}', GRAU), (f'Inhaber {INH}', GRAU)],
        [(BANK, GRAU), (f'IBAN {IBAN}', GRAU), (f'BIC {BIC}', GRAU)]]

def rahmen(p, nr, n):
    """Logo, Falzmarken, Fusszeile (4 Spalten, gleichmaessig verteilt)"""
    for k, f in FN.items(): p.insert_font(fontname=f, fontfile=VR if k == 'r' else VB)
    lw = 56; lh = lw * logo[0].rect.height / logo[0].rect.width
    p.show_pdf_page(fitz.Rect((R - lw) * MM, 14 * MM, R * MM, (14 + lh) * MM), logo, 0)
    for y, b in ((105, 5), (148.5, 7), (210, 5)):
        linie(p, y, 4, 4 + b, HELL, 0.7)
    linie(p, 271, col=LINIE, d=0.55)
    bw = [max(breite(t, 6.6) for t, _ in sp) for sp in FUSS]
    gap = (R - L - sum(bw)) / (len(FUSS) - 1)
    x = L
    for sp, b in zip(FUSS, bw):
        for i, (t, c) in enumerate(sp):
            text(p, x, 276 + i * 3.45, t, 6.6, 'r', c)
        x += b + gap
    s = f'Seite {nr} von {n}'
    text(p, R - breite(s, 6.6), 268, s, 6.6, 'r', HELL)

def kopf(p, titel):
    text(p, L, 49.4, f'APM Ulm · altun property management · {STR} · {ORT}', 6.6, 'r', GRAU)
    feld(p, 'Empfaenger', L, 55, 85, 27, 'Empfänger: Firma, z. Hd., Straße, PLZ Ort', multi=True)
    x2 = 125
    label(p, x2, 57.4, 'Ihr Ansprechpartner')
    text(p, x2, 62.4, INH, BODY, 'b')
    text(p, x2, 66.9, f'Telefon {TEL}', 8.2, 'r', GRAU)
    text(p, x2, 71.2, f'E-Mail {MAIL}', 8.2, 'r', GRAU)
    text(p, x2, 75.5, f'Website {WEB}', 8.2, 'r', GRAU)
    label(p, x2, 82, 'Datum')
    feld(p, 'Datum', x2 - 0.4, 83, R - x2 + 0.4, 5.2, 'Datum, z. B. 19. Oktober 2026')
    text(p, L, 99, titel, 13, 'b')

def datenblock(p, zellen):
    """Eigentuemer + Leistungsort volle Breite, danach 6 Felder in 3 Spalten"""
    y = 104
    linie(p, y)
    zelle(p, L, y, R - L, 'Eigentümer/in', 'Eigentuemer', 'Eigentümer/in mit Anschrift')
    zelle(p, L, y + 10.5, R - L, 'Leistungsort / Objekt-Nr.', 'Leistungsort')
    c = (R - L) / 3
    for i, (lab, name) in enumerate(zellen):
        zelle(p, L + (i % 3) * c, y + 21 + (i // 3) * 10.5, c - 3, lab, name)
    y += 21 + 2 * 10.5 + 1.5
    linie(p, y)
    return y

def betragzeile(p, y):
    linie(p, y - 1.5, d=0.4)
    label(p, L, y + 3.2, 'Abrechnung nach')
    feld(p, 'Abrechnungsart', L - 0.4, y + 4.2, 70, 5.4, 'Abrechnungsart, z. B. Pauschalpreis', wert='Pauschalpreis')
    label(p, 107, y + 3.2, 'Auftragssumme in € netto')
    feld(p, 'Betrag', 106.6, y + 4.2, R - 106.6, 5.6, 'Betrag in Euro netto, z. B. 1.911,27', fett=True, size=11)
    y += 12.5
    linie(p, y, d=0.4)
    return y

def vertrag_zeitraum(p, y, zeitraum='Leistungszeitraum'):
    label(p, L, y + 1, 'Art des Vertrages')
    feld(p, 'Vertragsart', L - 0.4, y + 2, 80, 5.2, 'Art des Vertrages, z. B. Werkvertrag VOB')
    label(p, 107, y + 1, zeitraum)
    feld(p, 'Leistungszeitraum', 106.6, y + 2, R - 106.6, 5.2, f'{zeitraum}, z. B. 31.03.2026 – 15.04.2026')
    return y + 14

def gruss(p, y):
    text(p, L, y, 'Mit freundlichen Grüßen', BODY)
    y += 20
    text(p, L, y, INH, BODY, 'b')
    text(p, L, y + LH, FIRMA, BODY, 'r', GRAU)
    return y

def speichern(art):
    doc.set_metadata({'title': ('Beauftragung' if art == 'beauftragung' else 'Auftragsbestätigung') + ' – APM Ulm',
                      'author': FIRMA, 'creator': 'APM Ulm'})
    if MUSTER:
        ziel = os.path.join(PRUEF, f'muster_{art}.pdf')
    else:
        os.makedirs(OUT_DIR, exist_ok=True); ziel = os.path.join(OUT_DIR, DATEIEN[art])
    doc.save(ziel, garbage=3, deflate=True)
    print(ziel)

# ================= Beauftragung =================
def beauftragung():
    global doc
    doc = fitz.open()
    p = doc.new_page(width=210 * MM, height=297 * MM)
    rahmen(p, 1, 2)
    kopf(p, 'Beauftragung')
    y = datenblock(p, [('Auftragsnummer', 'Auftragsnummer'), ('Externe Auftragsnr.', 'Externe_Auftragsnr'),
                       ('Auftragsart', 'Auftragsart'), ('Gewerk / Bereich', 'Gewerk'),
                       ('Gemäß Angebot vom', 'Angebot_vom'), ('Angebotsnummer', 'Angebotsnummer')])
    y += 8
    text(p, L, y, 'Sehr geehrte Damen und Herren,', BODY)
    y += 7.5
    y = absatz(p, y, 'hiermit beauftragen wir Sie namens und in Vollmacht der o. g. Eigentümerin. Die Beauftragung '
                     'erfolgt auf Grundlage des o. g. Angebots bis zu der unten genannten Auftragssumme, inkl. '
                     'sämtlicher Nebenkosten, zzgl. der gesetzlichen Umsatzsteuer.')
    y = betragzeile(p, y + 3)
    y += 7.5
    y = absatz(p, y, 'Die nachfolgend aufgeführten Leistungen sind auf Grundlage der anerkannten Regeln der Technik auszuführen:')
    feld(p, 'Leistung', L - 0.4, y - 2.9, R - L + 0.4, 15, 'Leistungsbeschreibung', multi=True, fett=True, size=BODY + 0.4)
    y = vertrag_zeitraum(p, y + 15.5)
    label(p, L, y, 'Ihr Ansprechpartner vor Ort')
    feld(p, 'Ansprechpartner', L - 0.4, y + 1.2, 110, 17, 'Ansprechpartner vor Ort: Name, Telefon, Mail', multi=True)
    text(p, L, y + 22, 'Bitte stimmen Sie die Terminvereinbarung direkt mit diesem Ansprechpartner ab.', BODY)
    maennchen(p, 156, 271, 'winkt', 0.42)

    p = doc.new_page(width=210 * MM, height=297 * MM)
    rahmen(p, 2, 2)
    y = 50
    text(p, L, y, 'Rechnungsstellung', 11, 'b')
    y += 7
    label(p, L, y, 'Rechnungsanschrift')
    feld(p, 'Rechnungsanschrift', L - 0.4, y + 1.2, 82, 22, 'Rechnungsanschrift', multi=True)
    label(p, 107, y, 'Leistungsempfänger')
    feld(p, 'Leistungsempfaenger', 106.6, y + 1.2, R - 106.6, 22, 'Leistungsempfänger', multi=True)
    y += 31
    y = absatz(p, y, 'Zur Bezahlung der Rechnung sind folgende Angaben aufzunehmen und Nachweise beizulegen:')
    y += 1
    for t in ['Auftragsnummer', 'externe Auftragsnummer',
              'unterschriebener Arbeitsnachweis und/oder Materialverbrauchszettel und/oder Wartungsbericht und/oder Prüfbericht',
              'Leistungsempfänger', 'Leistungszeitraum']:
        p.draw_circle(((L + 1.3) * MM, (y - 1.15) * MM), 0.55 * MM, color=None, fill=NAVY)
        y = absatz(p, y, t, x=L + 5)
    y += 3
    label(p, L, y, 'Rechnungsversand per E-Mail an')
    feld(p, 'Rechnung_Mail', L - 0.4, y + 1.2, 100, 5.4, 'E-Mail-Adresse für Rechnungen', wert=INFO)
    y += 13
    y = absatz(p, y, 'Bitte fassen Sie die Rechnung inklusive aller Angaben und Nachweise in einer PDF-Datei zusammen.')
    y += 6
    text(p, L, y, 'Vertraulichkeit', BODY, 'b'); y += LH + 0.5
    y = absatz(p, y, 'Der Auftragnehmer verpflichtet sich, sämtliche im Rahmen der durchzuführenden Arbeiten erlangten '
                     'Informationen und Kenntnisse streng vertraulich zu behandeln. Diese Informationen sind ausschließlich '
                     'mit dem Auftraggeber zu teilen und dürfen nicht an den Mieter oder sonstige Dritte weitergegeben '
                     'werden. Diese Vertraulichkeitsverpflichtung gilt auch nach Abschluss der beauftragten Arbeiten fort.')
    y += 6
    y = absatz(p, y, 'Bei weiteren Rückfragen können Sie uns gerne kontaktieren.')
    gruss(p, y + 4)
    maennchen(p, 156, 271, 'koffer', 0.42)
    speichern('beauftragung')

# ================= Auftragsbestaetigung (Aufbau wie Valon-Vorlage, Jan 19.10.) =================
AR, ARB = '/System/Library/Fonts/Supplemental/Arial.ttf', '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
HF, HB = fitz.Font(fontfile=AR), fitz.Font(fontfile=ARB)   # Arial = Helvetica-Masse, passt zu den Formularfeldern
SZ, ZL = 9.5, 4.3   # Schriftgroesse pt, Zeilenabstand mm
VX = 64             # Spalte fuer Werte im Datenblock

def ht(p, x, y, t, b=False, size=SZ, col=NAVY):
    p.insert_text((x * MM, y * MM), t, fontname='ariab' if b else 'aria', fontsize=size, color=col)

def hw(t, b=False, size=SZ): return (HB if b else HF).text_length(t, fontsize=size) / MM

def hzeilen(p, y, t, b=False, x=L, bis=R):
    zeile = ''
    for wort in t.split(' '):
        probe = (zeile + ' ' + wort).strip()
        if hw(probe, b) > bis - x and zeile:
            ht(p, x, y, zeile, b); y += ZL; zeile = wort
        else:
            zeile = probe
    if zeile: ht(p, x, y, zeile, b); y += ZL
    return y

def hfeld(p, name, x, y, b, zeilen=1, tip='', fett=False, wert='', rechts=False):
    """Feld so gesetzt, dass die erste Textzeile auf Grundlinie y steht"""
    h = 4.6 + (zeilen - 1) * ZL
    w = feld(p, name, x - 0.2, y - 3.4, b + 0.2, h, tip, multi=zeilen > 1, fett=fett, wert=wert, size=SZ)
    if rechts:
        doc.xref_set_key(w.xref, 'Q', '2'); w.update()
    return w

def rahmen_v(p):
    p.insert_font(fontname='aria', fontfile=AR); p.insert_font(fontname='ariab', fontfile=ARB)
    lw = 56; lh = lw * logo[0].rect.height / logo[0].rect.width
    p.show_pdf_page(fitz.Rect((R - lw) * MM, 14 * MM, R * MM, (14 + lh) * MM), logo, 0)
    for y, b in ((105, 5), (148.5, 7), (210, 5)):
        linie(p, y, 4, 4 + b, HELL, 0.7)
    sp = [[('APM Ulm – altun property management', False), (f'Inhaber {INH}', False),
           (f'Steuer-Nr. {STNR}', False), (f'USt-IdNr. {UST}', False)],
          [(f'Telefon {TEL}', False), (f'E-Mail {INFO}', False), (f'Website {WEB}', False)],
          [('Anschrift', True), (STR, False), (ORT, False)],
          [('Bankverbindung', True), (BANK, False), (f'IBAN {IBAN}', False), (f'BIC {BIC}', False)]]
    bw = [max(hw(t, b, 6.5) for t, b in s) for s in sp]
    gap = (R - L - sum(bw)) / 3
    x = L
    for i, (s, b_) in enumerate(zip(sp, bw)):
        if i >= 2:
            p.draw_line(((x - gap / 2) * MM, 273.5 * MM), ((x - gap / 2) * MM, 287 * MM), color=NAVY, width=0.4)
        for k, (t, b) in enumerate(s):
            ht(p, x, 276 + k * 3.1, t, b, 6.5, NAVY if b else GRAU)
        x += b_ + gap

def bestaetigung():
    global doc
    doc = fitz.open()
    p = doc.new_page(width=210 * MM, height=297 * MM)
    rahmen_v(p)
    ht(p, L, 48, 'APM Ulm – altun property management', size=6.8, col=GRAU)
    ht(p, L, 51, f'{STR} · {ORT}', size=6.8, col=GRAU)
    hfeld(p, 'Empfaenger', L, 64, 90, 5, 'Empfänger: Firma, z. Hd., Straße, PLZ Ort')
    x2 = 125
    ht(p, x2, 63, INH, True)
    ht(p, x2, 67.3, f'Telefon {TEL}')
    ht(p, x2, 71.6, f'E-Mail {MAIL}')
    ht(p, x2, 75.9, f'Website {WEB}')
    ht(p, x2, 84.5, 'Ulm,')
    hfeld(p, 'Datum', x2 + hw('Ulm, '), 84.5, R - x2 - hw('Ulm, '), tip='Datum, z. B. 19. Oktober 2026')

    ht(p, L, 97, 'Auftragsbestätigung', True, 11)
    y = 105
    for e in [('Eigentümerin:', 'Eigentuemer'), ('Leistungsort / Objekt-Nr.:', 'Leistungsort'),
                      ('Ihre Auftragsnummer:', 'Auftragsnummer'), ('Unsere Auftragsnr.:', 'Externe_Auftragsnr'),
                      None,
                      ('Auftragsart:', 'Auftragsart'), ('Gewerk / Bereich:', 'Gewerk'),
                      ('Gemäß Angebot vom:', 'Angebot_vom'), ('Angebotsnummer:', 'Angebotsnummer')]:
        if e is None: y += 2.6; continue
        lab, name = e
        ht(p, L, y, lab, True)
        hfeld(p, name, VX, y, R - VX, tip=lab.rstrip(':'))
        y += ZL
    y += 6
    ht(p, L, y, 'Sehr geehrte Damen und Herren,'); y += ZL * 2
    t1 = 'vielen Dank für Ihren Auftrag. Hiermit bestätigen wir die Beauftragung zur Abrechnung nach'
    ht(p, L, y, t1)
    hfeld(p, 'Abrechnungsart', L + hw(t1 + ' '), y, R - L - hw(t1 + ' '), tip='Abrechnungsart', wert='Pauschalpreis.')
    y += ZL
    ht(p, L, y, 'Die Ausführung erfolgt auf Grundlage des o. g. Angebots bis zu einer Auftragssumme in Höhe von'); y += ZL
    bb = 24
    hfeld(p, 'Betrag', L, y, bb, tip='Betrag in Euro netto, z. B. 1.911,27', fett=True, rechts=True)
    ht(p, L + bb + 0.3, y, '€ netto,', True)
    ht(p, L + bb + 0.3 + hw('€ netto, ', True), y, 'inkl. sämtlicher Nebenkosten zzgl. der gesetzlichen Umsatzsteuer.')
    y += ZL * 2
    y = hzeilen(p, y, 'Die nachfolgend aufgeführten Leistungen führen wir auf Grundlage der anerkannten Regeln der Technik aus:')
    y += ZL
    hfeld(p, 'Leistung', L, y, R - L, 3, 'Leistungsbeschreibung', fett=True)
    y += ZL * 4
    for lab, name, tip in [('Art des Vertrages:', 'Vertragsart', 'z. B. Werkvertrag VOB'),
                           ('Leistungszeitraum:', 'Leistungszeitraum', 'z. B. 31.03.2026 – 15.04.2026')]:
        ht(p, L, y, lab, True)
        x = L + max(hw('Art des Vertrages:', True), hw('Leistungszeitraum:', True)) + 2
        hfeld(p, name, x, y, R - x, tip=f'{lab.rstrip(":")}, {tip}')
        y += ZL
    y += ZL
    ht(p, L, y, 'Ihr Ansprechpartner vor Ort:', True); y += ZL
    hfeld(p, 'Ansprechpartner', L, y, 120, 3, 'Ansprechpartner vor Ort: Name, Telefon, Mail')
    y += ZL * 3
    ht(p, L, y, 'Die Terminvereinbarung stimmen wir direkt mit diesem Ansprechpartner ab.')
    y += ZL * 2
    ht(p, L, y, 'Rechnungsanschrift:', True); y += ZL
    hfeld(p, 'Rechnungsanschrift', L, y, 120, 4, 'Rechnungsanschrift')

    p = doc.new_page(width=210 * MM, height=297 * MM)
    rahmen_v(p)
    y = 50
    ht(p, L, y, 'Leistungsempfänger:', True); y += ZL
    hfeld(p, 'Leistungsempfaenger', L, y, 120, 4, 'Leistungsempfänger')
    y += ZL * 5
    y = hzeilen(p, y, 'Unsere Rechnung enthält folgende Angaben, die Nachweise legen wir bei:')
    for t in ['Auftragsnummer', 'externe Auftragsnummer',
              'Unterschriebener Arbeitsnachweis und/oder Materialverbrauchszettel und/oder Wartungsbericht',
              'und/oder Prüfbericht', 'Leistungsempfänger', 'Leistungszeitraum']:
        if t.startswith('und/'):
            ht(p, L + 3.2, y, t)
        else:
            ht(p, L + 1, y, '-'); ht(p, L + 3.2, y, t)
        y += ZL
    y += ZL
    t2 = 'Die Rechnung senden wir per Mail an'
    ht(p, L, y, t2)
    hfeld(p, 'Rechnung_Mail', L + hw(t2 + ' '), y, 90, tip='E-Mail-Adresse für Rechnungen')
    y += ZL
    ht(p, L, y, 'Hierbei fassen wir die Rechnung inklusive aller Angaben und Nachweise in einem PDF zusammen.')
    y += ZL * 2
    y = hzeilen(p, y, 'Sämtliche im Rahmen der durchzuführenden Arbeiten erlangten Informationen und Kenntnisse behandeln '
                      'wir streng vertraulich. Diese Informationen teilen wir ausschließlich mit dem Auftraggeber und geben '
                      'sie nicht an den Mieter oder sonstige Dritte weiter. Diese Vertraulichkeitsverpflichtung gilt auch '
                      'nach Abschluss der beauftragten Arbeiten fort.')
    y += ZL
    ht(p, L, y, 'Bei weiteren Rückfragen können Sie uns gerne kontaktieren.'); y += ZL * 2
    ht(p, L, y, 'Mit freundlichen Grüßen'); y += ZL * 2
    ht(p, L, y, FIRMA)
    speichern('bestaetigung')


# ================= Auftragsbestaetigung im APM-Stil (wie Beauftragung, Jan 19.10.) =================
def bestaetigung_apm():
    global doc
    doc = fitz.open()
    p = doc.new_page(width=210 * MM, height=297 * MM)
    rahmen(p, 1, 2)
    kopf(p, 'Auftragsbestätigung')
    y = datenblock(p, [('Ihre Auftragsnummer', 'Auftragsnummer'), ('Ihr Auftrag vom', 'Auftrag_vom'),
                       ('Unsere Auftragsnr.', 'Externe_Auftragsnr'), ('Auftragsart', 'Auftragsart'),
                       ('Gewerk / Bereich', 'Gewerk'), ('Unser Angebot vom / Nr.', 'Angebot')])
    y += 8
    text(p, L, y, 'Sehr geehrte Damen und Herren,', BODY)
    y += 7.5
    y = absatz(p, y, 'vielen Dank für Ihren Auftrag. Hiermit bestätigen wir die Beauftragung auf Grundlage Ihres '
                     'Auftragsschreibens und unseres o. g. Angebots. Die Auftragssumme versteht sich inkl. sämtlicher '
                     'Nebenkosten, zzgl. der gesetzlichen Umsatzsteuer.')
    y = betragzeile(p, y + 3)
    y += 7.5
    y = absatz(p, y, 'Wir führen die folgenden Leistungen nach den anerkannten Regeln der Technik aus:')
    feld(p, 'Leistung', L - 0.4, y - 2.9, R - L + 0.4, 15, 'Leistungsbeschreibung', multi=True, fett=True, size=BODY + 0.4)
    y = vertrag_zeitraum(p, y + 15.5, 'Ausführungszeitraum')
    label(p, L, y, 'Ihr Ansprechpartner vor Ort')
    feld(p, 'Ansprechpartner', L - 0.4, y + 1.2, 110, 17, 'Ansprechpartner vor Ort: Name, Telefon, Mail', multi=True)
    text(p, L, y + 22, 'Die Termine stimmen wir direkt mit Ihrem Ansprechpartner vor Ort ab.', BODY)

    p = doc.new_page(width=210 * MM, height=297 * MM)
    rahmen(p, 2, 2)
    y = 50
    text(p, L, y, 'Rechnungsstellung', 11, 'b')
    y += 7
    label(p, L, y, 'Rechnungsanschrift')
    feld(p, 'Rechnungsanschrift', L - 0.4, y + 1.2, 82, 22, 'Rechnungsanschrift', multi=True)
    label(p, 107, y, 'Leistungsempfänger')
    feld(p, 'Leistungsempfaenger', 106.6, y + 1.2, R - 106.6, 22, 'Leistungsempfänger', multi=True)
    y += 31
    y = absatz(p, y, 'Nach Abschluss der Arbeiten erhalten Sie unsere Rechnung mit allen geforderten Angaben '
                     '(Auftragsnummer, Leistungsempfänger, Leistungszeitraum) und den unterschriebenen Nachweisen '
                     'in einer PDF-Datei per E-Mail an:')
    feld(p, 'Rechnung_Mail', L - 0.4, y - 2.6, 100, 5.4, 'E-Mail-Adresse für Rechnungen')
    y += 10
    text(p, L, y, 'Vertraulichkeit', BODY, 'b'); y += LH + 0.5
    y = absatz(p, y, 'Alle Informationen, die wir im Rahmen der Arbeiten erhalten, behandeln wir streng vertraulich. '
                     'Wir teilen sie ausschließlich mit Ihnen als Auftraggeber und geben sie nicht an Mieter oder '
                     'sonstige Dritte weiter – auch nach Abschluss der Arbeiten.')
    y += 6
    y = absatz(p, y, 'Für Rückfragen stehen wir Ihnen gerne zur Verfügung.')
    gruss(p, y + 4)
    speichern('bestaetigung_apm')

beauftragung()          # APM-Stil
bestaetigung()          # Aufbau wie Valon-Vorlage
bestaetigung_apm()      # APM-Stil
