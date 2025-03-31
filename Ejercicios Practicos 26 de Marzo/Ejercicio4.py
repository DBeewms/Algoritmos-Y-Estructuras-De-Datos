"""4. Diseñe un programa que lea un número de tres cifras y determine si es igual al revés del número."""

while True:
    print("\n--- Verificar si un numero de tres cifras es igual al reves ---")
    
    numero = input("Ingrese un numero de tres cifras: ")
    
    if len(numero) == 3 and numero.isdigit():
        numero_reves = numero[2] + numero[1] + numero[0]
        if numero == numero_reves:
            print(f"El numero {numero} es igual al reves.")
        else:
            print(f"El numero {numero} no es igual al reves.")
    else:
        print("Por favor, ingrese un numero valido de tres cifras.")

    continuar = input("\nDesea realizar otra operacion? (s/n): ").strip().lower()
    if continuar != 's':
        print("Gracias por usar el programa. Hasta luego!")
        break