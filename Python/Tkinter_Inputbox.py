from tkinter import *
from tkinter import messagebox
import MasterApp

def taalNL():
    koptekst["text"] = "Huidig Station"
    knopsluiten["text"] = "Venster Sluiten"
    global taal
    taal = "NL"
    reisinformatie.delete(1.0, END)
    station_invullen()

def taalENG():
    koptekst["text"] = "Current Station"
    knopsluiten["text"] = "Close Window"
    global taal
    taal = "ENG"
    reisinformatie.delete(1.0, END)
    station_invullen()

def station_invullen():
    station = entry.get()
    print(station)
    if station in MasterApp.stationsLijst():
        reisinformatie.insert(END, MasterApp.tijden_ophalen(station, taal))
    else:
        messagebox.showerror("Foutmelding","Dat station kennen wij niet")


def venster_openen():
    global taal
    taal = "NL"
    root = Toplevel()
    root.title("NS actuele vertrektijden")
    root.geometry("1500x1000")

    achterkant = Label(master=root,
                       background="#FFCD4C"
    )
    achterkant.pack(fill=BOTH, expand=True)

    #Tekst boven
    global koptekst
    koptekst = Label(master=achterkant,
                  font = ('Raleway', 30),
                  text='Huidig Station',
                  background='#FFCD4C',
                  height=3
                  )
    koptekst.pack()

    global entry
    entry = Entry(master=achterkant)
    entry.pack()

    knop = Button(master=achterkant, text="Invullen", width=10, command=station_invullen)
    knop.pack()

    global reisinformatie
    reisinformatie = Text(master=achterkant,
              font = ('Raleway', 16),

              #text=station,

              background='#FFC846',
              height=25,
              width=150
              )
    reisinformatie.pack()

    #Onderste blauwe balk
    balk = Canvas(master=achterkant,
                    bg= '#053593',
                    height=100)
    balk.pack(side=BOTTOM, fill=X)

    #knoppen voor de taal
    #Taal knop 1
    vlagNL = PhotoImage(file='vlagNL.gif').subsample(4)
    knop1 = Button(master=balk,
                   image=vlagNL,
                   command=taalNL,
                   )
    knop1.pack(side=LEFT, pady=10, padx=10)

    #Taal knop 2
    vlagENG= PhotoImage(file='vlagENG.gif').subsample(4)
    knop2 = Button(master=balk,
                   image=vlagENG,
                   command=taalENG,
                   )
    knop2.pack(side=LEFT, pady=10, padx=10)

    #Knop sluiten
    global knopsluiten
    knopsluiten = Button(master=balk,
                         text= "Venster sluiten",
                         font= ('Raleway', 12),
                         bg= '#053593',
                         fg= 'white',
                         command=root.destroy)
    knopsluiten.pack(side=RIGHT, pady=10, padx=10)

    root.mainloop()
