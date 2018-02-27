import subprocess

AANI = "file.wav" #analysoitavan aanitiedoston nimi
TULOS = "formanttejako.txt" #tiedosto johon data menee
SKRIPTI = "formanttiSkripti.praat" #kaytettavan skriptin nimi

#tama patka avaa skriptitiedoston ja jakaa sen rivit
#listaksi kokoajaskriptia varten
def lataaSkripti(skriptinNimi):
    f = file(skriptinNimi, "r")
    skripti = []
    for line in f:
        skripti.append(line)
    f.close()
    return skripti

#tama menetelma ottaa listamuodossa olevan skriptin seka
#annetut tiedostonimet, ja lisaa ne skriptiin oikeisiin kohtiin
#jonka jalkeen se kasaa skriptin jalleen luettavaan muotoon
def kokoaSkripti(skripti, aaniNimi, tulosNimi, polkuNimi):
    skripti[0] = "Read from file: \"" + polkuNimi + "\\" + aaniNimi + "\"\n"    
    skripti[12] = "fileName$ = \"" + "\\" + polkuNimi + "\\" + tulosNimi + "\"\n"
    return ''.join(skripti)

#tama menetelma ajaa skriptin. se ottaa argumenteiksi
#listamuotoisen skriptin ja tiedostonimet, ja valittaa
#ne kokoajaskriptille, jonka tulosteen se sitten ylikirjoittaa
#SKRIPTI-muuttujassa maaritettyyn tiedostoon.
#sitten se ajaa skriptin
def ajaSkripti(skripti, aaniNimi, tulosNimi, polkuNimi):
    tuloste = kokoaSkripti(skripti, aaniNimi, tulosNimi, polkuNimi)
    f = file(SKRIPTI, "w")
    f.write(tuloste)
    f.close()
    subprocess.call("praat --run \"" + SKRIPTI + "\"", shell = True)
