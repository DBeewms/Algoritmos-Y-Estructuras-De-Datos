class Estudiante:
    def __init__(self):
        self.nombre = ""
        self.edad = 0  
        self.carrera = ""
        self.calificaciones = []
    
    
    def agregar_calificacion(self, nota):
        if 100 >= nota >= 0:
            self.calificaciones.append(nota)
            self.promedio = self.promedio()
        else:
            print("La nota debe estar entre 0 y 100.")

    
    def promedio(self):
        sumatoria = 0
        numero_calificaciones = len(self.calificaciones)
        
        if numero_calificaciones > 0:
            
            for i in range(numero_calificaciones):
                self.calificaciones[i] += sumatoria
            
            return sumatoria / numero_calificaciones
        else:
            return 0
    
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        
        if self.calificaciones:
            print(f"Calificaciones: {self.calificaciones}")
            print(f"Promedio: {self.promedio():.2f}")
        else:
            print("No hay calificaciones registradas.")
            
            
    def mostrar_estudiantes(self, estudiantes):
        for estudiante in estudiantes:
            estudiante.mostrar_info()
            print("=" * 30)
            
    
    def buscar_estudiante(self, estudiantes, nombre):
        for estudiante in estudiantes:
            if estudiante.nombre == nombre:
                return estudiante
        return None
        
        
    