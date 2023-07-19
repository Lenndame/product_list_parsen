"""
Gegegen ist die Datei prodcucts.csv mit drei Feldern
productid,name,date


Lese die Zeilen ein und versuche (try), das Feld date 
in ein Python-Dateobjekt zu parsen (datetime.strptime).
Manche Datefelder sind entweder leer oder kaputt, das Programm darf 
beim Konvertieren aber nicht abbrechen, soll diese Zeilen dann ignorieren.

Das Datum muss um zwei Tage nach vorne versetzt werden, dh. aus dem
18.10.2022 soll der 20.10.2022 werden. Das neue Datum erstetzt das alte Datum
in der Liste im selben Format (datetime, timedelta)

Die veränderte Liste soll dann auf Standard-Out ausgegeben werden, ein
abspeichern als CSV ist nicht nötig (Zusatzaufgabe.)

Kapsel die einzelnen Bereiche in Funktionen, nutze Typehints und 
Docstrings, wo nötig.
"""

import csv
from pathlib import Path
from datetime import datetime, timedelta

FILENAME = "products.csv"
"""
1. datei einlesen
2. (string in dateformat) tage vorstellen
3. speichern

"""

def load_data(filename):
    with open(Path(__file__).parent / filename, mode="r", newline="", encoding= "utf-8") as f:
        data = csv.DictReader(f, delimiter=",")
        result = list(data)
        result = strip_data(result)
    return result


def strip_data(data):
    data_new = []
    for el in data:
        if (len(el["date"]) == 10):
            data_new.append(el)
    return data_new


def convert_data(data: list[dict]):
    for el in data:
        dateobj_from_iso = datetime.strptime(el["date"], "%d/%m/%Y")
        el.update({"date": add_days(dateobj_from_iso)})
    return data


def add_days(data):
    return data + timedelta(days=2)


def save_data(data, filename):
    fieldnames = ("productid", "name", "date")
    with open(Path(__file__).parent / filename, mode="w", newline="", encoding= "utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
        writer.writeheader()
        writer.writerows(data)


save_data(convert_data(load_data(FILENAME)), "products_clear.csv")
