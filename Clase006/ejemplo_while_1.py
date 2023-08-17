
"""
Leer numeros hasta que se ingrese un cero.
Mostrar la suma

lista1 ==> 1,5,4,7,8,9,5,4,1,7,8,5,1,0
lista2 ==> 1,5,4,8,5,1,0
lista3 ==> 0
"""

import random

# ANTES (PARA TODOS)
sumador = 0 
contador = 0
numero = random.randint(0,1000)
while numero != 0:
    # DURANTE (PARA CADA DATO)   
    
    sumador += numero # sumador = sumador + numero
    contador += 1 # contador = contador + 1 
    
    numero = random.randint(0,1000)
# DESPUES (TOTALES)
print(f"La cantidad de numeros es: {contador}\nLa suma es: {sumador}")







