import auxiliar
import estudiante

def main():
    estudiante1 = estudiante.Estudiante()
    lista_estudiantes = []
    
    while True:
        opcion = auxiliar.menu()
        match opcion:
            case 1:
                print("Registrando estudiante...")
                estudiante1.nombre = input("Ingresa el nombre del estudiante: ")
                estudiante1.edad = int(input("Ingresa la edad del estudiante: "))
                estudiante1.carrera = input("Ingresa la carrera del estudiante: ")
                
                lista_estudiantes.append(estudiante1)
            case 2:
                print("Agregando calificacion a estudiante...")
                nombre = input("Escribe el nombre de estudiante para agregar la calificacion... ")
                estudiante1 = estudiante.Estudiante.buscar_estudiante(estudiante1, lista_estudiantes, nombre)
                estudiante1.mostrar_info()
                nota = int(input("Escribe la nota a ingresar... "))
                estudiante1.agregar_calificacion(nota)
            case 3:
                nombre = input("Escribe el nombre de estudiante para buscarlo dentro de la base de datos... ")
                estudiante1 = estudiante.Estudiante.buscar_estudiante(estudiante1, lista_estudiantes, nombre)
                estudiante1.mostrar_info()
            case 4:
                estudiante.Estudiante.mostrar_estudiantes(estudiante1, lista_estudiantes)
            case 5:
                break
            
            

if __name__ == "__main__":
    main()