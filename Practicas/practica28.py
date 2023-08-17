""" Ejercicio 028
Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). 
Verificar que el mes sea válido e informar en caso que no lo sea. """

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

while True:
    mes = int(input("Ingrese numero de mes (0 para salir): "))
    if mes == 0:
        break
    if 1 <= mes <= 12:
        print(f"El mes es: {meses[mes-1]}")
    else:
        print(f"El numero ingresado es incorrecto")
print("Hasta luego!")
