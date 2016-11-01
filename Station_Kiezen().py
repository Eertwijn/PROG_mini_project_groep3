#stations = ["Arnhem","Utrecht","Amsterdam"]
import requests
import xmltodict

def stationsLijst():

    #inlog gegevens als variable
    inlogegevens = ('sam.zandee@gmail.com', 'PR15gnkYhlxUuWrjXFnZ_yBHswBfR-clw1oYMkbMW7eeeNLD0sGd5A')
    #Aanroepen van het ns stations xml
    stationsVanAPI = 'http://webservices.ns.nl/ns-api-stations-v2'
    responseStationLijst = requests.get(stationsVanAPI, auth=inlogegevens)
    #parsen van de tekst naar een variable
    stationsNamen = xmltodict.parse((responseStationLijst.text))
    checkWelkStation = stationsNamen['Stations']['Station']
    #lijst aanmaken waar de stations in komen
    lijstVanStations = []
    for station in checkWelkStation:
        #Korte namen van de stations toevoegen
        lijstVanStations.append(station['Code'])
        lijstVanStations.append(station['Namen']['Kort'])
    #print(lijstVanStations)
    return(lijstVanStations)
lijstVanStations = stationsLijst()



def station_Kiezen(lijstVanStations):
    invoer_station = input("Is dit uw huidige station? ")
    station = ""

    if invoer_station == "Nee":
        while station not in lijstVanStations:
            station = input("Geef het station waar u zich bevindt: ")
    else:
        station = "Utrecht"
    print("U heeft",station,"aangegeven.")

    return station

