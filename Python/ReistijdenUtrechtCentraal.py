from tkinter import *
import MasterApp


def taalNL():
    # Functie om de taal naar het Nederlands aan te passen.
    global g_taal
    g_taal = "NL"
    g_knopsluiten["text"] = "Venster Sluiten"
    g_reisinformatie.config(state=NORMAL)
    g_reisinformatie.delete(1.0, END)
    g_reisinformatie.insert(END, MasterApp.tijden_ophalen("ut", g_taal))
    g_reisinformatie.config(state=DISABLED)

# Functie om de taal naar het Engels aan te passen.
def taalENG():
    global g_taal
    g_taal = "ENG"
    g_knopsluiten["text"] = "Close Window"
    g_reisinformatie.config(state=NORMAL)
    g_reisinformatie.delete(1.0, END)
    g_reisinformatie.insert(END, MasterApp.tijden_ophalen("ut", g_taal))
    g_reisinformatie.config(state=DISABLED)

# Functie voor het openen van het nieuwe venster
def venster_openen(meegeeftaal):
    global g_taal, g_koptekst, g_reisinformatie, g_knopsluiten
    g_taal = meegeeftaal
    root = Toplevel()
    root.title("NS actuele vertrektijden")
    root.geometry("1500x1000")

    # Achtergrond kleur
    achterkant = Label(master=root,
                       bg='#%02x%02x%02x' % (255, 205, 76))
    achterkant.pack(fill=BOTH, expand=True)

    # Tekst boven
    koptekst = Label(master=achterkant,
                     font=('Raleway', 30),
                     text='Utrecht Centraal',
                     bg='#%02x%02x%02x' % (255, 205, 76),
                     height=3)
    koptekst.pack()

    # Frame voor de text en de scrollbar
    textenscrollframe = Frame(master=achterkant)

    # De scrollbar voor de text
    scrollbar = Scrollbar(master=textenscrollframe)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Tekst box aanmaken
    g_reisinformatie = Text(master=textenscrollframe,
                          wrap=NONE,
                          font=('Raleway', 16),
                          bg='#%02x%02x%02x' % (255, 205, 76),
                          height=25,
                          width=150)
    g_reisinformatie.pack()
    scrollbar.config(command=g_reisinformatie.yview)
    g_reisinformatie.insert(END, MasterApp.tijden_ophalen("ut", g_taal))
    g_reisinformatie.config(state=DISABLED)

    textenscrollframe.pack()

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
    g_knopsluiten = Button(master=balk,
                         text="Venster Sluiten",
                         font=('Raleway', 12),
                         bg='#%02x%02x%02x' % (5, 53, 147),
                         fg='white',
                         command=root.destroy)
    g_knopsluiten.pack(side=RIGHT, pady=10, padx=10)

    if g_taal != "NL":
        taalENG()

    root.mainloop()
