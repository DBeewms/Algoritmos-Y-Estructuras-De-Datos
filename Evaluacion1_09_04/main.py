import auxiliar
import estudiante


def registrar_estudiante(lista_estudiantes):
    print("Registrando estudiante...")
    nuevo_estudiante = estudiante.Estudiante()
    nuevo_estudiante.nombre = input("Ingresa el nombre del estudiante: ")
    nuevo_estudiante.edad = int(input("Ingresa la edad del estudiante: "))
    nuevo_estudiante.carrera = input("Ingresa la carrera del estudiante: ")
    lista_estudiantes.append(nuevo_estudiante)
    print("Estudiante registrado exitosamente.")


def agregar_calificacion(lista_estudiantes):
    print("Agregando calificación a estudiante...")
    nombre = input("Escribe el nombre del estudiante para agregar la calificación: ")
    estudiante_encontrado = buscar_estudiante(lista_estudiantes, nombre)
    if estudiante_encontrado:
        nota = int(input("Escribe la nota a ingresar: "))
        estudiante_encontrado.agregar_calificacion(nota)
        print("Calificación agregada exitosamente.")
    else:
        print("Estudiante no encontrado.")


def buscar_estudiante(lista_estudiantes, nombre):
    for estudiante in lista_estudiantes:
        if estudiante.nombre.lower() == nombre.lower():
            return estudiante
    return None


def mostrar_estudiantes(lista_estudiantes):
    print("Mostrando todos los estudiantes...")
    if lista_estudiantes:
        for estudiante in lista_estudiantes:
            estudiante.mostrar_info()
            print("=" * 30)
    else:
        print("No hay estudiantes registrados.")



def main():
    lista_estudiantes = []
    
    while True:
        opcion = auxiliar.menu()
        match opcion:
            case 1:
                registrar_estudiante(lista_estudiantes)
            case 2:
                agregar_calificacion(lista_estudiantes)
            case 3:
                print("Buscando estudiante...")
                nombre = input("Escribe el nombre del estudiante para buscarlo: ")
                estudiante_encontrado = buscar_estudiante(lista_estudiantes, nombre)
                if estudiante_encontrado:
                    estudiante_encontrado.mostrar_info()
                else:
                    print("Estudiante no encontrado.")
            case 4:
                mostrar_estudiantes(lista_estudiantes)
            case 5:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")

            
            


if __name__ == "__main__":
    main()