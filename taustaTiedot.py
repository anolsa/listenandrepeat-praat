import json

try:
    f = open("osallistujat.json", "r")
    osalLista = json.load(f)
    f.close()
except IOError:
    osalLista = {}
    
osalMaara = len(osalLista.keys())

kieliLista = ["englanti", "ruotsi", "saksa", "espanja"]

def tallennaOsallistujat(sanakirja):
    f = open("osallistujat.json", "w")
    json.dump(sanakirja, f)
    f.close()

def kysyKieli(kielenNimi):
    kieli = 6
    while kieli > 5 or kieli < 0:
        kieli = input("Kielitaitosi kielessa " + kielenNimi + " (0-5): ")
    return kieli

def uusiOsallistuja():
    nimi = raw_input("Etu- ja sukunimesi: ")
    while True:
        try:
            ika = int(raw_input("Ikasi?: "))
        except ValueError:
            continue
        break
    asuinPaikka = raw_input("Asuinpaikkasi?: ")
    kieliTaito = [(i, kysyKieli(i)) for i in kieliLista]
    global osalMaara
    osalMaara += 1
    khTiedot = {"Nimi" : nimi, "Ika" : ika, "Asuinpaikka" : asuinPaikka, "Kielitaito" : kieliTaito}
    return khTiedot

def lisaaOsallistuja(osalLista, osalMaara):
    osalLista["KH" + str(osalMaara)] = uusiOsallistuja()
    tallennaOsallistujat(osalLista)
