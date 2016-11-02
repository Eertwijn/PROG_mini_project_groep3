from tkinter import *
#from MasterApp import *
import requests
import xmltodict

def taalNL():
    koptekst["text"] = "Huidig Station"
    knopsluiten["text"] = "Venster Sluiten"

def taalENG():
    koptekst["text"] = "Current Station"
    knopsluiten["text"] = "Close Window"

def infoUTCentraal(taal):
    #inlogegevens
    authdetails = ('sam.zandee@gmail.com', 'PR15gnkYhlxUuWrjXFnZ_yBHswBfR-clw1oYMkbMW7eeeNLD0sGd5A')
    #de url die nodig is wordt bepaald door het station er aan te plakken
    apiurl = "http://webservices.ns.nl/ns-api-avt?station=ut"

    #de reactie wordt opgevraagt
    response = requests.get(apiurl, auth=authdetails)
    #de reactie wordt geparst
    vertrekXML = xmltodict.parse(response.text)

    nuttige_info = ""

    #De vertrektijden worden opgezocht en op geslagen in nuttige_info=""
    for vertek in vertrekXML["ActueleVertrekTijden"]["VertrekkendeTrein"]:
        if "VertrekVertragingTekst" not in vertek:
            nuttige_info += "{:<21} {:>10} {:>31}\n".format(vertek["EindBestemming"],vertek["VertrekTijd"][11:16], vertek["VertrekSpoor"]["#text"])
        else:
            nuttige_info += "{:<21} {:>10} {:>18} {:>12}\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16],vertek["VertrekVertragingTekst"], vertek["VertrekSpoor"]["#text"],)
    #de vertrektijden worden uitgeprint
    if taal == "NL":
        print("{:<26} {:>10} {:>15} {:>10}".format("Eindbestemming", "Vertrektijd", "Vertraging", "Spoor"))
    else:
        print("{:<26} {:>10} {:>15} {:>10}".format("Destination", "Time of Departure", "Delay", "Platform"))

    print(nuttige_info)
    return(nuttige_info)


root = Tk()
root.title("NS actuele vertrektijden")
root.geometry("1500x1000")

achterkant = Label(master=root,
                   background="#FFCD4C"
)
achterkant.pack(fill=BOTH, expand=True)

#Tekst boven
koptekst = Label(master=achterkant,
              font = ('Raleway', 30),
              text='Utrecht Centraal',
              background='#FFCD4C',
              height=3
              )
koptekst.pack()
taal = "NL"
station = infoUTCentraal(taal)

reisinformatie = Label(master=achterkant,
              font = ('Raleway', 12),
              #command=infoUTCentraal(taal),
              text=station,

              background='#FFCD4C',
              height=3
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
knopsluiten = Button(master=balk,
                     text= "Programma sluiten",
                     font= ('Raleway', 12),
                     bg= '#053593',
                     fg= 'white',
                     command=root.destroy)
knopsluiten.pack(side=RIGHT, pady=10, padx=10)

root.mainloop()
