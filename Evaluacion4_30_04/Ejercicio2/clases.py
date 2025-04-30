"""
Archivo de metodos para las lista enlazada y manejo de datos
Usando logica de pilas
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None  # Inicia vacía

    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def pop(self):
        if self.tope is None:
            return None
        eliminado = self.tope.dato
        self.tope = self.tope.siguiente
        return eliminado

    def cima(self):
        if self.tope is None:
            return None
        return self.tope.dato

    def imprimir(self):
        if self.tope is None:
            print("La pila esta vacia.")
        else:
            actual = self.tope
            while actual is not None:
                print(actual.dato, end=" ")
                actual = actual.siguiente
            print()

    def esta_vacia(self):
        return self.tope is None

def ordena(pila):
    pila_aux = Pila()

    # Ordenar la pila usando una pila auxiliar
    while not pila.esta_vacia():
        temp = pila.pop()

        # Mover elementos menores de pila_aux de vuelta a pila
        while not pila_aux.esta_vacia() and pila_aux.cima() < temp:
            pila.push(pila_aux.pop())

        # Insertar el elemento en la posición correcta en pila_aux
        pila_aux.push(temp)

    # Transferir los elementos de pila_aux de vuelta a pila
    while not pila_aux.esta_vacia():
        pila.push(pila_aux.pop())

    return pila