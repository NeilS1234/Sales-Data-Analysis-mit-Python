# Verkaufsdatenanalyse mit Python

## 1. Problemstellung

Ziel dieses Projekts ist es, Verkaufsdaten mit Python zu analysieren. Dabei sollen Verkaufstrends, meistverkaufte Produkte und monatliche Umsatzentwicklungen untersucht werden. Die Ergebnisse sollen dabei helfen, Geschäftsentscheidungen auf Grundlage von Daten zu treffen.

## 2. Zielgruppe

Das Projekt richtet sich an Geschäftsinhaber, Verkaufsmanager und Mitarbeitende im Controlling. Sie können die Ergebnisse nutzen, um die Verkaufsleistung zu bewerten und Verbesserungspotenziale zu erkennen.

## 3. Datenquelle

Für das Projekt wird der öffentlich verfügbare Sample-Superstore-Datensatz verwendet.

Der Datensatz enthält Informationen zu Bestelldaten, Produktnamen, Umsätzen und verkauften Mengen. Die Daten werden mit Python und pandas eingelesen und verarbeitet.

## 4. Analysefragen

- Wie hoch ist der Gesamtumsatz im untersuchten Zeitraum?
- In welchen Monaten wird der höchste Umsatz erzielt?
- Welche Produkte werden am häufigsten verkauft?
- Welche Produkte erzielen den höchsten Umsatz?
- Wie entwickelt sich der Umsatz im Zeitverlauf?

## 5. Geplante Berechnungen und Diagramme

### Berechnungen

- Gesamtumsatz berechnen.
- Monatlichen Umsatz ermitteln.
- Verkaufte Mengen pro Produkt zusammenfassen.
- Produkte mit dem höchsten Umsatz identifizieren.
- Durchschnittlichen Bestellwert berechnen, sofern die Daten dies ermöglichen.

### Diagramme

- Liniendiagramm zur Darstellung der monatlichen Umsatzentwicklung.
- Balkendiagramm für die umsatzstärksten Produkte.
- Balkendiagramm für die meistverkauften Produkte nach Menge.

## 6. Repository-Struktur

sales-data-analysis/
├── data/
│   └── sales.csv
├── notebooks/
│   └── analysis.ipynb
├── src/
│   ├── data_loader.py
│   ├── cleaning.py
│   ├── analysis.py
│   └── visualization.py
├── tests/
│   └── test_analysis.py
├── output/
│   └── charts/
├── requirements.txt
├── .gitignore
└── README.md

## 7. GitHub Milestones und Issues

### Milestone 1: Projektvorbereitung

- [ ] Issue 1: Projektanforderungen definieren
- [ ] Issue 2: Datensatz auswählen und herunterladen
- [ ] Issue 3: Repository-Struktur erstellen
- [ ] Issue 4: Python-Abhängigkeiten einrichten

### Milestone 2: Datenanalyse

- [ ] Issue 5: Verkaufsdaten laden und bereinigen
- [ ] Issue 6: Kennzahlen berechnen
- [ ] Issue 7: Analysefragen beantworten
- [ ] Issue 8: Diagramme erstellen

### Milestone 3: Tests und Dokumentation

- [ ] Issue 9: Berechnungen testen
- [ ] Issue 10: Analyseergebnisse überprüfen
- [ ] Issue 11: Projektdokumentation vervollständigen

Jedes Issue beschreibt eine konkrete Aufgabe mit nachvollziehbaren Akzeptanzkriterien. Die Issues werden den passenden Milestones zugeordnet und nach erfolgreicher Bearbeitung geschlossen.

## 8. Definition of Done

Das Projekt gilt als abgeschlossen, wenn folgende Kriterien erfüllt sind:

- [ ] Der Datensatz wurde erfolgreich eingelesen und bereinigt.
- [ ] Fehlende und fehlerhafte Werte wurden überprüft und angemessen behandelt.
- [ ] Alle geplanten Berechnungen wurden umgesetzt und getestet.
- [ ] Alle Analysefragen wurden beantwortet.
- [ ] Alle geplanten Diagramme wurden erstellt und gespeichert.
- [ ] Die Ergebnisse wurden auf ihre Richtigkeit überprüft.
- [ ] Der Code wurde in geeignete Python-Module aufgeteilt.
- [ ] Die automatisierten Tests wurden erfolgreich durchgeführt.
- [ ] Die README dokumentiert die Projektstruktur und die Ausführung.
- [ ] Alle erforderlichen Dateien sind im GitHub-Repository vorhanden.

## 9. Risiken und Annahmen

### Risiken

- Der Datensatz kann fehlende oder fehlerhafte Werte enthalten.
- Einige Analysefragen lassen sich möglicherweise mit den verfügbaren Daten nicht beantworten.
- Fehlerhafte Berechnungen können zu falschen Schlussfolgerungen führen.
- Die tatsächliche Struktur des Datensatzes kann von den Erwartungen abweichen.
- Bei der Installation von Python-Bibliotheken können Probleme auftreten.

### Annahmen

- Ein geeigneter öffentlicher Verkaufsdatensatz ist verfügbar.
- Die benötigten Datenfelder sind vorhanden.
- Python und die erforderlichen Bibliotheken können installiert werden.
- Der Datensatz ist für die geplante Analyse geeignet.
- Die Daten dürfen für Lern- und Analysezwecke verwendet werden.