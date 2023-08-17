""" Ejercicio 043
Escribir un programa que lea números enteros hasta que se la suma de éstos sea mayor que 100, y muestre la cantidad de números ingresados. """



enteros = [] # Crea una lista vacía llamada enteros para almacenar los números enteros ingresados por el usuario.
suma = 0 # Inicializa una variable llamada suma en 0 para llevar un registro de la suma de los números ingresados por el usuario.
while suma <= 100: # Inicia un bucle while que continúa hasta que la suma de los números ingresados sea mayor que 100.
    num = int(input("Ingrese un numero: ")) # Dentro del bucle while, esta línea lee un número entero del usuario y lo almacena en una variable llamada num
    enteros.append(num) # Agrega el número ingresado por el usuario a la lista enteros
    suma += num # Actualiza la variable suma sumando el número ingresado por el usuario.
cantidad = len(enteros) # Después de que el bucle while haya terminado, esta línea calcula la cantidad de números ingresados utilizando la función len() en la lista enteros

print(f"La cantidad de numeros ingresados es: {cantidad}") # Muestra la cantidad de números ingresados
