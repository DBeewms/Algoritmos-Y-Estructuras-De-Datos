#Ejercicio 7. Calcular el total a pagar por la compra de articulos en una tienda
#Se sabe que el impuesto que se aplica es el 10% y se realiza un descuento del 5%
#sobre la compra
print("Ingrese el total a pagar para aplicarle el descuento de 5% luego calcular el IVA")

precio = float(input("Precio($): "))

precioConDescuento = precio - precio*0.05

precioTotalConImpuestos = precioConDescuento + precioConDescuento*0.10

# La f antes de las comillas convierte la cadena en una f-string.
#Las llaves {} permiten insertar variables o expresiones directamente.

print(f"Total a pagar: ${precioTotalConImpuestos:.2f}")
