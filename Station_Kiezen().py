stations = ["Arnhem","Utrecht","Amsterdam"]
def Station_Kiezen():
    keuze = input("Is dit uw huidige station? ")
    if keuze == "nee" or "no" or "Nee" or "No":
        nieuw_station = ""
        while nieuw_station not in stations:
            nieuw_station = input("Voer een station in: ")
    return station

Station_Kiezen()
