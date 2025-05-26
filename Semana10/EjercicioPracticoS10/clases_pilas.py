class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def pop(self):
        if self.esta_vacia():
            return None
        valor = self.tope.dato
        self.tope = self.tope.siguiente
        return valor

    def cima(self):
        if self.esta_vacia():
            return None
        return self.tope.dato

    def esta_vacia(self):
        return self.tope is None