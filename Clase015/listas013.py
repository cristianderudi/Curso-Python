"""
Dada una lista de números, eliminar todos los elementos 
repetidos y mostrar la lista resultante.
"""
from random import randint

def crear_lista(cantidad,min,max,tipo):
    lis = []
   
    for x in range(cantidad):
        if tipo is str:
            lis.append(f"******{randint(min,max)}******")
        else:
            lis.append(randint(min,max))
    return lis

def crearlistacadenas(cantidad,min,max):
    lis = []
   
    for x in range(cantidad):
        lis.append(f"******{randint(min,max)}******")
    return lis


def desrepetir(lista):
    
    return list(   set(    lista   )    )



def main():
    lista = crearlistacadenas(20,1,10)
    if isinstance(lista[0],str):
        print("lista de cadenas: ",lista)
    else:
        print("lista de enteros: ",lista)
    lista = desrepetir(lista)
    print(lista)
    print(type(str))
    
    
main()