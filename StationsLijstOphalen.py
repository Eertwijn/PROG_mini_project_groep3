import requests
import xmltodict


def stationsLijst():

    #inlog gegevens als variable
    inlogegevens = ('sam.zandee@gmail.com', 'PR15gnkYhlxUuWrjXFnZ_yBHswBfR-clw1oYMkbMW7eeeNLD0sGd5A')

    stationsVanAPI = 'http://webservices.ns.nl/ns-api-stations-v2'
    responseStationLijst = requests.get(stationsVanAPI, auth=inlogegevens)

    stationsNamen = xmltodict.parse((responseStationLijst.text))
    checkWelkStation = stationsNamen['Stations']['Station']
    lijstVanStations = []
    for station in checkWelkStation:
        lijstVanStations.append(station['Namen']['Kort'])
    #print(lijstVanStations)
    return(lijstVanStations)
print(stationsLijst())
