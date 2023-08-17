
def leer_entero(texto):

    n = input(texto)
    while not n.isnumeric():
        print(f"{n} No es un numero entero.")
        n = input(texto)

    return int(n)

def main():
    a = leer_entero("CUANTAS PATAS TIENE SU GATO? ")


main()

