""" Ejercicio 048
Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter por cada una la operación a realizar 
('+', '-', '*', '/', 'F') y dos números enteros en el caso que no haya elegido 'F'. 
La computadora debe mostrar el resultado para la operación ingresada. 
Considerar que no se puede dividir por cero. 
Cuando la operación ingresada sea 'F' nos indicará que no se desean calcular más operaciones. """


""" 
while True:
    while True:
        simbolo = input("Ingrese operacion matematica ('+')('-')('*')('/')('F' finalizar): ").upper()
        if simbolo in ['+', '-', '*', '/', 'F']:
            break
        else:
            print("Operacion no valida. Ingrese operacion matematica.")
    if simbolo == 'F':
        print("Hasta luego")
        break
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese un numero: "))
    if simbolo == '+':
        suma = numero1 + numero2
        print(f"La suma de los numeros es: {suma}")
    elif simbolo == '-':
        resta = numero1 - numero2
        print(f"La resta de los numeros es: {resta}")
    elif simbolo == '*':
        multiplicacion = numero1 * numero2
        print(f"La multiplicacion de los numeros es: {multiplicacion}")
    elif simbolo == '/':
        if numero2 == 0:
            print("No se puede dividir por cero!")
        else:
            division = numero1 / numero2
            print(f"La division de los numeros es: {division}") """

op = (input("Ingrese la operacion a realizar entre dos numeros: +|-|*|/ (F para salir)): ")).upper()
while op != 'F':
  while op!= '+' and op!= '-' and op != '*' and op != '/':
    op = (input("La operacion ingresada es incorrecta, reingrese +|-|*|/ :")).upper()
  num1 = int(input("Ingrese el primer numero: "))
  num2 = int(input("Ingrese el segundo numero: "))
  if op == '+':
    rdo = num1 + num2
  elif op == '-':
    rdo = num1 - num2
  elif op == '*':
    rdo = num1 * num2
  elif op == '/' and num2 == 0:
    print("ERROR - No es posible dividir por cero")
    rdo = 'ERROR'
  else:
    rdo = num1 / num2
  print(f"{num1} {op} {num2} = {rdo}")
  op = (input("Ingrese la operacion a realizar entre ambos: +|-|*|/ (F para salir)): ")).upper()
print("Usted ha salido del programa")
