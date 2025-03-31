"""3. Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% 
por la compra de más de 3 docenas y 10% en caso contrario. Además, por la compra de más de 3 docenas se obsequia 
una unidad del producto por cada docena en exceso sobre 3. Diseñe un programa que determine el monto de la compra, 
el monto del descuento, el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de 
docenas del producto."""

while True:
    print("\n--- Supermercado - Cálculo de compra mayorista ---")
    
    precio_por_docena = float(input("Ingrese el precio por docena del producto: "))
    cantidad_docenas = int(input("Ingrese la cantidad de docenas que desea comprar: "))

    monto_compra = precio_por_docena * cantidad_docenas

    if cantidad_docenas > 3:
        descuento = monto_compra * 0.15
        unidades_obsequio = cantidad_docenas - 3
    else:
        descuento = monto_compra * 0.10
        unidades_obsequio = 0

    monto_a_pagar = monto_compra - descuento

    print("\n--- Resultados de la compra ---")
    print(f"Monto de la compra: ${monto_compra:.2f}")
    print(f"Monto del descuento: ${descuento:.2f}")
    print(f"Monto a pagar: ${monto_a_pagar:.2f}")
    print(f"Unidades de obsequio: {unidades_obsequio}")

    continuar = input("\n¿Desea realizar otra operacion? (s/n): ").strip().lower()
    if continuar != 's':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break