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


def tijden_ophalen(station):
    authdetails = ('sam.zandee@gmail.com', 'PR15gnkYhlxUuWrjXFnZ_yBHswBfR-clw1oYMkbMW7eeeNLD0sGd5A')
    apiurl = "http://webservices.ns.nl/ns-api-avt?station=" + station

    response = requests.get(apiurl, auth=authdetails)

    vertrekXML = xmltodict.parse(response.text)

    nuttige_info = ""

    for vertek in vertrekXML["ActueleVertrekTijden"]["VertrekkendeTrein"]:
        if "VertrekVertragingTekst" not in vertek:
            nuttige_info += "De trein naar {} vertrekt om {} op spoor {}.\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16], vertek["VertrekSpoor"]["#text"])
        else:
            nuttige_info += "De trein naar {} vertrekt om {} {} op spoor {}.\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16], vertek["VertrekVertragingTekst"], vertek["VertrekSpoor"]["#text"])

    print (nuttige_info)

station = station_Kiezen(lijstVanStations)
tijden_ophalen(station)
