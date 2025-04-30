"""
Archivo para el manejo de los metodos mediante un menu
"""

from clases import Convbinario

def mostrar_menu():
    print("=== Menu de Opciones ===")
    print("1. Convertir un numero a binario")
    print("2. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                numero = int(input("Ingrese un numero entero: "))
                Convbinario(numero)

            case "2":
                print("Saliendo del programa...")
                break

            case _:
                print("Opcion no valida. Intente nuevamente.")