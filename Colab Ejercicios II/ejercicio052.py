""" Ejercicio 052
Escribir un programa que permita ingresar la estatura (en metros con decimales) de cada jugador de un equipo de baloncesto. 
La carga finalizará al ingresar cero. 
Calcular y mostrar la estatura promedio del equipo. """



alturas_ingresadas = []
while True:
    altura_jugador = float(input("Altura de Jugador : "))
    if altura_jugador == 0:
        break
    alturas_ingresadas.append(altura_jugador)
suma = 0
contador = 0
for estatura in alturas_ingresadas:
    suma += estatura
    contador += 1

promedio = suma / contador
print(f"La estatura promedio de los altura_jugador es de {promedio}")
