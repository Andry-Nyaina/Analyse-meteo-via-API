import requests

ville = input("Entrer votre ville que vous souhaitez regarder la meteo : ")
url = f"https://wttr.in/{ville}?format=j1"
r = requests.get(url).json()

print("Température actuelle:", r["current_condition"][0]["temp_C"], "°C")