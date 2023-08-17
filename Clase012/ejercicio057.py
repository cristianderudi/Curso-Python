"""
Ejercicio 057
Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo.
Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
Cantidad de alumnos que aprobaron (nota >= 4).
Cantidad de alumnos que desaprobaron el examen (nota < 4).
Porcentaje de alumnos que están aplazados (nota == 1).
"""

#"999"
# 012
"123"
"-000123"
"-123"
"123-"
"123.3"


def es_numero_entero(cadena):
    index = 0
    while index < len(cadena):
#        if (index == 0 and cadena[index] == '-') or  (cadena[index] in "0123456789"):
        if (index != 0 or cadena[index] != '-') and (cadena[index] not in "0123456789"):
            return False
        index += 1
    
    return True



def leer_entero(mensaje):
    todo_ok = False
    while not todo_ok:
        cadena = input(mensaje)
        if es_numero_entero(cadena):
            todo_ok = True
        else:
            print(f"{cadena} No es un numero")
    
    return int(cadena)


def main():
    legajo = leer_entero("Legajo: ")
    while legajo != -1:
        nota = leer_entero("Nota: ")

        legajo = leer_entero("Legajo: ")



main()




