"""El siguiente ejemplo imprimirá los dos primeros números impares de la lista: 1 y 3."""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
contador = 0
for impar in numeros:
    if not impar % 2:
        continue
    print(impar)
    contador += 1
    if contador == 2:     # Aca definimos la cantidad de numeros impar a mostrar, en este caso (1, 3)
        break