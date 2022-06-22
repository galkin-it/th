import os
import math
import numpy as np
from matplotlib import pyplot as plt # pip install matplotlib
import pandas as pd # pip install pandas

# KONSTANTE für das ganze Program
# Aus der CSV Datei kopiert
spaltennamen = ["Data", "Stato", 
  "V L1-N (V)", "V L2-N (V)", "V L3-N (V)", 
  "A-L1 (A)", "A-L2 (A)", "A-L3 (A)", 
  "W tot (W)", 
  "VA L1 (VA)", "VA L2 (VA)", "VA L3 (VA)", 
  "VA tot (VA)", 
  "VAR L1 (VAR)", "VAR L2 (VAR)", "VAR L3 (VAR)", 
  "VAR tot (VAR)",
  "Energy (kWh)"]

datumliste = None

def main():
    dateiname = "CSV_File.csv"
    # CSV datei lesen und inhalt speichern
    inhalt = pd.read_csv(dateiname, names=spaltennamen, sep=";", skiprows=[0])
    global datumliste 
    datumliste = inhalt['Data']
    inhalt['Data'] = inhalt['Data'].apply(lambda x: str(x.replace("/", "-").replace(".", ":"))).astype(str)
    inhalt.set_index('Data', inplace=True)
    # Aufgabe 1: Inhalt bereitstellen
    print(inhalt)
    # Aufgabe 2: Mathematische Statistik machen
    mathematische_statistik(inhalt)
    # Aufgabe 3: Zeitreihenplot
    plotten(inhalt)


def berechne_std_abweichung(liste, mittelwert):
    nenner = 0
    for value in liste:
        str_value = str(value)
        if "," in str_value:
            wert = float(str_value.replace(",", "."))
        else:
            wert = float(str_value)

        nenner = nenner + (wert - mittelwert)**2
    
    varianz = nenner / ( liste.size - 1)
    return math.sqrt(varianz)

def berechne(liste, name):
    maximum = 0
    minimum = 1000000
    summe = 0
    std_abweichung = 0
    anzahl = liste.size

    for value in liste:
        str_value = str(value)
        if "," in str_value:
            wert = float(str_value.replace(",", "."))
        else:
            wert = float(str_value)

        summe = summe + wert
        if maximum < wert:
            maximum = wert
        if minimum > wert:
            minimum = wert

    mittelwert = summe / anzahl
    std_abweichung = berechne_std_abweichung(liste, mittelwert)

    print(name + " Minimum:       " + str(minimum))
    print(name + " Maximum:       " + str(maximum))
    print(name + " Mittelwert:    " + str(mittelwert))
    print(name + " Stdabweichung: " + str(std_abweichung))
    print("----------------------")

def mathematische_statistik(inhalt):
    for x in range(2, 17):
        berechne(inhalt[spaltennamen[x]], spaltennamen[x])

def plotten(inhalt):
    for x in range(2, 17):
        plot_ts(inhalt[spaltennamen[x]], spaltennamen[x])

def plot_ts(spaltewerte, name):    
    xachse = np.array(zeit_array())
    yachse = np.array(spalten_array(spaltewerte))
    plt.scatter(xachse, yachse)
    plt.title(name)
    plt.xlabel('Sekunden')    
    plt.show()

def spalten_array(spaltewerte):
    werte = []
    for value in spaltewerte:
        str_value = str(value)
        if "," in str_value:
            wert = float(str_value.replace(",", "."))
        else:
            wert = float(str_value)
        werte.append(wert)
    return werte

def zeit_array():
    werte = []
    for value in datumliste:
        datumunduhr = str(value).split()
        uhrzeit = datumunduhr[1].split(".")
        sekunden = 60.0*60.0*float(uhrzeit[0]) + 60.0*float(uhrzeit[1]) + float(uhrzeit[2])
        werte.append(sekunden)
    return werte

if __name__ == "__main__":
    main()
