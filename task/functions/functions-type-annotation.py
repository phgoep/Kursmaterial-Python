#
# MODULARISIERUNG UND TYPE ANNOTATIONS - AUFGABEN
#
# THEMA: Funktionen in Module auslagern und mit Type Hints arbeiten
#
# HINWEIS: Für diese Aufgaben brauchst du mehrere Dateien.
# Erstelle folgende Dateien im gleichen Ordner:
# - main.py (Hauptprogramm)
# - rechner.py (Rechner-Funktionen)
# - hilfe.py (Hilfsfunktionen)
# - daten.py (Datenbank-Funktionen)
#

#
# AUFGABE 1: EINFACHE MODULARISIERUNG (EINFACH)
#
# Lagere einfache Funktionen in separate Module aus.
#
# 1. Erstelle die Datei 'rechner.py' mit folgenden Funktionen:
#    1.a def addieren(a: float, b: float) -> float:
#    1.b def subtrahieren(a: float, b: float) -> float:
#    1.c def multiplizieren(a: float, b: float) -> float:
#    1.d def dividieren(a: float, b: float) -> float:
#         TIPP: Bei Division durch 0 eine Fehlermeldung ausgeben
#
# 2. In 'main.py' importiere die Funktionen aus 'rechner.py'
# 3. Der Benutzer gibt 2 Zahlen und eine Operation ein
# 4. Rufe die passende Funktion auf
# 5. Gib das Ergebnis mit korrekter Type Annotation aus
#
# BEISPIEL:
# Erste Zahl: 10
# Zweite Zahl: 5
# Operation (+, -, *, /): +
# Ergebnis: 10 + 5 = 15
#

#
# AUFGABE 2: MEHRERE MODULE (MITTEL)
#
# Erstelle drei Module mit verschiedenen Funktionalitäten.
#
# 1. Erstelle 'hilfe.py' mit:
#    1.a def zeige_menu() -> None:
#         Gibt ein Menü aus
#    1.b def eingabe_zahl(prompt: str) -> float:
#         Nimmt eine Zahl als input und gibt sie als float zurück
#    1.c def bestaetigung(prompt: str) -> bool:
#         Gibt True zurück bei "ja", sonst False
#         TIPP: Verwende .lower() für die Eingabe
#
# 2. Erstelle 'daten.py' mit:
#    2.a def speichere_daten(dateiname: str, daten: dict) -> None:
#         Speichert ein Wörterbuch in eine Datei
#         TIPP: Verwende open() mit "w" und write()
#    2.b def lade_daten(dateiname: str) -> dict:
#         Lädt ein Wörterbuch aus einer Datei
#         TIPP: Verwende open() mit "r" und read()
#
# 3. In 'main.py' importiere die Funktionen aus beiden Modulen
# 4. Verwende die Funktionen für ein kleines Programm
#
# BEISPIEL:
# hilfe.zeige_menu()
# zahl1 = hilfe.eingabe_zahl("Erste Zahl: ")
# if hilfe.bestaetigung("Speichern? "):
#     daten.speichere_daten("zahlen.txt", {"zahl1": zahl1})
#

#
# AUFGABE 3: DATENBANK-MODUL MIT TYPE ANNOTATIONS (MITTEL)
#
# Erstelle ein Modul für eine einfache Datenbank von Benutzern.
#
# 1. Erstelle 'user_db.py' mit:
#    1.a def benutzer_hinzufuegen(datenbank: dict, name: str, alter: int) -> dict:
#         Fügt einen neuen Benutzer zur Datenbank hinzu
#         Gibt die aktualisierte Datenbank zurück
#    1.b def benutzer_loeschen(datenbank: dict, name: str) -> dict:
#         Löscht einen Benutzer aus der Datenbank
#         Gibt die aktualisierte Datenbank zurück
#    1.c def benutzer_suchen(datenbank: dict, name: str) -> dict | None:
#         Sucht einen Benutzer und gibt ihn zurück (oder None)
#    1.d def zeige_alle_benutzer(datenbank: dict) -> None:
#         Gibt alle Benutzer aus
#    1.e def durchschnittsalter(datenbank: dict) -> float:
#         Berechnet das Durchschnittsalter aller Benutzer
#
# 2. In 'main.py' importiere die Funktionen
# 3. Erstelle ein Menü für die Benutzerverwaltung
# 4. Verwende Type Annotations für alle Funktionen
# 5. TIPP: Für Typ | None verwende from typing import Optional oder Union
#    ODER: from typing import Optional, dann Optional[dict]
#
# BEISPIEL:
# db = {}
# db = user_db.benutzer_hinzufuegen(db, "Anna", 25)
# db = user_db.benutzer_hinzufuegen(db, "Ben", 30)
# user_db.zeige_alle_benutzer(db)
# durchschnitt = user_db.durchschnittsalter(db)
# print("Durchschnittsalter:", durchschnitt)
#

#
# AUFGABE 4: FUNKTIONEN MIT DEFAULT-WERTEN UND ANNOTATIONS (MITTEL)
#
# Erstelle Funktionen mit Type Annotations und Default-Werten.
#
# 1. Erstelle 'formatierer.py' mit:
#    1.a def zentriere_text(text: str, breite: int = 50) -> str:
#         Zentriert den Text in einer Zeile der gegebenen Breite
#         TIPP: Verwende text.center(breite)
#    1.b def trennlinie(zeichen: str = "-", laenge: int = 50) -> str:
#         Erstellt eine Trennlinie aus dem Zeichen
#         TIPP: Verwende zeichen * laenge
#    1.c def ausgabe_mit_rahmen(text: str, zeichen: str = "*") -> None:
#         Gibt den Text mit einem Rahmen aus
#         TIPP: Kombiniere zentriere_text und trennlinie
#    1.d def farbiger_text(text: str, farbe: str = "gruen") -> str:
#         Gibt den Text in einer Farbe zurück
#         TIPP: ANSI-Farbcodes verwenden
#
# 2. In 'main.py' importiere die Funktionen
# 3. Teste die Funktionen mit verschiedenen Parametern
#
# BEISPIEL:
# formatierer.zentriere_text("Hallo Welt")
# formatierer.trennlinie("=", 30)
# formatierer.ausgabe_mit_rahmen("Wichtig!", "#")
# print(formatierer.farbiger_text("Fehler", "rot"))
#

#
# AUFGABE 5: KOMPLEXE TYPE ANNOTATIONS (SCHWER)
#
# Verwende komplexere Type Annotations für Listen, Dictionaries und Optionale Werte.
#
# 1. Erstelle 'statistik.py' mit:
#    1.a from typing import List, Dict, Optional, Union
#    1.b def berechne_durchschnitt(zahlen: List[float]) -> float:
#         Berechnet den Durchschnitt einer Liste
#    1.c def finde_maximum(zahlen: List[float]) -> Optional[float]:
#         Findet das Maximum oder gibt None zurück bei leerer Liste
#    1.d def haeufigkeit(woerter: List[str]) -> Dict[str, int]:
#         Zählt die Häufigkeit von Wörtern in einer Liste
#    1.e def zusammenfuegen(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
#         Fügt zwei Wörterbücher zusammen (addiert Werte bei gleichen Schlüsseln)
#    1.f def filtere_dict(daten: Dict[str, int], grenze: int) -> Dict[str, int]:
#         Filtert ein Wörterbuch nach Werten (nur Werte > grenze behalten)
#
# 2. In 'main.py' importiere die Funktionen
# 3. Teste die Funktionen mit verschiedenen Daten
# 4. Verwende die Type Hints korrekt mit List, Dict, Optional
#
# BEISPIEL:
# zahlen = [1, 2, 3, 4, 5]
# durchschnitt = statistik.berechne_durchschnitt(zahlen)
# max_wert = statistik.finde_maximum(zahlen)
# woerter = ["a", "b", "a", "c", "b", "a"]
# haeufigkeit = statistik.haeufigkeit(woerter)
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# merged = statistik.zusammenfuegen(dict1, dict2)
#

#
# AUFGABE 6: DATENBANK MIT FUNKTIONEN (SCHWER)
#
# Erstelle eine vollständige Datenbank mit Funktionen für eine Bibliothek.
#
# 1. Erstelle 'bibliothek.py' mit:
#    1.a from typing import Dict, List, Optional, Tuple
#    1.b def buch_hinzufuegen(bibliothek: Dict[str, Dict], titel: str, autor: str, jahr: int) -> Dict:
#         Fügt ein Buch zur Bibliothek hinzu
#         Struktur: { "titel": {"autor": "Name", "jahr": 2024} }
#    1.c def buch_loeschen(bibliothek: Dict[str, Dict], titel: str) -> Dict:
#         Löscht ein Buch aus der Bibliothek
#    1.d def buch_suchen(bibliothek: Dict[str, Dict], suchbegriff: str) -> List[Tuple[str, Dict]]:
#         Sucht nach Büchern (Titel oder Autor)
#         Gibt eine Liste von (titel, buch_info) zurück
#    1.e def buecher_nach_jahr(bibliothek: Dict[str, Dict], jahr: int) -> List[str]:
#         Gibt alle Bücher aus einem bestimmten Jahr zurück
#    1.f def zeige_bibliothek(bibliothek: Dict[str, Dict]) -> None:
#         Gibt alle Bücher aus
#    1.g def durchschnittsjahr(bibliothek: Dict[str, Dict]) -> float:
#         Berechnet das durchschnittliche Erscheinungsjahr
#
# 2. In 'main.py' importiere die Funktionen
# 3. Erstelle ein Menü für die Bibliotheksverwaltung
# 4. Verwende Type Hints für alle Funktionen
# 5. TIPP: Für komplexe Typen importiere Dict, List, Tuple, Optional
#
# BEISPIEL:
# bibliothek = {}
# bibliothek = bibliothek.buch_hinzufuegen(bibliothek, "Python 101", "Max", 2023)
# bibliothek = bibliothek.buch_hinzufuegen(bibliothek, "Data Science", "Anna", 2024)
# suchergebnisse = bibliothek.buch_suchen(bibliothek, "Python")
# bibliothek.zeige_bibliothek(bibliothek)
# durchschnitt = bibliothek.durchschnittsjahr(bibliothek)
# print("Durchschnittsjahr:", durchschnitt)
#

#
# ALLGEMEINE TIPS FÜR ALLE AUFGABEN:
#
# - Type Annotations: def funktion(parameter: typ) -> rueckgabetyp:
# - Wichtige Typen: int, float, str, bool, None, List, Dict, Tuple, Optional
# - Optional verwenden: Optional[Dict] oder Union[Dict, None]
# - Module importieren: import modulname oder from modul import funktion
# - Module müssen im gleichen Ordner oder im PYTHONPATH sein
# - Verwende from typing import List, Dict, Optional, Union, Tuple
# - Module werden mit def und Code in einer .py-Datei erstellt
# - Die Hauptdatei (main.py) importiert und verwendet die Funktionen
# - Bei "from module import *" importiert man alles (nicht empfohlen)
# - Spezifische Importe sind besser: from module import funktion1, funktion2
#
# DOKUMENTATION:
# - Type Hints: https://docs.python.org/3/library/typing.html
# - Module: https://docs.python.org/3/tutorial/modules.html
# - Import: https://docs.python.org/3/reference/import.html