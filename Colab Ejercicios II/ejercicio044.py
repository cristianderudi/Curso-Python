""" Ejercicio 044
Escribir un programa que permita leer dos números A y B (enteros positivos). 
Calcular el producto A * B por sumas sucesivas e imprimir el resultado.
Ejemplo:
4*3 = 4 + 4 + 4 (4 sumado 3 veces).
3*4 = 3 + 3 + 3 + 3 (3 sumado 4 veces). """


A = int(input("Ingrese un entero positivo A: "))
B = int(input("Ingrese un entero positivo B: "))

# Se inicializa la variable producto en 0 para almacenar el resultado del producto de A y B
producto = 0
# Se inicializa la variable suma como una cadena vacía para almacenar la representación de la suma sucesiva
suma = ""
# Se itera B veces
for i in range(B):
    # En cada iteración, se suma A al producto acumulado
    producto += A
    # También se agrega A a la cadena suma
    suma += str(A)
    # Si no es la última iteración, se agrega el símbolo "+" a la cadena suma
    if i < B - 1:
        suma += " + "

# Finalmente, se imprime el resultado en el formato especificado
print(f"{A} * {B} = {suma} ({A} sumado {B} veces) = {producto}")



""" # Otro metodo
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
sum = 0
positivos = a > 0 and b > 0
if positivos:
  print(f"{a} x {b} = {a}", end='')
  cont = 1
  sum += a
  while cont < b:
    sum += a
    print(f" + {a}", end='')
    cont += 1
  print(f" = {sum}")
else:
  print("Ambos numeros deben ser positivos") """