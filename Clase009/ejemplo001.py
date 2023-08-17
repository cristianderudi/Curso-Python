"""
mostrar la suma de cada subsec


1 4 -5 7 0 -1 

1 4 -1 7 0 -1 

8 4 0 4 7 8 5 6 9 0 0 0 0 1 0 1 4 5 7 8 0 -1

0 -1

"""
mayor_suma_sub = -float('inf')
suma_tot = 0
numero = int(input("Numero: "))
while numero != -1: # FIN DE DATOS
    suma_sub = 0
    while numero != 0: # FIN DE SUB SEC
        suma_sub += numero
        suma_tot += numero
        numero = int(input("Numero: "))
    # FIN WHILE
    print(f"Suma Sub: {suma_sub}")
    if suma_sub > mayor_suma_sub:
        mayor_suma_sub = suma_sub
    # OTRA FORMA ==> suma_tot += suma_sub
    numero = int(input("Numero: "))
# FIN WHILE
print(f"Suma total: {suma_tot}")
print(f"La suma sub mayor es: {mayor_suma_sub} ")





