""" Ejercicio 036
Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/'). 
Debe mostrarse el resultado para la operación ingresada. 
Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR'). """



num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))

operacion = input("Ingrese tipo de operacion (+) (-) (*) (/) : ")

if operacion == '+':
    print(f"La suma entre {num1} y {num2} es= {num1 + num2}")

elif operacion == '-':
    print(f"La resta entre {num1} y {num2} es= {num1 - num2}")

elif operacion == '*':
    print(f"La multiplicacion entre {num1} y {num2} es= {num1 * num2}")

elif operacion == '/':
    if num2 == 0:
        print(f"ERROR, no se puede dividir por cero")
    else:
        print(f"La division entre {num1} y {num2} es= {round(num1 / num2)}")
else:
    print("ERROR, operacion no valida!")