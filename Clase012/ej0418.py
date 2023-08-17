"""
Ejercicio 048
Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter por cada una la operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) y dos números enteros en el caso que no haya elegido ‘F’. La computadora debe mostrar el resultado para la operación ingresada. Considerar que no se puede dividir por cero. Cuando la operación ingresada sea ‘F’ nos indicará que no se desean calcular más operaciones.
"""


def isint(str_numero):
    try:
        int(str_numero)
    except:
        return False
    return True


def leer_entero(mensaje):
    todo_ok = False
    while not todo_ok:
        cadena = input(mensaje)
        if isint(cadena):
            todo_ok = True
        else:
            print(f"{cadena} No es un numero")    
    return int(cadena)

POSIBLES_OPERACIONES = ('+','-','*','/','F')


def main():
    op = ' '
    while op != 'F':
        op = input(f"Operacion {POSIBLES_OPERACIONES}: ").upper()
        
        a = leer_entero("Numero 1: ")
        b = leer_entero("Numero 2: ")
        if op == '+':
            r  = a + b
        elif op == '/':
            if b == 0:
                r = "Error"
            else:
                r = a/b
        print(f"{a} {op} {b} = {r}")        
        

main()