import requests
from urllib.parse import urlencode
import math

url = 'https://www.mapquestapi.com/directions/v2/route?'
apikey = input("Ingresar la API KEY: ")
inicio = input("Por Favor Ingresa Ciudad de Origen: ")
destino = input("Por Favor Ingresa Ciudad de Destino: ")

consulta = url + urlencode({"key":apikey, "from":inicio, "to":destino})
print(" ")
print("La URL es: ",consulta)
print(" ")
#print("[XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]")
#print("A partir de aquí sólo hay datos de consulta")

vis = requests.get(consulta).json()
numero0 = round(float(vis["route"]["distance"] * 1.609344), 1)

print("Consulta exitosa")
print(" ")
print("La distancia entre las dos ciudades en kilómetros es --> ", format(numero0, ), "km")

distancia_millas =vis["route"]["distance"]
distancia_kms = distancia_millas * 1.609344
consumo_litros_por_km = 0.12  # Valor de consumo promedio
combustible_requerido = round(distancia_kms * consumo_litros_por_km, 1)

numero1 = float(vis["route"]["realTime"] / 60)
numero2 = float(vis["route"]["realTime"] / 3600)
print("El tiempo en segundos es:                            --> ",vis["route"]["realTime"], "segundos")
print("El tiempo en minutos es:                             --> ", format(numero1, '.1f'), "minutos")
print("El tiempo en horas es:                             --> ", format(numero2, '.1f'), "horas")
print("Combustible requerido:", combustible_requerido, "litros")
print("################################################################################")
print("A partir de aquí sólo hay datos de narrative")
print("################################################################################")
narrative = vis['route']['legs'][0]['maneuvers']
for step in narrative:
    print(step['narrative'])