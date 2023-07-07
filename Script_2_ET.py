import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "jFIgZ3TQ2erpdzCYtfjKzkYd1a03j7jb"

while True:
    orig = input("Indique la ciudad de origen: ")
    if orig == "salir" or orig == "s":
        break
    dest = input("Indique la ciudad de destino: ")
    if dest == "salir" or orig == "s":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    print("--------------------------------------------\n")
    if json_status == 0:
        distance_km = round(json_data["route"]["distance"] * 1.61, 2)
        duration = json_data["route"]["formattedtime"]
        combustible = round((json_data["route"]["distance"]* 1.61) / 10)
        print("La distancia entre ciudades es de: {:.1f}".format(distance_km),"km")
        print("La duracion del viaje es de: "+ duration,"Hrs")
        print("El combustible utilizado es :{:.1f}".format(combustible),"Ltrs\n")
        print("-----------------------------------------\n")
        print("Indicaciones de como llegar:\n")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"])+ " (" + str("{:.1f}".format((each["distance"])*1.61 ) + "km"))
        print("------------------------------------------\n")
    elif json_status == 402:
        print("--------------------------------------")
        print("status code: " + str(json_status)+ ": Invalid user inputs for one or both location")
        print("--------------------------------------")
    elif json_status == 611:
        print("--------------------------------------")
        print("Status Code: "+ str(json_status)+ ": missing an entry for one or both locations.")
        print("--------------------------------------")
    else:
        print("----------------------------------------")
        print("For staus code: " + str(json_status)+ ": reder to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("---------------------------------------\n")