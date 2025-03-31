"""5. Se desea escribir un programa para el cálculo del área de diversas superficies: cuadrado, 
rectángulo, círculo, triángulo y trapecio. El programa mostrará al inicio el siguiente menú:
Seguidamente leerá de la entrada estándar un valor que estará comprendido entre 1 y 5, indicando 
el tipo de superficie cuya área se desea calcular.  El programa leerá entonces los datos que necesite 
para calcular el área en cuestión.  El resultado se mostrará en la salida estándar, tras lo cual el programa terminará.

-	Implementa estructuras repetitivas de tal forma que los programas se ejecuten mientras el usuario lo desea.
"""

import math

while True:
    print("\n--- Calculo del area de diversas superficies ---")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Circulo")
    print("4. Triangulo")
    print("5. Trapecio")
    
    opcion = input("Seleccione una opcion (1-5): ")
    
    match opcion:
        case "1":
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = lado * lado
            print(f"El area del cuadrado es: {area:.2f}")
        case "2":
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            area = base * altura
            print(f"El area del rectangulo es: {area:.2f}")
        case "3":
            radio = float(input("Ingrese el radio del circulo: "))
            area = math.pi * radio * radio
            print(f"El area del circulo es: {area:.2f}")
        case "4":
            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            area = (base * altura) / 2
            print(f"El area del triangulo es: {area:.2f}")
        case "5":
            base_mayor = float(input("Ingrese la base mayor del trapecio: "))
            base_menor = float(input("Ingrese la base menor del trapecio: "))
            altura = float(input("Ingrese la altura del trapecio: "))
            area = ((base_mayor + base_menor) * altura) / 2
            print(f"El area del trapecio es: {area:.2f}")
        case _:
            print("Opcion invalida. Por favor, seleccione una opcion entre 1 y 5.")
    
    continuar = input("\nDesea realizar otra operacion? (s/n): ").strip().lower()
    if continuar != 's':
        print("Gracias por usar el programa. Hasta luego!")
        break