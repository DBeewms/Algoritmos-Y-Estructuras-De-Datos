"""
Archivo para el manejo de los métodos mediante un menú
"""

from clases import Pila, separarParImpar

def mostrar_menu():
    print("=== Menú de Opciones ===")
    print("1. Insertar elementos en la pila")
    print("2. Separar pares e impares")
    print("3. Mostrar pila")
    print("4. Salir")

def ejecutar_menu():
    pila = Pila()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                elementos = input("Ingrese los elementos separados por comas: ")
                for elemento in elementos.split(","):
                    pila.push(int(elemento.strip()))
                print("Elementos insertados correctamente.")

            case "2":
                pila = separarParImpar(pila)
                print("Pila separada en pares e impares.")

            case "3":
                print("Contenido de la pila:")
                pila.imprimir()

            case "4":
                print("Saliendo del programa...")
                break

            case _:
                print("Opción no válida. Intente nuevamente.")