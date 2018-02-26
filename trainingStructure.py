import audioRecorder as ar
import praatInterFace_noCommandLine as pr

def kalibraatio(tiedostoLista, skripti):
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
            ar.nauhoitus(7, i)    
            pr.ajaSkripti(skripti, i + ".wav", i + "_form.txt")
            f = open(i + "_form.txt", "r")
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
