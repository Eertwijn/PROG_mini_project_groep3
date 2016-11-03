from tkinter import *
import MasterApp
import requests
import xmltodict

#Functies voor het wijzigen van de taal
def taalNL():
    #koptekst["text"] = "Huidig Station"
    knopsluiten["text"] = "Venster Sluiten"
    global taal
    taal = "NL"
    reisinformatie.delete(1.0, END)
    reisinformatie.insert(END, MasterApp.tijden_ophalen("ut", taal))

def taalENG():
    #koptekst["text"] = "Current Station"
    knopsluiten["text"] = "Close Window"
    global taal
    taal = "ENG"
    reisinformatie.delete(1.0, END)
    reisinformatie.insert(END, MasterApp.tijden_ophalen("ut", taal))

#Functie voor het openen van het nieuwe venster
def venster_openen(meegeeftaal):
    root = Toplevel()
    root.title("NS actuele vertrektijden")
    root.geometry("1500x1000")
    global taal
    taal = meegeeftaal

    #Achterkant
    achterkant = Label(master=root,
                       background="#FFC846")
    achterkant.pack(fill=BOTH, expand=True)

    #Tekst boven
    global koptekst
    koptekst = Label(master=achterkant,
                  font = ('Raleway', 30),
                  text='Utrecht Centraal',
                  background='#FFC846',
                  height=3
                  )
    koptekst.pack()

    #Tekst box aanmaken
    global reisinformatie
    reisinformatie = Text(master=achterkant,
                  font = ('Raleway', 16),
                  background='#FFC846',
                  height=25,
                  width=150
                  )
    reisinformatie.pack()
    reisinformatie.insert(END, MasterApp.tijden_ophalen("ut", taal))

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
