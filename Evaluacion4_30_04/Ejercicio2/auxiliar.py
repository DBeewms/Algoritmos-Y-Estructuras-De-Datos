"""
Archivo para el manejo de los metodos mediante un menu
"""

from clases import Pila, ordena

def mostrar_menu():
    print("=== Menu de Opciones ===")
    print("1. Insertar elementos en la pila")
    print("2. Ordenar la pila de mayor a menor")
    print("3. Mostrar pila")
    print("4. Salir")

def ejecutar_menu():
    pila = Pila()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                elementos = input("Ingrese los elementos separados por comas: ")
                for elemento in elementos.split(","):
                    pila.push(int(elemento.strip()))
                print("Elementos insertados correctamente.")

            case "2":
                pila = ordena(pila)
                print("Pila ordenada de mayor (fondo de la pila) a menor (top de la pila).")

            case "3":
                print("Contenido de la pila:")
                pila.imprimir()

            case "4":
                print("Saliendo del programa...")
                break

            case _:
                print("Opcion no valida. Intente nuevamente.")