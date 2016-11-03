import requests
import xmltodict


def stationsLijst():
    """Deze functie doet een request naar de ns api. Het response van de api wordt geparst.
    Daarna worden de stations opgeslagen in een lijst. Deze lijst wordt meegegeven aan station_Kiezen()"""

    # Inlog gegevens als variable
    inlogegevens = ('sam.zandee@gmail.com', 'PR15gnkYhlxUuWrjXFnZ_yBHswBfR-clw1oYMkbMW7eeeNLD0sGd5A')
    # Aanroepen van het ns stations xml
    stationsVanAPI = 'http://webservices.ns.nl/ns-api-stations-v2'
    responseStationLijst = requests.get(stationsVanAPI, auth=inlogegevens)
    # parsen van de tekst naar een variable
    stationsNamen = xmltodict.parse((responseStationLijst.text))
    checkWelkStation = stationsNamen['Stations']['Station']
    # lijst aanmaken waar de stations in komen
    lijstVanStations = []
    for station in checkWelkStation:
        # Korte namen van de stations toevoegen
        lijstVanStations.append(station['Namen']['Kort'])

    return(lijstVanStations)


def tijden_ophalen(station, taal):
    """Deze functie wordt gebruikt om de de vertrektijden van het ingevoerde station op te vragen
    van de ns api. Deze informatie wordt vervolgens weer teruggegeven"""

    # Inlogegevens
    authdetails = ('sam.zandee@gmail.com', 'PR15gnkYhlxUuWrjXFnZ_yBHswBfR-clw1oYMkbMW7eeeNLD0sGd5A')
    # De url die nodig is wordt bepaald door het station er aan te plakken
    apiurl = "http://webservices.ns.nl/ns-api-avt?station=" + station

    # de reactie wordt opgevraagt
    response = requests.get(apiurl, auth=authdetails)
    # De reactie wordt geparst
    vertrekXML = xmltodict.parse(response.text)

    nuttige_info = ""
    # Hij kijkt wat de meegegeven taal is en slaat de informatie van elke vertrekkende trein in die taal op met een for loop.
    if taal == "NL":
        for vertek in vertrekXML["ActueleVertrekTijden"]["VertrekkendeTrein"]:
            if "VertrekVertragingTekst" not in vertek:
                nuttige_info += "De trein naar {} vertrekt om {} op spoor {}.\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16], vertek["VertrekSpoor"]["#text"])
            else:
                nuttige_info += "De trein naar {} vertrekt om {} {} op spoor {}.\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16], vertek["VertrekVertragingTekst"], vertek["VertrekSpoor"]["#text"])
    else:
        for vertek in vertrekXML["ActueleVertrekTijden"]["VertrekkendeTrein"]:
            if "VertrekVertragingTekst" not in vertek:
                nuttige_info += "The train to {} departs at {} on platform {}.\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16], vertek["VertrekSpoor"]["#text"])
            else:
                nuttige_info += "The train to {} departs at {} {} on platform {}.\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16], vertek["VertrekVertragingTekst"], vertek["VertrekSpoor"]["#text"])
    return nuttige_info
