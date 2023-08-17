""" Ejercicio 028
Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). 
Verificar que el mes sea válido e informar en caso que no lo sea. """

""" import random """

""" numero_mes = int(input("Numero de mes: "))
# numero_mes = random.randint(1,12)

if numero_mes == 1:
    nombre = "Enero"
elif numero_mes == 2:
    nombre = "Febrero"
elif numero_mes == 3:
    nombre = "Marzo"
elif numero_mes == 4:
    nombre = "Abril"
elif numero_mes == 5:
    nombre = "Mayo"
elif numero_mes == 6:
    nombre = "Junio"
elif numero_mes == 7:
    nombre = "Julio"
elif numero_mes == 8:
    nombre = "Agosto"
elif numero_mes == 9:
    nombre = "Septiembre"
elif numero_mes == 10:
    nombre = "Octubre"
elif numero_mes == 11:
    nombre = "Noviembre"
elif numero_mes == 12:
    nombre = "Diciembre"
else:
    nombre = "Error"

print(f"Numero del mes: {numero_mes}\nNombre del mes: {nombre} ") """


meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
while True:
    mes = int(input("Ingrese un número de mes (0 para salir): "))
    if mes == 0:
        break
    if 1 <= mes <= 12:
        print(f"El mes es: {meses[mes-1]}")
    else:
        print("El mes ingresado no es válido")
        