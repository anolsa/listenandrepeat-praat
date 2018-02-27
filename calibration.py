import trainingStructure as ts
import audioRecorder as ar
import praatInterFace_noCommandLine as pr
import taustaTiedot as tau
import json
import os

skripti = pr.lataaSkripti(pr.SKRIPTI)
koehenkilo = ""

try:
    f = open("osallistujat.json", "r")
    osalLista = json.load(f)
    f.close()
except IOError:
    osalLista = {}

osalMaara = 0
if len(osalLista.keys()) == 0:
    osalMaara = 1
else:
    osalMaara = len(osalLista.keys()) + 1

kieliLista = ["englanti", "ruotsi", "saksa", "espanja"]

osalLista["KH" + str(osalMaara)] = tau.uusiOsallistuja()
koehenkilo = "KH" + str(osalMaara)
osalMaara = len(osalLista.keys())
tiedostot = [koehenkilo + "_kalib1", koehenkilo + "_kalib2", koehenkilo + "_kalib3"]
os.makedirs(koehenkilo)

tau.tallennaOsallistujat(osalLista)

ts.kalibraatio(tiedostot, skripti, koehenkilo)
