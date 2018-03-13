import matplotlib.pyplot as plt
import numpy as np

vokaalit = ["a", "e", "i", "o", "u", "y", "ae", "oe"]

lista = ['589,985', '446,1801', '255,2218', '406,782', '312,597', '283,1567', '632,1310', '421,1288']
lista2 = [int(i.split(",")[0]) for i in lista]
lista3 = [int(i.split(",")[1]) for i in lista]

f1range = float(sorted(lista2)[-1]) - float(sorted(lista2)[0])
f2range = float(sorted(lista3)[-1]) - float(sorted(lista3)[0])

f1suhde = [(i - sorted(lista2)[0])/f1range for i in lista2]
f2suhde = [(i - sorted(lista3)[0])/f2range for i in lista3]

def piirraKartta(f1suhde, f2suhde, f1=0, f2=0):           
    fig, ax = plt.subplots()
    ax.scatter(f2suhde, f1suhde)

    for i, txt in enumerate(vokaalit):
        ax.annotate(txt, (f2suhde[i] + -.01, f1suhde[i] + -.01))

    plt.title("Vowels")
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()

    plt.show()
