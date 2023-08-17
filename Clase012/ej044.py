"""
Ejercicio 044
Escribir un programa que permita leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e imprimir el resultado.
Ejemplo:
4*3 = 4 + 4 + 4 (4 sumado 3 veces).
3*4 = 3 + 3 + 3 + 3 (3 sumado 4 veces).
"""

def potencia(b,e):
    prod = 1
    for x in range(e):
        prod *= b
    return prod

def multiplicar(a,b):
    resultado = 0
    while b > 0:
        resultado += a
        b-=1
    return resultado

def multiplicar1(a,b):
    resultado = 0
    for x in range(b):
        resultado += a
    return resultado


def main():
    a = 2
    b = 8
    r =  multiplicar1(a,b)
    print(f"Multiplicar1 {a} * {b} = {r}")
    r =  multiplicar(a,b)
    print(f"multiplicar {a} * {b} = {r}")
    print(f"{a}^{b} = {potencia(a,b)}")

main()

