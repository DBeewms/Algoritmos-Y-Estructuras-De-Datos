"""Archivo que contiene el menu principal del programa."""

from clases import ListaPacientes

def menu():
    lista_pacientes = ListaPacientes()

    while True:
        print("\nMenu de opciones:")
        print("1. Insertar nuevo paciente")
        print("2. Mostrar lista de pacientes")
        print("3. Atender al siguiente paciente")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                nombre = input("Ingrese el nombre completo del paciente: ")
                edad = int(input("Ingrese la edad del paciente: "))
                sintoma = input("Ingrese el sintoma principal del paciente: ")
                prioridad = int(input("Ingrese la prioridad del paciente (1 a 5): "))
                lista_pacientes.insertar_paciente(nombre, edad, sintoma, prioridad)
                print(f"Paciente '{nombre}' ingresado al sistema.")
            case "2":
                lista_pacientes.mostrar_pacientes()
            case "3":
                lista_pacientes.atender_paciente()
            case "4":
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion no valida. Intente de nuevo.")