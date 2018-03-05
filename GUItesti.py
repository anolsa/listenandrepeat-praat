from GUI import RadioButton, RadioGroup, Label, Font, Window, TextField, Button, application

win_num = 0
tiedot = []

class TestWindow(Window):
    
    def key_down(self, event):
        c = event.char
        if c == '\r':
            print "Default"
        elif c == '\x1b':
            print "Cancel"
        else:
            Window.key_down(self, event)

class TestTextField(TextField):

    def __init__(self, number, *args, **kwds):
        TextField.__init__(self, *args, **kwds)
        self.number = number

nimiLabel = Label("Nimi:")
nimiLabel.position = (20, 20)

grp = RadioGroup()

def set_to_1():
    grp.value = 4

def make_window():
    global win_num
    global tiedot
    nimi = ""
    win_num += 1
    win = TestWindow(size = (320, 200), title = "Text fields %d" % (win_num))
    win.tf1 = TestTextField(1,
        position = (nimiLabel.right + 20, 20),
        width = 200, text = "")
    buty = win.tf1.bottom + 20
##    buttons = [RadioButton(x = engLabel.right + 20 * i, y = win.tf3.bottom + 20, title = "", group = grp) for i in range(1,6)]
##    for i, v in enumerate(buttons):
##        v.set_value(i+1)
    show_but = Button("Show",
        position = (20, buty),
        action = tiedot.append(repr(win.tf1.text)))
    win.add(nimiLabel)
    win.add(win.tf1)
    win.add(show_but)
    
    win.width = win.tf1.right + 20
    win.height = show_but.bottom + 20
    win.tf1.become_target()
    win.show()
    return win

win = make_window()

def sigterm(*a):
    raise Exception("SIGTERM")

import signal
signal.signal(signal.SIGTERM, sigterm)

application().run()
