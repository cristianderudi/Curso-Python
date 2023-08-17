""" Ejercicio 024
Para acceder a cierta atracción, es necesario cumplir con dos requisitos: 
- tener al menos 10 años de edad y medir más de 1,60 metros.

(Ojo, tener en cuenta las palabras: más, al menos y sobre todo la letra y)
Escribir un programa en Python que solicite al usuario su edad y estatura, y que determine si cumple con los requisitos para subir a la atracción. 
Si cumple con ambos requisitos, el programa debe imprimir "¡Puede acceder!" en la pantalla. 
Si no cumple con alguno de los requisitos, el programa debe imprimir un mensaje que indique el motivo por el cual no puede subir. 
Por ejemplo, si no cumple con el requisito de la edad, el programa debe imprimir "Lo siento, eres demasiado joven para acceder." 
Si no cumple con el requisito de la estatura, el programa debe imprimir "Lo siento, eres demasiado bajo para acceder" """


EDAD_MINIMA_PARA_ENTRAR = 10
ESTATURA_MINIMA_PARA_ENTRAR = 1.6

edad = int(input("Edad: "))
estatura = float(input("Estatura: "))

"""entra_por_edad = edad >= EDAD_MINIMA_PARA_ENTRAR
entra_por_estatura = estatura > ESTATURA_MINIMA_PARA_ENTRAR
entra = entra_por_edad and entra_por_estatura"""

if edad >= EDAD_MINIMA_PARA_ENTRAR and estatura > ESTATURA_MINIMA_PARA_ENTRAR:
    print("Entraste!!!")
else:
    if edad < EDAD_MINIMA_PARA_ENTRAR:
        print("Lo siento, eres demasiado joven para acceder.")
    if estatura <= ESTATURA_MINIMA_PARA_ENTRAR:
        print("Lo siento, eres demasiado bajo para acceder.")

