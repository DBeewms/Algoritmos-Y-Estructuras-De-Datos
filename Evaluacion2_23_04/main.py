#Ejemplificando la creación de una lista enlazada simple

# Clase Nodo - representa un nodo de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo valor al final de la lista
    # Implementacion de colas
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            
    # Insertar un nuevo valor al inicio de la lista
    # Implementacion de pilas
    def insertar_al_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente

        return False  # Valor no encontrado

    # Método para buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False
    
    # Método que cuenta el número de nodos en la lista
    def longitudLista(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    # Método que imprime los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
        
"""Esta línea asegura que el siguiente bloque solo se ejecuta si el archivo se corre directamente, y no cuando es importado como módulo en otro archivo"""
if __name__ == "__main__":
    lista = ListaEnlazada()  #Creando el objeto lista
    
    while True:
        print("\nMenú de opciones:")
        print("1. Insertar al inicio (Pilas)")
        print("2. Insertar al final (Colas)")
        print("3. Contar longitud de la lista")
        print("4. Imprimir la lista")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                valor = input("Ingrese el valor a insertar al inicio: ")
                lista.insertar_al_inicio(valor)
                print(f"Valor '{valor}' insertado al inicio.")
            case "2":
                valor = input("Ingrese el valor a insertar al final: ")
                lista.insertar(valor)
                print(f"Valor '{valor}' insertado al final.")
            case "3":
                longitud = lista.longitudLista()
                print(f"La longitud de la lista es: {longitud}")
            case "4":
                print("Contenido de la lista:")
                lista.imprimir()
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
