"""Archivo que contiene las clases NodoPaciente y ListaPacientes.
Para el manejo de los pacientes por medio de una lista enlazada simple.
"""

# Clase Nodo - representa un paciente en la lista
class NodoPaciente:
    def __init__(self, nombre, edad, sintoma, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma
        self.prioridad = prioridad
        self.siguiente = None # Puntero al siguiente nodo en la lista

# Clase ListaPacientes - gestiona la lista y sus operaciones
class ListaPacientes:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo paciente al final de la lista
    def insertar_paciente(self, nombre, edad, sintoma, prioridad):
        nuevo_paciente = NodoPaciente(nombre, edad, sintoma, prioridad)
        if not self.cabeza:
            # Si la lista está vacía, el nuevo paciente es la cabeza
            self.cabeza = nuevo_paciente
        else:
            # Recorre la lista hasta el último nodo y lo enlaza con el nuevo paciente
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_paciente

    # Mostrar el orden de atencion de los pacientes
    def mostrar_pacientes(self):
        actual = self.cabeza
        if not actual:
            print("No hay pacientes en la lista.")
            return
        print("Orden de atencion:")
        while actual:
            # Imprime los datos del paciente actual
            print(f"Nombre: {actual.nombre}, Edad: {actual.edad}, Sintoma: {actual.sintoma}, Prioridad: {actual.prioridad}")
            actual = actual.siguiente # Avanza al siguiente nodo

    # Eliminar al primer paciente de la lista (el que ya fue atendido)
    def atender_paciente(self):
        if not self.cabeza:
            print("No hay pacientes para atender.")
            return
        # Muestra el nombre del paciente que está siendo atendido
        print(f"Atendiendo al paciente: {self.cabeza.nombre}")
        # Cambia la cabeza al siguiente nodo, eliminando al actual
        self.cabeza = self.cabeza.siguiente