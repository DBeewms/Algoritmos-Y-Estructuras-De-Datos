"""
Desarrolla un programa que calcule el importe a pagar por un vehiculo
al circular por una autopista. El vehiculo puede ser una bicicleta, un
carro o un camion. Para definir el conjunto de vehiculos deben utilizar 
una estructura adecuada. El importe se calculara segun los siguientes datos.

a) Un importe fijo de 100 cordobas para la bicicleta.
b) Las motos y los carros pagaran 30 cordobaspor KM.
c) Los camiones pagaran 30 cordobas por KM mas 25 cordobas por tonelada.
"""

# Solicitud de datos al usuario
vehiculo = input("Introduce el tipo de vehiculo (bicicleta, moto, carro, camion): ").lower()
distancia = 0
toneladas = 0

if vehiculo == "moto" or vehiculo == "carro" or vehiculo == "camion":
    distancia = float(input("Introduce la distancia recorrida (en KM): "))
if vehiculo == "camion":
    toneladas = float(input("Introduce el peso del camión en toneladas: "))

# Cálculo del importe
importe = 0

match vehiculo:
    case "bicicleta":
        importe = 100
    case "moto":
        importe = 30 * distancia
    case "carro":
        importe = 30 * distancia
    case "camion":
        importe = 30 * distancia + 25 * toneladas
    case _:
        print("Tipo de vehículo no válido")

if importe > 0:
    print(f"El importe a pagar por el vehículo {vehiculo} es: {importe} cordobas")