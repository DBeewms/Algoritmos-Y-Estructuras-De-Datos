#Ejercicio 6. Determina la edad de una persona

#Se importa la libreria para poder usar el tipo de dato Datetime
from datetime import datetime

FechaNac = input("Ingresa tu fecha de nacimiento con el formato yyyy-mm-dd: ")

#Convertimos la fecha que ingreso el usuario a Datetime
nacimiento = datetime.strptime(FechaNac, "%Y-%m-%d")

#obtenemos la fecha de hoy

hoy = datetime.now()

#Se calcula la edad
edad = hoy.year - nacimiento.year

#Condicional por si la persona aun no ha cumplido

#Se crea una tupla. Una tupla es una estructura de datos que guarda varios
#elementos en orden —como una lista— pero con una gran diferencia: es inmutable.
#Esto significa que una vez creada, no se puede modificar (no puedes agregar,
#eliminar o cambiar sus elementos).


if(hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
    edad -= 1

#La f antes de las comillas convierte la cadena en una f-string.
#Las llaves {} permiten insertar variables o expresiones directamente.
#El equivalente a $""
    
print(f"Tienes {edad} años")
