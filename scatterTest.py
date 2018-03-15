import matplotlib.pyplot as plt

def piirraKartta(f1suhde, f2suhde, vokaalit):
    fig, ax = plt.subplots()
    ax.scatter(f2suhde, f1suhde)

    for i, txt in enumerate(vokaalit):
        ax.annotate(txt, (f2suhde[i] + -.01, f1suhde[i] + -.01))

    plt.title("Vowels")
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()

    plt.show()
