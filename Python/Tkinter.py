from tkinter import *

def taalNL():
    koptekst["text"] = "Actuele reistijden"
    knop3["text"] = "Huidig Station"
    knop4["text"] = "Ander Station"
    knopsluiten["text"] = "Programma Sluiten"

def taalENG():
    koptekst["text"] = "Actual traveltimes"
    knop3["text"] = "Current Station"
    knop4["text"] = "Other Station"
    knopsluiten["text"] = "Close Programme"

def knopHuidig():
    print("Ok")


def knopAnder():
    print("OK2")

root = Tk()
root.title("NS actuele vertrektijden")
root.geometry("1500x1000")

achterkant = Label(master=root,
                   background="#FFC846"
)
achterkant.pack(fill=BOTH, expand=True)

#Tekst boven plaatje
koptekst = Label(master=achterkant,
              font = ('Raleway', 30),
              text='Actuele reistijden',
              background='#FFC846',
              height=3
              )
koptekst.pack()

#Plaatje
plaatjeNS = PhotoImage(file='plaatjeNS.gif')

plaatje = Label(master=achterkant,
                image=plaatjeNS,
                width=1140,
                height=400)
plaatje.pack()

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



#Knop eigenstation
knop3 = Button(master=achterkant,
               text="Huidig Station",
               font = ('Raleway', 15),
               bg= 'blue',
               fg= 'white',
               height= 3,
               width= 15,
               command= knopHuidig)
knop3.pack()

#Knop anderstation
knop4 = Button(master=achterkant,
               text="Ander station",
               font = ('Raleway', 15),
               bg= '#053593',
               fg= 'white',
               height= 3,
               width= 15,
               command= knopAnder)
knop4.pack()

root.mainloop()
