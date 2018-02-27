import audioRecorder as ar
import praatInterFace_noCommandLine as pr
import listaMetodit as lm
import json

def kalibraatio(tiedostoLista, skripti, polku):
    while True:
        aloitus = raw_input("Aloita? k/e?: ")
        if aloitus == "k":
            break
        elif aloitus == "e":
            quit()
        else:
            continue
        
    for i in tiedostoLista:
        while True:
            ar.nauhoitus(7, i, polku)    
            pr.ajaSkripti(skripti, i + ".wav", i + "_form.txt", polku)
            f = open(polku + "/" + i + "_form.txt", "r")
            temp = len(f.readlines())
            f.close()
            if temp > 8 or temp < 8:            
                print "Kalibraatio epaonnistui, nauhoita uudelleen: "
                while True:
                    jatko = raw_input("Paina k nauhoittaaksesi kalibraatio uudelleen: ")
                    if jatko == "k":
                        break
                    else:
                        quit()
                continue
            else:
                break
        while True:
            jatko = raw_input("Paina k jatkaaksesi: ")
            if jatko == "k":
                break
            else:
                continue

    for i in tiedostoLista:
        f = open(polku + "/" + i + "_form.txt", "r")
        tulos = lm.laskeSuhteet(f.readlines())
        f.close()
        f = open(polku + "/" + i + "_suhteet.txt", "w")
        json.dump(tulos, f)
        f.close()
        
