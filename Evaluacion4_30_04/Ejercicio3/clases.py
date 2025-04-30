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
                print(actual.dato, end="")
                actual = actual.siguiente
            print()

    def esta_vacia(self):
        return self.tope is None

def Convbinario(numero):
    pila = Pila()

    # Convertir el número a binario usando una pila
    while numero > 0:
        residuo = numero % 2
        pila.push(residuo)
        numero //= 2

    # Imprimir el número binario desde la pila
    print("Numero en binario: ", end="")
    pila.imprimir()