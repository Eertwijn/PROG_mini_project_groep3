from tkinter import *
import AnderStation
import ReistijdenUtrechtCentraal

# Functie om de taal naar het Nederlands aan te passen.
def taalNL():
    global g_taal
    koptekst["text"] = "Actuele reistijden"
    knopHier["text"] = "Huidig Station"
    knopAnders["text"] = "Ander Station"
    knopsluiten["text"] = "Programma Sluiten"
    g_taal = "NL"

# Functie om de taal naar het Engels aan te passen.
def taalENG():
    global g_taal
    koptekst["text"] = "Actual traveltimes"
    knopHier["text"] = "Current Station"
    knopAnders["text"] = "Other Station"
    knopsluiten["text"] = "Close Program"
    g_taal = "ENG"


g_taal = "NL"

# Hoofdscherm
root = Tk()
root.title("NS actuele vertrektijden")
root.geometry("1500x1000")

# Achtergrond kleur
achterkant = Label(master=root,
                   bg='#%02x%02x%02x' % (255, 205, 76))
achterkant.pack(fill=BOTH, expand=True)

# Tekst boven plaatje
koptekst = Label(master=achterkant,
                 font=('Raleway', 30),
                 text='Actuele Reistijden',
                 bg='#%02x%02x%02x' % (255, 205, 76),
                 height=3)
koptekst.pack()

# Plaatje
plaatjeNS = PhotoImage(file='plaatjeNS.gif')

plaatje = Label(master=achterkant,
                image=plaatjeNS,
                width=1140,
                height=400)
plaatje.pack()

# Onderste blauwe balk
balk = Canvas(master=achterkant,
              bg='#%02x%02x%02x' % (5, 53, 147),
              height=100)
balk.pack(side=BOTTOM, fill=X)

# knoppen voor de talen
# Taal knop Nederlands
vlagNL = PhotoImage(file='vlagNL.gif').subsample(4)
knopNL = Button(master=balk,
                image=vlagNL,
                command=taalNL)
knopNL.pack(side=LEFT, pady=10, padx=10)

# Taal knop Engels
vlagENG = PhotoImage(file='vlagENG.gif').subsample(4)
knopENG = Button(master=balk,
                 image=vlagENG,
                 command=taalENG)
knopENG.pack(side=LEFT, pady=10, padx=10)

# Knop sluiten
knopsluiten = Button(master=balk,
                     text="Programma Sluiten",
                     font=('Raleway', 12),
                     bg='#%02x%02x%02x' % (5, 53, 147),
                     fg='white',
                     command=root.destroy)
knopsluiten.pack(side=RIGHT, pady=10, padx=10)

# Een frame waar de knoppen "hier" en "anders" in staan
box = Frame(master=achterkant,
            bg='#%02x%02x%02x' % (255, 205, 76))
box.pack()

# Knop eigenstation
knopHier = Button(master=box,
                  text="Huidig Station",
                  font=('Raleway', 15),
                  bg='#%02x%02x%02x' % (5, 53, 147),
                  fg='white',
                  height=3,
                  width=15,
                  command=lambda: ReistijdenUtrechtCentraal.venster_openen(g_taal))
knopHier.pack(side=LEFT, padx=20, pady=30)

# Knop anderstation
knopAnders = Button(master=box,
                    text="Ander Station",
                    font=('Raleway', 15),
                    bg='#%02x%02x%02x' % (5, 53, 147),
                    fg='white',
                    height=3,
                    width=15,
                    command=lambda: AnderStation.venster_openen(g_taal))
knopAnders.pack(side=RIGHT, padx=20, pady=30)

root.mainloop()
