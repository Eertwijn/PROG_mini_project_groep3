stations = ["Arnhem","Utrecht","Amsterdam"]

def station_Kiezen():
    invoer_station = input("Is dit uw huidige station? ")
    station = ""
    if invoer_station == "Nee":
        while station not in stations:
            station = input("Geef het station waar u zich bevindt: ")
    else:
        station = "Utrecht"
    return station

print("U heeft",station_Kiezen(),"aangegeven.")
