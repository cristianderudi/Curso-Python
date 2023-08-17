""" Ejercicio 050
Escribir un programa que permita validar la nota de un examen. 
Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.
La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.
Las notas 1 y 3 no usan nunca.
La nota 0 se reserva para los ausentes.
Las notas válidas pueden ser un 2 o un valor entre 4 y 10. """



while True:
    nota = float(input("Ingrese nota: "))
    if nota >= 0 and nota <= 10:
        if nota == 2 or (nota >= 4 and nota <= 10):
            print("La nota es valida")
            break
        if nota == 0:
            print("Nota reservada para ausentes")
        else:
            print("Las notas 1 y 3 no se usan")
            