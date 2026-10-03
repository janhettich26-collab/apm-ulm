# Baut index.html der Variante D (Layout nach Vorbild duu-mbh.de, Leistungen in zwei Bereichen)
I = {
 'objekt': '<circle cx="8" cy="15" r="4"/><path d="M11 12l8-8M16 7l2 2M14 9l2 2"/>',
 'doku': '<path d="M7 3h7l5 5v13H7zM14 3v5h5M10 13h6M10 17h6"/>',
 'gruen': '<path d="M5 19c0-8 5-13 14-14 0 9-5 14-13 14M5 19c3-5 6-8 10-10"/>',
 'winter': '<path d="M12 2v20M4.2 6.5l15.6 11M19.8 6.5 4.2 17.5M9.5 3.5 12 6l2.5-2.5M9.5 20.5 12 18l2.5 2.5"/>',
 'galabau': '<path d="M12 22v-7M12 15c-4 0-6-2.5-6-5.5S8.5 3 12 3s6 3.5 6 6.5-2 5.5-6 5.5z"/>',
 'pforte': '<circle cx="12" cy="8" r="3.6"/><path d="M4.5 21c.6-4.2 3.6-6.6 7.5-6.6s6.9 2.4 7.5 6.6"/>',
 'park': '<path d="M4 4h16v16H4zM9 17V7h3.5a3 3 0 0 1 0 6H9"/>',
 'abfall': '<path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13M10 11v6M14 11v6"/>',
 'rein': '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8zM19 16v5M16.5 18.5h5"/>',
 'betreiber': '<path d="M12 3l7 3v5.5c0 4.5-3 8-7 9.5-4-1.5-7-5-7-9.5V6zM9 12l2.2 2.2L15.5 10"/>',
 'cafm': '<path d="M3.5 5h17v11h-17zM9 20h6M12 16v4M7 12l3-3 2.5 2.5L17 8"/>',
 'wartung': '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.2L3.5 17.3a1.8 1.8 0 0 0 2.6 2.6l5.8-5.8a4 4 0 0 0 5.2-5.4l-2.6 2.6-2.4-.4-.4-2.4z"/>',
 'instand': '<path d="M14 5l5 5-2.5 2.5-5-5zM11.5 7.5l-8 8a1.8 1.8 0 0 0 2.6 2.6l8-8"/>',
 'brand': '<path d="M12 21c4 0 6.5-2.6 6.5-6.2 0-3.4-2.4-5.6-3.6-8.3-.5 1.8-1.4 3-2.6 3.6C12.5 7 11.2 4.6 9 3c.3 3-1.6 5-2.9 6.8A7 7 0 0 0 5.5 14.8C5.5 18.4 8 21 12 21z"/>',
 'stoer': '<path d="M6 16.5V11a6 6 0 1 1 12 0v5.5l1.5 2h-15zM10 21h4"/>',
 'omgmt': '<path d="M5 21V4h9v17M14 9h5v12M3 21h18M8 8h3M8 12h3M8 16h3"/>',
 'gewaehr': '<path d="M8 4h8v3H8zM6 5.5H5v15h14v-15h-1M9 14l2 2 4-4.5"/>',
}
svg = lambda k: f'<svg viewBox="0 0 24 24" aria-hidden="true">{I[k]}</svg>'
# (Schluessel, Titel, Unterpunkte, Kurztext)
INFRA = [
 ('objekt','Objektbetreuung',[], 'Hausmeister und Gebäudetechniker als fester Ansprechpartner im Objekt: Rundgänge, Kleinreparaturen, Schlüssel und Zugänge.'),
 ('doku','Dokumentation',[], 'Nutzerinformationen, Aushänge und Protokolle – alles zum Objekt geordnet und nachvollziehbar.'),
 ('gruen','Grünanlagenpflege',['Rasen-, Gehölz-, Hecken- und Baumschnitt','Pflege von Beeten, Vorgärten und Pflanzgefäßen','Bewässerung und Düngung','Entsorgung von Grünschnitt und Laub'], 'Schnitt, Pflege, Bewässerung und Laubentsorgung für alle Grünflächen der Liegenschaft.'),
 ('winter','Winterdienst',[], 'Räumen und Streuen von Wegen, Zufahrten und Parkflächen – früh genug, damit die Verkehrssicherungspflicht erfüllt ist.'),
 ('galabau','Garten- und Landschaftsbau',[], 'Außenanlagen herrichten, instand setzen, neu bepflanzen oder umgestalten.'),
 ('pforte','Post- und Pförtnerdienste',[], 'Empfang, Postverteilung und Pforte, damit im Haus alles an der richtigen Stelle ankommt.'),
 ('park','Parkhausdienste',[], 'Ordnung, Kontrolle und sicherer Ablauf in Parkhäusern und Tiefgaragen.'),
 ('abfall','Abfallmanagement',[], 'Tonnen pünktlich bereitstellen, Standplätze sauber halten, Entsorgung koordinieren.'),
 ('rein','Reinigung und Pflege',[], 'Unterhaltsreinigung der Allgemeinflächen innen und außen – gesteuert und kontrolliert aus einer Hand.'),
]
TECH = [
 ('betreiber','Betreiberverantwortung',[], 'Wir achten darauf, dass Prüfungen und Wartungen der technischen Anlagen fristgerecht stattfinden und belegt sind.'),
 ('cafm','Digitale Objektakte (CAFM)',['Anlagen und Stammdaten aufnehmen','Prüftermine anlegen','Wartungspläne festlegen','Budget planen und überwachen'], 'Anlagen, Fristen, Wartungspläne und Budget an einem Ort – mit klarem Bericht für den Eigentümer.'),
 ('wartung','Inspektion und Wartung',[], 'Heizung, Lüftung, Sanitär, Elektro: regelmäßig geprüft, gewartet und dokumentiert.'),
 ('instand','Instandsetzung',[], 'Kleine und größere Reparaturen von der Planung über das Ersatzteil bis zur Abnahme.'),
 ('brand','Brandschutz und Prüffristen',[], 'Rettungswege, Feuerlöscher, Rauchabzug, Brandmeldeanlage und Begehungen im Blick.'),
 ('stoer','Störungsannahme',[], 'Meldung aufnehmen, Fachfirma beauftragen, Erledigung zurückmelden.'),
 ('omgmt','Objektmanagement',[], 'Steuerung aller Dienstleister und Fachfirmen im Gebäude – ein Ansprechpartner für den Eigentümer.'),
 ('gewaehr','Gewährleistungsverfolgung',[], 'Mängel bei Neubau, Umbau und Sanierung anmelden, nachverfolgen und die Beseitigung koordinieren.'),
]
def liste(L):
    o=''
    for k,t,u,_ in L:
        o+=f'<li>{t}'
        if u: o+='<ul>'+''.join(f'<li>{x}</li>' for x in u)+'</ul>'
        o+='</li>\n'
    return o
def karten(L,art,name):
    return ''.join(f'<article class="karte auf" data-art="{art}"><span class="k-icon">{svg(k)}</span><span class="k-art">{name}</span><h3>{t}</h3><p>{x}</p></article>\n' for k,t,_,x in L)
HELD = [('objekt','Objektbetreuung',64,10),('gruen','Grünpflege',84,22),('wartung','Wartung',61,40),('brand','Brandschutz',74,50),('winter','Winterdienst',89,62),('rein','Reinigung',66,74)]
held = ''.join(f'<a href="#leistungen" class="h-icon" style="--x:{x}%;--y:{y}%;--d:{i*0.4:.1f}s">{svg(k)}<span>{t}</span></a>' for i,(k,t,x,y) in enumerate(HELD))
n = len(INFRA)+len(TECH)
html = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>APM Ulm – Facility Management für Ulm und die Region</title>
<meta name="description" content="Infrastrukturelles und technisches Gebäudemanagement aus einer Hand: Objektbetreuung, Grünpflege, Winterdienst, Wartung, Brandschutz und Objektmanagement in Ulm und der Region.">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" href="../img/logo.svg" type="image/svg+xml">
<link rel="preload" href="../fonts/source-sans-3.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="d.css?v=1">
</head>
<body>
<header class="kopf">
  <div class="kopf-in">
    <a href="#start" class="logo" aria-label="APM Ulm – nach oben"><img src="../img/logo.svg" alt="APM Ulm" width="92" height="40"></a>
    <button class="menue-knopf" aria-label="Menü" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav" aria-label="Hauptnavigation">
      <a href="#leistungen">Dienstleistungen</a>
      <a href="#ueberblick">Alle Leistungen</a>
      <a href="#praxis">Praxisbeispiel</a>
      <a href="#ablauf">Ablauf</a>
      <a href="#kontakt" class="nav-cta">Kontakt</a>
    </nav>
  </div>
</header>

<main>
<section class="held" id="start">
  <img class="held-bild" src="../img/energon-wide-1920.webp" srcset="../img/energon-wide-1000.webp 1000w, ../img/energon-wide-1920.webp 1920w" sizes="100vw" alt="Bürogebäude im Science Park II am Oberen Eselsberg in Ulm" width="1920" height="883" fetchpriority="high">
  <div class="held-in">
    <div class="held-text">
      <h1>APM –<br>Facility Management für Ulm und die Region</h1>
      <p class="drei-zeilen">Für Ihr Gebäude.<br>Für Ihre Mieter.<br>Für einen ruhigen Betrieb.</p>
    </div>
    <div class="h-icons">{held}</div>
  </div>
</section>

<section class="teil mitte" id="intro">
  <h2 class="auf">Unser Herz schlägt für <em>Gebäude, die einfach laufen</em></h2>
  <p class="gross auf">Von der Objektbetreuung über Grünpflege und Winterdienst bis zu Wartung, Brandschutz und Objektmanagement – wir übernehmen das komplette Facility Management Ihrer Immobilie.</p>
  <p class="auf">Sie haben einen Ansprechpartner, der Ihr Gebäude kennt, weil er regelmäßig vor Ort ist. Prüfungen, Wartungen und Mängel halten wir nachvollziehbar fest.</p>
  <dl class="zahlen auf">
    <div><dt data-zaehle="{n}">{n}</dt><dd>Leistungen</dd></div>
    <div><dt data-zaehle="2">2</dt><dd>Bereiche</dd></div>
    <div><dt data-zaehle="1">1</dt><dd>Ansprechpartner</dd></div>
    <div><dt data-zaehle="4">4</dt><dd>Schritte zum Start</dd></div>
  </dl>
</section>

<section class="teil" id="leistungen">
  <div class="kopfzeile auf"><p class="label">Dienstleistungen</p><h2>Zwei Bereiche, <em>ein Ansprechpartner</em></h2></div>
  <div class="duo">
    <img class="duo-bild auf" src="../img/energon-fassade.webp" alt="Fassade im Science Park II" loading="lazy">
    <div class="tafel dunkel auf">
      <h3>Infrastrukturelles Gebäudemanagement</h3>
      <ul class="t-liste">
{liste(INFRA)}      </ul>
    </div>
    <div class="tafel gold auf">
      <h3>Technisches Gebäudemanagement</h3>
      <ul class="t-liste">
{liste(TECH)}      </ul>
    </div>
  </div>
</section>

<section class="teil" id="ueberblick">
  <div class="kopfzeile auf"><p class="label">Alle Leistungen im Überblick</p><h2>Was wir für Ihr Gebäude <em>übernehmen</em></h2></div>
  <div class="filter auf" role="group" aria-label="Leistungen filtern">
    <button class="aktiv" data-filter="alle">Alle</button>
    <button data-filter="infra">Infrastrukturell</button>
    <button data-filter="tech">Technisch</button>
  </div>
  <div class="karten">
{karten(INFRA,'infra','Infrastrukturell')}{karten(TECH,'tech','Technisch')}  </div>
</section>

<section class="teil" id="praxis">
  <div class="block">
    <figure class="block-bild auf"><img src="../img/energon-1600.webp" srcset="../img/energon-800.webp 800w, ../img/energon-1600.webp 1600w" sizes="(max-width: 900px) 100vw, 620px" alt="Science Park II, Ulm" loading="lazy"><figcaption>Science Park II, Ulm</figcaption></figure>
    <div class="block-text auf">
      <p class="label">Praxisbeispiel</p>
      <h2>Science Park <em>Ulm</em></h2>
      <p>Am Oberen Eselsberg ist seit den 1980er-Jahren die Wissenschaftsstadt gewachsen: Forschungsinstitute, Labore und Entwicklungszentren namhafter Unternehmen. Hier betreuen wir Objekte im kompletten Facility Management.</p>
      <ul class="haken">
        <li>Objektbetreuung und Hausmeisterdienst</li>
        <li>Haustechnik und Wartungsmanagement</li>
        <li>Brandschutz und Prüffristen</li>
        <li>Außenanlagen und Winterdienst</li>
        <li>Steuerung von Reinigung und Fachfirmen</li>
      </ul>
    </div>
  </div>
</section>

<section class="teil" id="ablauf">
  <div class="kopfzeile auf"><p class="label">Ablauf</p><h2>Vier Schritte bis zum <em>ruhigen Betrieb</em></h2></div>
  <ol class="schritte">
    <li class="auf"><span>1</span><h3>Begehung</h3><p>Technik, Flächen, Prüfpflichten und offene Punkte gemeinsam ansehen.</p></li>
    <li class="auf"><span>2</span><h3>Objektakte</h3><p>Anlagen, Fristen und Ansprechpartner an einem Ort dokumentiert.</p></li>
    <li class="auf"><span>3</span><h3>Laufender Betrieb</h3><p>Feste Rundgänge, schnelle Reaktion, Fachfirmen im Griff.</p></li>
    <li class="auf"><span>4</span><h3>Kurzer Bericht</h3><p>Was erledigt ist, was geplant ist, was ansteht.</p></li>
  </ol>
</section>

<section class="band" id="kontakt">
  <div class="band-in">
    <div class="auf">
      <p class="label">Kontakt</p>
      <h2>Sprechen wir über <em>Ihr Gebäude</em></h2>
      <p>Kurz anrufen oder schreiben – wir schauen uns das Objekt an und machen Ihnen ein klares Angebot.</p>
    </div>
    <ul class="kontakt auf">
      <li><span class="k-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 3.5h3.2l1.8 4.6-2.4 1.5a11 11 0 0 0 6.8 6.8l1.5-2.4 4.6 1.8v3.2a2 2 0 0 1-2 2A16.5 16.5 0 0 1 3 5.5a2 2 0 0 1 2-2z"/></svg></span><b>Anrufen</b><span>Nummer folgt</span></li>
      <li><span class="k-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.5 6h17v12h-17z"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/></svg></span><b>Schreiben</b><span>E-Mail folgt</span></li>
      <li><span class="k-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg></span><b>Einsatzgebiet</b><span>Ulm, Neu-Ulm und Region</span></li>
    </ul>
  </div>
</section>
</main>

<footer class="fuss">
  <div class="fuss-zeile"><img src="../img/logo.svg" alt="APM Ulm" width="70" height="30"><span>© 2026 APM Ulm · Facility Management</span><span>Impressum (folgt) · Datenschutz (folgt)</span></div>
  <p class="vorschau">Vorschau – Kontaktdaten, Impressum und Datenschutz werden noch ergänzt.</p>
  <details><summary>Bildnachweis</summary>
    <ul><li>Science Park II (Energon): G8w, <a href="https://commons.wikimedia.org/wiki/File:Ulm_Energon.jpg" rel="noopener">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.de" rel="noopener">CC BY-SA 3.0</a></li></ul>
    <p>Bilder zugeschnitten, verkleinert und ins WebP-Format umgewandelt; die Bearbeitung steht unter derselben Lizenz.</p>
  </details>
</footer>
<script src="d.js?v=1" defer></script>
</body>
</html>
'''
open('index.html','w').write(html); print(n,'Leistungen')
