"""
La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. 
Para cada uno de los estantes (usando 'F' para indicar el fin del estante), se deben ingresar los libros, 
y para cada libro, se debe ingresar su nombre (usando 'FIN' si no hay más libros para ese estante), género 
(usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). 
Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro 
con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos 
los estantes, se deben mostrar la cantidad de libros por género y el promedio de libros por estante.
"""

# ANTES DE ESTANTES
tot_i = 0
tot_h = 0
tot_n = 0

estante = input("* Estante: ").upper()

terminar_estante = False

while terminar_estante == False:
# DURANTE UN ESTANTE
    # ANTES DE UN LIBRO
    
    max_cant_p = -float('inf')
    
    print(f"Procesando estante {estante}.")
    
    nombre_libro = input("* Título: ").upper()        
    
    # DURANTE CADA LIBRO
    while nombre_libro != 'FIN':
        cant_p = int(input("* Cantidad de páginas: "))
        genero = input("* Genero: ").upper()
        while genero not in ('N','I','H'):
            print(f"Error: el género {genero} ingresado no es valido.")
            genero = input("* Genero: ").upper()            
        if genero == 'I':
            tot_i += 1
        elif genero == 'H':
            tot_h += 1
        else:                                
            tot_n += 1 
        # PARA CADA LIBRO DE CADA ESTANTE
        if cant_p > max_cant_p:
            max_cant_p = cant_p
            nombre_maximo = nombre_libro
        nombre_libro = input("* Título: ")
        
    # FIN DE LOS LIBROS DE UN ESTANTE
    print(f"El libro del estante {estante} con mas páginas es '{nombre_maximo}' y tiene {max_cant_p} páginas.")
    
    terminar_estante = input('Continua con siguiente estante? [S/N]: ').upper() == 'N'
    
    if not terminar_estante:
        estante = input("* Estante: ").upper()
    # El problema es que cuando pongo S (continuar con siguiente estante), me pone "Procesando estante A" de vuelta.   
    # Quiero que me pida nombre de nuevo estante y "Procesando estante B" (o el que defina yo).

informe = f"""
- INFORME DE BIBLIOTECA - 
* Total novela: {tot_n}
* Total historia: {tot_h}
* Total infantil: {tot_i}
"""
print(informe) 


