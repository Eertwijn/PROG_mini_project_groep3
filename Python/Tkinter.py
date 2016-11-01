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
photo = PhotoImage(file='plaatjeNS.gif')

plaatje = Label(master=achterkant,
                image=photo,
                width=1140,
                height=400)
plaatje.pack()

#Onderste blauwe balk


#knoppen voor de taal
#Knop 1
knop1 = Button(master=achterkant, text='Druk hierNL', command=taalNL)
knop1.pack(pady=10)

#Knop 2
knop2 = Button(master=achterkant, text='Druk hierENG', command=taalENG)
knop2.pack(pady=10)

root.mainloop()
