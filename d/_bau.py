# Baut index.html der Variante D (helles Firmen-Layout, eigener Aufbau, Leistungen in zwei Reitern)
import json as _json
# --- Suchmaschinen: LIVE erst auf True, wenn die Domain gekauft und mit Wix verbunden ist ---
LIVE = True   # seit 04.10.2026 auf Jans Wunsch: Seite für Google sichtbar
DOMAIN = 'https://www.apm-ulm.de'
BASIS = 'https://instant-phkxpjlnzrzj-altun6109-1409.wix-site-host.com'  # Bilder-Adresse; auf DOMAIN umstellen, sobald apm-ulm.de erreichbar ist
SEO_TITEL = 'APM Ulm – Facility Management in Ulm, Neu-Ulm und Region'
SEO_TEXT = 'Facility Management in Ulm und Neu-Ulm aus einer Hand: Hausmeisterdienst, Reinigung, Winterdienst, Wartung, Brandschutz, Modernisierung. Ein fester Ansprechpartner.'
_firma = {"@context":"https://schema.org","@type":"ProfessionalService","name":"APM Ulm","alternateName":"apm ulm – altun property management",
 "description":SEO_TEXT,"image":BASIS+"/img/teilen.png","logo":BASIS+"/img/apple-touch-icon.png","telephone":"+49 170 5810174","email":"taha.altun@outlook.de",
 "address":{"@type":"PostalAddress","streetAddress":"Weinbergweg 81","postalCode":"89075","addressLocality":"Ulm","addressCountry":"DE"},
 "areaServed":[{"@type":"City","name":"Ulm"},{"@type":"City","name":"Neu-Ulm"}],
 "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"17:00"}],
 "knowsAbout":["Facility Management","Hausmeisterdienst","Gebäudereinigung","Winterdienst","Grünpflege","Wartung und Inspektion","Brandschutz","Gebäudemodernisierung"]}
if LIVE: _firma["url"] = DOMAIN + "/"
ROBOTS = 'index, follow' if LIVE else 'noindex, nofollow'
SEO_KOPF = (f'<title>{SEO_TITEL}</title>\n<meta name="description" content="{SEO_TEXT}">\n<meta name="robots" content="{ROBOTS}">\n'
 + (f'<link rel="canonical" href="{DOMAIN}/">\n<meta property="og:url" content="{DOMAIN}/">\n' if LIVE else '')
 + f'<meta property="og:type" content="website">\n<meta property="og:locale" content="de_DE">\n<meta property="og:site_name" content="APM Ulm">\n<meta property="og:title" content="{SEO_TITEL}">\n<meta property="og:description" content="{SEO_TEXT}">\n<meta property="og:image" content="{BASIS}/img/teilen.png">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta name="twitter:card" content="summary_large_image">\n'
 + '<script type="application/ld+json">' + _json.dumps(_firma, ensure_ascii=False) + '</script>')
ICONS = '<link rel="icon" href="../img/logo.svg" type="image/svg+xml">\n<link rel="icon" href="../img/favicon-32.png" sizes="32x32" type="image/png">\n<link rel="apple-touch-icon" href="../img/apple-touch-icon.png">'
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
 'gewaehr': '<path d="M8 4h8v3H8zM6 5.5H5v15h14v-15h-1M9 14l2 2 4-4.5"/>', 'm_teil': '<path d="M4 4h16v16H4zM4 12h8M12 4v8M12 16v4"/>',
 'm_energie': '<path d="M13 3L5 14h6l-1 7 8-11h-6z"/>',
 'm_fassade': '<path d="M3 11l9-7 9 7M5.5 9.5V20h13V9.5M9 20v-6h6v6"/>',
 'm_innen': '<path d="M5 4h12v5H5zM17 6.5h3V12h-8v3M11 15h2v6h-2z"/>',
 'm_technik': '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.2L3.5 17.3a1.8 1.8 0 0 0 2.6 2.6l5.8-5.8a4 4 0 0 0 5.2-5.4l-2.6 2.6-2.4-.4-.4-2.4z"/>',
 'm_leitung': '<path d="M4 17a8 8 0 0 1 16 0zM2.5 17h19M10 9V6h4v3"/>',
}
svg = lambda k: f'<svg viewBox="0 0 24 24" aria-hidden="true">{I[k]}</svg>'
# gleiche Symbole, aber zeichenbar (pathLength=1) fuer die Kachel-Animation
svg_z = lambda k: svg(k).replace('<path ','<path pathLength="1" ').replace('<circle ','<circle pathLength="1" ')
# (Schluessel, Titel, Kurztext) – eigene Benennung und Reihenfolge
AUSSEN = [
 ('objekt','Hausmeisterdienst','Ein fester Betreuer im Objekt: Rundgänge, Kleinreparaturen, Schlüssel und Zugänge.'),
 ('rein','Reinigung','Treppenhäuser, Flure und Eingänge sauber halten – wir beauftragen, kontrollieren und sorgen für Nachbesserung.'),
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
 'mod': {'m_teil':(350,290),'m_energie':(350,84),'m_fassade':(196,236),'m_innen':(350,218),'m_technik':(500,94),'m_leitung':(430,372)},
 'technik': {'wartung':(322,94),'instand':(160,330),'brand':(486,290),'betreiber':(456,440),'stoer':(441,200),'omgmt':(-22,346),'cafm':(306,146),'gewaehr':(538,222)},
}
MOD = [
 ('m_teil','Teilflächenmodernisierung','Einzelne Etagen, Büros, Flure oder Sanitärbereiche erneuern – abschnittsweise und im laufenden Betrieb.'),
 ('m_energie','Energieeffizienz','Dämmung, Fenster, Beleuchtung und Heizung auf den heutigen Stand bringen, damit Verbrauch und Nebenkosten sinken.'),
 ('m_fassade','Fassade und Dach','Fassade ausbessern, streichen oder dämmen, das Dach abdichten und instand setzen.'),
 ('m_innen','Innenausbau','Böden, Wände, Decken und Türen – vom Mieterwechsel bis zum kompletten Umbau.'),
 ('m_technik','Haustechnik erneuern','Alte Heizungs-, Lüftungs-, Elektro- und Sanitäranlagen durch zeitgemäße Technik ersetzen.'),
 ('m_leitung','Planung und Bauleitung','Ein Ansprechpartner koordiniert alle Gewerke, Termine und Kosten bis zur Abnahme.'),
]
def punkte(L,art):
    return ''.join(f'<li><button class="h-wahl" data-art="{art}" data-k="{k}" data-x="{ORT[art][k][0]}" data-y="{ORT[art][k][1]}" data-text="{x}"><span class="l-icon">{svg_z(k)}</span><span class="l-name">{t}</span></button></li>\n' for k,t,x in L)
# Jede Leistung hat ihren eigenen Gegenstand im Bild (g data-k) – der wird hervorgehoben, wenn sie gewaehlt ist
HAUS = '''<svg class="haus haus-haupt" viewBox="-60 0 760 480" aria-hidden="true">
<path class="wolke" d="M70 122a16 16 0 0 1 30-6 14 14 0 0 1 26 8 12 12 0 0 1-4 23H74a13 13 0 0 1-4-25z"/>
<path d="M-56 400H694"/>
<path d="M210 400V110H520V400"/>
<path d="M210 182H520M210 254H520M210 326H520"/>
<path d="M462 110V400"/>
<path class="leicht" d="M420 110V400"/>
<path class="leicht" d="M210 400V458H520M520 400V424M400 400V436M520 458L596 400"/>
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
<g data-k="park"><g class="auto-tg"><path d="M240 450v-8l10-2 8-10h32l10 10 8 2v8z"/><circle cx="256" cy="452" r="5"/><circle cx="298" cy="452" r="5"/></g><path d="M340 450V424h9a7 7 0 0 1 0 14h-9"/></g>
<g data-k="betreiber"><path d="M478 412h26v40h-26z"/><path class="blitz" d="M494 417l-9 15h7l-4 14 10-17h-7z"/></g>
<g data-k="gruen"><path d="M130 400V330"/><circle cx="130" cy="296" r="32"/><path d="M150 400q9-20 20 0"/></g>
<g data-k="galabau"><path d="M22 390h34M22 382h34M27 382v18M51 382v18"/><path d="M84 400V368M91 400V374M84 380h7"/><circle cx="84" cy="357" r="11"/></g>
<g data-k="omgmt" class="auto-oben"><path d="M-52 390v-30h32l12 14h14v16z"/><path d="M-22 364v10h12"/><circle cx="-38" cy="393" r="6"/><circle cx="-4" cy="393" r="6"/></g>
<g data-k="winter"><path d="M548 324v12M543 327l10 6M553 327l-10 6"/><path d="M574 342v12M569 345l10 6M579 345l-10 6"/><path d="M594 318v12M589 321l10 6M599 321l-10 6"/><path d="M536 446l52-40"/></g>
<g data-k="abfall"><path class="t-gelb" d="M622 400V372H640V400ZM619 372H643"/><path class="t-braun" d="M646 400V376H662V400ZM644 376H665"/></g>
<g class="sz szene">
<path class="himmelblitz" d="M534 -16L510 28h12L500 68l9-32h-11l14-52z"/>
<path class="leiter" d="M500 108H527V444H504"/>
<path class="strom" pathLength="1" d="M500 68V108H527V444H504"/>
<g class="sz rauch"><circle cx="484" cy="408" r="5.5"/><circle cx="492" cy="405" r="7"/><circle cx="499" cy="408" r="5"/><circle cx="489" cy="410" r="4.5"/></g>
<g class="sz funken"><path d="M509 425l6-4M510 432h7M509 439l6 4"/></g>
<g class="sz ok"><circle cx="491" cy="386" r="9"/><path d="M486.6 386l3 3 6-6.6"/></g>
<g class="sz mann"><g class="sz mann-in"><circle cx="0" cy="-25" r="4"/><path d="M0 -21V-10"/><path d="M0 -18L6 -12"/><g class="sz arm"><path d="M0 -18L-8 -13M-8 -13l-4 -4"/></g><g class="sz bein-lauf"><path class="b1" d="M0 -10V0"/><path class="b2" d="M0 -10V0"/></g><g class="sz bein-steh"><path d="M0 -10L-2 0M0 -10L3 0"/></g></g></g>
</g>
</svg>'''
HAUS_MOD = '<svg class="haus haus-mod" viewBox="-60 0 760 480" aria-hidden="true"><g class="sz neu"><path d="M-56 400H694"/><path d="M210 400V110H520V400"/><path d="M210 182H520M210 254H520M210 326H520"/><path d="M236 128h34v36h-34zM253 128v36M300 128h34v36h-34zM317 128v36M400 128h34v36h-34zM417 128v36M464 128h34v36h-34zM481 128v36M236 200h34v36h-34zM253 200v36M300 200h34v36h-34zM317 200v36M400 200h34v36h-34zM417 200v36M464 200h34v36h-34zM481 200v36M236 272h34v36h-34zM253 272v36M300 272h34v36h-34zM317 272v36M400 272h34v36h-34zM417 272v36M464 272h34v36h-34zM481 272v36"/><path d="M236 344h34v36h-34zM253 344v36M464 344h34v36h-34zM481 344v36"/><path d="M340 400V342H390V400M365 342V400M330 334H400"/><path class="pv" d="M232 110l10-24h92l-10 24zM264 86l-10 24M294 86l-10 24M237 98h93"/><path d="M440 110V86h44v24"/><circle cx="462" cy="98" r="8"/><path d="M455 98h14M462 91v14"/><path class="gruen" d="M360 110q4-12 8 0M376 110q4-10 8 0M392 110q4-12 8 0M408 110q4-10 8 0"/><path class="gruen" d="M590 400V334"/><circle class="gruen" cx="590" cy="302" r="30"/><path class="gruen" d="M112 400q10-26 26 0M140 400q8-18 20 0M162 400q6-14 16 0"/><circle class="sonne" cx="110" cy="112" r="17"/><path class="sonne" d="M110 82v-9M110 151v-9M80 112h-9M149 112h-9M89 91l-6-6M137 139l-6-6M89 133l-6 6M137 85l-6 6"/></g><g class="sz alt"><path pathLength="1" d="M-56 400H694"/><path pathLength="1" d="M210 400V118l40-6 30 10 46-12 40 9 50-8 44 10 30-9 30 6V400"/><path pathLength="1" d="M210 182q80 8 155 0t155 4M210 254q70-6 150 2t160-2M210 326h310"/><path pathLength="1" d="M236 130l10 18-8 14 12 20M470 200l-12 16 10 14-14 22M300 330l8 18-6 16 10 14"/><path pathLength="1" d="M240 200h30v32h-30zM240 200l30 32M380 200h30v32h-30zM380 232l30-32"/><path pathLength="1" d="M300 272h30v32h-30zM312 272l-8 14 12 6-6 12M240 272h30v32h-30zM236 280l38 6M236 296l38-8M430 272h30v32h-30z"/><path pathLength="1" d="M340 400V346h40v54M344 348l30 6v46"/><path pathLength="1" d="M440 340q10-8 20 0t18 4q4 12-6 18t-24 0q-12-8-8-22z"/><path pathLength="1" d="M480 112l14-36M486 92l12 4"/><path pathLength="1" d="M40 400V352H180V400M40 364H180M75 352V400M110 352V400M145 352V400"/><path pathLength="1" class="warn" d="M92 344l14-24 14 24zM106 328v8"/><path pathLength="1" d="M130 400q8-18 22-12 6-14 22-6 14-4 16 18z"/><path pathLength="1" d="M560 400V370M620 400V370"/><path pathLength="1" class="warn" d="M552 370h76v14h-76z"/><path pathLength="1" d="M566 370l-10 14M584 370l-10 14M602 370l-10 14M620 370l-10 14"/><path pathLength="1" class="warn" d="M650 400l8-26h6l8 26zM646 400h30"/></g><g class="sz wolken"><g class="sz" transform="translate(270 160) scale(2.0)"><path class="puff" style="--n:0" d="M-30 12a14 14 0 0 1 3-27 18 18 0 0 1 34-7 15 15 0 0 1 23 13 12 12 0 0 1-3 24H-24a12 12 0 0 1-6-3z"/></g><g class="sz" transform="translate(385 140) scale(2.2)"><path class="puff" style="--n:1" d="M-30 12a14 14 0 0 1 3-27 18 18 0 0 1 34-7 15 15 0 0 1 23 13 12 12 0 0 1-3 24H-24a12 12 0 0 1-6-3z"/></g><g class="sz" transform="translate(478 178) scale(1.8)"><path class="puff" style="--n:2" d="M-30 12a14 14 0 0 1 3-27 18 18 0 0 1 34-7 15 15 0 0 1 23 13 12 12 0 0 1-3 24H-24a12 12 0 0 1-6-3z"/></g><g class="sz" transform="translate(250 262) scale(2.1)"><path class="puff" style="--n:3" d="M-30 12a14 14 0 0 1 3-27 18 18 0 0 1 34-7 15 15 0 0 1 23 13 12 12 0 0 1-3 24H-24a12 12 0 0 1-6-3z"/></g><g class="sz" transform="translate(366 252) scale(2.4)"><path class="puff" style="--n:4" d="M-30 12a14 14 0 0 1 3-27 18 18 0 0 1 34-7 15 15 0 0 1 23 13 12 12 0 0 1-3 24H-24a12 12 0 0 1-6-3z"/></g><g class="sz" transform="translate(486 280) scale(1.9)"><path class="puff" style="--n:5" d="M-30 12a14 14 0 0 1 3-27 18 18 0 0 1 34-7 15 15 0 0 1 23 13 12 12 0 0 1-3 24H-24a12 12 0 0 1-6-3z"/></g><g class="sz" transform="translate(290 352) scale(2.0)"><path class="puff" style="--n:6" d="M-30 12a14 14 0 0 1 3-27 18 18 0 0 1 34-7 15 15 0 0 1 23 13 12 12 0 0 1-3 24H-24a12 12 0 0 1-6-3z"/></g><g class="sz" transform="translate(412 346) scale(2.2)"><path class="puff" style="--n:7" d="M-30 12a14 14 0 0 1 3-27 18 18 0 0 1 34-7 15 15 0 0 1 23 13 12 12 0 0 1-3 24H-24a12 12 0 0 1-6-3z"/></g><g class="sz" transform="translate(505 362) scale(1.6)"><path class="puff" style="--n:8" d="M-30 12a14 14 0 0 1 3-27 18 18 0 0 1 34-7 15 15 0 0 1 23 13 12 12 0 0 1-3 24H-24a12 12 0 0 1-6-3z"/></g><g class="sz" transform="translate(205 330) scale(1.5)"><path class="puff" style="--n:9" d="M-30 12a14 14 0 0 1 3-27 18 18 0 0 1 34-7 15 15 0 0 1 23 13 12 12 0 0 1-3 24H-24a12 12 0 0 1-6-3z"/></g><path class="schlag" style="--n:0" d="M330 191v18M321 200h18M324 194l12 12M336 194l-12 12"/><path class="schlag" style="--n:1" d="M440 226v18M431 235h18M434 229l12 12M446 229l-12 12"/><path class="schlag" style="--n:2" d="M310 291v18M301 300h18M304 294l12 12M316 294l-12 12"/><path class="schlag" style="--n:3" d="M455 321v18M446 330h18M449 324l12 12M461 324l-12 12"/><path class="schlag" style="--n:4" d="M240 321v18M231 330h18M234 324l12 12M246 324l-12 12"/></g><g class="sz" transform="translate(545 150)"><path class="funkel" style="--n:0" d="M0 -9L2.2 -2.2 9 0 2.2 2.2 0 9 -2.2 2.2 -9 0 -2.2 -2.2Z"/></g><g class="sz" transform="translate(186 206)"><path class="funkel" style="--n:1" d="M0 -9L2.2 -2.2 9 0 2.2 2.2 0 9 -2.2 2.2 -9 0 -2.2 -2.2Z"/></g><g class="sz" transform="translate(366 62)"><path class="funkel" style="--n:2" d="M0 -9L2.2 -2.2 9 0 2.2 2.2 0 9 -2.2 2.2 -9 0 -2.2 -2.2Z"/></g><g class="sz" transform="translate(548 330)"><path class="funkel" style="--n:3" d="M0 -9L2.2 -2.2 9 0 2.2 2.2 0 9 -2.2 2.2 -9 0 -2.2 -2.2Z"/></g></svg>'
alle = AUSSEN+TECHNIK+MOD
band1 = ''.join(f'<span>{t}</span>' for k,t,_ in alle)
band2 = ''.join(f'<span>{t}</span>' for k,t,_ in reversed(alle))
import json
# Original-Logo, je Buchstabe ein Pfad (Geometrie unveraendert) – fuer die Einflug-Animation
AB = 22  # Jan 03.10.: a p m minimal auseinander (Zusatzabstand je Buchstabe in Logo-Einheiten)
logo = f'<svg class="logo-svg" viewBox="100 100 {1124+5*AB} 377" role="img" aria-label="APM Ulm">' + ''.join(f'<g transform="translate({min(i,3)*AB + (AB if i>=3 else 0) + max(0,i-3)*6} 0)"><path class="{"gross" if i<3 else "klein"}" style="--n:{i}" d="{d}"/></g>' for i,d in enumerate(json.load(open('_logo_teile.json')))) + '</svg>'
logo_gross = logo.replace('class="logo-svg"','class="logo-svg gross-logo"').replace(' role="img" aria-label="APM Ulm"','')
# Stadtlinie im Kontaktbereich: EINE durchgehende Linie, alles im selben Strich. In der Mitte der Umriss des Ulmer Muensters
# wie von der Donau gesehen: hoher Westturm mit schlanker Spitze, Dachfirst des Langhauses, zwei kleinere Osttuerme, Chor.
STADT = ('<svg class="k-stadt auf" viewBox="0 -10 1200 124" preserveAspectRatio="xMidYMax slice" aria-hidden="true">'
 '<path class="linie" pathLength="1" d="M0 112H96V86H150V112H214V72H250V112H318V94H380V112H452V62l15-13 15 13v50'
 'H548V64h3V40h3V30l5-26V-3V4l5 26V40h3V64h3V71H606V66l4-14 4 14V71h4V66l4-14 4 14V71H636l4 12V112'
 'H672V84h48v28H760V90h56v22H880V66H934V112H1004V92H1056V112H1200"/></svg>')
SP = '<svg class="sp" viewBox="0 0 720 360" aria-hidden="true"><path class="wolke" d="M96 62a13 13 0 0 1 24-5 11 11 0 0 1 21 6 10 10 0 0 1-3 19H99a11 11 0 0 1-3-20z"/><path class="wolke w2" d="M606 46a11 11 0 0 1 20-4 9 9 0 0 1 18 5 8 8 0 0 1-3 16H609a9 9 0 0 1-3-17z"/><path pathLength="1" style="--i:0" d="M10 330H710"/><path pathLength="1" style="--i:1" d="M70 330V112H570V330"/><path pathLength="1" style="--i:2" d="M58 104H582V112H58Z"/><path pathLength="1" style="--i:3" d="M70 166H570M70 220H570M70 274H570"/><path pathLength="1" style="--i:4" d="M290 112V330M350 112V330"/><path pathLength="1" class="fein" style="--i:5" d="M320 112V274"/><path pathLength="1" class="fein" style="--i:6" d="M80 122H280M360 122H560M80 129H280M360 129H560M80 136H280M360 136H560"/><path pathLength="1" class="fein" style="--i:7" d="M80.0 143h20v16h-20zM105.7 143h20v16h-20zM131.4 143h20v16h-20zM157.1 143h20v16h-20zM182.9 143h20v16h-20zM208.6 143h20v16h-20zM234.3 143h20v16h-20zM260.0 143h20v16h-20zM360.0 143h20v16h-20zM385.7 143h20v16h-20zM411.4 143h20v16h-20zM437.1 143h20v16h-20zM462.9 143h20v16h-20zM488.6 143h20v16h-20zM514.3 143h20v16h-20zM540.0 143h20v16h-20z"/><path pathLength="1" class="fein" style="--i:8" d="M80 176H280M360 176H560M80 183H280M360 183H560M80 190H280M360 190H560"/><path pathLength="1" class="fein" style="--i:9" d="M80.0 197h20v16h-20zM105.7 197h20v16h-20zM131.4 197h20v16h-20zM157.1 197h20v16h-20zM182.9 197h20v16h-20zM208.6 197h20v16h-20zM234.3 197h20v16h-20zM260.0 197h20v16h-20zM360.0 197h20v16h-20zM385.7 197h20v16h-20zM411.4 197h20v16h-20zM437.1 197h20v16h-20zM462.9 197h20v16h-20zM488.6 197h20v16h-20zM514.3 197h20v16h-20zM540.0 197h20v16h-20z"/><path pathLength="1" class="fein" style="--i:10" d="M80 230H280M360 230H560M80 237H280M360 237H560M80 244H280M360 244H560"/><path pathLength="1" class="fein" style="--i:11" d="M80.0 251h20v16h-20zM105.7 251h20v16h-20zM131.4 251h20v16h-20zM157.1 251h20v16h-20zM182.9 251h20v16h-20zM208.6 251h20v16h-20zM234.3 251h20v16h-20zM260.0 251h20v16h-20zM360.0 251h20v16h-20zM385.7 251h20v16h-20zM411.4 251h20v16h-20zM437.1 251h20v16h-20zM462.9 251h20v16h-20zM488.6 251h20v16h-20zM514.3 251h20v16h-20zM540.0 251h20v16h-20z"/><path pathLength="1" class="fein" style="--i:12" d="M86 288h32v26h-32zM138 288h32v26h-32zM190 288h32v26h-32zM242 288h32v26h-32z"/><path pathLength="1" class="fein" style="--i:13" d="M366 288h32v26h-32zM418 288h32v26h-32zM470 288h32v26h-32zM522 288h32v26h-32z"/><path pathLength="1" style="--i:14" d="M300 330V292H340V330M320 292V330M294 286H346"/><path pathLength="1" class="gruen" style="--i:15" d="M36 330V250"/><circle pathLength="1" class="gruen" style="--i:16" cx="36" cy="222" r="26"/><path pathLength="1" class="gruen" style="--i:17" d="M690 330V282"/><circle pathLength="1" class="gruen" style="--i:18" cx="690" cy="266" r="15"/><g class="sp-auto"><g transform="translate(96 0)"><path d="M500 324v-8l10-2 8-10h32l10 10 8 2v8z"/><circle cx="516" cy="325" r="5"/><circle cx="552" cy="325" r="5"/></g></g><g class="sp-pin"><path d="M320 96s-17-15-17-30a17 17 0 0 1 34 0c0 15-17 30-17 30z"/><circle cx="320" cy="66" r="6"/></g><circle class="sp-ring" cx="320" cy="100" r="6"/><g class="sp-schild"><path d="M356 50h150v30H356z"/><text x="431" y="70" text-anchor="middle">Science Park II</text></g></svg>'
html = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{SEO_KOPF}
<meta name="theme-color" content="#FFFFFF">
{ICONS}
<link rel="stylesheet" href="d.css?v=72">
</head>
<body>
<header class="kopf">
  <div class="kopf-in">
    <a href="#start" class="logo" aria-label="APM Ulm – nach oben">{logo}</a>
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
    <h1 data-worte>Gebäude in Ulm, <em>um Ulm und um Ulm herum</em></h1>
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
    <li class="auf"><span class="v-punkt"><svg viewBox="0 0 20 20" aria-hidden="true"><path pathLength="1" d="M5.6 10.4l3 3 5.8-6.4"/></svg></span><svg class="v-bild" viewBox="0 0 120 80" aria-hidden="true"><path pathLength="1" d="M10 70h100"/><circle pathLength="1" cx="60" cy="31" r="11"/><path pathLength="1" d="M38 70c1-14 10-22 22-22s21 8 22 22"/><path pathLength="1" class="gruen" d="M80 10h22v15H91l-6 6v-6h-5z"/><path pathLength="1" class="gruen" d="M85 15.5h12M85 20h8"/></svg><span class="v-zahl">persönlich</span><h3>Ein Ansprechpartner</h3><p>Eine Nummer für Hausmeister, Technik, Brandschutz und Außenanlagen.</p></li>
    <li class="auf"><span class="v-punkt"><svg viewBox="0 0 20 20" aria-hidden="true"><path pathLength="1" d="M5.6 10.4l3 3 5.8-6.4"/></svg></span><svg class="v-bild" viewBox="0 0 120 80" aria-hidden="true"><path pathLength="1" d="M10 70h100"/><path pathLength="1" d="M22 70V28h36v42"/><path pathLength="1" d="M30 38h7M43 38h7M30 49h7M43 49h7M36 70V60h8v10"/><path pathLength="1" class="gruen" d="M86 64s-15-13-15-26a15 15 0 0 1 30 0c0 13-15 26-15 26z"/><circle pathLength="1" class="gruen" cx="86" cy="38" r="5"/></svg><span class="v-zahl">vor Ort</span><h3>Statt Hotline</h3><p>Wir kennen Ihr Gebäude, weil wir regelmäßig drin sind.</p></li>
    <li class="auf"><span class="v-punkt"><svg viewBox="0 0 20 20" aria-hidden="true"><path pathLength="1" d="M5.6 10.4l3 3 5.8-6.4"/></svg></span><svg class="v-bild" viewBox="0 0 120 80" aria-hidden="true"><path pathLength="1" d="M38 16h44v56H38z"/><path pathLength="1" d="M50 11h20v10H50z"/><path pathLength="1" class="gruen" d="M46 34l4 4 7-8"/><path pathLength="1" d="M63 34h12"/><path pathLength="1" class="gruen" d="M46 47l4 4 7-8"/><path pathLength="1" d="M63 47h12"/><path pathLength="1" class="gruen" d="M46 60l4 4 7-8"/><path pathLength="1" d="M63 60h12"/></svg><span class="v-zahl">lückenlos</span><h3>Alles dokumentiert</h3><p>Prüfungen, Wartungen und Mängel nachvollziehbar festgehalten.</p></li>
  </ul>
</section>

<section class="nebel" id="leistungen">
  <div class="teil">
    <div class="kopfzeile auf"><h2>Alles, was Ihr Gebäude braucht – <em>aus einer Hand</em></h2></div>
    <div class="reiter auf" role="tablist" aria-label="Leistungsbereich wählen">
      <button class="aktiv" role="tab" aria-selected="true" data-art="aussen">Infrastrukturelles Management</button>
      <button role="tab" aria-selected="false" data-art="technik">Technisches Management</button>
      <button role="tab" aria-selected="false" data-art="mod">Gebäudemodernisierung</button>
    </div>
    <div class="h-buehne auf">
      <div class="h-bild">{HAUS}{HAUS_MOD}<div class="h-punkte"></div></div>
      <div class="h-seite">
        <div class="h-detail" aria-live="polite"><span class="k-icon"></span><h3></h3><p></p></div>
        <ul class="h-liste">
{punkte(AUSSEN,'aussen')}{punkte(TECHNIK,'technik')}{punkte(MOD,'mod')}        </ul>
      </div>
    </div>
  </div>
</section>

<section class="teil" id="praxis">
  <div class="block">
    <div class="sp-bild auf">{SP}</div>
    <div class="block-text auf">
      
      <h2>Science Park II <em>Ulm</em></h2>
      <p>Am Oberen Eselsberg ist seit den 1980er-Jahren die Wissenschaftsstadt gewachsen: Forschungsinstitute, Labore und Entwicklungszentren namhafter Unternehmen. Hier betreuen wir Objekte im ganzheitlichen Facility Management.</p>
      <ul class="haken" data-nacheinander>
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
  <div class="kopfzeile auf"><h2>Vier Schritte bis zum <em>sicheren Betrieb</em></h2></div>
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
      <h2 class="riesig auf">Sprechen wir über <em>Ihr Gebäude</em></h2>
      <p class="k-lead auf">Kurz anrufen oder schreiben – wir schauen uns das Objekt an und machen Ihnen ein klares Angebot.</p>
    </div>
    <ul class="k-liste">
      <li class="auf"><span class="k-bild"><svg viewBox="0 0 24 24" aria-hidden="true"><path pathLength="1" d="M5 3.5h3.2l1.8 4.6-2.4 1.5a11 11 0 0 0 6.8 6.8l1.5-2.4 4.6 1.8v3.2a2 2 0 0 1-2 2A16.5 16.5 0 0 1 3 5.5a2 2 0 0 1 2-2z"/></svg></span><span class="k-was">Telefon</span><b><a href="tel:+491705810174">+49 170 5810174</a></b></li>
      <li class="auf"><span class="k-bild"><svg viewBox="0 0 24 24" aria-hidden="true"><path pathLength="1" d="M3.5 6h17v12h-17z"/><path pathLength="1" d="M3.5 6.5l8.5 6.5 8.5-6.5"/></svg></span><span class="k-was">E-Mail</span><b><a href="mailto:taha.altun@outlook.de">taha.altun@outlook.de</a></b></li>
      <li class="auf"><span class="k-bild"><svg viewBox="0 0 24 24" aria-hidden="true"><path pathLength="1" d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle pathLength="1" cx="12" cy="9.5" r="2.5"/></svg></span><span class="k-was">Einsatzgebiet</span><b><a class="k-karte" href="https://www.google.com/maps/search/?api=1&amp;query=Ulm" target="_blank" rel="noopener" aria-label="Einsatzgebiet Ulm, Neu-Ulm und Region in der Karte öffnen">Ulm, Neu-Ulm und Region</a></b></li>
    </ul>
  </div>
  {STADT}
</section>
</main>

<footer class="fuss">
  <div class="fuss-zeile"><img src="../img/logo.svg" alt="APM Ulm" width="70" height="30"><span>© 2026 APM Ulm</span><span><a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a></span></div>
  <details><summary>Bildnachweis</summary>
    <ul><li>Science Park II (Energon): G8w, <a href="https://commons.wikimedia.org/wiki/File:Ulm_Energon.jpg" rel="noopener">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.de" rel="noopener">CC BY-SA 3.0</a></li></ul>
    <p>Bilder zugeschnitten, verkleinert und ins WebP-Format umgewandelt; die Bearbeitung steht unter derselben Lizenz.</p>
  </details>
</footer>
<script src="../vendor/lenis.min.js" defer></script>
<script src="d.js?v=72" defer></script>
</body>
</html>
"""
open('index.html','w').write(html); print(len(AUSSEN)+len(TECHNIK)+len(MOD),'Leistungen')


# ------------------------------------------------------------------------------------------
# Rechtsseiten (Impressum, Datenschutz) im selben Stil
# ------------------------------------------------------------------------------------------
def Z(inner):
    return inner.replace('<path ','<path pathLength="1" ').replace('<circle ','<circle pathLength="1" ')
BILD_IMPRESSUM = '<svg class="r-bild" viewBox="0 0 320 220" aria-hidden="true">' + Z(
 '<path d="M30 40h260a12 12 0 0 1 12 12v116a12 12 0 0 1-12 12H30a12 12 0 0 1-12-12V52a12 12 0 0 1 12-12z"/>'
 '<circle cx="84" cy="96" r="22"/><path d="M48 156c3-22 18-33 36-33s33 11 36 33"/>'
 '<path d="M150 82h120M150 104h96M150 126h110M150 148h70"/>'
 '<path class="gruen" d="M252 176s-16-14-16-28a16 16 0 0 1 32 0c0 14-16 28-16 28z"/><circle class="gruen" cx="252" cy="148" r="5.5"/>') + '</svg>'
BILD_DATENSCHUTZ = '<svg class="r-bild" viewBox="0 0 320 220" aria-hidden="true">' + Z(
 '<path d="M160 18l86 32v60c0 52-36 86-86 100-50-14-86-48-86-100V50z"/>'
 '<path d="M130 104h60v50h-60z"/><path d="M140 104V88a20 20 0 0 1 40 0v16"/><circle cx="160" cy="124" r="6"/><path d="M160 130v12"/>'
 '<path class="gruen" d="M262 150a22 22 0 1 0 .1 0zM251 172l8 8 14-16"/>'
 '<path d="M22 150h34M22 164h24M22 178h30"/>') + '</svg>'

def rechtsseite(datei, titel, kurz, bild, inhalt):
    seite = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel} – APM Ulm</title>
<meta name="robots" content="noindex, follow">
<meta name="theme-color" content="#FFFFFF">
{ICONS}
<link rel="stylesheet" href="d.css?v=72">
<link rel="stylesheet" href="recht.css?v=3">
</head>
<body class="recht-seite">
<header class="kopf">
  <div class="kopf-in">
    <a href="index.html" class="logo" aria-label="APM Ulm – zur Startseite">{logo}</a>
    <button class="menue-knopf" aria-label="Menü" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav" aria-label="Hauptnavigation">
      <a href="index.html#leistungen">Leistungen</a>
      <a href="index.html#praxis">Praxisbeispiel</a>
      <a href="index.html#ablauf">Ablauf</a>
      <a href="index.html#kontakt" class="nav-cta">Kontakt</a>
    </nav>
  </div>
</header>
<main>
<section class="dunkel r-held">
  <div class="teil r-held-in">
    <div>
      <p class="label"><i></i>Rechtliches</p>
      <h1 data-worte>{titel}</h1>
      <p class="k-lead">{kurz}</p>
    </div>
    {bild}
  </div>
</section>
<section class="teil r-inhalt">
{inhalt}
  <p class="r-zurueck auf"><a href="index.html" class="btn r-btn">Zur Startseite</a></p>
</section>
</main>
<footer class="fuss r-fuss">
  {STADT}
  <div class="fuss-zeile"><img src="../img/logo.svg" alt="APM Ulm" width="70" height="30"><span>© 2026 APM Ulm</span><span><a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a></span></div>
</footer>
<script src="../vendor/lenis.min.js" defer></script>
<script src="recht.js?v=1" defer></script>
</body>
</html>
"""
    open(datei,'w').write(seite)

def abschnitt(titel, html):
    return f'  <article class="r-teil auf"><span class="v-punkt"><svg viewBox="0 0 20 20" aria-hidden="true"><path pathLength="1" d="M5.6 10.4l3 3 5.8-6.4"/></svg></span><h2>{titel}</h2>\n{html}\n  </article>\n'
def zeilen(paare):
    return '<dl class="r-daten">'+''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a,b in paare)+'</dl>'

NAME='Emre Altun'; STR='Weinbergweg 81'; ORT_='89075 Ulm'; TEL='+49 170 5810174'; MAIL='taha.altun@outlook.de'; USTID='DE364898141'
tel_l=f'<a href="tel:+491705810174">{TEL}</a>'; mail_l=f'<a href="mailto:{MAIL}">{MAIL}</a>'

imp = (
 abschnitt('Angaben gemäß § 5 DDG', zeilen([('Unternehmen','apm ulm – altun property management'),('Inhaber',NAME),('Anschrift',f'{STR}<br>{ORT_}<br>Deutschland')])) +
 abschnitt('Kontakt', zeilen([('Telefon',tel_l),('E-Mail',mail_l)])) +
 abschnitt('Umsatzsteuer', zeilen([('Umsatzsteuer-Identifikationsnummer nach § 27a UStG',USTID)])) +
 abschnitt('Verantwortlich für den Inhalt', f'<p>Verantwortlich nach § 18 Abs. 2 MStV: {NAME}, {STR}, {ORT_}.</p>') +
 abschnitt('Verbraucherstreitbeilegung', '<p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>') +
 abschnitt('Haftung für Inhalte und Links', '<p>Die Inhalte dieser Website wurden sorgfältig erstellt. Für eigene Inhalte sind wir nach den allgemeinen Gesetzen verantwortlich. Für Inhalte fremder Websites, auf die wir verlinken, ist der jeweilige Anbieter verantwortlich. Bei Bekanntwerden von Rechtsverletzungen entfernen wir solche Links umgehend.</p>') +
 abschnitt('Urheberrecht und Bildnachweis', '<p>Texte, Zeichnungen und Gestaltung dieser Website sind urheberrechtlich geschützt.</p><p>Foto auf der Startseite (Bürogebäude im Science Park II): G8w, <a href="https://commons.wikimedia.org/wiki/File:Ulm_Energon.jpg" rel="noopener">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.de" rel="noopener">CC BY-SA 3.0</a>. Das Bild wurde zugeschnitten, verkleinert, in Graustufen und ins WebP-Format umgewandelt; die Bearbeitung steht unter derselben Lizenz.</p>')
)
rechtsseite('impressum.html','Impressum','Wer hinter dieser Website steht und wie Sie uns erreichen.',BILD_IMPRESSUM,imp)

ds = (
 abschnitt('Kurz gesagt', '<ul class="r-haken"><li>Wir setzen keine Cookies zu Analyse- oder Werbezwecken ein.</li><li>Es gibt kein Tracking, keine Statistik-Werkzeuge und keine eingebetteten Inhalte fremder Anbieter.</li><li>Es gibt kein Kontaktformular. Sie erreichen uns per Telefon oder E-Mail.</li><li>Schriften, Zeichnungen und Skripte werden von dieser Website selbst geladen, nicht von Dritten.</li></ul>') +
 abschnitt('Verantwortlicher', zeilen([('Verantwortlich im Sinne der DSGVO',f'{NAME}<br>{STR}<br>{ORT_}<br>Deutschland'),('Telefon',tel_l),('E-Mail',mail_l)])) +
 abschnitt('Hosting', '<p>Diese Website wird bei der Wix.com Ltd., 40 Namal Tel Aviv St., Tel Aviv 6350671, Israel, gehostet. Beim Aufruf der Seiten verarbeitet der Anbieter technisch notwendige Daten in sogenannten Server-Protokollen: IP-Adresse, Datum und Uhrzeit des Zugriffs, aufgerufene Seite, übertragene Datenmenge, Browser und Betriebssystem sowie die zuvor besuchte Seite.</p><p>Die Verarbeitung ist erforderlich, um die Website sicher und stabil auszuliefern. Rechtsgrundlage ist Art. 6 Abs. 1 Buchst. f DSGVO; unser berechtigtes Interesse liegt im sicheren Betrieb. Der Anbieter kann zu diesem Zweck technisch notwendige Cookies setzen, etwa zur Sicherheit und zur Lastverteilung.</p><p>Für Israel besteht ein Angemessenheitsbeschluss der Europäischen Kommission. Soweit Daten in weitere Länder außerhalb der EU übermittelt werden, geschieht das auf Grundlage eines Angemessenheitsbeschlusses oder der Standardvertragsklauseln der Europäischen Kommission. Mit dem Anbieter besteht ein Vertrag zur Auftragsverarbeitung.</p>') +
 abschnitt('Kontakt per Telefon oder E-Mail', '<p>Wenn Sie uns anrufen oder schreiben, verarbeiten wir Ihre Angaben (Name, Kontaktdaten, Inhalt der Anfrage), um Ihre Anfrage zu bearbeiten. Rechtsgrundlage ist Art. 6 Abs. 1 Buchst. b DSGVO, soweit es um einen Vertrag oder dessen Anbahnung geht, im Übrigen Art. 6 Abs. 1 Buchst. f DSGVO.</p><p>Wir löschen die Daten, sobald die Anfrage erledigt ist und keine gesetzlichen Aufbewahrungspflichten entgegenstehen. Geschäftliche Korrespondenz bewahren wir nach § 147 AO und § 257 HGB sechs Jahre auf, Buchungsbelege acht Jahre.</p>') +
 abschnitt('Ihre Rechte', '<ul class="r-haken"><li>Auskunft über die zu Ihnen gespeicherten Daten (Art. 15 DSGVO)</li><li>Berichtigung unrichtiger Daten (Art. 16 DSGVO)</li><li>Löschung (Art. 17 DSGVO) und Einschränkung der Verarbeitung (Art. 18 DSGVO)</li><li>Datenübertragbarkeit (Art. 20 DSGVO)</li><li>Widerspruch gegen Verarbeitungen, die auf Art. 6 Abs. 1 Buchst. f DSGVO beruhen (Art. 21 DSGVO)</li><li>Widerruf einer erteilten Einwilligung mit Wirkung für die Zukunft (Art. 7 Abs. 3 DSGVO)</li></ul><p>Zur Ausübung genügt eine formlose Nachricht an die oben genannte Adresse.</p>') +
 abschnitt('Beschwerderecht', '<p>Sie haben das Recht, sich bei einer Datenschutz-Aufsichtsbehörde zu beschweren (Art. 77 DSGVO). Zuständig für uns ist: Der Landesbeauftragte für den Datenschutz und die Informationsfreiheit Baden-Württemberg, Lautenschlagerstraße 20, 70173 Stuttgart.</p>') +
 abschnitt('Stand', '<p>Oktober 2026. Wenn sich die Website oder die Rechtslage ändert, passen wir diese Erklärung an.</p>')
)
rechtsseite('datenschutz.html','Datenschutz','Welche Daten beim Besuch dieser Website anfallen und was mit ihnen geschieht.',BILD_DATENSCHUTZ,ds)
print('Rechtsseiten gebaut')

# Suchmaschinen-Dateien
open('robots.txt','w').write('User-agent: *\nAllow: /\nSitemap: '+DOMAIN+'/sitemap.xml\n' if LIVE else 'User-agent: *\nDisallow: /\n')
import datetime as _dt
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<url><loc>'+DOMAIN+'/</loc><lastmod>'+_dt.date.today().isoformat()+'</lastmod></url>\n</urlset>\n')
