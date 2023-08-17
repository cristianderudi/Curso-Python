


import random


def validar_nota(nota):
    return nota < 0 or nota > 10


def programa():
    2/0
    print(random.__name__)
    nota = int(input("Nota: ")) 
    while validar_nota(nota):
        print(type(nota).__name__)
        print("error")
        nota = int(input("Nota: ")) 



programa()







