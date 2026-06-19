#==================================THEMA: DICTIONARIES==================================
#
# AUFGABE 1: TELEFONBUCH (SEHR EINFACH)
#
# Erstelle ein Wörterbuch, das Namen als Schlüssel und Telefonnummern als Wert speichert.
#
# 0. Leeres Wörterbuch anlegen: phonebook = {}
# 1. Der Benutzer gibt 3 Namen und Telefonnummern ein (OHNE Schleife)
# 2. Jeder Eintrag wird im Wörterbuch gespeichert
# 3. Gib das gesamte Telefonbuch aus
# 4. Frage den Benutzer nach einem Namen und gib die dazugehörige Nummer aus
#
# BEISPIEL:
# Eingabe: Name = "Anna", Nummer = "0123456789"
# Eingabe: Name = "Ben", Nummer = "9876543210"
# Eingabe: Name = "Clara", Nummer = "5551234567"
# Ausgabe: Telefonbuch: {'Anna': '0123456789', 'Ben': '9876543210', 'Clara': '5551234567'}
# Suche: "Anna" -> Anna hat die Nummer 0123456789
#

#
# AUFGABE 2: NOTENSPEICHER (SEHR EINFACH)
#
# Erstelle ein Wörterbuch, das Fächer als Schlüssel und Noten als Wert speichert.
#
# 0. Leeres Wörterbuch anlegen: grades = {}
# 1. Der Benutzer gibt 3 Fächer und Noten ein (OHNE Schleife)
# 2. Die Note wird als float gespeichert (TIPP: float() für Umwandlung)
# 3. Gib alle Fächer und Noten aus
# 4. Berechne den Notendurchschnitt (TIPP: sum() und len())
#
# BEISPIEL:
# Eingabe: Fach = "Mathe", Note = 2.0
# Eingabe: Fach = "Deutsch", Note = 1.5
# Eingabe: Fach = "Englisch", Note = 2.5
# Ausgabe: Mathe: 2.0, Deutsch: 1.5, Englisch: 2.5
# Durchschnitt: 2.0
#

#
# AUFGABE 3: LÄNDER-HAUPTSTÄDTE (SEHR EINFACH)
#
# Erstelle ein Wörterbuch mit vordefinierten Ländern und Hauptstädten.
# Der Benutzer soll nach einem Land fragen und die Hauptstadt angezeigt bekommen.
#
# 0. Wörterbuch mit 3 Ländern erstellen: countries = {"Deutschland": "Berlin", "Frankreich": "Paris", "Italien": "Rom"}
# 1. Gib dem Benutzer die Auswahl: Zeige alle Länder an
# 2. Der Benutzer gibt ein Land ein
# 3. Wenn das Land existiert, gib die Hauptstadt aus
# 4. Wenn das Land nicht existiert, gib "Land nicht gefunden" aus
#
# BEISPIEL:
# Länder: Deutschland, Frankreich, Italien
# Eingabe: "Deutschland" -> Die Hauptstadt von Deutschland ist Berlin
# Eingabe: "Spanien" -> Spanien nicht gefunden
#

#
# AUFGABE 4: WÖRTERBUCH ERWEITERN (SEHR EINFACH)
#
# Starte mit einem leeren Wörterbuch und füge nach und nach Einträge hinzu.
#
# 0. Leeres Wörterbuch anlegen: my_dict = {}
# 1. Füge 3 Schlüssel-Wert-Paare hinzu (ohne Benutzereingabe, direkt im Code)
#    TIPP: my_dict["key1"] = "value1"
# 2. Ändere den Wert von einem Schlüssel
#    TIPP: my_dict["key1"] = "neuer_wert"
# 3. Lösche einen Schlüssel mit del
#    TIPP: del my_dict["key2"]
# 4. Gib das fertige Wörterbuch aus
#
# BEISPIEL:
# Start: {}
# Nach Hinzufügen: {"name": "Anna", "alter": 25, "stadt": "Berlin"}
# Nach Ändern: {"name": "Anna", "alter": 26, "stadt": "Berlin"}
# Nach Löschen: {"name": "Anna", "stadt": "Berlin"}
#

#
# AUFGABE 5: EINKAUFSZETTEL (EINFACH MIT SCHLEIFE)
#
# Erstelle ein Wörterbuch für einen Einkaufszettel. Der Benutzer kann Produkte und Mengen eingeben.
#
# 0. Leeres Wörterbuch: shopping_list = {}
# 1. Schleife für die Eingabe (3 Durchgänge)
# 2. Pro Durchgang: Produktname und Menge eingeben
# 3. Speichere im Wörterbuch: shopping_list[produkt] = menge
# 4. Nach der Schleife: Gib den gesamten Einkaufszettel aus
# 5. Frage den Benutzer, ob er ein Produkt löschen möchte (ja/nein)
# 6. Wenn ja: Produktname eingeben und aus Wörterbuch löschen
#
# BEISPIEL:
# 1. Produkt: "Äpfel", Menge: 3
# 2. Produkt: "Milch", Menge: 1
# 3. Produkt: "Brot", Menge: 2
# Einkaufszettel: Äpfel: 3, Milch: 1, Brot: 2
# Löschen? ja
# Welches Produkt? "Milch"
# Neuer Einkaufszettel: Äpfel: 3, Brot: 2
#

#
# ALLGEMEINE TIPS FÜR ALLE AUFGABEN:
#
# - Wörterbücher werden mit {} erstellt
# - Auf Werte zugreifen: dictionary[key]
# - Werte setzen: dictionary[key] = value
# - Auf Existenz prüfen: if key in dictionary:
# - Löschen: del dictionary[key] oder dictionary.pop(key)
# - Alle Schlüssel: dictionary.keys()
# - Alle Werte: dictionary.values()
# - Alle Paare: dictionary.items()
# - Bei Eingaben mit input() immer den richtigen Datentyp verwenden (int, float, str)



#==================================THEMA: FUNKTIONEN==================================
#
# AUFGABE 1: BEGRÜSSUNGS-FUNKTION (SEHR EINFACH)
#
# Schreibe eine Funktion, die einen Namen als Parameter nimmt und eine Begrüßung ausgibt.
#
# 0. Definiere die Funktion: def gruesse(name):
# 1. Die Funktion gibt "Hallo [name]!" aus
# 2. Rufe die Funktion mit 3 verschiedenen Namen auf (OHNE Schleife)
#
# BEISPIEL:
# gruesse("Anna") -> Hallo Anna!
# gruesse("Ben") -> Hallo Ben!
# gruesse("Clara") -> Hallo Clara!
#

#
# AUFGABE 2: SUMME BEREICHNEN (SEHR EINFACH)
#
# Schreibe eine Funktion, die zwei Zahlen als Parameter nimmt und deren Summe zurückgibt.
#
# 0. Definiere die Funktion: def summe(zahl1, zahl2):
# 1. Die Funktion berechnet die Summe und gibt sie mit return zurück
# 2. Rufe die Funktion mit 3 verschiedenen Zahlenpaaren auf
# 3. Gib die Ergebnisse aus
#
# BEISPIEL:
# summe(5, 3) -> 8
# summe(10, 7) -> 17
# summe(2.5, 4.5) -> 7.0
#

#
# AUFGABE 3: QUADRAT-FUNKTION (SEHR EINFACH)
#
# Schreibe eine Funktion, die eine Zahl als Parameter nimmt und das Quadrat zurückgibt.
#
# 0. Definiere die Funktion: def quadrat(zahl):
# 1. Die Funktion berechnet zahl * zahl und gibt es mit return zurück
# 2. Der Benutzer gibt eine Zahl ein (input)
# 3. Rufe die Funktion mit der eingegebenen Zahl auf
# 4. Gib das Ergebnis aus
#
# BEISPIEL:
# Eingabe: 5 -> Das Quadrat von 5 ist 25
# Eingabe: 3 -> Das Quadrat von 3 ist 9
#

#
# AUFGABE 4: GERADE ODER UNGERADE (EINFACH)
#
# Schreibe eine Funktion, die prüft, ob eine Zahl gerade oder ungerade ist.
#
# 0. Definiere die Funktion: def ist_gerade(zahl):
# 1. Die Funktion gibt True zurück, wenn die Zahl gerade ist, sonst False
#    TIPP: Verwende den Modulo-Operator % (zahl % 2 == 0)
# 2. Der Benutzer gibt eine Zahl ein (input)
# 3. Rufe die Funktion mit der eingegebenen Zahl auf
# 4. Gib aus: "Die Zahl ist gerade" oder "Die Zahl ist ungerade"
#
# BEISPIEL:
# Eingabe: 4 -> Die Zahl 4 ist gerade
# Eingabe: 7 -> Die Zahl 7 ist ungerade
#

#
# AUFGABE 5: MEHRERE FUNKTIONEN (EINFACH)
#
# Schreibe 3 Funktionen für einen einfachen Taschenrechner.
#
# 0. Definiere die Funktionen:
#    0.a def addieren(a, b): gibt a + b zurück
#    0.b def subtrahieren(a, b): gibt a - b zurück
#    0.c def multiplizieren(a, b): gibt a * b zurück
# 1. Der Benutzer gibt 2 Zahlen und eine Operation ein (+, -, *)
# 2. Rufe die passende Funktion auf
# 3. Gib das Ergebnis aus
#
# BEISPIEL:
# Erste Zahl: 10
# Zweite Zahl: 5
# Operation: + -> 10 + 5 = 15
# Operation: - -> 10 - 5 = 5
# Operation: * -> 10 * 5 = 50
#

#
# AUFGABE 6: STANDARDWERTE (EINFACH)
#
# Schreibe eine Funktion mit Standardwerten für Parameter.
#
# 0. Definiere die Funktion: def begruessung(name, anrede="Hallo"):
# 1. Die Funktion gibt "[anrede] [name]!" aus
# 2. Rufe die Funktion auf:
#    2.a Mit nur einem Parameter (name) -> Standardwert "Hallo" wird verwendet
#    2.b Mit zwei Parametern (name, anrede) -> Eigener Wert wird verwendet
#
# BEISPIEL:
# begruessung("Anna") -> Hallo Anna!
# begruessung("Ben", "Guten Morgen") -> Guten Morgen Ben!
#

#
# AUFGABE 7: LISTE DURCHGEHEN (MITTEL)
#
# Schreibe eine Funktion, die eine Liste von Zahlen als Parameter nimmt
# und den Durchschnitt berechnet.
#
# 0. Definiere die Funktion: def durchschnitt(zahlen_liste):
# 1. Die Funktion berechnet den Durchschnitt mit sum() und len()
# 2. Die Funktion gibt den Durchschnitt zurück
# 3. Erstelle eine Liste mit 5 Zahlen (OHNE Benutzereingabe)
# 4. Rufe die Funktion mit der Liste auf
# 5. Gib den Durchschnitt aus
#
# BEISPIEL:
# Liste: [4, 5, 6, 7, 8] -> Durchschnitt: 6.0
# Liste: [10, 20, 30, 40, 50] -> Durchschnitt: 30.0
#

#
# AUFGABE 8: MEHRERE RÜCKGABEWERTE (MITTEL)
#
# Schreibe eine Funktion, die mehrere Werte zurückgibt.
#
# 0. Definiere die Funktion: def min_max(zahlen_liste):
# 1. Die Funktion berechnet das Minimum und Maximum der Liste
#    TIPP: min() und max() Funktionen verwenden
# 2. Die Funktion gibt beide Werte zurück (TIPP: return min_wert, max_wert)
# 3. Erstelle eine Liste mit beliebigen Zahlen
# 4. Rufe die Funktion auf und speichere beide Rückgabewerte
# 5. Gib Minimum und Maximum aus
#
# BEISPIEL:
# Liste: [5, 2, 8, 1, 9] -> Minimum: 1, Maximum: 9
# Liste: [3.5, 2.1, 7.8, 4.2] -> Minimum: 2.1, Maximum: 7.8
#

#
# AUFGABE 9: FUNKTION MIT SCHLEIFE (MITTEL)
#
# Schreibe eine Funktion, die eine Liste von Namen bekommt
# und jeden Namen mit einer Begrüßung ausgibt.
#
# 0. Definiere die Funktion: def begruesse_alle(namen_liste):
# 1. Die Funktion geht mit einer for-Schleife durch die Liste
# 2. Für jeden Namen wird "Hallo [name]!" ausgegeben
# 3. Erstelle eine Liste mit 5 Namen (OHNE Benutzereingabe)
# 4. Rufe die Funktion mit der Liste auf
#
# BEISPIEL:
# Liste: ["Anna", "Ben", "Clara", "David", "Emma"]
# Ausgabe:
# Hallo Anna!
# Hallo Ben!
# Hallo Clara!
# Hallo David!
# Hallo Emma!
#

#
# AUFGABE 10: FUNKTIONEN ZUSAMMENSETZEN (SCHWER)
#
# Schreibe mehrere kleine Funktionen, die zusammen ein Programm ergeben.
#
# 0. Definiere die Funktionen:
#    0.a def eingabe_zahl(prompt): gibt input als float zurück
#    0.b def berechne_flaeche(breite, hoehe): gibt breite * hoehe zurück
#    0.c def ausgabe(flaeche): gibt "Die Fläche ist: [flaeche]" aus
# 1. Rufe die Funktionen in der richtigen Reihenfolge auf:
#    1.a Breite mit eingabe_zahl() einlesen
#    1.b Höhe mit eingabe_zahl() einlesen
#    1.c Fläche mit berechne_flaeche() berechnen
#    1.d Ergebnis mit ausgabe() anzeigen
#
# BEISPIEL:
# Breite: 5
# Höhe: 3
# Die Fläche ist: 15.0
#

#
# ALLGEMEINE TIPS FÜR ALLE AUFGABEN:
#
# - Funktionen werden mit def definiert: def funktionsname(parameter):
# - Der Code einer Funktion wird eingerückt
# - Mit return gibt eine Funktion einen Wert zurück
# - Ohne return gibt die Funktion None zurück
# - Funktionen werden mit funktionsname(argument) aufgerufen
# - Parameter können Standardwerte haben: def name(parameter="wert"):
# - Mehrere Rückgabewerte: return wert1, wert2
# - Die Dokumentation findest du unter:
#   https://www.w3schools.com/python/python_functions.asp




#==================================THEMA: MODULARISIEREN &TYPE ANNOTATIONS==================================
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




#===============================================================================================================================================================
# AUFGABE: PASSWORTGENERATOR MIT BENUTZERVERWALTUNG
#
# Eine umfassende Aufgabe, die alle bisherigen Konzepte vereint:
# - Variablen und Datentypen
# - Eingaben und Ausgaben
# - Listen und Wörterbücher
# - Funktionen (mit Type Annotations)
# - Bedingungen (if/elif/else)
# - Schleifen (for/while)
# - Modularisierung (Aufteilung in verschiedene Dateien)
#
# ZIEL: Ein Programm zur Benutzerverwaltung mit automatischem Passwortgenerator
#

# ==================================================================================
# MODUL 1: PASSWORTGENERATOR (passwort_generator.py)
# ==================================================================================

#
# Erstelle Funktionen für die Passwortgenerierung.
#
# WICHTIGE IMPORTS:
# - import random
# - import string
#

def generiere_passwort(laenge: int = 8) -> str:
    """
    Generiert ein einfaches Passwort mit Kleinbuchstaben und Zahlen.
    
    Args:
        laenge: Länge des Passworts (Standard: 8)
    
    Returns:
        Das generierte Passwort als String
    
    Vorgehensweise:
    1. Erstelle einen String mit allen möglichen Zeichen:
       zeichen = string.ascii_lowercase + string.digits
    2. Generiere das Passwort mit random.choice(zeichen) in einer Schleife
    3. TIPP: Verwende eine Liste und ''.join() für bessere Performance
    4. Gib das Passwort zurück
    
    BEISPIEL:
    >>> generiere_passwort()
    'a7k3m9x2'
    >>> generiere_passwort(12)
    'b4n8q2w5e1r6'
    """

def bewertung_passwort_staerke(passwort: str) -> str:
    """
    Bewertet die Stärke eines Passworts.
    
    Args:
        passwort: Das zu bewertende Passwort
    
    Returns:
        "Schwach", "Mittel" oder "Stark"
    
    Vorgehensweise:
    1. Prüfe die Länge des Passworts
    2. Prüfe auf Großbuchstaben (any(c.isupper() for c in passwort))
    3. Prüfe auf Zahlen (any(c.isdigit() for c in passwort))
    4. Prüfe auf Sonderzeichen (any(c in string.punctuation for c in passwort))
    5. Punkte verteilen:
       - Länge >= 12: +2 Punkte, >= 8: +1 Punkt
       - Großbuchstaben: +1 Punkt
       - Zahlen: +1 Punkt
       - Sonderzeichen: +1 Punkt
    6. Bewertung:
       - 0-2 Punkte: "Schwach"
       - 3-4 Punkte: "Mittel"
       - 5+ Punkte: "Stark"
    7. Gib die Bewertung zurück
    
    BEISPIEL:
    >>> bewertung_passwort_staerke("abc123")
    'Mittel'
    >>> bewertung_passwort_staerke("Abc123!@#")
    'Stark'
    """


# ==================================================================================
# MODUL 2: BENUTZERVERWALTUNG (benutzer_verwaltung.py)
# ==================================================================================

#
# Erstelle Funktionen für die Benutzerverwaltung.
#
# WICHTIGE IMPORTS:
# - from datetime import datetime
#

def benutzer_erstellen(name: str, passwort: str) -> dict:
    """
    Erstellt einen neuen Benutzer als Dictionary.
    
    Args:
        name: Der Benutzername
        passwort: Das Passwort
    
    Returns:
        Dictionary mit Benutzerdaten:
        {
            "name": name,
            "passwort": passwort,
            "erstellt_am": aktuelles Datum,
            "passwort_staerke": Bewertung des Passworts
        }
    
    Vorgehensweise:
    1. Erstelle ein leeres Dictionary: benutzer = {}
    2. Füge "name": name hinzu
    3. Füge "passwort": passwort hinzu
    4. Füge "erstellt_am": datetime.now().strftime("%Y-%m-%d %H:%M:%S") hinzu
    5. Rufe bewertung_passwort_staerke(passwort) auf
    6. Füge "passwort_staerke": ergebnis hinzu
    7. Gib das Dictionary zurück
    
    BEISPIEL:
    >>> benutzer_erstellen("Anna", "abc123")
    {'name': 'Anna', 'passwort': 'abc123', 'erstellt_am': '2024-01-15 10:30:00', 'passwort_staerke': 'Mittel'}
    """

def benutzer_hinzufuegen(datenbank: list, benutzer: dict) -> list:
    """
    Fügt einen Benutzer zur Datenbank hinzu, wenn der Name noch nicht existiert.
    
    Args:
        datenbank: Liste aller Benutzer (jeder Benutzer ist ein Dictionary)
        benutzer: Der neue Benutzer (Dictionary)
    
    Returns:
        Aktualisierte Datenbank
    
    Vorgehensweise:
    1. Extrahiere den Namen des neuen Benutzers: name = benutzer["name"]
    2. Durchsuche die Datenbank, ob der Name bereits existiert
    3. TIPP: Verwende eine for-Schleife über datenbank
    4. Wenn Name existiert: Gib eine Fehlermeldung aus und gib datenbank zurück
    5. Wenn Name nicht existiert: Füge benutzer mit datenbank.append(benutzer) hinzu
    6. Gib die aktualisierte Datenbank zurück
    
    BEISPIEL:
    >>> db = []
    >>> neuer_user = {"name": "Anna", "passwort": "abc123"}
    >>> benutzer_hinzufuegen(db, neuer_user)
    [{"name": "Anna", "passwort": "abc123"}]
    """

def benutzer_suchen(datenbank: list, name: str):
    """
    Sucht einen Benutzer nach Namen.
    
    Args:
        datenbank: Liste aller Benutzer
        name: Der gesuchte Benutzername
    
    Returns:
        Den gefundenen Benutzer (Dictionary) oder None
    
    Vorgehensweise:
    1. Durchsuche die Datenbank mit einer for-Schleife
    2. Für jeden Benutzer: Überprüfe benutzer["name"] == name
    3. Wenn gefunden: Gib den Benutzer zurück
    4. Wenn nicht gefunden: Gib None zurück
    
    BEISPIEL:
    >>> db = [{"name": "Anna", "passwort": "abc123"}]
    >>> benutzer_suchen(db, "Anna")
    {"name": "Anna", "passwort": "abc123"}
    >>> benutzer_suchen(db, "Ben")
    None
    """

def benutzer_loeschen(datenbank: list, name: str) -> list:
    """
    Löscht einen Benutzer aus der Datenbank.
    
    Args:
        datenbank: Liste aller Benutzer
        name: Der zu löschende Benutzername
    
    Returns:
        Aktualisierte Datenbank
    
    Vorgehensweise:
    1. Finde den Benutzer mit benutzer_suchen(datenbank, name)
    2. Wenn None: Gib Fehlermeldung aus, gib datenbank zurück
    3. Wenn gefunden: Lösche den Benutzer mit datenbank.remove(gefundener_benutzer)
    4. Gib die aktualisierte Datenbank zurück
    
    BEISPIEL:
    >>> db = [{"name": "Anna", "passwort": "abc123"}]
    >>> benutzer_loeschen(db, "Anna")
    []
    """

def benutzer_aktualisieren(datenbank: list, name: str, neues_passwort: str) -> list:
    """
    Aktualisiert das Passwort eines Benutzers.
    
    Args:
        datenbank: Liste aller Benutzer
        name: Der Benutzername
        neues_passwort: Das neue Passwort
    
    Returns:
        Aktualisierte Datenbank
    
    Vorgehensweise:
    1. Finde den Benutzer mit benutzer_suchen(datenbank, name)
    2. Wenn None: Gib Fehlermeldung aus, gib datenbank zurück
    3. Wenn gefunden: Aktualisiere "passwort" mit neues_passwort
    4. Rufe bewertung_passwort_staerke(neues_passwort) auf
    5. Aktualisiere "passwort_staerke" mit dem Ergebnis
    6. Gib die aktualisierte Datenbank zurück
    """

def benutzer_ausgabe(benutzer: dict) -> str:
    """
    Formatiert einen Benutzer für die Ausgabe.
    
    Args:
        benutzer: Der Benutzer als Dictionary
    
    Returns:
        Formatierter String für die Ausgabe
    
    Vorgehensweise:
    1. Erstelle einen String mit allen Benutzerdaten
    2. TIPP: Verwende f-Strings für die Formatierung
    3. Gib den String zurück
    
    BEISPIEL:
    >>> user = {"name": "Anna", "passwort": "abc123", "erstellt_am": "2024-01-15", "passwort_staerke": "Mittel"}
    >>> benutzer_ausgabe(user)
    'Name: Anna | Passwort: abc123 | Erstellt: 2024-01-15 | Stärke: Mittel'
    """

def alle_benutzer_ausgeben(datenbank: list) -> None:
    """
    Gibt alle Benutzer aus der Datenbank aus.
    
    Args:
        datenbank: Liste aller Benutzer
    
    Vorgehensweise:
    1. Überprüfe, ob die Datenbank leer ist (len(datenbank) == 0)
    2. Wenn leer: Gib "Keine Benutzer gefunden" aus
    3. Wenn nicht leer: Gib jeden Benutzer mit benutzer_ausgabe() aus
    4. Gib eine Trennlinie zwischen den Benutzern aus
    """


# ==================================================================================
# MODUL 3: HILFSFUNKTIONEN (hilfe.py)
# ==================================================================================

#
# Erstelle Hilfsfunktionen für Eingaben und Ausgaben.
#

def eingabe_text(prompt: str) -> str:
    """
    Liest einen Text vom Benutzer ein.
    
    Args:
        prompt: Der Eingabe-Prompt (was angezeigt wird)
    
    Returns:
        Der eingegebene Text
    
    Vorgehensweise:
    1. Frage mit input(prompt) ab
    2. Gib den Text zurück
    
    BEISPIEL:
    >>> name = eingabe_text("Benutzername: ")
    Benutzername: Anna
    >>> name
    'Anna'
    """

def eingabe_zahl(prompt: str) -> float:
    """
    Liest eine Zahl vom Benutzer ein.
    
    Args:
        prompt: Der Eingabe-Prompt
    
    Returns:
        Die eingegebene Zahl als float
    
    Vorgehensweise:
    1. Frage mit input(prompt) ab
    2. Wandle die Eingabe in float um
    3. Gib die Zahl zurück
    
    BEISPIEL:
    >>> zahl = eingabe_zahl("Passwortlänge: ")
    Passwortlänge: 12
    >>> zahl
    12.0
    """

def eingabe_ja_nein(prompt: str) -> bool:
    """
    Fragt den Benutzer nach einer Bestätigung (ja/nein).
    
    Args:
        prompt: Der Eingabe-Prompt
    
    Returns:
        True bei "ja", False bei "nein"
    
    Vorgehensweise:
    1. Frage mit input(prompt + " (j/n): ") ab
    2. Verwende .lower() für die Eingabe
    3. Wenn Eingabe "ja" oder "j" ist: Gib True zurück
    4. Wenn Eingabe "nein" oder "n" ist: Gib False zurück
    5. Sonst: Wiederhole die Frage
    
    BEISPIEL:
    >>> bestaetigung = eingabe_ja_nein("Möchten Sie fortfahren?")
    Möchten Sie fortfahren? (j/n): j
    >>> bestaetigung
    True
    """

def zeige_menu() -> None:
    """
    Zeigt das Hauptmenü an.
    
    Vorgehensweise:
    1. Zeige einen Titel mit Trennlinien
    2. Zeige alle Menüoptionen mit Beschreibung
    3. Zeige eine Trennlinie am Ende
    
    BEISPIEL:
    ==================================
       PASSWORTGENERATOR & USERVERWALTUNG
    ==================================
    [1] Neuen Benutzer erstellen
    [2] Alle Benutzer anzeigen
    [3] Benutzer suchen
    [4] Benutzer löschen
    [5] Passwort ändern
    [6] Programm beenden
    ==================================
    """


# ==================================================================================
# MODUL 4: HAUPTPROGRAMM (main.py)
# ==================================================================================

#
# Erstelle das Hauptprogramm, das alle Module verwendet.
#
# WICHTIGE IMPORTS:
# - import passwort_generator as pg
# - import benutzer_verwaltung as bv
# - import hilfe as hf
#

def hauptprogramm() -> None:
    """
    Das Hauptprogramm mit dem Menü.
    
    Vorgehensweise:
    
    1. DATENBANK INITIALISIEREN:
       - Erstelle eine leere Liste: datenbank = []
    
    2. HAUPTSCHEIFE:
       - Starte eine while True-Schleife
       - Rufe hf.zeige_menu() auf
       - Frage mit input() nach der Option
       - Führe die gewählte Aktion aus
    
    3. OPTION 1: NEUEN BENUTZER ERSTELLEN
       - Frage nach dem Benutzernamen mit hf.eingabe_text()
       - Frage nach der Passwortlänge mit hf.eingabe_zahl()
       - Rufe pg.generiere_passwort(laenge) auf
       - Zeige das generierte Passwort an
       - Rufe pg.bewertung_passwort_staerke(passwort) auf
       - Zeige die Passwort-Stärke an
       - Erstelle den Benutzer mit bv.benutzer_erstellen(name, passwort)
       - Füge den Benutzer mit bv.benutzer_hinzufuegen(datenbank, benutzer) hinzu
       - Gib eine Bestätigung aus
    
    4. OPTION 2: ALLE BENUTZER ANZEIGEN
       - Rufe bv.alle_benutzer_ausgeben(datenbank) auf
    
    5. OPTION 3: BENUTZER SUCHEN
       - Frage nach dem Benutzernamen mit hf.eingabe_text()
       - Rufe bv.benutzer_suchen(datenbank, name) auf
       - Wenn gefunden: Zeige den Benutzer mit bv.benutzer_ausgabe()
       - Wenn nicht: Gib "Benutzer nicht gefunden" aus
    
    6. OPTION 4: BENUTZER LÖSCHEN
       - Frage nach dem Benutzernamen mit hf.eingabe_text()
       - Bestätigung mit hf.eingabe_ja_nein()
       - Wenn bestätigt: Rufe bv.benutzer_loeschen(datenbank, name) auf
       - Gib Erfolgs- oder Fehlermeldung aus
    
    7. OPTION 5: PASSWORT ÄNDERN
       - Frage nach dem Benutzernamen mit hf.eingabe_text()
       - Überprüfe mit bv.benutzer_suchen(), ob der Benutzer existiert
       - Wenn nicht: Gib Fehlermeldung aus
       - Wenn ja: Frage nach neuer Passwortlänge
       - Generiere neues Passwort mit pg.generiere_passwort()
       - Rufe bv.benutzer_aktualisieren(datenbank, name, neues_passwort) auf
       - Gib Bestätigung aus
    
    8. OPTION 6: PROGRAMM BEENDEN
       - Gib "Programm beendet" aus
       - Beende die Schleife mit break
    
    9. UNGÜLTIGE EINGABE:
       - Bei Wahl einer nicht existierenden Option: Gib Fehlermeldung aus
    """

if __name__ == "__main__":
    hauptprogramm()


# ==================================================================================
# BEISPIELE FÜR DIE AUSGABE
# ==================================================================================

#
# Beispiel 1: Neuen Benutzer erstellen
#
# ==================================
#    PASSWORTGENERATOR & USERVERWALTUNG
# ==================================
# [1] Neuen Benutzer erstellen
# [2] Alle Benutzer anzeigen
# [3] Benutzer suchen
# [4] Benutzer löschen
# [5] Passwort ändern
# [6] Programm beenden
# ==================================
# Ihre Wahl: 1
# 
# Benutzername: Anna
# Passwortlänge: 10
# Generiertes Passwort: a7k3m9x2b4
# Passwort-Stärke: Mittel
# Benutzer 'Anna' wurde erfolgreich erstellt!
#
# Beispiel 2: Alle Benutzer anzeigen
#
# Ihre Wahl: 2
# 
# Alle Benutzer:
# Name: Anna | Passwort: a7k3m9x2b4 | Erstellt: 2024-01-15 10:30:00 | Stärke: Mittel
# --------------------------------------------------
# Name: Ben | Passwort: c5n8q2w5e1 | Erstellt: 2024-01-15 10:35:00 | Stärke: Stark
# --------------------------------------------------
#
# Beispiel 3: Benutzer suchen
#
# Ihre Wahl: 3
# 
# Benutzername: Anna
# Name: Anna | Passwort: a7k3m9x2b4 | Erstellt: 2024-01-15 10:30:00 | Stärke: Mittel
#
# Beispiel 4: Benutzer löschen
#
# Ihre Wahl: 4
# 
# Benutzername: Anna
# Möchten Sie Anna wirklich löschen? (j/n): j
# Benutzer 'Anna' wurde gelöscht.
#
# Beispiel 5: Passwort ändern
#
# Ihre Wahl: 5
# 
# Benutzername: Ben
# Neue Passwortlänge: 12
# Neues Passwort: x7p3m9q2w5e1
# Passwort-Stärke: Stark
# Passwort für 'Ben' wurde aktualisiert.
#

# ==================================================================================
# TIPS FÜR DIE UMSETZUNG
# ==================================================================================

#
# 1. MODUL-STRUKTUR (Dateien die erstellt werden müssen):
#    - passwort_generator.py (enthält generiere_passwort, bewertung_passwort_staerke)
#    - benutzer_verwaltung.py (enthält alle benutzer_* Funktionen)
#    - hilfe.py (enthält eingabe_*, zeige_menu)
#    - main.py (enthält hauptprogramm und verwendet alle anderen Module)
#
# 2. WICHTIGE IMPORTS IN DEN MODULEN:
#    - passwort_generator.py: import random, import string
#    - benutzer_verwaltung.py: from datetime import datetime
#    - hilfe.py: keine speziellen imports nötig
#    - main.py: import passwort_generator as pg, import benutzer_verwaltung as bv, import hilfe as hf
#
# 3. TYPE ANNOTATIONS (verwende sie überall):
#    - str, int, float, bool, list, dict, None
#    - def funktion(parameter: typ) -> rueckgabetyp:
#
# 4. FUNKTIONEN NACHBAUEN:
#    - Verwende die Beispiele und Beschreibungen
#    - Teste jede Funktion einzeln, bevor du sie in main.py einbaust
#    - Verwende print() für Debugging
#
# 5. DOKUMENTATION (nützliche Links):
#    - W3Schools Python: https://www.w3schools.com/python/
#    - Python Docs: https://docs.python.org/3/
#    - Random: https://docs.python.org/3/library/random.html
#    - String: https://docs.python.org/3/library/string.html
#    - Datetime: https://docs.python.org/3/library/datetime.html
#    - F-Strings: https://docs.python.org/3/tutorial/inputoutput.html#f-strings
#
# VIEL ERFOLG BEI DER UMSETZUNG!
# ==================================================================================




