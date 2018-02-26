class Koehenkilo:

    def __init__(self, nimi, ika, koti, kielitaito):
        self.nimi = nimi
        self.ika = ika
        self.kotikunta = koti
        self.kielitaito = kielitaito

    def tallennus(self):
        tiedot = {}
        tiedot["Ika"] = self.ika
        tiedot["Nimi"] = self.nimi
        tiedot["Kotikunta"] = self.kotikunta
        tiedot["Kielitaito"] = self.kielitaito
        return tiedot


    
