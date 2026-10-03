# Baut index.html der Variante D (helles Firmen-Layout, eigener Aufbau, Leistungen in zwei Reitern)
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
# (Schluessel, Titel, Kurztext) – eigene Benennung und Reihenfolge
AUSSEN = [
 ('objekt','Hausmeisterdienst','Ein fester Betreuer im Objekt: Rundgänge, Kleinreparaturen, Schlüssel und Zugänge.'),
 ('rein','Reinigung steuern','Treppenhäuser, Flure und Eingänge sauber halten – wir beauftragen, kontrollieren und rügen nach.'),
 ('gruen','Grünpflege','Rasen, Hecken, Bäume und Beete schneiden und pflegen, gießen, Laub und Schnittgut abfahren.'),
 ('winter','Winterdienst','Wege, Zufahrten und Parkflächen räumen und streuen, bevor morgens der Betrieb beginnt.'),
 ('galabau','Außenanlagen erneuern','Flächen herrichten, ausbessern, neu bepflanzen oder umgestalten.'),
 ('abfall','Abfall und Wertstoffe','Tonnen rechtzeitig bereitstellen, Standplätze sauber halten, Abholung abstimmen.'),
 ('park','Parkflächen und Tiefgaragen','Ordnung, Beleuchtung, Beschilderung und ein sicherer Ablauf für Mieter und Besucher.'),
 ('pforte','Empfang und Post','Besucher empfangen, Post und Pakete annehmen und im Haus verteilen.'),
 ('doku','Objektunterlagen','Aushänge, Nutzerinfos und Protokolle zum Gebäude geordnet an einem Ort.'),
]
TECHNIK = [
 ('wartung','Wartung und Inspektion','Heizung, Lüftung, Sanitär und Elektro regelmäßig prüfen und warten lassen – mit Nachweis.'),
 ('instand','Reparaturen','Vom tropfenden Ventil bis zur größeren Instandsetzung: planen, Ersatzteil besorgen, erledigen, abnehmen.'),
 ('brand','Brandschutz und Prüffristen','Rettungswege, Feuerlöscher, Rauchabzug und Brandmeldeanlage im Blick, Begehungen inklusive.'),
 ('betreiber','Betreiberpflichten','Wir achten darauf, dass vorgeschriebene Prüfungen fristgerecht stattfinden und belegt sind.'),
 ('stoer','Störungsannahme','Meldung aufnehmen, Fachfirma beauftragen, Erledigung an Sie zurückmelden.'),
 ('omgmt','Dienstleister steuern','Handwerker und Fachfirmen koordinieren – Sie haben einen Ansprechpartner statt zehn.'),
 ('cafm','Digitale Objektakte','Anlagen, Fristen, Wartungspläne und Kosten übersichtlich erfasst, mit kurzem Bericht für Sie.'),
 ('gewaehr','Gewährleistung und Mängel','Nach Neubau oder Sanierung Mängel anzeigen, nachhalten und die Beseitigung abstimmen.'),
]
def karten(L,art):
    return ''.join(f'<article class="karte auf" data-art="{art}"><span class="k-icon">{svg(k)}</span><h3>{t}</h3><p>{x}</p></article>\n' for k,t,x in L)
band = ''.join(f'<span>{svg(k)}{t}</span>' for k,t,_ in AUSSEN+TECHNIK)
html = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>APM Ulm – Facility Management für Ulm und die Region</title>
<meta name="description" content="Facility Management aus einer Hand: Hausmeisterdienst, Grünpflege, Winterdienst, Wartung, Brandschutz und Steuerung aller Dienstleister – in Ulm und der Region.">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" href="../img/logo.svg" type="image/svg+xml">
<link rel="preload" href="../fonts/source-sans-3.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="d.css?v=2">
</head>
<body>
<header class="kopf">
  <div class="kopf-in">
    <a href="#start" class="logo" aria-label="APM Ulm – nach oben"><img src="../img/logo.svg" alt="APM Ulm" width="92" height="40"></a>
    <button class="menue-knopf" aria-label="Menü" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav" aria-label="Hauptnavigation">
      <a href="#leistungen">Leistungen</a>
      <a href="#praxis">Praxisbeispiel</a>
      <a href="#ablauf">Ablauf</a>
      <a href="#kontakt" class="nav-cta">Kontakt</a>
    </nav>
  </div>
</header>

<main>
<section class="held" id="start">
  <div class="held-text">
    <p class="label"><i></i>Facility Management · Ulm und Region</p>
    <h1>Gebäude, die <em>einfach laufen.</em></h1>
    <p class="lead">Wir kümmern uns um Ihre Immobilie – außen, innen und an der Technik. Sie haben einen Ansprechpartner, der Ihr Gebäude kennt, weil er regelmäßig vor Ort ist.</p>
    <div class="knoepfe">
      <a href="#kontakt" class="btn">Objekt anfragen</a>
      <a href="#leistungen" class="btn hell">Leistungen ansehen</a>
    </div>
  </div>
  <div class="held-foto">
    <img src="../img/energon-1600.webp" srcset="../img/energon-800.webp 800w, ../img/energon-1600.webp 1600w" sizes="(max-width: 980px) 100vw, 640px" alt="Bürogebäude im Science Park II am Oberen Eselsberg in Ulm" width="1600" height="1200" fetchpriority="high">
    <div class="held-karte"><b>{len(AUSSEN)+len(TECHNIK)} Leistungen</b><span>ein Ansprechpartner</span></div>
  </div>
</section>

<div class="laufband" aria-hidden="true"><div class="laufband-in">{band}{band}</div></div>

<section class="teil" id="vorteile">
  <ul class="vorteile">
    <li class="auf"><span class="v-zahl">1</span><h3>Ein Ansprechpartner</h3><p>Eine Nummer für Hausmeister, Technik, Brandschutz und Außenanlagen.</p></li>
    <li class="auf"><span class="v-zahl">vor Ort</span><h3>Statt Hotline</h3><p>Wir kennen Ihr Gebäude, weil wir regelmäßig drin sind.</p></li>
    <li class="auf"><span class="v-zahl">lückenlos</span><h3>Alles dokumentiert</h3><p>Prüfungen, Wartungen und Mängel nachvollziehbar festgehalten.</p></li>
  </ul>
</section>

<section class="teil" id="leistungen">
  <div class="kopfzeile auf"><p class="label"><i></i>Leistungen</p><h2>Alles, was Ihr Gebäude braucht – <em>aus einer Hand</em></h2></div>
  <div class="reiter auf" role="tablist" aria-label="Leistungsbereich wählen">
    <button class="aktiv" role="tab" aria-selected="true" data-art="aussen"><b>Gebäude und Außenanlagen</b><span>{len(AUSSEN)} Leistungen rund ums Haus</span></button>
    <button role="tab" aria-selected="false" data-art="technik"><b>Technik und Betrieb</b><span>{len(TECHNIK)} Leistungen für Anlagen und Abläufe</span></button>
  </div>
  <div class="karten">
{karten(AUSSEN,'aussen')}{karten(TECHNIK,'technik')}  </div>
</section>

<section class="teil" id="praxis">
  <div class="block">
    <figure class="block-bild auf"><img src="../img/energon-wide-1920.webp" srcset="../img/energon-wide-1000.webp 1000w, ../img/energon-wide-1920.webp 1920w" sizes="(max-width: 980px) 100vw, 620px" alt="Science Park II, Ulm" loading="lazy"><figcaption>Science Park II, Ulm</figcaption></figure>
    <div class="block-text auf">
      <p class="label"><i></i>Praxisbeispiel</p>
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
  <div class="kopfzeile auf"><p class="label"><i></i>Ablauf</p><h2>Vier Schritte bis zum <em>ruhigen Betrieb</em></h2></div>
  <ol class="schritte">
    <li class="auf"><span>1</span><h3>Begehung</h3><p>Technik, Flächen, Prüfpflichten und offene Punkte gemeinsam ansehen.</p></li>
    <li class="auf"><span>2</span><h3>Objektakte</h3><p>Anlagen, Fristen und Ansprechpartner an einem Ort dokumentiert.</p></li>
    <li class="auf"><span>3</span><h3>Laufender Betrieb</h3><p>Feste Rundgänge, schnelle Reaktion, Fachfirmen im Griff.</p></li>
    <li class="auf"><span>4</span><h3>Kurzer Bericht</h3><p>Was erledigt ist, was geplant ist, was ansteht.</p></li>
  </ol>
</section>

<section class="teil" id="kontakt">
  <div class="band">
    <div class="auf">
      <p class="label"><i></i>Kontakt</p>
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
<script src="d.js?v=2" defer></script>
</body>
</html>
"""
open('index.html','w').write(html); print(len(AUSSEN)+len(TECHNIK),'Leistungen')
