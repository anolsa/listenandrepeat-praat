from Tkinter import *

fields = ["Nimi", "Ika", "Asuinpaikka"]
sanakirja = {}

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries

def fetch(entries, dictionary):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        dictionary[field] = text
    print dictionary

top = Tk()
ents = makeform(top, fields)
top.bind('<Return>', (lambda event, e=ents: fetch(e, sanakirja)))   
b1 = Button(top, text='Show',
            command=(lambda e=ents: fetch(e, sanakirja)))
b1.pack(side=LEFT, padx=5, pady=5)
b2 = Button(top, text='Quit', command = top.destroy)
b2.pack(side=LEFT, padx=5, pady=5)
top.mainloop()
