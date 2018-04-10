import trainingStructure as ts
import audioRecorder as ar
import praatInterFace_noCommandLine as pr
import taustaTiedot as tau
import listaMetodit as lm
import json
import os
import scatterTest as st

skripti = pr.lataaSkripti(pr.SKRIPTI)
koehenkilo = ""
aakkoset = ['a', 'e', 'i', 'o', 'u', 'y', 'ae', 'oe']

def tarkistaKalibrointi(koehenkilo):
    avaimet = osalLista[koehenkilo]["suhdeluvut"].keys()
    suhteet = lm.suhdeListat(osalLista[koehenkilo]["suhdeluvut"])
    st.piirraKartta(suhteet[0], suhteet[1], avaimet)
    
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
tiedostot = [koehenkilo + "_kalib1",
             koehenkilo + "_kalib2",
             koehenkilo + "_kalib3"]
os.makedirs(koehenkilo)

tau.tallennaOsallistujat(osalLista)

ts.kalibraatio(tiedostot, skripti, koehenkilo)

for i, e in enumerate(tiedostot):
    f = open(koehenkilo + "/" + e + "_form.txt", "r")
    temp = f.readlines()
    f.close()
    osalLista[koehenkilo]["formantit" + str(i+1)] = temp

osalLista[koehenkilo]["f1max"] = float(max(
    lm.f1Lista(osalLista[koehenkilo]["formantit1"]) +
    lm.f1Lista(osalLista[koehenkilo]["formantit2"]) +
    lm.f1Lista(osalLista[koehenkilo]["formantit3"])))
osalLista[koehenkilo]["f2max"] = float(max(
    lm.f2Lista(osalLista[koehenkilo]["formantit1"]) +
    lm.f2Lista(osalLista[koehenkilo]["formantit2"]) +
    lm.f2Lista(osalLista[koehenkilo]["formantit3"])))
osalLista[koehenkilo]["f1min"] = float(min(
    lm.f1Lista(osalLista[koehenkilo]["formantit1"]) +
    lm.f1Lista(osalLista[koehenkilo]["formantit2"]) +
    lm.f1Lista(osalLista[koehenkilo]["formantit3"])))
osalLista[koehenkilo]["f2min"] = float(min(
    lm.f2Lista(osalLista[koehenkilo]["formantit1"]) +
    lm.f2Lista(osalLista[koehenkilo]["formantit2"]) +
    lm.f2Lista(osalLista[koehenkilo]["formantit3"])))    

osalLista[koehenkilo]["f1range"] = (osalLista[koehenkilo]["f1max"]
                                    - osalLista[koehenkilo]["f1min"])
osalLista[koehenkilo]["f2range"] = (osalLista[koehenkilo]["f2max"]
                                    - osalLista[koehenkilo]["f2min"])

keskiarvot = []
suhteet1 = lm.laskeSuhteet(osalLista[koehenkilo]["formantit1"],
                           osalLista[koehenkilo]["f1min"],
                           osalLista[koehenkilo]["f2min"],
                           osalLista[koehenkilo]["f1range"],
                           osalLista[koehenkilo]["f2range"])
suhteet2 = lm.laskeSuhteet(osalLista[koehenkilo]["formantit2"],
                           osalLista[koehenkilo]["f1min"],
                           osalLista[koehenkilo]["f2min"],
                           osalLista[koehenkilo]["f1range"],
                           osalLista[koehenkilo]["f2range"])
suhteet3 = lm.laskeSuhteet(osalLista[koehenkilo]["formantit3"],
                           osalLista[koehenkilo]["f1min"],
                           osalLista[koehenkilo]["f2min"],
                           osalLista[koehenkilo]["f1range"],
                           osalLista[koehenkilo]["f2range"])                                    
for i in range(8):
	aver1 = (suhteet1[i][0] + suhteet2[i][0] + suhteet3[i][0])/3
	aver2 = (suhteet1[i][1] + suhteet2[i][1] + suhteet3[i][1])/3
	keskiarvot.append((aver1, aver2))

osalLista[koehenkilo]["suhdeluvut"] = {}
for i, a in enumerate(keskiarvot):
    osalLista[koehenkilo]["suhdeluvut"][aakkoset[i]] = a

tau.tallennaOsallistujat(osalLista)
