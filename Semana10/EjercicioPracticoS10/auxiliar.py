from clases_colas import Cola
from clases_pilas import Pila

def procesar_cola(cola, pila):
    cola_aux = Cola()
    n = cola.tamano()  # se obtiene el tamaño inicial
    for indice in range(n):
        elemento = cola.avanzar()  # se extrae de la cola original
        if indice % 2 == 0:         # posición par: se guarda en la cola auxiliar
            cola_aux.agregar(elemento)
        else:                       # posición impar: se transfiere a la pila
            pila.push(elemento)
    # Se reasigna la cola auxiliar a la cola original
    cola.cabeza = cola_aux.cabeza
    cola.cola = cola_aux.cola

def mostrar_cola(cola):
    print("Contenido de la cola:", end=" ")
    actual = cola.cabeza
    while actual:
        print(actual.dato, end=" ")
        actual = actual.siguiente
    print("")

def mostrar_pila(pila):
    print("Contenido de la pila:", end=" ")
    actual = pila.tope
    while actual:
        print(actual.dato, end=" ")
        actual = actual.siguiente
    print("")

def agregar_elemento(cola):
    dato = input("Ingrese un elemento para la cola: ")
    cola.agregar(dato)
    print("Elemento agregado.")

def menu_principal():
    cola = Cola()
    pila = Pila()

    while True:
        print("\nMenú:")
        print("1. Agregar elemento a la cola")
        print("2. Procesar cola (trasladar elementos impares a la pila)")
        print("3. Mostrar cola")
        print("4. Mostrar pila")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_elemento(cola)
        elif opcion == "2":
            if cola.estaVacia():
                print("La cola está vacía, no se puede procesar.")
            else:
                procesar_cola(cola, pila)
                print("Procesamiento finalizado.")
        elif opcion == "3":
            mostrar_cola(cola)
        elif opcion == "4":
            mostrar_pila(pila)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")