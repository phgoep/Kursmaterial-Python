#===============================================================================================================================================================
# AUFGABE: PASSWORTGENERATOR MIT BENUTZERVERWALTUNG /MIT FUNKTIONEN)
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







#
# AUFGABE: PASSWORTGENERATOR MIT BENUTZERVERWALTUNG (OHNE FUNKTIONEN)
#
# Eine umfassende Aufgabe, die alle bisherigen Konzepte vereint:
# - Variablen und Datentypen
# - Eingaben und Ausgaben
# - Listen und Wörterbücher
# - Bedingungen (if/elif/else)
# - Schleifen (for/while)
#
# ZIEL: Ein Programm zur Benutzerverwaltung mit automatischem Passwortgenerator
#       OHNE eigene Funktionen zu definieren! Verwende nur die Hauptschleife.
#

# ==================================================================================
# IMPORTE
# ==================================================================================

import random
import string
from datetime import datetime

# ==================================================================================
# PROGRAMMSTART
# ==================================================================================

#
# 1. DATENBANK INITIALISIEREN
#
# Erstelle eine leere Liste namens 'datenbank', die später alle Benutzer speichert.
# Jeder Benutzer wird als Dictionary gespeichert.
#
# TIPP: datenbank = []
#

#
# 2. HAUPTSCHEIFE STARTEN
#
# Starte eine while-Schleife, die solange läuft, bis der Benutzer "6" eingibt.
#
# TIPP: while True:
#

#
# 3. MENÜ ANZEIGEN
#
# Zeige dem Benutzer das Hauptmenü an:
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
#
# TIPP: Verwende print() für die Ausgabe
#

#
# 4. BENUTZEREINGABE FÜR MENÜAUSWAHL
#
# Frage den Benutzer mit input("Ihre Wahl: ") nach seiner Auswahl.
# Speichere die Eingabe in einer Variable (z.B. 'wahl').
#

#
# 5. FALLUNTERSCHEIDUNGEN FÜR DIE MENÜAUSWAHL
#
# Verwende if/elif/else, um die verschiedenen Optionen zu behandeln.
#
# TIPP: if wahl == "1": ... elif wahl == "2": ... elif wahl == "6": break
#

#
# ==================================================================================
# OPTION 1: NEUEN BENUTZER ERSTELLEN
# ==================================================================================

#
# 1.1 BENUTZERNAMEN EINGEBEN
#
# Frage den Benutzer mit input("Benutzername: ") nach dem Namen.
# Speichere den Namen in einer Variable (z.B. 'name').
#

#
# 1.2 PASSWORTLÄNGE EINGEBEN
#
# Frage den Benutzer mit input("Passwortlänge (min. 4): ") nach der Länge.
# Wandle die Eingabe in einen Integer um.
# TIPP: laenge = int(input("Passwortlänge: "))
#

#
# 1.3 PASSWORT GENERIEREN
#
# Erstelle einen String mit allen möglichen Zeichen für das Passwort:
# zeichen = string.ascii_lowercase + string.digits
#
# Generiere das Passwort mit random.choice() in einer Schleife.
# TIPP: Verwende eine for-Schleife mit range(laenge) und baue das Passwort auf.
#
# Beispiel für die Schleife:
# passwort = ""
# for i in range(laenge):
#     passwort = passwort + random.choice(zeichen)
#

#
# 1.4 PASSWORT-STÄRKE BEWERTEN
#
# Bewerte das generierte Passwort:
# - Punkte sammeln für:
#   * Länge >= 8: 1 Punkt, >= 12: 2 Punkte
#   * Enthält Großbuchstaben: 1 Punkt (TIPP: any(c.isupper() for c in passwort))
#   * Enthält Zahlen: 1 Punkt (TIPP: any(c.isdigit() for c in passwort))
#   * Enthält Sonderzeichen: 1 Punkt (TIPP: any(c in string.punctuation for c in passwort))
#
# - Gesamtbewertung:
#   * 0-2 Punkte: "Schwach"
#   * 3-4 Punkte: "Mittel"
#   * 5+ Punkte: "Stark"
#

#
# 1.5 BENUTZER OBJEKT ERSTELLEN
#
# Erstelle ein Dictionary für den neuen Benutzer mit folgenden Schlüsseln:
# - "name": der eingegebene Name
# - "passwort": das generierte Passwort
# - "erstellt_am": aktuelles Datum und Uhrzeit (TIPP: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# - "passwort_staerke": die berechnete Stärke
#

#
# 1.6 BENUTZER ZUR DATENBANK HINZUFÜGEN
#
# Überprüfe zuerst, ob der Benutzername bereits existiert.
# Durchsuche die datenbank mit einer for-Schleife:
# for benutzer in datenbank:
#     if benutzer["name"] == name:
#         print("Benutzername existiert bereits!")
#         break
# else:
#     datenbank.append(neuer_benutzer)
#     print("Benutzer wurde erfolgreich erstellt!")
#

#
# ==================================================================================
# OPTION 2: ALLE BENUTZER ANZEIGEN
# ==================================================================================

#
# 2.1 PRÜFEN, OB DATENBANK LEER IST
#
# Wenn die datenbank leer ist (len(datenbank) == 0), gib "Keine Benutzer gefunden" aus.
#

#
# 2.2 ALLE BENUTZER AUSGEBEN
#
# Durchlaufe die datenbank mit einer for-Schleife und gib jeden Benutzer aus.
# Verwende dafür eine Trennlinie zwischen den Benutzern.
#
# Ausgabeformat:
# Name: Anna | Passwort: abc123 | Erstellt: 2024-01-15 | Stärke: Mittel
# --------------------------------------------------
#

#
# ==================================================================================
# OPTION 3: BENUTZER SUCHEN
# ==================================================================================

#
# 3.1 BENUTZERNAMEN EINGEBEN
#
# Frage den Benutzer mit input("Benutzername: ") nach dem Namen.
#

#
# 3.2 BENUTZER IN DATENBANK SUCHEN
#
# Durchsuche die datenbank mit einer for-Schleife:
# for benutzer in datenbank:
#     if benutzer["name"] == name:
#         print(benutzer)  # Oder besser formatiert
#         break
# else:
#     print("Benutzer nicht gefunden")
#

#
# ==================================================================================
# OPTION 4: BENUTZER LÖSCHEN
# ==================================================================================

#
# 4.1 BENUTZERNAMEN EINGEBEN
#
# Frage den Benutzer mit input("Benutzername: ") nach dem Namen.
#

#
# 4.2 BESTÄTIGUNG ABFRAGEN
#
# Frage den Benutzer: "Möchten Sie diesen Benutzer wirklich löschen? (j/n): "
# Verwende .lower() für die Eingabe.
#

#
# 4.3 BENUTZER LÖSCHEN (WENN BESTÄTIGT)
#
# Durchsuche die datenbank mit einer for-Schleife:
# for benutzer in datenbank:
#     if benutzer["name"] == name:
#         datenbank.remove(benutzer)
#         print("Benutzer wurde gelöscht")
#         break
# else:
#     print("Benutzer nicht gefunden")
#

#
# ==================================================================================
# OPTION 5: PASSWORT ÄNDERN
# ==================================================================================

#
# 5.1 BENUTZERNAMEN EINGEBEN
#
# Frage den Benutzer mit input("Benutzername: ") nach dem Namen.
#

#
# 5.2 BENUTZER IN DATENBANK SUCHEN
#
# Durchsuche die datenbank mit einer for-Schleife, um den Benutzer zu finden.
# Wenn nicht gefunden: Gib eine Fehlermeldung aus.
#

#
# 5.3 NEUE PASSWORTLÄNGE EINGEBEN
#
# Frage den Benutzer mit input("Neue Passwortlänge: ") nach der Länge.
#

#
# 5.4 NEUES PASSWORT GENERIEREN
#
# Verwende den gleichen Code wie bei Option 1, um ein neues Passwort zu generieren.
#

#
# 5.5 PASSWORT-STÄRKE BEWERTEN
#
# Bewerte das neue Passwort mit dem gleichen Code wie bei Option 1.
#

#
# 5.6 PASSWORT AKTUALISIEREN
#
# Aktualisiere das Passwort und die Passwort-Stärke des gefundenen Benutzers.
# TIPP: benutzer["passwort"] = neues_passwort
#       benutzer["passwort_staerke"] = neue_staerke
#

#
# ==================================================================================
# OPTION 6: PROGRAMM BEENDEN
# ==================================================================================

#
# 6.1 ABSCHIEDSNACHRICHT
#
# Gib "Programm beendet. Auf Wiedersehen!" aus.
#

#
# 6.2 SCHLEIFE BEENDEN
#
# Verwende break, um die while-Schleife zu beenden.
#

#
# ==================================================================================
# UNGÜLTIGE EINGABE BEHANDELN
# ==================================================================================

#
# 7.1 ELSE-ZWEIG FÜR UNGÜLTIGE EINGABE
#
# Wenn die Wahl nicht 1-6 ist, gib "Ungültige Auswahl! Bitte wählen Sie 1-6." aus.
#
# TIPP: else: (nach allen elifs)
#

#
# ==================================================================================
# PAUSE AM ENDE JEDER AKTION
# ==================================================================================

#
# 8.1 PAUSE EINFÜGEN
#
# Nach jeder Aktion soll der Benutzer die Möglichkeit haben, die Ausgabe zu lesen.
# Füge am Ende jedes if-Zweigs ein input("Drücken Sie Enter, um fortzufahren...") ein.
#
# TIPP: input("Drücken Sie Enter, um fortzufahren...")
#

#
# ==================================================================================
# BEISPIELE FÜR DIE AUSGABE
# ==================================================================================

#
# BEISPIEL 1: Neuen Benutzer erstellen
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
# Passwortlänge (min. 4): 10
# Generiertes Passwort: a7k3m9x2b4
# Passwort-Stärke: Mittel
# Benutzer 'Anna' wurde erfolgreich erstellt!
# Drücken Sie Enter, um fortzufahren...
#

#
# BEISPIEL 2: Alle Benutzer anzeigen
#
# Ihre Wahl: 2
# 
# Alle Benutzer:
# Name: Anna | Passwort: a7k3m9x2b4 | Erstellt: 2024-01-15 10:30:00 | Stärke: Mittel
# --------------------------------------------------
# Name: Ben | Passwort: c5n8q2w5e1 | Erstellt: 2024-01-15 10:35:00 | Stärke: Stark
# --------------------------------------------------
# Drücken Sie Enter, um fortzufahren...
#

#
# BEISPIEL 3: Benutzer suchen
#
# Ihre Wahl: 3
# 
# Benutzername: Anna
# Name: Anna | Passwort: a7k3m9x2b4 | Erstellt: 2024-01-15 10:30:00 | Stärke: Mittel
# Drücken Sie Enter, um fortzufahren...
#

#
# BEISPIEL 4: Benutzer löschen
#
# Ihre Wahl: 4
# 
# Benutzername: Anna
# Möchten Sie Anna wirklich löschen? (j/n): j
# Benutzer 'Anna' wurde gelöscht.
# Drücken Sie Enter, um fortzufahren...
#

#
# BEISPIEL 5: Passwort ändern
#
# Ihre Wahl: 5
# 
# Benutzername: Ben
# Neue Passwortlänge: 12
# Neues Passwort: x7p3m9q2w5e1
# Passwort-Stärke: Stark
# Passwort für 'Ben' wurde aktualisiert.
# Drücken Sie Enter, um fortzufahren...
#

#
# BEISPIEL 6: Programm beenden
#
# Ihre Wahl: 6
# Programm beendet. Auf Wiedersehen!
#

# ==================================================================================
# TIPS FÜR DIE UMSETZUNG
# ==================================================================================

#
# 1. STRING-METHODEN:
#    - .lower() für Kleinschreibung bei Bestätigungen
#    - any() für die Überprüfung von Zeichen im Passwort
#
# 2. LISTEN-METHODEN:
#    - .append() zum Hinzufügen von Benutzern
#    - .remove() zum Löschen von Benutzern
#
# 3. WÖRTERBUCH-METHODEN:
#    - dict["key"] = wert zum Setzen von Werten
#    - for benutzer in datenbank: zum Durchlaufen der Liste
#
# 4. IMPORTE:
#    - import random (für random.choice)
#    - import string (für string.ascii_lowercase, string.digits, string.punctuation)
#    - from datetime import datetime (für datetime.now())
#
# 5. DOKUMENTATION (nützliche Links):
#    - W3Schools Python: https://www.w3schools.com/python/
#    - Python Docs: https://docs.python.org/3/
#    - Random: https://docs.python.org/3/library/random.html
#    - String: https://docs.python.org/3/library/string.html
#    - Datetime: https://docs.python.org/3/library/datetime.html
#
# VIEL ERFOLG BEI DER UMSETZUNG!
# ==================================================================================