""" 
Uso de Lista Enlazada con Logica de Pila
Ordenamiento de una lista de numeros, 
primero numeros pares, y luego impares 
en la misma lista
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
            print("La pila está vacía.")
        else:
            actual = self.tope
            while actual is not None:
                print(actual.dato, end=" ")
                actual = actual.siguiente
            print()

    def esta_vacia(self):
        return self.tope is None

def separarParImpar(pila):
    pila_pares = Pila()
    pila_impares = Pila()

    # Separar los elementos en dos pilas
    while not pila.esta_vacia():
        elemento = pila.pop()
        if elemento % 2 == 0:
            pila_pares.push(elemento)
        else:
            pila_impares.push(elemento)

    # Reconstruir la pila original con pares en la parte inferior
    while not pila_pares.esta_vacia():
        pila.push(pila_pares.pop())

    while not pila_impares.esta_vacia():
        pila.push(pila_impares.pop())

    return pila