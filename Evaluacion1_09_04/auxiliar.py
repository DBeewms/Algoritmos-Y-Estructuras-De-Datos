def menu():
    opcion = int(input(
        "Bienvenido. Escoge una opcion:\n"
        "1. Registrar nuevo estudiante.\n"
        "2. Agregar calificacion a un estudiante.\n"
        "3. Mostrar informacion a un estudiante.\n"
        "4. Mostrar todos los estudiantes.\n"
        "5. Salir del programa.\n"
    ))
    return opcion

def validar_edad(edad):
    if edad > 0:
        return edad
    else:
        print("El valor ingresado no es valido.")
    