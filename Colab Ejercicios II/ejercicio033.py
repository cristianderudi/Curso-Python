""" Ejercicio 033
La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:
Menor de 5500.0 el descuento es del 4.5%  
- ### Entre5500.0 y 10000.0 el descuento es del 8%  
- ### Más de10000.0 el descuento es del 10.5%
Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios. """

DESCUENTO_MINIMO = 4.5
DESCUENTO_MEDIO = 8
DESCUENTO_MAX = 10.5

importe = float(input("Ingrese importe: "))

if importe < 5500.0:
    descuento = importe * DESCUENTO_MINIMO / 100
    precio_neto = importe - descuento
    print(f"Descuento del {DESCUENTO_MINIMO}%: ${round(descuento, 2)}")
    print(f"El precio neto es: ${precio_neto}")

elif importe >= 5500.0 and importe < 10000.0:
    descuento = importe * DESCUENTO_MEDIO / 100
    precio_neto = importe - descuento
    print(f"Descuento del {DESCUENTO_MEDIO}%: ${round(descuento, 2)}")
    print(f"El precio neto es: ${precio_neto}")
    
else:
    descuento = importe * DESCUENTO_MAX / 100
    precio_neto = importe - descuento
    print(f"Descuento del {DESCUENTO_MAX}%: ${round(descuento, 2)}")
    print(f"El precio neto es: ${precio_neto}")
