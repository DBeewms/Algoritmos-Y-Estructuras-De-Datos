class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.cabeza = None  # Nodo de donde se extrae
        self.cola = None    # Nodo donde se agrega

    def estaVacia(self):
        return self.cabeza is None

    def agregar(self, item):
        nuevo = Nodo(item)
        if self.estaVacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo

    def avanzar(self):
        if self.estaVacia():
            raise Exception("La cola está vacía")
        valor = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.cola = None
        return valor

    def tamano(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador