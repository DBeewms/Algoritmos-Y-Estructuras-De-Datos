# Ejemplo 1
edad = int(input("Introduce tu edad: "))
if edad >= 16:
    print("Mayor de edad")

# Ejemplo 2
precio = float(input("Introduce el precio del producto: "))
if precio <= 1000:
    descuento = precio * 0.10

monto = precio - descuento
print("El monto a pagar es C$: ", monto)

# Ejemplo 3

dia = int(input("Introduce el día de la semana: "))
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("No valido")

# Ejemplo 4

usuario = input("Introduce tu usuario: ")
usuario = usuario.upper();

if usuario == "DOCENTE":
    print("Bienvenido docente")
    password = input("Introduce tu contraseña: ".upper())
    if password.upper() == "ABC123":
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario incorrecto")