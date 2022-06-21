import os
import math
import numpy as np
import matplotlib
matplotlib.use("MacOSX")
#import matplotlib.pyplot as plt # pip install matplotlib
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

def main():
    dateiname = "CSV_File.csv"
    # CSV datei lesen und inhalt speichern
    inhalt = pd.read_csv(dateiname, names=spaltennamen, sep=";", skiprows=[0])
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
    v_l1 = inhalt[spaltennamen[2]]
    v_l2 = inhalt[spaltennamen[3]]
    v_l3 = inhalt[spaltennamen[4]]
    a_l1 = inhalt[spaltennamen[5]]
    a_l2 = inhalt[spaltennamen[6]]
    a_l3 = inhalt[spaltennamen[7]]
    w_tot = inhalt[spaltennamen[8]]

    va_l1 = inhalt[spaltennamen[9]]
    va_l2 = inhalt[spaltennamen[10]]
    va_l3 = inhalt[spaltennamen[11]]
    va_tot = inhalt[spaltennamen[12]]

    var_l1 = inhalt[spaltennamen[13]]
    var_l2 = inhalt[spaltennamen[14]]
    var_l3 = inhalt[spaltennamen[15]]
    var_tot = inhalt[spaltennamen[16]]

    berechne(v_l1, spaltennamen[2])
    berechne(v_l2, spaltennamen[3])
    berechne(v_l3, spaltennamen[4])
    berechne(a_l1, spaltennamen[5])
    berechne(a_l2, spaltennamen[6])
    berechne(a_l3, spaltennamen[7])
    berechne(w_tot, spaltennamen[8])

    berechne(va_l1, spaltennamen[9])
    berechne(va_l2, spaltennamen[10])
    berechne(va_l3, spaltennamen[11])
    berechne(va_tot, spaltennamen[12])
    
    berechne(var_l1, spaltennamen[13])
    berechne(var_l2, spaltennamen[14])
    berechne(var_l3, spaltennamen[15])
    berechne(var_tot, spaltennamen[16])

def plotten(inhalt):
    v_l1 = inhalt[spaltennamen[2]]
    plot_ts(v_l1, spaltennamen[2])
   
    

def plot_ts(inhalt, name):
   ypoints = np.array([3, 8, 1, 10, 5, 7])
   #matplotlib.pyplot.plot(ypoints)
   #matplotlib.pyplot.show()

if __name__ == "__main__":
    main()
