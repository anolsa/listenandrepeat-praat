import json
import audioRecorder as ar
import praatInterFace_noCommandLine as pr
import taustaTiedot as tau
import listaMetodit
import scatterTest as st

skripti = pr.lataaSkripti("formanttiSkripti.praat")
aakkoset = ['a', 'e', 'i', 'o', 'u', 'y', 'ae', 'oe']

try:
    f = open("osallistujat.json", "r")
    osalLista = json.load(f)
    f.close()
except IOError:
    print "\nEi tallennettuja koehenkiloita!"
    quit

for i, e in enumerate(osalLista.keys()):
    print str(i+1) + '. ' + e
kh_valinta = input("Valitse haluamasi koehenkilo listasta: ")
koehenkilo = "KH" + str(kh_valinta)

harjoituskerrat = 2
tehdyt_harjoitukset = 0
harj_formantit = []

while tehdyt_harjoitukset < harjoituskerrat:
    tiedosto = koehenkilo + '_' + str(tehdyt_harjoitukset)
    ar.nauhoitus(5, tiedosto, koehenkilo)
    pr.ajaSkripti(skripti, tiedosto + '.wav', tiedosto + '_form.txt', koehenkilo)
    f = open(koehenkilo + '/' + tiedosto + '_form.txt', 'r')
    temp = f.readlines()[0]
    f.close()
    harj_formantit.append(temp)
    osalLista[koehenkilo]["Harjoitus"] = harj_formantit    
    tehdyt_harjoitukset += 1
