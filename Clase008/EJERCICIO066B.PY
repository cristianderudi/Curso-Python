"""
## Ejercicio 066b

La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene 
en sus estantes. Para cada uno de los estantes (usando 'F' para indicar el fin de los estantes), 
se deben ingresar 15 libros, y para cada libro, se debe ingresar su nombre, 
género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y 
cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, 
se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su 
cantidad correspondiente. 
Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de 
libros por género.
"""
CANT_LIBROS_POR_ESTANTE = 2
tot_i=0
tot_h =0
tot_n =0
estante = input("Estante: ").upper()
while estante != 'F':
    print(f"Proceso el estante {estante}")

    mayor_cant_p = 0
    nombre_libro_mayor = ""
    for numero_libro in range(CANT_LIBROS_POR_ESTANTE):
        nombre = input("Nombre: ")
        
        genero = input("genero:\nN: Novela\nI: Infantil\nHistoria : ").upper()
        while genero not in ('N','I','H'):
            print("Error en el genero")
            genero = input("genero:\nN: Novela\nI: Infantil\nHistoria : ").upper()

        cant_p = int(input("Cant de p: "))

        if genero == 'I':
            tot_i += 1
        elif genero == 'H':
            tot_h += 1
        else:
            tot_n += 1


        if cant_p > mayor_cant_p:
            mayor_cant_p = cant_p
            nombre_libro_mayor = nombre

    # FIN FOR (FIN ESTANTE)
    print(
        f"Estante: {estante} Libro con mas p: {nombre_libro_mayor} con {mayor_cant_p}")

    estante = input("Estante: ").upper()
# FIN WHILE
print(f"Total H: {tot_h}")
print(f"Total I: {tot_i}")
print(f"Total N: {tot_n}")
