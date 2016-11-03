from tkinter import *
import AnderStation
import ReistijdenUtrechtCentraal


def taalNL():
    # Functie om de taal naar het Nederlands aan te passen.
    koptekst["text"] = "Actuele reistijden"
    knopHier["text"] = "Huidig Station"
    knopAnders["text"] = "Ander Station"
    knopsluiten["text"] = "Programma Sluiten"
    global taal
    taal = "NL"


def taalENG():
    # Functie om de taal naar het Engels aan te passen.
    koptekst["text"] = "Actual traveltimes"
    knopHier["text"] = "Current Station"
    knopAnders["text"] = "Other Station"
    knopsluiten["text"] = "Close Programme"
    global taal
    taal = "ENG"


global taal
taal = "NL"

# Hoofdscherm
root = Tk()
root.title("NS actuele vertrektijden")
root.geometry("1500x1000")

# Achtergrond kleur
achterkant = Label(master=root,
                   background="#FFCD4C")
achterkant.pack(fill=BOTH, expand=True)

# Tekst boven plaatje
koptekst = Label(master=achterkant,
                 font=('Raleway', 30),
                 text='Actuele reistijden',
                 background='#FFCD4C',
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
              bg='#053593',
              height=100)
balk.pack(side=BOTTOM, fill=X)

# knoppen voor de taal
# Taal knop 1
vlagNL = PhotoImage(file='vlagNL.gif').subsample(4)
knopNL = Button(master=balk,
                image=vlagNL,
                command=taalNL)
knopNL.pack(side=LEFT, pady=10, padx=10)

# Taal knop 2
vlagENG = PhotoImage(file='vlagENG.gif').subsample(4)
knopENG = Button(master=balk,
                 image=vlagENG,
                 command=taalENG)
knopENG.pack(side=LEFT, pady=10, padx=10)

# Knop sluiten
knopsluiten = Button(master=balk,
                     text="Programma sluiten",
                     font=('Raleway', 12),
                     bg='#053593',
                     fg='white',
                     command=root.destroy)
knopsluiten.pack(side=RIGHT, pady=10, padx=10)

# Een Frame waar de knoppen Hier en Anders in staan
box = Frame(master=achterkant,
            bg='#FFCD4C')
box.pack()

# Knop eigenstation
knopHier = Button(master=box,
                  text="Huidig Station",
                  font=('Raleway', 15),
                  bg='#053593',
                  fg='white',
                  height=3,
                  width=15,
                  command=lambda: ReistijdenUtrechtCentraal.venster_openen(taal))
knopHier.pack(side=LEFT, padx=20, pady=30)

# Knop anderstation
knopAnders = Button(master=box,
                    text="Ander Station",
                    font=('Raleway', 15),
                    bg='#053593',
                    fg='white',
                    height=3,
                    width=15,
                    command=lambda: AnderStation.venster_openen(taal))
knopAnders.pack(side=RIGHT, padx=20, pady=30)

root.mainloop()
