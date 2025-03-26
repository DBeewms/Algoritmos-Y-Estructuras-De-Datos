"""1. Desarrolla un programa que calcule el importe a pagar por un vehículo al circular por una autopista. 
El vehículo puede ser una bicicleta, una moto, un carro o un camión. Para definir el conjunto de vehículos 
deben utilizar una estructura adecuada. El importe se calculará según los siguientes datos:

a) Un importe fijo de 100 córdobas para la bicicleta.
b) Las motos y los carros pagarán 30 córdobas por Km.
c) Los camiones pagarán 30 córdobas por Km. más 25 córdobas por toneladas.
"""
continuar = True

while continuar:
    vehiculo = input("Introduce el tipo de vehiculo (bicicleta, moto, carro, camion): ").lower()
    distancia = 0
    toneladas = 0

    if vehiculo == "moto" or vehiculo == "carro" or vehiculo == "camion":
        distancia = float(input("Introduce la distancia recorrida (en KM): "))
    if vehiculo == "camion":
        toneladas = float(input("Introduce el peso del camion en toneladas: "))

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
            print("Tipo de vehiculo no valido")

    if importe > 0:
        print(f"El importe a pagar por el vehiculo {vehiculo} es: {importe} cordobas")

    print("Desea continuar?")
    if input("S/N: ").upper() == "S":
        continuar = True
    else:
        continuar = False
