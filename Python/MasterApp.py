import requests
import xmltodict
import doctest

def stationsLijst():
    """Deze functie doet een request naar de ns api. Het response van de api wordt geparst,
    daarna worden de stations opgeslagen in een lijst."""

    # Inlog gegevens als variable
    inlogegevens = ('sam.zandee@gmail.com', 'PR15gnkYhlxUuWrjXFnZ_yBHswBfR-clw1oYMkbMW7eeeNLD0sGd5A')
    # Aanroepen van het ns stations xml
    stationsVanAPI = 'http://webservices.ns.nl/ns-api-stations-v2'
    responseStationLijst = requests.get(stationsVanAPI, auth=inlogegevens)

    # parsen van de tekst naar een variable
    stationsNamen = xmltodict.parse(responseStationLijst.text)
    checkWelkStation = stationsNamen['Stations']['Station']
    # lijst aanmaken waar de stations in komen
    lijstVanStations = []
    for station in checkWelkStation:
        # Korte namen van de stations toevoegen
        lijstVanStations.append(station['Code'])
        lijstVanStations.append(station['Namen']['Kort'])
        lijstVanStations.append(station['Namen']['Middel'])
        lijstVanStations.append(station['Namen']['Lang'])

    return lijstVanStations


def tijden_ophalen(station, taal):
    """Deze functie wordt gebruikt om de vertrektijden van het ingevoerde station op te vragen
    met de ns api. Deze informatie wordt vervolgens weer teruggegeven
    """

    # Inlogegevens
    authdetails = ('sam.zandee@gmail.com', 'PR15gnkYhlxUuWrjXFnZ_yBHswBfR-clw1oYMkbMW7eeeNLD0sGd5A')
    # De url die nodig is wordt bepaald door het station er aan te plakken
    apiurl = "http://webservices.ns.nl/ns-api-avt?station=" + station

    # De reactie wordt opgevraagt
    response = requests.get(apiurl, auth=authdetails)
    # De reactie wordt geparst
    vertrekXML = xmltodict.parse(response.text)

    nuttige_info = ""
    # Hij kijkt wat de meegegeven taal is en slaat de informatie van elke vertrekkende trein in die taal op met een for loop.
    if taal == "NL":
        for vertrek in vertrekXML["ActueleVertrekTijden"]["VertrekkendeTrein"]:
            if "VertrekVertragingTekst" not in vertrek:
                nuttige_info += "De trein naar {} vertrekt om {} op spoor {}.\n".format(vertrek["EindBestemming"], vertrek["VertrekTijd"][11:16], vertrek["VertrekSpoor"]["#text"])
            else:
                nuttige_info += "De trein naar {} vertrekt om {} {} op spoor {}.\n".format(vertrek["EindBestemming"], vertrek["VertrekTijd"][11:16], vertrek["VertrekVertragingTekst"], vertrek["VertrekSpoor"]["#text"])
    else:
        for vertrek in vertrekXML["ActueleVertrekTijden"]["VertrekkendeTrein"]:
            if "VertrekVertragingTekst" not in vertrek:
                nuttige_info += "The train to {} departs at {} on platform {}.\n".format(vertrek["EindBestemming"], vertrek["VertrekTijd"][11:16], vertrek["VertrekSpoor"]["#text"])
            else:
                nuttige_info += "The train to {} departs at {} {} on platform {}.\n".format(vertrek["EindBestemming"], vertrek["VertrekTijd"][11:16], vertrek["VertrekVertragingTekst"], vertrek["VertrekSpoor"]["#text"])
    return nuttige_info


def tijden_ophalenv2(station, taal):
    """
    Deze functie dot feitelijk het zelfde als tijden_ophalen() behalve dat hij de vertrektijden eerst in een  nested list zet
    en daarna met die list de nuttige info returned
    """

    # Inlogegevens
    authdetails = ('sam.zandee@gmail.com', 'PR15gnkYhlxUuWrjXFnZ_yBHswBfR-clw1oYMkbMW7eeeNLD0sGd5A')
    # De url die nodig is wordt bepaald door het station er aan te plakken
    apiurl = "http://webservices.ns.nl/ns-api-avt?station=" + station

    # De reactie wordt opgevraagt
    response = requests.get(apiurl, auth=authdetails)
    # De reactie wordt geparst
    vertrekXML = xmltodict.parse(response.text)

    rijstijdenlist = [],[],[]

    # Hij slaat hier voor elke vertrekkende trein of die het attribuut VertrekVertragingsTekst heeft en zet dan de info van die trein in een nested list
    for vertrek in vertrekXML["ActueleVertrekTijden"]["VertrekkendeTrein"]:
        if  "VertrekVertragingTekst" not in vertrek:
            rijstijdenlist[0].append(vertrek["EindBestemming"])
            rijstijdenlist[1].append(vertrek["VertrekTijd"][11:16])
            rijstijdenlist[2].append(vertrek["VertrekSpoor"]["#text"])
        else:
            rijstijdenlist[0].append(vertrek["EindBestemming"])
            rijstijdenlist[1].append(vertrek["VertrekTijd"][11:16] + " " + vertrek["VertrekVertragingTekst"])
            rijstijdenlist[2].append(vertrek["VertrekSpoor"]["#text"])

    nuttige_info = ""
    # Hij kijkt hier wat de taal is, voegt de info in die taal toe aan een string met een for loop en returned die dan.
    if taal == "NL":
        for index in range(0, len(rijstijdenlist[0])):
            nuttige_info += "De trein naar {} vertrekt om {} op spoor {}.\n".format(rijstijdenlist[0][index], rijstijdenlist[1][index], rijstijdenlist[2][index])
    else:
        for index in range(0, len(rijstijdenlist[0])):
            nuttige_info += "The train to {} departs at {} on platform {}.\n".format(rijstijdenlist[0][index], rijstijdenlist[1][index], rijstijdenlist[2][index])

    return nuttige_info
