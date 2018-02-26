import trainingStructure as ts
import audioRecorder as ar
import praatInterFace_noCommandLine as pr
import taustaTiedot as tau
import json

skripti = pr.lataaSkripti(pr.SKRIPTI)
koehenkilo = ""

try:
    f = open("osallistujat.json", "r")
    osalLista = json.load(f)
    f.close()
except IOError:
    osalLista = {}

osalMaara = len(osalLista.keys())

kieliLista = ["englanti", "ruotsi", "saksa", "espanja"]

osalLista["KH" + str(osalMaara)] = tau.uusiOsallistuja()
koehenkilo = "KH" + str(osalMaara)
osalMaara = len(osalLista.keys())
tiedostot = [koehenkilo + "_kalib1", koehenkilo + "_kalib2", koehenkilo + "_kalib3"]

ts.kalibraatio(tiedostot, skripti)
