import listaMetodit as lm
import scatterTest as st
import json

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

avaimet = osalLista[koehenkilo]["suhdeluvut"].keys()
suhteet = lm.suhdeListat(osalLista[koehenkilo]["suhdeluvut"])
st.piirraKartta(suhteet[0], suhteet[1], avaimet)
