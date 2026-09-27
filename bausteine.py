#!/usr/bin/env python3
"""Baut die vier Seiten von Site/ aus einer gemeinsamen Vorlage.

    python3 Site/bausteine.py

So bleiben Kopf, Navigation und Fußzeile über alle Seiten gleich, und ein
geänderter Rechtstext muss nur an einer Stelle nachgezogen werden.
"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
STAND = "27. September 2026"

ANKER = ('<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
         '<g stroke="#FBF6EC" stroke-width="8" fill="none" stroke-linecap="round" '
         'stroke-linejoin="round"><circle cx="60" cy="29" r="9"/><path d="M60 38 V93"/>'
         '<path d="M40 50 H80"/><path d="M28 70 C28 88 42 97 60 97 C78 97 92 88 92 70"/></g>'
         '<g fill="#FBF6EC"><path d="M28 66 l-11 6 l14 8 z"/>'
         '<path d="M92 66 l11 6 l-14 8 z"/></g></svg>')

SEITEN = [("index.html", "Support"), ("datenschutz.html", "Datenschutz"),
          ("agb.html", "Nutzungsbedingungen"), ("impressum.html", "Impressum")]

VORLAGE = """<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel} — Bootsschein</title>
<meta name="description" content="{beschreibung}">
<link rel="stylesheet" href="stil.css">
</head><body><div class="seite">
<header class="kopf">
  <div class="anker">{anker}</div>
  <div><h1>Bootsschein</h1><p>SBF See &amp; Binnen — Theorie üben</p></div>
</header>
<nav>{navigation}</nav>
{inhalt}
<footer>
  <a href="index.html">Support</a><a href="datenschutz.html">Datenschutz</a>
  <a href="agb.html">Nutzungsbedingungen</a><a href="impressum.html">Impressum</a>
  <a href="https://www.brockdesign.de/apps/bootsschein">Mehr zur App</a>
  <p>Stand: {stand}</p>
</footer>
</div></body></html>
"""

INDEX = """
<div class="karte">
<h2>Hilfe und Kontakt</h2>
<p>Schreib uns einfach — am schnellsten geht es direkt aus der App heraus über
<strong>Einstellungen → Kontakt</strong>. Dort sind App-Version, iOS-Version und
Gerätemodell schon eingetragen, das hilft bei der Suche.</p>
<p>Verbesserungen und Fehler: <a href="mailto:kontakt@brockdesign.de">kontakt@brockdesign.de</a><br>
Alles Übrige: <a href="mailto:apple@brockdesign.de">apple@brockdesign.de</a></p>
</div>

<h2>Häufige Fragen</h2>

<div class="karte">
<h3>Sind das die echten Prüfungsfragen?</h3>
<p>Ja. Fragen, Antworten und Abbildungen stammen unverändert aus dem amtlichen
Fragen- und Antwortenkatalog des Bundesministeriums für Digitales und Verkehr
(Stand 1. August 2023). Auch die Zusammensetzung der 15 Prüfungsbögen folgt der
amtlichen Bekanntmachung. In der Prüfung bekommst du genau einen dieser Bögen.</p>

<h3>Warum sind die Antworten anders sortiert als im Katalog?</h3>
<p>Im amtlichen Katalog steht die richtige Antwort immer an erster Stelle. In der
echten Prüfung sind die Antworten gemischt. Die App mischt deshalb ebenfalls bei
jedem Durchgang neu — sonst würde man sich Positionen merken statt Antworten.</p>

<h3>Wann ist ein Bogen bestanden?</h3>
<p>Ein Bogen hat 7 Basisfragen und 23 spezifische Fragen. Bestanden ist er nur,
wenn mindestens 5 Basisfragen <em>und</em> mindestens 18 spezifische Fragen richtig
sind. Beide Hürden zählen getrennt — 27 von 30 richtig können trotzdem
nicht reichen. Die Auswertung zeigt deshalb zwei Balken statt einer Zahl.</p>

<h3>Was kostet die App?</h3>
<p>Der Download ist kostenlos, je Bereich ist der erste Prüfungsbogen frei.
Die übrigen Bögen schaltest du mit einem einmaligen Kauf frei — kein Abo, keine
laufenden Kosten. Der Kauf hängt an deiner Apple-ID und lässt sich auf deinen
Geräten wiederherstellen.</p>

<h3>Sind die Navigationsaufgaben dabei?</h3>
<p>Noch nicht. Version 1 enthält die 15 Prüfungsbögen für See und Binnen. Die
Navigationsaufgaben für den Sportbootführerschein See kommen in einem späteren
Update. Für die Prüfung brauchst du sie zusätzlich zum Bogen.</p>

<h3>Bleiben meine Ergebnisse erhalten?</h3>
<p>Ja, alles wird auf deinem iPhone gespeichert und überlebt App-Updates.
Löschst du die App, sind die Daten weg — es gibt bewusst kein Konto und keine
Übertragung auf unsere Server.</p>

<h3>Ist die App ein amtliches Angebot?</h3>
<p>Nein. Es handelt sich um eine private Lernhilfe. Sie steht in keiner
Verbindung zu einer Behörde und ersetzt keine Fahrschule.</p>
</div>
"""

DATENSCHUTZ = """
<div class="karte">
<h2>Kurz gesagt</h2>
<p>Deine Lernergebnisse bleiben auf deinem iPhone. Es gibt kein Benutzerkonto,
keine Anmeldung und keine Werbung. Nach außen geht nur eine anonyme
Nutzungsstatistik, die du in den Einstellungen abschalten kannst.</p>
</div>

<h2>Verantwortlich</h2>
<p>Johann Brockstedt, Burkamp 1, 24220 Flintbek, Deutschland<br>
<a href="mailto:apple@brockdesign.de">apple@brockdesign.de</a></p>

<h2>Was auf dem Gerät bleibt</h2>
<p>Alle bearbeiteten Prüfungsbögen, deine Ergebnisse, dein Fehlerspeicher, ein
eingetragener Prüfungstermin und deine Einstellungen werden ausschließlich lokal
gespeichert. Sie werden nicht übertragen und nicht ausgewertet. Löschst du die
App, sind sie vollständig weg.</p>

<h2>Anonyme Nutzungsstatistik</h2>
<p>Zur Verbesserung der App wird TelemetryDeck eingesetzt (TelemetryDeck GmbH,
Von-der-Tann-Str. 54, 86159 Augsburg, Deutschland). Übertragen wird nur,
<strong>dass</strong> ein Ereignis stattgefunden hat:</p>
<ul>
  <li>welcher Schein beim ersten Start gewählt wurde (See, Binnen oder beides),</li>
  <li>dass ein Bogen gestartet, abgegeben oder abgebrochen wurde,</li>
  <li>ob ein Bogen bestanden wurde (ja/nein, nie die Punktzahl),</li>
  <li>dass der Fehlerspeicher zum Lernen geöffnet wurde,</li>
  <li>dass die Kaufseite geöffnet wurde, von welcher Stelle der App aus
    (gesperrter Bogen oder Hinweiskarte) und für welchen Bereich,</li>
  <li>dass ein Kauf abgeschlossen wurde. Dabei überträgt das Statistik-Werkzeug
    die Produktkennung, die Kaufart, das Land deines App-Store-Kontos, die
    Währung und den Preis. <strong>Zahlungsdaten, Rechnungsdaten und deine
    Apple-ID werden nicht übertragen</strong> — die Zahlung wickelt
    ausschließlich Apple ab,</li>
  <li>dass beim Laden der Preise, beim Kaufen oder beim Wiederherstellen ein
    Fehler aufgetreten ist, als feste Kennung wie „kauf.kaufen.netz“. Die
    Fehlermeldung selbst wird nie übertragen,</li>
  <li>dass diese Statistik ausgeschaltet wurde. Dieser eine Zähler wird im
    Moment des Ausschaltens gesendet; danach wird nichts mehr gesendet.</li>
</ul>
<p>Mit jedem Ereignis gehen technische Rahmendaten mit: App- und iOS-Version,
Gerätemodell, Sprach- und Regionseinstellung, Zeitzone sowie eine zufällige
Sitzungskennung.</p>
<p><strong>Nicht erfasst werden:</strong> deine Punktzahlen, welche Fragen du falsch
beantwortet hast, dein Prüfungstermin, dein Name, deine E-Mail-Adresse, deine
IP-Adresse oder dein Standort.</p>
<p>TelemetryDeck ordnet die Ereignisse einem Gerät über eine pseudonyme Kennung
zu. Sie entsteht auf dem Gerät als Prüfsumme aus der Gerätekennung, die Apple
allen Apps eines Anbieters gemeinsam zuteilt, und lässt sich nicht auf dein
Gerät zurückrechnen. Sie bleibt gleich, solange auf dem Gerät eine unserer Apps
installiert ist, und ist bei allen unseren Apps auf demselben Gerät dieselbe.
Mit Daten anderer Unternehmen wird sie nicht verknüpft. Es wird keine
Werbe-Kennung verwendet, kein Profil über dich gebildet, und es werden keine
Daten an Werbenetzwerke weitergegeben oder verkauft.</p>
<p>Rechtsgrundlage ist Artikel 6 Absatz 1 Buchstabe f DSGVO — das berechtigte
Interesse an einer funktionierenden, verbesserten App. Du kannst jederzeit
widersprechen: <strong>Einstellungen → Datenschutz → „Anonyme Statistiken
senden“ ausschalten</strong>. Danach wird nichts mehr gesendet.</p>

<h2>Wenn du uns schreibst</h2>
<p>Nutzt du „Verbesserung vorschlagen“ oder „Fehler melden“, öffnet sich dein
E-Mail-Programm mit einem vorbereiteten Text. Erst wenn du selbst auf Senden
tippst, gehen deine E-Mail-Adresse und dein Text an uns. Sichtbar im Text stehen
App-Version, iOS-Version und Gerätemodell — sonst nichts. Wir nutzen die Angaben
nur zur Beantwortung und löschen sie danach.</p>

<h2>Käufe</h2>
<p>Käufe innerhalb der App werden vollständig über Apple abgewickelt. Wir
erhalten weder deine Zahlungsdaten noch deine Apple-ID. Es gilt zusätzlich die
Datenschutzerklärung von Apple. Was die anonyme Nutzungsstatistik zu Käufen
zählt, steht oben.</p>

<h2>Deine Rechte</h2>
<p>Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der
Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht, dich bei
einer Aufsichtsbehörde zu beschweren. Zuständig ist das Unabhängige
Landeszentrum für Datenschutz Schleswig-Holstein, Holstenstraße 98, 24103 Kiel.
Da wir keine personenbezogenen Daten speichern, können wir zu deiner Person
allerdings auch keine Auskunft erteilen.</p>
"""

AGB = """
<div class="karte">
<h2>Geltungsbereich</h2>
<p>Diese Bedingungen gelten für die Nutzung der App „Bootsschein“ von Johann
Brockstedt. Für die Abwicklung des Kaufs gelten zusätzlich die Bedingungen von
Apple.</p>
</div>

<h2>Was die App ist — und was nicht</h2>
<p>Die App ist eine private Lernhilfe zur Vorbereitung auf die theoretische
Prüfung zum Sportbootführerschein. Sie ist kein amtliches Angebot, steht in
keiner Verbindung zu einer Behörde und ersetzt weder eine Fahrschule noch die
vorgeschriebene Ausbildung. Ein Bestehen der Prüfung wird nicht zugesichert.</p>

<h2>Inhalte</h2>
<p>Fragen, Antworten und Abbildungen stammen unverändert aus dem amtlichen
Fragen- und Antwortenkatalog des Bundesministeriums für Digitales und Verkehr,
bekannt gemacht im Verkehrsblatt (Stand 1. August 2023); die Zusammensetzung der
15 Fragebogen folgt der Bekanntmachung im Verkehrsblatt 2012, Seite 224.
Maßgeblich ist immer die jeweils geltende amtliche Fassung. Wir übernehmen keine
Gewähr für Vollständigkeit und Aktualität; Fehler bitte über „Fehler melden“
mitteilen.</p>

<h2>Käufe</h2>
<p>Die App ist kostenlos. Je Bereich ist der erste Prüfungsbogen frei nutzbar.
Die übrigen Bögen lassen sich durch einen einmaligen Kauf freischalten — es gibt
kein Abonnement und keine laufenden Kosten. Der Kauf ist an deine Apple-ID
gebunden und lässt sich auf deinen Geräten wiederherstellen. Erstattungen
wickelt ausschließlich Apple ab.</p>

<h2>Widerrufsrecht</h2>
<p>Beim Kauf digitaler Inhalte über den App Store gilt das Widerrufsrecht
gegenüber Apple als Vertragspartner. Anfragen zur Erstattung richtest du bitte
direkt an Apple.</p>

<h2>Haftung</h2>
<p>Wir haften unbeschränkt bei Vorsatz und grober Fahrlässigkeit sowie bei
Verletzung von Leben, Körper oder Gesundheit. Bei leichter Fahrlässigkeit haften
wir nur bei Verletzung einer wesentlichen Vertragspflicht und begrenzt auf den
vertragstypischen, vorhersehbaren Schaden. Für Entscheidungen im Schiffsverkehr
ist allein der Schiffsführer verantwortlich.</p>

<h2>Urheberrecht</h2>
<p>Gestaltung, Aufbau und Programmierung der App sind geschützt. Die amtlichen
Prüfungsinhalte sind davon nicht erfasst.</p>

<h2>Schlussbestimmungen</h2>
<p>Es gilt deutsches Recht. Sollte eine Bestimmung unwirksam sein, bleibt der
Rest wirksam. Die Europäische Kommission stellt eine Plattform zur
Online-Streitbeilegung bereit
(<a href="https://ec.europa.eu/consumers/odr">ec.europa.eu/consumers/odr</a>);
wir sind weder verpflichtet noch bereit, an einem Streitbeilegungsverfahren vor
einer Verbraucherschlichtungsstelle teilzunehmen.</p>
"""

IMPRESSUM = """
<div class="karte">
<h2>Angaben gemäß § 5 DDG</h2>
<p>Johann Brockstedt<br>Burkamp 1<br>24220 Flintbek<br>Deutschland</p>
<h3>Kontakt</h3>
<p>E-Mail: <a href="mailto:apple@brockdesign.de">apple@brockdesign.de</a></p>
<h3>Verantwortlich nach § 18 Absatz 2 MStV</h3>
<p>Johann Brockstedt, Anschrift wie oben</p>
</div>

<h2>Quelle der Prüfungsinhalte</h2>
<p>Fragen- und Antwortenkatalog für den amtlichen Sportbootführerschein,
herausgegeben vom Bundesministerium für Digitales und Verkehr, bekannt gemacht
im Verkehrsblatt (Stand 1. August 2023). Verteilung der Fragen auf die einzelnen
Fragebogen: Verkehrsblatt 2012, Seite 224. Wiedergabe unverändert.</p>

<h2>Haftung für Links</h2>
<p>Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte
wir keinen Einfluss haben. Für diese fremden Inhalte kann keine Gewähr
übernommen werden; verantwortlich ist stets der jeweilige Anbieter.</p>
"""

INHALTE = {
    "index.html": ("Support", "Hilfe, häufige Fragen und Kontakt zur App Bootsschein.", INDEX),
    "datenschutz.html": ("Datenschutz",
                         "Datenschutzerklärung der App Bootsschein — was auf dem Gerät "
                         "bleibt und was anonym erfasst wird.", DATENSCHUTZ),
    "agb.html": ("Nutzungsbedingungen",
                 "Nutzungsbedingungen der App Bootsschein.", AGB),
    "impressum.html": ("Impressum", "Impressum und Anbieterkennzeichnung.", IMPRESSUM),
}


def bauen():
    for datei, (titel, beschreibung, inhalt) in INHALTE.items():
        aktiv = ' aria-current="page"'
        nav = "".join('<a href="%s"%s>%s</a>' % (ziel, aktiv if ziel == datei else "", name)
                      for ziel, name in SEITEN)
        seite = VORLAGE.format(titel=titel, beschreibung=beschreibung, anker=ANKER,
                               navigation=nav, inhalt=inhalt.strip(), stand=STAND)
        with open(os.path.join(HIER, datei), "w", encoding="utf-8") as f:
            f.write(seite)
        print(f"  {datei}  {len(seite):>6} Zeichen")


if __name__ == "__main__":
    bauen()
    print("Site gebaut.")
