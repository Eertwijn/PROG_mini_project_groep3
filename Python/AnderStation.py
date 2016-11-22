from tkinter import *
from tkinter import messagebox
import MasterApp


def taalNL():
    global g_taal
    """
    Deze functie verandert alle text naar Nederlands.
    """
    g_koptekst["text"] = "Voer hier uw gewenste station in:"
    g_knopsluiten["text"] = "Venster Sluiten"
    g_invulknop["text"] = "invullen"
    g_taal = "NL"
    station_invullen()


def taalENG():
    global g_taal
    """
    Deze functie verandert alle text naar Engels.
    """
    g_koptekst["text"] = "Please enter your station here:"
    g_knopsluiten["text"] = "Close Window"
    g_invulknop["text"] = "Enter"
    g_taal = "ENG"
    station_invullen()


def station_invullen(event=None):
    """
    Deze functie kijkt eerst of er iets ingevuld is, is dat het geval dan kijkt de functie of het een bestaand station is en print daarvan de info uit.
    Als het station niet bestaat geeft de functie een foutmelding aan de gebruiker.
    """

    station = g_entry.get()
    if station != "":
        if station in g_stationslijst:
            g_reisinformatie.config(state=NORMAL)
            g_reisinformatie.delete(1.0, END)
            g_reisinformatie.insert(END, MasterApp.tijden_ophalen(station, g_taal))
            g_reisinformatie.config(state=DISABLED)
        else:
            messagebox.showerror("Foutmelding", "Dat station kennen wij niet")


def venster_openen(meegeeftaal):
    global g_taal, g_knopsluiten, g_reisinformatie, g_invulknop, g_entry, g_koptekst, g_stationslijst
    g_taal = meegeeftaal
    g_stationslijst = MasterApp.stationsLijst()
    """
    Deze functie openend een nieuw venster en kijkt of de taal niet Nederlands is, is dat het geval dan roept hij taalENG() aan.
    """

    root = Toplevel()
    root.title("NS actuele vertrektijden")
    root.geometry("1500x1000")
    root.bind("<Return>", station_invullen)

    # Achtergrond kleur
    achterkant = Label(master=root,
                       bg='#%02x%02x%02x' % (255, 205, 76))
    achterkant.pack(fill=BOTH, expand=True)

    # Tekst boven
    g_koptekst = Label(master=achterkant,
                     font=('Raleway', 30),
                     text='Voer hier uw gewenste station in:',
                     bg='#%02x%02x%02x' % (255, 205, 76),
                     height=3)
    g_koptekst.pack()

    # Frame om invoer balk en de knop mooi naast elkaar te krijgen
    box1 = Frame(master=achterkant,
                 bg='#%02x%02x%02x' % (255, 205, 76))
    box1.pack()

    # Invoer balk
    g_entry = Entry(master=box1,
                  font=('Raleway', 15),
                  width=15)
    g_entry.pack(side=LEFT)

    # Knop om de invoer te activeren
    g_invulknop = Button(master=box1,
                       text="Invullen",
                       font=('Raleway', 15),
                       bg='#%02x%02x%02x' % (5, 53, 147),
                       fg='white',
                       width=15,
                       command=station_invullen)
    g_invulknop.pack(side=RIGHT)

    # Frame voor de text en de scrollbar
    textenscrollframe = Frame(master=achterkant)

    # De scrollbar voor de text
    scrollbar = Scrollbar(master=textenscrollframe)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Widget om de text in te stoppen
    g_reisinformatie = Text(master=textenscrollframe,
                          font=('Raleway', 16),
                          bg='#%02x%02x%02x' % (255, 205, 76),
                          height=25,
                          width=150,
                          yscrollcommand=scrollbar.set)
    g_reisinformatie.pack()
    g_reisinformatie.config(state=DISABLED)

    scrollbar.config(command=g_reisinformatie.yview)

    textenscrollframe.pack()

    # Onderste blauwe balk
    balk = Canvas(master=achterkant,
                  bg='#%02x%02x%02x' % (5, 53, 147),
                  height=100)
    balk.pack(side=BOTTOM, fill=X)

    # Knoppen voor de talen
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
