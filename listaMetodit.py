def laskeSuhteet(formanttiLista):    
    lista2 = [int(i.split(",")[0]) for i in formanttiLista]
    lista3 = [int(i.split(",")[1]) for i in formanttiLista]

    f1range = float(sorted(lista2)[-1]) - float(sorted(lista2)[0])
    f2range = float(sorted(lista3)[-1]) - float(sorted(lista3)[0])

    f1suhde = [(i - sorted(lista2)[0])/f1range for i in lista2]
    f2suhde = [(i - sorted(lista3)[0])/f2range for i in lista3]

    suhteet = []
    for i in range(0,len(f1suhde)):
        suhteet.append((float(f1suhde[i]), float(f2suhde[i])))

    return suhteet

def laskeSuhteetPari(formanttiTuple):
    pass
