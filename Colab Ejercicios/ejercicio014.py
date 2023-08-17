""" Ejercicio 014
Escribir un programa que permita al usuario ingresar el ancho y largo de un terreno en metros, junto con el valor del metro cuadrado de tierra. 
El programa debe calcular y mostrar el valor total del terreno. 
Además, debe calcular la cantidad de metros de alambre necesarios para cercar completamente el terreno a tres alturas distintas.
Pensando los pasos para resolver el problema:

1. Solicitar al usuario que ingrese el ancho del terreno en metros y almacenarlo en una variable. ✓
2. Solicitar al usuario que ingrese el largo del terreno en metros y almacenarlo en otra variable. ✓
3. Solicitar al usuario que ingrese el valor del metro cuadrado de tierra y almacenarlo en otra variable. ✓
4. Calcular el valor total del terreno multiplicando el ancho por el largo y luego multiplicando el resultado por el valor del metro cuadrado de tierra. ✓
6. Mostrar el valor total del terreno al usuario. ✓

7. Calcular la cantidad de metros de alambre necesarios para cercar el terreno a tres alturas distintas. 
   Por ejemplo, se puede calcular la cantidad de alambre necesaria para cercar a 1 metro de altura, a 2 metros de altura y a 3 metros de altura. 
   Para hacerlo, se debe sumar el perímetro del terreno (2 veces el ancho más 2 veces el largo) y luego multiplicarlo por la cantidad de alturas. 
8. Mostrar la cantidad de metros de alambre necesarios para cercar el terreno a las tres alturas distintas al usuario. """

# Solicitar al usuario que ingrese el ancho del terreno en metros y almacenarlo en una variable.
ancho = float(input("Ingrese el ancho del terreno en metros: ")) 
#Solicitar al usuario que ingrese el largo del terreno en metros y almacenarlo en otra variable.
largo = float(input("Ingrese el largo del terreno en metros: "))
# Solicitar al usuario que ingrese el valor del metro cuadrado de tierra y almacenarlo en otra variable.
valor = float(input("Ingrese el valor del metro cuadrado: "))

valor_total = ancho * largo * valor
print(f"El valor total del terreno es: $ {round(valor_total)}")

alambre_1 = (2 * ancho + 2 * largo) * 1 # Cantidad de alambre para cercar a 1 metro de altura
alambre_2 = (2 * ancho + 2 * largo) * 2 # Cantidad de alambre para cercar a 2 metros de altura
alambre_3 = (2 * ancho + 2 * largo) * 3 # Cantidad de alambre para cercar a 3 metros de altura

print(f"La cantidad de metros de alambre necesarios para cercar el terreno a 1 metro de altura es: {alambre_1} m")
print(f"La cantidad de metros de alambre necesarios para cercar el terreno a 2 metros de altura es: {alambre_2} m")
print(f"La cantidad de metros de alambre necesarios para cercar el terreno a 3 metros de altura es: {alambre_3} m")
