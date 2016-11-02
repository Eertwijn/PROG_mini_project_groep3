from tkinter import *

def taalNL():
    koptekst["text"] = "Huidig Station"
    knopsluiten["text"] = "Venster Sluiten"

def taalENG():
    koptekst["text"] = "Current Station"
    knopsluiten["text"] = "Close Window"

root = Tk()
root.title("NS actuele vertrektijden")
root.geometry("1500x1000")

achterkant = Label(master=root,
                   background="#FFC846"
)
achterkant.pack(fill=BOTH, expand=True)

#Tekst boven
koptekst = Label(master=achterkant,
              font = ('Raleway', 30),
              text='Huidig Station',
              background='#FFC846',
              height=3
              )
koptekst.pack()

#Onderste blauwe balk
balk = Canvas(master=achterkant,
                bg= 'blue',
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
knopsluiten = Button(master=balk,
                     text= "Programma sluiten",
                     font= ('Raleway', 12),
                     bg= 'blue',
                     fg= 'white',
                     command=root.destroy)
knopsluiten.pack(side=RIGHT, pady=10, padx=10)

root.mainloop()
