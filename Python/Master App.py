import requests
import xmltodict

def tijden_ophalen(station, taal):
    authdetails = ('sam.zandee@gmail.com', 'PR15gnkYhlxUuWrjXFnZ_yBHswBfR-clw1oYMkbMW7eeeNLD0sGd5A')
    apiurl = "http://webservices.ns.nl/ns-api-avt?station=" + station

    response = requests.get(apiurl, auth=authdetails)

    vertrekXML = xmltodict.parse(response.text)

    nuttige_info = ""

    if taal == "NL":
        for vertek in vertrekXML["ActueleVertrekTijden"]["VertrekkendeTrein"]:
            if "VertrekVertragingTekst" not in vertek:
                nuttige_info += "De trein naar {} vertrekt om {} op spoor {}.\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16], vertek["VertrekSpoor"]["#text"])
            else:
                nuttige_info += "De trein naar {} vertrekt om {} {} op spoor {}.\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16], vertek["VertrekVertragingTekst"], vertek["VertrekSpoor"]["#text"])
    else:
        for vertek in vertrekXML["ActueleVertrekTijden"]["VertrekkendeTrein"]:
            if "VertrekVertragingTekst" not in vertek:
                nuttige_info += "The train to {} leaves at {} on platform {}.\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16], vertek["VertrekSpoor"]["#text"])
            else:
                nuttige_info += "The train to {} leaves at {} {} on platform {}.\n".format(vertek["EindBestemming"], vertek["VertrekTijd"][11:16], vertek["VertrekVertragingTekst"], vertek["VertrekSpoor"]["#text"])
    print(nuttige_info)
    return nuttige_info

#tijden_ophalen("ut", "NL") #om te proberen
