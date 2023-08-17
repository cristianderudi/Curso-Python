def print_letter_F(filas):
    for fila in range(filas):
        for col in range(filas):
            if col == 0 or (fila == 0 or fila == filas // 2):
                print("*", end = "")
            else:
                print(" ", end = "")
        print()

filas = int(input("Ingrese el numero de filas para la letra F: "))
print_letter_F(filas)