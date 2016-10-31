import requests
import xmltodict



#inlog gegevens als variable
inlogegevens = ('sam.zandee@gmail.com', 'PR15gnkYhlxUuWrjXFnZ_yBHswBfR-clw1oYMkbMW7eeeNLD0sGd5A')

stationsVanAPI = 'http://webservices.ns.nl/ns-api-stations-v2'
responseStationLijst = requests.get(stationsVanAPI, auth=inlogegevens)

stationsNamen = xmltodict.parse((responseStationLijst.text))
checkWelkStation = stationsNamen['Stations']['Station']

stationInput = input("Van welk station wil je informatie?(Vul de korte naam van het station in) ")

for kortenamen in checkWelkStation:
    while stationInput not in kortenamen['Namen']['Kort']:
        stationInput = input("Je station komt niet voor in onze database vul opnieuw in: ")
    else:
        code = kortenamen['Code'].lower()
        print(code)
        break



#Alle Ritten die van Utrecht Centraal komen ophalen(Gebruik van utrecht centraal gemaakt om code te testen)

VertrekUtrecht = 'http://webservices.ns.nl/ns-api-avt?station=' + code
#VertrekUtrecht[-1] = code
print(VertrekUtrecht)

#xml bestand ophalen van de api
responseEinstations = requests.get(VertrekUtrecht, auth=inlogegevens)

#Optionele code. Als het bestand opgeslagen moet worden.
#with open('VertrekUtrecht.xml', 'w') as XMLbestand:
#    XMLbestand.write(XMLvanNSapi.text)

#parsen van het Response uit de API
ResponseStationsXML = xmltodict.parse(responseEinstations.text)


bestemmingen = ResponseStationsXML['ActueleVertrekTijden']['VertrekkendeTrein']

print("EindBestemmingen vanaf ", kortenamen['Namen']['Kort'], ": \n")
for namen in bestemmingen:
    eindBestemmingen  = namen['EindBestemming']
    vertrekTijden = namen['VertrekTijd']

    #print("De trein naar ", eindBestemmingen,"vertrekt om", vertrekTijden[11:16])
    print("{}\t{}\t{}\t{}".format("De trein naar", eindBestemmingen,"vertrekt om", vertrekTijden[11:16]))

