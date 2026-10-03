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
# gleiche Symbole, aber zeichenbar (pathLength=1) fuer die Kachel-Animation
svg_z = lambda k: svg(k).replace('<path ','<path pathLength="1" ').replace('<circle ','<circle pathLength="1" ')
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
# Wo die Leistung am gezeichneten Haus sitzt (x, y im Bild 640 x 480)
ORT = {
 'aussen': {'objekt':(300,286),'rein':(250,216),'gruen':(110,298),'winter':(150,392),'galabau':(52,372),'abfall':(571,366),'park':(330,432),'pforte':(356,366),'doku':(410,216)},
 'technik': {'wartung':(425,92),'instand':(250,286),'brand':(486,232),'betreiber':(300,146),'stoer':(356,366),'omgmt':(130,388),'cafm':(410,216),'gewaehr':(240,362)},
}
def punkte(L,art):
    return ''.join(f'<li><button class="h-wahl" data-art="{art}" data-x="{ORT[art][k][0]}" data-y="{ORT[art][k][1]}" data-text="{x}"><span class="l-icon">{svg_z(k)}</span><span class="l-name">{t}</span></button></li>\n' for k,t,x in L)
HAUS = '''<svg class="haus" viewBox="0 0 640 480" aria-hidden="true">
<path class="leicht" d="M70 122a16 16 0 0 1 30-6 14 14 0 0 1 26 8 12 12 0 0 1-4 23H74a13 13 0 0 1-4-25z"/>
<path d="M14 400H626"/>
<path d="M200 400V110H520V400"/>
<path d="M200 180H520M200 250H520M200 320H520"/>
<path d="M460 110V400"/>
<path d="M468 398L504 360 468 322 504 286 468 252 504 216 468 182 504 146 468 112"/>
<path d="M220 130h28v30h-28zM262 130h28v30h-28zM304 130h28v30h-28zM346 130h28v30h-28zM388 130h28v30h-28z"/>
<path d="M220 200h28v30h-28zM262 200h28v30h-28zM304 200h28v30h-28zM346 200h28v30h-28zM388 200h28v30h-28z"/>
<path d="M220 270h28v30h-28zM262 270h28v30h-28zM304 270h28v30h-28zM346 270h28v30h-28zM388 270h28v30h-28z"/>
<path d="M220 340h28v30h-28zM262 340h28v30h-28zM404 340h28v30h-28z"/>
<path d="M332 400V346H380V400M356 346V400M322 338H390"/>
<path d="M400 110V84H450V110"/><circle cx="425" cy="97" r="7"/>
<path d="M490 110V68M482 80H498"/>
<path class="leicht" d="M200 400V458H520V400M520 458L596 400"/>
<path class="leicht" d="M246 450v-8l10-2 8-10h32l10 10 8 2v8z"/><circle class="leicht" cx="262" cy="450" r="5"/><circle class="leicht" cx="304" cy="450" r="5"/>
<circle class="leicht" cx="440" cy="432" r="13"/><path class="leicht" d="M440 419V400M453 432H480V400"/>
<path d="M110 400V332"/><circle cx="110" cy="298" r="34"/>
<path d="M52 400V366"/><circle cx="52" cy="350" r="17"/>
<path d="M146 400q9-20 20 0M168 400q7-14 16 0"/>
<path d="M556 400V374H572V400M576 400V378H590V400M553 374H575M574 378H593"/>
</svg>'''
alle = AUSSEN+TECHNIK
band1 = ''.join(f'<span>{t}</span>' for k,t,_ in alle)
band2 = ''.join(f'<span>{t}</span>' for k,t,_ in reversed(alle))
import json
# Original-Logo, je Buchstabe ein Pfad (Geometrie unveraendert) – fuer die Einflug-Animation
AB = 22  # Jan 03.10.: a p m minimal auseinander (Zusatzabstand je Buchstabe in Logo-Einheiten)
logo = f'<svg class="logo-svg" viewBox="100 100 {1124+5*AB} 377" role="img" aria-label="APM Ulm">' + ''.join(f'<g transform="translate({min(i,3)*AB + (AB if i>=3 else 0) + max(0,i-3)*6} 0)"><path class="{"gross" if i<3 else "klein"}" style="--n:{i}" d="{d}"/></g>' for i,d in enumerate(json.load(open('_logo_teile.json')))) + '</svg>'
logo_gross = logo.replace('class="logo-svg"','class="logo-svg gross-logo"').replace(' role="img" aria-label="APM Ulm"','')
html = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>APM Ulm – property management für Ulm und die Region</title>
<meta name="description" content="property management aus einer Hand: Hausmeisterdienst, Grünpflege, Winterdienst, Wartung, Brandschutz und Steuerung aller Dienstleister – in Ulm und der Region.">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" href="../img/logo.svg" type="image/svg+xml">
<link rel="preload" href="../fonts/source-sans-3.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="d.css?v=12">
</head>
<body>
<header class="kopf">
  <div class="kopf-in">
    <a href="#start" class="logo" aria-label="APM Ulm – nach oben">{logo}<span class="logo-text"><b>property management</b><small>Gebäude in Ulm, um Ulm und um Ulm herum.</small></span></a>
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
  <img class="held-bild" src="../img/energon-wide-1920.webp" srcset="../img/energon-wide-1000.webp 1000w, ../img/energon-wide-1920.webp 1920w" sizes="100vw" alt="Bürogebäude im Science Park II am Oberen Eselsberg in Ulm" width="1920" height="883" fetchpriority="high">
  <div class="held-text">
    <p class="label ohne-gross"><i></i>property management · Ulm und Region</p>
    <h1 data-worte>Gebäude in Ulm, <em>um Ulm und um Ulm herum.</em></h1>
    <p class="lead">Vom Hausmeisterdienst bis zur Haustechnik: Wir halten Ihre Immobilie in Schuss. Sie sprechen mit einem festen Ansprechpartner, der Ihr Gebäude kennt, weil er selbst regelmäßig vor Ort ist.</p>
    <div class="knoepfe">
      <a href="#kontakt" class="btn">Objekt anfragen</a>
      <a href="#leistungen" class="btn hell">Leistungen ansehen</a>
    </div>
  </div>
  <div class="held-logo" aria-hidden="true">{logo_gross}</div>
</section>

<div class="laufband" aria-hidden="true">
  <div class="lb-reihe" data-tempo="-1">{band1}{band1}</div>
  <div class="lb-reihe zwei" data-tempo="1">{band2}{band2}</div>
</div>

<section class="teil" id="vorteile">
  <ul class="vorteile">
    <li class="auf"><span class="v-zahl">1</span><h3>Ein Ansprechpartner</h3><p>Eine Nummer für Hausmeister, Technik, Brandschutz und Außenanlagen.</p></li>
    <li class="auf"><span class="v-zahl">vor Ort</span><h3>Statt Hotline</h3><p>Wir kennen Ihr Gebäude, weil wir regelmäßig drin sind.</p></li>
    <li class="auf"><span class="v-zahl">lückenlos</span><h3>Alles dokumentiert</h3><p>Prüfungen, Wartungen und Mängel nachvollziehbar festgehalten.</p></li>
  </ul>
</section>

<section class="nebel" id="leistungen">
  <div class="teil">
    <div class="kopfzeile auf"><p class="label"><i></i>Leistungen</p><h2>Alles, was Ihr Gebäude braucht – <em>aus einer Hand</em></h2></div>
    <div class="reiter auf" role="tablist" aria-label="Leistungsbereich wählen">
      <button class="aktiv" role="tab" aria-selected="true" data-art="aussen">Building Management</button>
      <button role="tab" aria-selected="false" data-art="technik">Technical Management</button>
    </div>
    <div class="h-buehne auf">
      <div class="h-bild">{HAUS}<div class="h-punkte"></div></div>
      <div class="h-seite">
        <div class="h-detail" aria-live="polite"><span class="k-icon"></span><h3></h3><p></p></div>
        <ul class="h-liste">
{punkte(AUSSEN,'aussen')}{punkte(TECHNIK,'technik')}        </ul>
      </div>
    </div>
  </div>
</section>

<section class="teil" id="praxis">
  <div class="block">
    <figure class="block-bild auf"><img src="../img/sciencepark-1500.webp" srcset="../img/sciencepark-800.webp 800w, ../img/sciencepark-1500.webp 1500w" sizes="(max-width: 980px) 100vw, 620px" alt="Bürogebäude an der Lise-Meitner-Straße im Science Park Ulm" loading="lazy" width="1500" height="1000"><figcaption>Science Park Ulm, Lise-Meitner-Straße</figcaption></figure>
    <div class="block-text auf">
      <p class="label"><i></i>Praxisbeispiel</p>
      <h2>Science Park <em>Ulm</em></h2>
      <p>Am Oberen Eselsberg ist seit den 1980er-Jahren die Wissenschaftsstadt gewachsen: Forschungsinstitute, Labore und Entwicklungszentren namhafter Unternehmen. Hier betreuen wir Objekte im kompletten property management.</p>
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

<section class="nebel" id="ablauf">
<div class="teil">
  <div class="kopfzeile auf"><p class="label"><i></i>Ablauf</p><h2>Vier Schritte bis zum <em>ruhigen Betrieb</em></h2></div>
  <ol class="schritte" style="--fuell:0">
    <li class="auf"><span>1</span><h3>Begehung</h3><p>Technik, Flächen, Prüfpflichten und offene Punkte gemeinsam ansehen.</p></li>
    <li class="auf"><span>2</span><h3>Objektakte</h3><p>Anlagen, Fristen und Ansprechpartner an einem Ort dokumentiert.</p></li>
    <li class="auf"><span>3</span><h3>Laufender Betrieb</h3><p>Feste Rundgänge, schnelle Reaktion, Fachfirmen im Griff.</p></li>
    <li class="auf"><span>4</span><h3>Kurzer Bericht</h3><p>Was erledigt ist, was geplant ist, was ansteht.</p></li>
  </ol>
</div>
</section>

<section class="dunkel" id="kontakt">
  <div class="teil kontakt">
    <p class="label auf"><i></i>Kontakt</p>
    <h2 class="riesig auf">Sprechen wir über <em>Ihr Gebäude.</em></h2>
    <p class="k-lead auf">Kurz anrufen oder schreiben – wir schauen uns das Objekt an und machen Ihnen ein klares Angebot.</p>
    <ul class="k-liste auf">
      <li><span>Telefon</span><b>Nummer folgt</b></li>
      <li><span>E-Mail</span><b>E-Mail folgt</b></li>
      <li><span>Einsatzgebiet</span><b>Ulm, Neu-Ulm und Region</b></li>
    </ul>
  </div>
</section>
</main>

<footer class="fuss">
  <div class="fuss-zeile"><img src="../img/logo.svg" alt="APM Ulm" width="70" height="30"><span>© 2026 APM Ulm · property management</span><span>Impressum (folgt) · Datenschutz (folgt)</span></div>
  <p class="vorschau">Vorschau – Kontaktdaten, Impressum und Datenschutz werden noch ergänzt.</p>
  <details><summary>Bildnachweis</summary>
    <ul><li>Science Park II (Energon): G8w, <a href="https://commons.wikimedia.org/wiki/File:Ulm_Energon.jpg" rel="noopener">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.de" rel="noopener">CC BY-SA 3.0</a></li><li>Science Park, Lise-Meitner-Straße: Trop86, <a href="https://commons.wikimedia.org/wiki/File:Lise-Meitner-Stra%C3%9Fe_(Ulm)_101520.jpg" rel="noopener">Wikimedia Commons</a>, CC0</li></ul>
    <p>Bilder zugeschnitten, verkleinert und ins WebP-Format umgewandelt; die Bearbeitung steht unter derselben Lizenz.</p>
  </details>
</footer>
<script src="d.js?v=12" defer></script>
</body>
</html>
"""
open('index.html','w').write(html); print(len(AUSSEN)+len(TECHNIK),'Leistungen')
