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
 ('rein','Reinigung','Treppenhäuser, Flure und Eingänge sauber halten – wir beauftragen, kontrollieren und rügen nach.'),
 ('gruen','Grünpflege','Rasen, Hecken, Bäume und Beete schneiden und pflegen, gießen, Laub und Schnittgut abfahren.'),
 ('winter','Winterdienst','Wege, Zufahrten und Parkflächen räumen und streuen, bevor morgens der Betrieb beginnt.'),
 ('galabau','Außenanlage','Wege, Plätze, Beete und Bänke sauber und in Ordnung halten, kleine Schäden ausbessern.'),
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
# Wo der Punkt sitzt (x, y im Bild; Bild reicht von x=-60 bis 700, y=0 bis 480) – jeweils NEBEN dem gezeichneten Gegenstand
ORT = {
 'aussen': {'objekt':(284,366),'rein':(306,226),'gruen':(130,296),'winter':(566,366),'galabau':(62,352),'abfall':(642,352),'park':(376,434),'pforte':(354,372),'doku':(404,150)},
 'technik': {'wartung':(322,94),'instand':(160,330),'brand':(486,290),'betreiber':(456,440),'stoer':(441,200),'omgmt':(-22,346),'cafm':(306,146),'gewaehr':(538,222)},
}
def punkte(L,art):
    return ''.join(f'<li><button class="h-wahl" data-art="{art}" data-k="{k}" data-x="{ORT[art][k][0]}" data-y="{ORT[art][k][1]}" data-text="{x}"><span class="l-icon">{svg_z(k)}</span><span class="l-name">{t}</span></button></li>\n' for k,t,x in L)
# Jede Leistung hat ihren eigenen Gegenstand im Bild (g data-k) – der wird hervorgehoben, wenn sie gewaehlt ist
HAUS = '''<svg class="haus" viewBox="-60 0 760 480" aria-hidden="true">
<path class="wolke" d="M70 122a16 16 0 0 1 30-6 14 14 0 0 1 26 8 12 12 0 0 1-4 23H74a13 13 0 0 1-4-25z"/>
<path d="M-56 400H694"/>
<path d="M210 400V110H520V400"/>
<path d="M210 182H520M210 254H520M210 326H520"/>
<path d="M462 110V400"/>
<path class="leicht" d="M420 110V400"/>
<path class="leicht" d="M210 400V458H520M520 400V424M400 400V436M520 458L596 400M500 110H520"/>
<path class="leicht" d="M330 200h28v30h-28zM372 200h28v30h-28zM230 272h28v30h-28zM272 272h28v30h-28zM330 272h28v30h-28zM372 272h28v30h-28z"/>
<path class="leicht" d="M500 110V68M492 80H508"/>
<circle class="leicht" cx="424" cy="432" r="12"/><path class="leicht" d="M424 420V400"/>
<g data-k="wartung"><path d="M250 110V84H300V110"/><circle cx="275" cy="97" r="8"/><path d="M268 97h14M275 90v14"/></g>
<g data-k="cafm"><path d="M232 168H312M240 168V182M304 168V182"/><path d="M258 140h28v18h-28zM272 158v10M264 168h16"/></g>
<g data-k="doku"><path d="M330 128h60v48h-60zM330 144h60M330 160h60"/><path d="M340 128v16M348 128v16M356 128v16M366 144v16M374 144v16M344 160v16M352 160v16M372 160v16"/></g>
<g data-k="rein"><path d="M238 252l3-18h20l3 18z"/><path d="M241 234q10-12 20 0"/><path d="M290 252L276 196M282 252h16"/></g>
<g data-k="stoer"><path d="M426 268h30v54h-30zM441 268v54"/><path d="M441 222l11 19h-22z"/><path d="M441 229v5M441 237v1"/></g>
<g data-k="instand"><path d="M178 400L204 264M192 400L216 264"/><path d="M183 376h13M187 352h13M192 328h13M196 304h13M201 280h13"/></g>
<g data-k="pforte"><path d="M330 400V346H378V400M354 346V400M320 338H388"/><path d="M386 366h14v12h-14zM386 370l7 4 7-4"/></g>
<g data-k="objekt"><circle cx="245" cy="349" r="7"/><path d="M245 356v22M245 363l-11 8M245 363l11 8M245 378l-8 22M245 378l8 22"/><path d="M264 386h20v14h-20zM270 386v-5h8v5"/></g>
<g data-k="brand"><path d="M468 398L504 362 468 326 504 290 468 254 504 218 468 182 504 146 468 112"/><path d="M508 398v-14a4 4 0 0 1 8 0v14zM512 380v-5h5"/></g>
<g data-k="park"><g class="auto-tg"><path d="M240 450v-8l10-2 8-10h32l10 10 8 2v8z"/><circle cx="256" cy="450" r="5"/><circle cx="298" cy="450" r="5"/></g><path d="M340 450V424h9a7 7 0 0 1 0 14h-9"/></g>
<g data-k="betreiber"><path d="M478 412h26v40h-26z"/><path class="blitz" d="M494 417l-9 15h7l-4 14 10-17h-7z"/></g>
<g data-k="gruen"><path d="M130 400V330"/><circle cx="130" cy="296" r="32"/><path d="M150 400q9-20 20 0"/></g>
<g data-k="galabau"><path d="M22 390h34M22 382h34M27 382v18M51 382v18"/><path d="M84 400V368M91 400V374M84 380h7"/><circle cx="84" cy="357" r="11"/></g>
<g data-k="omgmt" class="auto-oben"><path d="M-52 394v-30h32l12 14h14v16z"/><path d="M-22 368v10h12"/><circle cx="-38" cy="396" r="6"/><circle cx="-4" cy="396" r="6"/></g>
<g data-k="winter"><path d="M548 324v12M543 327l10 6M553 327l-10 6"/><path d="M574 342v12M569 345l10 6M579 345l-10 6"/><path d="M594 318v12M589 321l10 6M599 321l-10 6"/><path d="M536 446l52-40"/></g>
<g data-k="abfall"><path class="t-gelb" d="M622 400V372H640V400ZM619 372H643"/><path class="t-braun" d="M646 400V376H662V400ZM644 376H665"/></g>
<g class="sz szene">
<path class="himmelblitz" pathLength="1" d="M526 -10L509 22H520L503 48 500 68"/>
<path class="strom" pathLength="1" d="M500 68V110H520V436H504"/>
<g class="sz rauch"><circle cx="484" cy="408" r="5.5"/><circle cx="492" cy="405" r="7"/><circle cx="499" cy="408" r="5"/><circle cx="489" cy="410" r="4.5"/></g>
<g class="sz funken"><path d="M509 425l6-4M510 432h7M509 439l6 4"/></g>
<g class="sz ok"><circle cx="491" cy="386" r="9"/><path d="M486.6 386l3 3 6-6.6"/></g>
<g class="sz mann"><g class="sz mann-in"><circle cx="0" cy="-25" r="4"/><path d="M0 -21V-10"/><path d="M0 -18L6 -12"/><g class="sz arm"><path d="M0 -18L-8 -13M-8 -13l-4 -4"/></g><g class="sz bein-lauf"><path class="b1" d="M0 -10V0"/><path class="b2" d="M0 -10V0"/></g><g class="sz bein-steh"><path d="M0 -10L-2 0M0 -10L3 0"/></g></g></g>
</g>
</svg>'''
alle = AUSSEN+TECHNIK
band1 = ''.join(f'<span>{t}</span>' for k,t,_ in alle)
band2 = ''.join(f'<span>{t}</span>' for k,t,_ in reversed(alle))
import json
# Original-Logo, je Buchstabe ein Pfad (Geometrie unveraendert) – fuer die Einflug-Animation
AB = 22  # Jan 03.10.: a p m minimal auseinander (Zusatzabstand je Buchstabe in Logo-Einheiten)
logo = f'<svg class="logo-svg" viewBox="100 100 {1124+5*AB} 377" role="img" aria-label="APM Ulm">' + ''.join(f'<g transform="translate({min(i,3)*AB + (AB if i>=3 else 0) + max(0,i-3)*6} 0)"><path class="{"gross" if i<3 else "klein"}" style="--n:{i}" d="{d}"/></g>' for i,d in enumerate(json.load(open('_logo_teile.json')))) + '</svg>'
logo_gross = logo.replace('class="logo-svg"','class="logo-svg gross-logo"').replace(' role="img" aria-label="APM Ulm"','')
# Stadtlinie im Kontaktbereich: schlichte Linie wie zuvor, in der Mitte nur der Turm des Ulmer Muensters (Jan 03.10.)
STADT = ('<svg class="k-stadt auf" viewBox="0 -40 1200 154" preserveAspectRatio="xMidYMax slice" aria-hidden="true">'
 '<path class="linie" pathLength="1" d="M0 112H96V86H150V112H214V72H250V112H318V94H380V112H452V62l15-13 15 13v50H672V84h48v28H760V90h56v22H880V66H934V112H1004V92H1056V112H1200"/>'
 '<g class="turm" transform="translate(600 112) scale(.7) translate(-600 -112)">'
 '<path pathLength="1" d="M572 112V24H628V112"/><path pathLength="1" d="M588 112V84a12 12 0 0 1 24 0V112"/>'
 '<path pathLength="1" d="M572 24V6l5-8 5 8V24M618 24V6l5-8 5 8V24"/><path pathLength="1" d="M594 72V46q6-10 12 0V72"/>'
 '<path pathLength="1" d="M582 24V-22H618V24"/><path pathLength="1" d="M592 16V-6q4-8 8 0V16M600 16V-6q4-8 8 0V16"/>'
 '<path pathLength="1" d="M582 -22L600 -82 618 -22"/><path pathLength="1" d="M588 -42h24M593 -58h14M600 -82V-94M596 -89h8"/>'
 '</g></svg>')
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
<link rel="stylesheet" href="d.css?v=33">
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
  <img class="held-bild" src="../img/energon-wide-1920-sw.webp" srcset="../img/energon-wide-1000-sw.webp 1000w, ../img/energon-wide-1920-sw.webp 1920w" sizes="100vw" alt="Bürogebäude im Science Park II am Oberen Eselsberg in Ulm" width="1920" height="883" fetchpriority="high">
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
    <li class="auf"><span class="v-punkt"><svg viewBox="0 0 20 20" aria-hidden="true"><path pathLength="1" d="M5.6 10.4l3 3 5.8-6.4"/></svg></span><svg class="v-bild" viewBox="0 0 120 80" aria-hidden="true"><circle pathLength="1" cx="52" cy="30" r="12"/><path pathLength="1" d="M28 72c2-15 12-23 24-23s22 8 24 23"/><path pathLength="1" d="M82 12h24v17H96l-7 7v-7h-7z"/><path pathLength="1" d="M88 18h12M88 23h8"/></svg><span class="v-zahl">1</span><h3>Ein Ansprechpartner</h3><p>Eine Nummer für Hausmeister, Technik, Brandschutz und Außenanlagen.</p></li>
    <li class="auf"><span class="v-punkt"><svg viewBox="0 0 20 20" aria-hidden="true"><path pathLength="1" d="M5.6 10.4l3 3 5.8-6.4"/></svg></span><svg class="v-bild" viewBox="0 0 120 80" aria-hidden="true"><path pathLength="1" d="M10 70h100"/><path pathLength="1" d="M22 70V28h36v42"/><path pathLength="1" d="M30 38h7M43 38h7M30 49h7M43 49h7M36 70V60h8v10"/><path pathLength="1" class="gruen" d="M86 64s-15-13-15-26a15 15 0 0 1 30 0c0 13-15 26-15 26z"/><circle pathLength="1" class="gruen" cx="86" cy="38" r="5"/></svg><span class="v-zahl">vor Ort</span><h3>Statt Hotline</h3><p>Wir kennen Ihr Gebäude, weil wir regelmäßig drin sind.</p></li>
    <li class="auf"><span class="v-punkt"><svg viewBox="0 0 20 20" aria-hidden="true"><path pathLength="1" d="M5.6 10.4l3 3 5.8-6.4"/></svg></span><svg class="v-bild" viewBox="0 0 120 80" aria-hidden="true"><path pathLength="1" d="M38 16h44v56H38z"/><path pathLength="1" d="M50 11h20v10H50z"/><path pathLength="1" class="gruen" d="M46 34l4 4 7-8"/><path pathLength="1" d="M63 34h12"/><path pathLength="1" class="gruen" d="M46 47l4 4 7-8"/><path pathLength="1" d="M63 47h12"/><path pathLength="1" class="gruen" d="M46 60l4 4 7-8"/><path pathLength="1" d="M63 60h12"/></svg><span class="v-zahl">lückenlos</span><h3>Alles dokumentiert</h3><p>Prüfungen, Wartungen und Mängel nachvollziehbar festgehalten.</p></li>
  </ul>
</section>

<section class="nebel" id="leistungen">
  <div class="teil">
    <div class="kopfzeile auf"><p class="label"><i></i>Leistungen</p><h2>Alles, was Ihr Gebäude braucht – <em>aus einer Hand</em></h2></div>
    <div class="reiter auf" role="tablist" aria-label="Leistungsbereich wählen">
      <button class="aktiv" role="tab" aria-selected="true" data-art="aussen">Infrastrukturelles Management</button>
      <button role="tab" aria-selected="false" data-art="technik">Technisches Management</button>
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
    <figure class="block-bild auf"><img src="../img/sciencepark-1500-sw.webp" srcset="../img/sciencepark-800-sw.webp 800w, ../img/sciencepark-1500-sw.webp 1500w" sizes="(max-width: 980px) 100vw, 620px" alt="Bürogebäude an der Lise-Meitner-Straße im Science Park II Ulm" loading="lazy" width="1500" height="1000"><figcaption>Science Park II Ulm, Lise-Meitner-Straße</figcaption></figure>
    <div class="block-text auf">
      <p class="label"><i></i>Praxisbeispiel</p>
      <h2>Science Park II <em>Ulm</em></h2>
      <p>Am Oberen Eselsberg ist seit den 1980er-Jahren die Wissenschaftsstadt gewachsen: Forschungsinstitute, Labore und Entwicklungszentren namhafter Unternehmen. Hier betreuen wir Objekte im ganzheitlichen Facility Management.</p>
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
  <div class="kopfzeile auf"><p class="label"><i></i>Ablauf</p><h2>Vier Schritte bis zum <em>sicheren Betrieb</em></h2></div>
  <ol class="schritte" style="--fuell:0">
    <li class="auf"><span><b>1</b><svg viewBox="0 0 20 20" aria-hidden="true"><path pathLength="1" d="M5.2 10.4l3.2 3.2 6.4-7"/></svg></span><h3>Begehung</h3><p>Technik, Flächen, Prüfpflichten und offene Punkte gemeinsam ansehen.</p></li>
    <li class="auf"><span><b>2</b><svg viewBox="0 0 20 20" aria-hidden="true"><path pathLength="1" d="M5.2 10.4l3.2 3.2 6.4-7"/></svg></span><h3>Objektakte</h3><p>Anlagen, Fristen und Ansprechpartner an einem Ort dokumentiert.</p></li>
    <li class="auf"><span><b>3</b><svg viewBox="0 0 20 20" aria-hidden="true"><path pathLength="1" d="M5.2 10.4l3.2 3.2 6.4-7"/></svg></span><h3>Laufender Betrieb</h3><p>Feste Rundgänge, schnelle Reaktion, Fachfirmen im Griff.</p></li>
    <li class="auf"><span><b>4</b><svg viewBox="0 0 20 20" aria-hidden="true"><path pathLength="1" d="M5.2 10.4l3.2 3.2 6.4-7"/></svg></span><h3>Kurzer Bericht</h3><p>Was erledigt ist, was geplant ist, was ansteht.</p></li>
  </ol>
</div>
</section>

<section class="dunkel" id="kontakt">
  <div class="teil kontakt">
    <div class="k-links">
      <p class="label auf"><i></i>Kontakt</p>
      <h2 class="riesig auf">Sprechen wir über <em>Ihr Gebäude.</em></h2>
      <p class="k-lead auf">Kurz anrufen oder schreiben – wir schauen uns das Objekt an und machen Ihnen ein klares Angebot.</p>
    </div>
    <ul class="k-liste">
      <li class="auf"><span class="k-bild"><svg viewBox="0 0 24 24" aria-hidden="true"><path pathLength="1" d="M5 3.5h3.2l1.8 4.6-2.4 1.5a11 11 0 0 0 6.8 6.8l1.5-2.4 4.6 1.8v3.2a2 2 0 0 1-2 2A16.5 16.5 0 0 1 3 5.5a2 2 0 0 1 2-2z"/></svg></span><span class="k-was">Telefon</span><b>Nummer folgt</b></li>
      <li class="auf"><span class="k-bild"><svg viewBox="0 0 24 24" aria-hidden="true"><path pathLength="1" d="M3.5 6h17v12h-17z"/><path pathLength="1" d="M3.5 6.5l8.5 6.5 8.5-6.5"/></svg></span><span class="k-was">E-Mail</span><b>E-Mail folgt</b></li>
      <li class="auf"><span class="k-bild"><svg viewBox="0 0 24 24" aria-hidden="true"><path pathLength="1" d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle pathLength="1" cx="12" cy="9.5" r="2.5"/></svg></span><span class="k-was">Einsatzgebiet</span><b>Ulm, Neu-Ulm und Region</b></li>
    </ul>
  </div>
  {STADT}
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
<script src="../vendor/lenis.min.js" defer></script>
<script src="d.js?v=33" defer></script>
</body>
</html>
"""
open('index.html','w').write(html); print(len(AUSSEN)+len(TECHNIK),'Leistungen')
