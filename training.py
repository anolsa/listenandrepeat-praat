import json
import audioRecorder as ar
import praatInterFace_noCommandLine as pr
import taustaTiedot as tau
import listaMetodit as lm
import scatterTest as st

skripti = pr.lataaSkripti("formanttiSkripti.praat")
treenattava = 'avoinO'

def num(string):
    eka = int(string.split(',')[0])
    toka = int(string.split(',')[1])
    return (eka, toka)

def jatko(ohje):
    jatko = 'xxx'
    while jatko != '':
        jatko = raw_input(ohje)

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
#harj_formantit = []
aakkoset = osalLista[koehenkilo]["suhdeluvut"].keys()
aakkoset.append(treenattava)

suhteet = lm.suhdeListat(osalLista[koehenkilo]["suhdeluvut"])
suhteet[0].append(0)
suhteet[1].append(0)

print """\nTassa harjoituksessa kuulet ja toistat
aanteita. Harjoituksen alettua kuulet aanteen, ja tehtavasi
on toistaa se mahdollisimman tarkasti. Puhu rauhallisella,
selkealla aanella alaka sano muuta kuin toistettava aanne.

Toiston jalkeen saat kuvan vokaalikartastasi, jossa nakyvat
seka tavoiteaanne etta oma tuotoksesi suhteessa kalibraatio-
vaiheessa aantamiisi vokaaleihin."""

while tehdyt_harjoitukset < harjoituskerrat:
    jatko("\nPaina Enter aloittaaksesi harjoittelun")
    tiedosto = (koehenkilo + '_' +
                str(len(osalLista[koehenkilo]["Harjoitus"]) + 1))
    ar.nauhoitus(5, tiedosto, koehenkilo)
    pr.ajaSkripti(skripti, tiedosto + '.wav',
                  tiedosto + '_form.txt', koehenkilo)
    f = open(koehenkilo + '/' + tiedosto + '_form.txt', 'r')
    temp = f.readlines()[0]
    f.close()
    #harj_formantit.append(temp)
    osalLista[koehenkilo]["Harjoitus"].append(temp)
    kuvaSuhteet = lm.laskeSuhteetPari(num(temp),
                        osalLista[koehenkilo]["f1min"],
                        osalLista[koehenkilo]["f2min"],
                        osalLista[koehenkilo]["f1range"],
                        osalLista[koehenkilo]["f2range"])
    suhteet[0][-1] = kuvaSuhteet[0]
    suhteet[1][-1] = kuvaSuhteet[1]
    st.piirraKartta(suhteet[0], suhteet[1], aakkoset)
    tau.tallennaOsallistujat(osalLista)
    tehdyt_harjoitukset += 1
