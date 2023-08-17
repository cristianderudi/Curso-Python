""" Ejercicio 035
Existen dos reglas que identifican dos conjuntos de valores:

a) El número es de un solo dígito.
b) El número es impar.

A partir de estas reglas, escribir un programa que permita ingresar un número entero.
Debe asignar el valor que corresponda a las variables booleanas:
esDeUnSoloDigito
esImpar
estaEnAmbos
noEstaEnNinguno

el valor Verdadero o Falso, según corresponda, para indicar si el valor número ingresado pertenece o no a cada conjunto. 
Definir un lote de prueba de varios números y probar el algoritmo, escribiendo los resultados. """

lote_de_prueba = [-5, 0, 3, 9, 10, 11, 15, 20]

for numero_entero in lote_de_prueba:


    if numero_entero % 2 == 1:
        esImpar = True
    else:
        esImpar = False

    if abs(numero_entero) < 10:
        esDeUnSoloDigito = True
    else:
        esDeUnSoloDigito = False

    if esImpar and esDeUnSoloDigito:
        estaEnAmbos = True
    else:
        estaEnAmbos = False

    if not esImpar and not esDeUnSoloDigito:
        noEstaEnNinguno = True
    else:
        noEstaEnNinguno = False

    print(f"Número {numero_entero}: Es de un solo digito = {esDeUnSoloDigito}, Es Impar = {esImpar}, Esta En Ambos = {estaEnAmbos}, No Esta En Ninguno = {noEstaEnNinguno}")