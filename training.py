import json
import audioRecorder as ar
import praatInterFace_noCommandLine as pr
import listaMetodit

try:
    f = open("osallistujat.json", "r")
    osalLista = json.load(f)
    f.close()
except IOError:
    print "\nEi tallennettuja koehenkiloita!"
