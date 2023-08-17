"""
Ejercicio 035
Existen dos reglas que identifican dos conjuntos de valores:

a) El número es de un solo dígito.
b) El número es impar.

A partir de estas reglas, escribir un programa que permita ingresar un número entero.
Debe asignar el valor que corresponda a las variables booleanas:
esDeUnSoloDigito
esImpar
estaEnAmbos
noEstaEnNinguno
el valor Verdadero o Falso, según corresponda, para indicar si el valor número ingresado pertenece o no a cada conjunto. Definir un lote de prueba de varios números y probr el algoritmo, escribiendo los resultados.


esDeUnSoloDigito: True
esImpar: True
estaEnAmbos: True
noEstaEnNinguno: False

"""

numero = 7



# a) El número es de un solo dígito.
esDeUnSoloDigito = 0 <= numero <= 9 # numero >= 0 and numero <= 9
esDeUnSoloDigito = numero >= 0 and numero <= 9 # 0 <= numero <= 9

# b) El número es impar.
esImpar =   (numero%2)  !=  0

print(f"Numerop: {numero}")
print(f"esDeUnSoloDigito: {esDeUnSoloDigito}")
print(f"esImpar: {esImpar}")

estaEnAmbos = esDeUnSoloDigito and esImpar
noEstaEnNinguno = not esDeUnSoloDigito or not esImpar
#noEstaEnNinguno = not (esDeUnSoloDigito and esImpar)
print(f"estaEnAmbos: {estaEnAmbos}")
print(f"noEstaEnNinguno: {noEstaEnNinguno}")

numero >= 0 and numero <= 9 and (numero%2)  !=  0

"""
a > b or m == 3 and j != 0
a <= b and m!= 3 or j == 0
"""
