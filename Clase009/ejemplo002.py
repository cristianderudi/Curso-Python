"""

5 5 5 5 2 2 2 2 2 2 2 2 2 2 2 2 2 8 8 8 8 8 3 3 3 3 3 3 3 7 4 4 4 0

1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 7 7 7 7 7 9 9 9 9 9 9 9 9 0


"""
cant_numeros = 0
numero = int(input("Numero: "))
while numero != 0: # FIN DE DATOS    
    numero_proceso = numero
    repet = 0
    while numero != 0 and numero_proceso == numero: # FIN DE DATOS Y EL MISMO NUMERO   
        repet += 1
        # cant_numeros += 1
        numero = int(input("Numero: "))
    # FIN NUMERO 
    print(f'Numero: {numero_proceso} Rep: {repet}')
    cant_numeros += repet
# FIN DE DATOS    
print(f"Cantidad: {cant_numeros} ")