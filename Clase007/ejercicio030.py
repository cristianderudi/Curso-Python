"""
Ejercicio 030

Escribir un programa que permita al usuario generar dos números enteros. 
La computadora debe indicar si el mayor es divisible por el menor. 

(Un número entero a es divisible por un número entero b cuando el 
resto de la división entre a y b es 0) 
"""

from random import randint



terminar = bool(False)
while not terminar:
    a = randint(1,100)
    b = randint(1,100)

    if a > b:
        es_div = (a%b) == 0
        resultado = f"{a} es div. por {b} ==> {es_div}"
    else:
        es_div = (b%a) == 0
        resultado = f"{b} es div. por {a} ==> {es_div}"

    
    
    
    if es_div == True:
        terminar = True

    print(resultado)