"""
- 28) Dada una lista de números, crear una función que devuelva 
la suma acumulada de los números en la lista 
(cada elemento de la nueva lista debe ser la suma de todos los 
números anteriores, incluyendo el número actual).
"""

def func(lista:list)->list:
    nueva = []

    for index in range(len(lista)):
        suma = 0
        for x in range(0,index+1):
            suma += lista[x]
        nueva.append(suma)



    return nueva





def main():
    lista = [2,8,7,41,9,63,7]

    nueva = func(lista)
    print(lista)
    print(nueva)



main()