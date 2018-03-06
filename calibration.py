import trainingStructure as ts
import audioRecorder as ar
import praatInterFace_noCommandLine as pr
import taustaTiedot as tau
import json
import os

skripti = pr.lataaSkripti(pr.SKRIPTI)
koehenkilo = ""
aakkoset = ['a', 'e', 'i', 'o', 'u', 'y', 'ae', 'oe']

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

tulokset = ts.kalibraatio(tiedostot, skripti, koehenkilo)
keskiarvot = []
suhteet1 = tulokset[1][0]
suhteet2 = tulokset[1][1]
suhteet3 = tulokset[1][2]
for i in range(8):
	aver1 = (suhteet1[i][0] + suhteet2[i][0] + suhteet3[i][0])/3
	aver2 = (suhteet1[i][1] + suhteet2[i][1] + suhteet3[i][1])/3
	keskiarvot.append((aver1, aver2))

osalLista[koehenkilo]["suhdeluvut"] = {}
for i, a in enumerate(keskiarvot):
    osalLista[koehenkilo]["suhdeluvut"][aakkoset[i]] = a
