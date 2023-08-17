"""
Leer numeros hasta que se ingrese un cero.
Mostrar la suma

lista1 ==> 1,5,4,7,8,9,5,4,1,7,8,5,1,0
lista2 ==> 1,5,4,8,5,1,0
lista3 ==> 0
"""

# ANTES (PARA TODOS)
sumador = 0 
numero = int(input("Numero: "))
while numero != 0:
    # DURANTE (PARA CADA DATO)   
    
    sumador += numero # sumador = sumador + numero
    
    numero = int(input("Numero: "))
# DESPUES (TOTALES)
print(f"La suma es: {sumador}")


