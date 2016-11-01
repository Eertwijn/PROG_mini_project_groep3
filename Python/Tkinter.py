from tkinter import *

def taalNL():
    koptekst["text"] = "Actuele reistijden"

def taalENG():
    koptekst["text"] = "Actual traveltimes"

root = Tk()
root.title("NS actuele vertrektijden")
root.geometry("1500x1000")

achterkant = Label(master=root,
                   background="yellow"
)
achterkant.pack(fill=BOTH, expand=True)

#Tekst boven plaatje
koptekst = Label(master=achterkant,
              font = ('Raleway', 30),
              text='Actuele reistijden',
              background='yellow',
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

#Knop eigenstation
knop3 = Button(master=achterkant,
               text="Eigenstation")
knop3.pack()

#Knop anderstation
knop4 = Button(master=achterkant,
               text="Anderstation")
knop4.pack()

root.mainloop()
