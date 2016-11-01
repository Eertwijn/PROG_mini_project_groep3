import requests
import xmltodict

def stationsLijst():
    """Deze functie doet een request naar de ns api. Het response van de api wordt geparst.
    Daarna worden de stations opgeslagen in een lijst. Deze lijst wordt meegegeven aan station_Kiezen()"""

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
        lijstVanStations.append(station['Namen']['Kort'])

    return(lijstVanStations)
#De uitkomst van stationsLijst() wordt opgeslagen als variable
lijstVanStations = stationsLijst()



def station_Kiezen(lijstVanStations):
    """Hier wordt aan de gebruiker gevraagt waar hij/zij is. Daarna wordt gekeken het station bestaat.
    Als dat het geval is wordt het station opgeslagen. Is dit niet het geval, dan wordt er opnieuw gevraagt
    of op welk station ze zijn."""
    #Er wordt gevraagt of utrecht het huidige station is
    invoer_station = input("Is dit uw huidige station(Utrecht Centraal)? ")
    station = ""
    #als Utrecht niet het huidige station is wordt er gevraagt waar de persoon zich bevindt
    if invoer_station == "Nee":
        while station not in lijstVanStations:
            station = input("Geef het station waar u zich bevindt: ")
    else:
        station = "Utrecht"
    #Het ingevoerde station wordt geprint en teruggegeven.
    print("U heeft",station,"aangegeven.")

    return station


def tijden_ophalen(station):
    """Deze functie wordt gebruikt om de de vertrektijden van het ingevoerde station op te vragen
    van de ns api. Deze informatie wordt vervolgens weer teruggegeven"""

    #inlogegevens
    authdetails = ('sam.zandee@gmail.com', 'PR15gnkYhlxUuWrjXFnZ_yBHswBfR-clw1oYMkbMW7eeeNLD0sGd5A')
    #de url die nodig is wordt bepaald door het station er aan te plakken
    apiurl = "http://webservices.ns.nl/ns-api-avt?station=" + station

    #de reactie wordt opgevraagt
    response = requests.get(apiurl, auth=authdetails)
    #de reactie wordt geparst
    vertrekXML = xmltodict.parse(response.text)

    nuttige_info = ""
    #De vertrektijden worden opgezocht en op geslagen in nuttige_info=""
    for vertek in vertrekXML["ActueleVertrekTijden"]["VertrekkendeTrein"]:
        if "VertrekVertragingTekst" not in vertek:
            nuttige_info += "De trein naar {} vertrekt om {} op spoor {}.\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16], vertek["VertrekSpoor"]["#text"])
        else:
            nuttige_info += "De trein naar {} vertrekt om {} {} op spoor {}.\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16], vertek["VertrekVertragingTekst"], vertek["VertrekSpoor"]["#text"])
    #de vertrektijden worden uitgeprint
    print (nuttige_info)

#Het ingoeverde station uit station_Kiezen wordt opgeslagen als variable
station = station_Kiezen(lijstVanStations)
#Van Het ingevoerde station worden de tijden opgehaald.
tijden_ophalen(station)
