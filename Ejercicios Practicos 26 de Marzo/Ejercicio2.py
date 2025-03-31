"""2. Escribir un programa que permita emitir la FACTURA correspondiente, a una compra de un artículo determinado
, del que se adquieren una o varias unidades. El IVA a aplicar es de 15% y si el Sub Total (precio de venta por cantidad),
 es mayor de 1000, se aplicará un descuento del 12%."""

import random

continuar = True
IVA = 0.15
descuento = 0.12

while continuar:
    producto = input("¿Que producto desea comprar? ").upper()
    cantidad = input("¿Cuantas unidades del producto desea comprar? ")

    if cantidad.isdigit():
        cantidad = int(cantidad)
        precio = random.randrange(300, 502, 2)
        subtotal = cantidad * precio
        IVACalculado = subtotal * IVA
        descuentoAplicado = 0.0
        descuentoBool = False

        if subtotal > 1000:
            descuentoAplicado = subtotal * descuento
            subtotal -= descuentoAplicado
            descuentoBool = True

        total = subtotal + IVACalculado

        print("="*30)
        print("="*10, " FACTURA ", "="*10)
        print("PRODUCTO: ", producto)
        print("CANTIDAD: ", cantidad)
        print("PRECIO UNITARIO: ", precio)
        print("SUBTOTAL: ", subtotal)
        if descuentoBool:
            print("DESCUENTO: -", descuentoAplicado)
        print("IVA: ", IVACalculado)
        print("TOTAL: ", total)
        print("="*30)
    else:
        print("Cantidad invalida.")

    continuar = input("¿Desea realizar otra compra? (s/n): ").strip().lower()
    if continuar != 's':
        break