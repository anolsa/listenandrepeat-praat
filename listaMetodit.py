def f1Lista(formanttiLista):
    lista = [int(i.split(",")[0]) for i in formanttiLista]
    return lista

def f2Lista(formanttiLista):
    lista = [int(i.split(",")[1]) for i in formanttiLista]
    return lista

def laskeSuhteet(formanttiLista, f1min, f2min, f1range, f2range):   
    lista2 = f1Lista(formanttiLista)
    lista3 = f2Lista(formanttiLista)    

    f1suhde = [(i - f1min)/f1range for i in lista2]
    f2suhde = [(i - f2min)/f2range for i in lista3]

    suhteet = []
    for i in range(0,len(f1suhde)):
        suhteet.append((float(f1suhde[i]), float(f2suhde[i])))

    return suhteet

def laskeSuhteetPari(formanttiTuple):
    pass
