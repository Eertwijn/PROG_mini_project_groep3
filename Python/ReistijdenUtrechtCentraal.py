from tkinter import *
import MasterApp
import requests
import xmltodict

def taalNL():
    #koptekst["text"] = "Huidig Station"
    knopsluiten["text"] = "Venster Sluiten"
    global taal
    taal = "NL"
    infoUTCentraal(taal)

def taalENG():
    #koptekst["text"] = "Current Station"
    knopsluiten["text"] = "Close Window"
    global taal
    taal = "ENG"

def venster_openen():
    root = Toplevel()
    root.title("NS actuele vertrektijden")
    root.geometry("1500x1000")
    global taal
    taal = "NL"

    # def infoUTCentraal(taal):
    #     #inlogegevens
    #     authdetails = ('sam.zandee@gmail.com', 'PR15gnkYhlxUuWrjXFnZ_yBHswBfR-clw1oYMkbMW7eeeNLD0sGd5A')
    #     #de url die nodig is wordt bepaald door het station er aan te plakken
    #     apiurl = "http://webservices.ns.nl/ns-api-avt?station=ut"
    #
    #     #de reactie wordt opgevraagt
    #     response = requests.get(apiurl, auth=authdetails)
    #     #de reactie wordt geparst
    #     vertrekXML = xmltodict.parse(response.text)
    #
    #     nuttige_info = ""
    #
    #     #de vertrektijden worden uitgeprint
    #     if taal == "NL":
    #         columninfo = "{:<26} {:>10} {:>15} {:>10}".format("Eindbestemming", "Vertrektijd", "Vertraging", "Spoor")
    #     else:
    #         columninfo = "{:<26} {:>10} {:>15} {:>10}".format("Destination", "Time of Departure", "Delay", "Platform")
    #     #De vertrektijden worden opgezocht en op geslagen in nuttige_info=""
    #     for vertek in vertrekXML["ActueleVertrekTijden"]["VertrekkendeTrein"]:
    #         if "VertrekVertragingTekst" not in vertek:
    #             nuttige_info += "{:<21} {:>20} {:>31}\n".format(vertek["EindBestemming"],vertek["VertrekTijd"][11:16], vertek["VertrekSpoor"]["#text"])
    #         else:
    #             nuttige_info += "{:<21} {:>20} {:>18} {:>12}\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16],vertek["VertrekVertragingTekst"], vertek["VertrekSpoor"]["#text"],)
    #     print(columninfo)
    #     print(nuttige_info)
    #     return(columninfo, nuttige_info)

    achterkant = Label(master=root,
                       background="#FFC846"
    )
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

    # station = infoUTCentraal(taal)
    # newline = "\n"
    reisinformatie = Text(master=achterkant,
                  font = ('Raleway', 16),

                  #text=station,

                  background='#FFC846',
                  height=25,
                  width=150
                  )
    reisinformatie.pack()
    # reisinformatie.insert(END, station[0])
    # reisinformatie.insert(END, newline)
    # reisinformatie.insert(END, station[1])
    reisinformatie.insert(END, MasterApp.tijden_ophalen("ut", taal))

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
    global knopsluiten
    knopsluiten = Button(master=balk,
                         text= "Venster sluiten",
                         font= ('Raleway', 12),
                         bg= 'blue',
                         fg= 'white',
                         command=root.destroy)
    knopsluiten.pack(side=RIGHT, pady=10, padx=10)

    root.mainloop()
