""" Ejercicio 025
Para acceder a cierta atracción, alcanza con que se cumpla solamente una de las siguientes condiciones: 
ser mayor de 6 años o medir más de 1,50 metros.
Escribir un programa en Python que solicite al usuario su edad y estatura, y que determine si cumple con los requisitos para subir a la atracción. 
Si cumple con al menos una de las condiciones, el programa debe imprimir "¡Puede acceder!" en la pantalla. 
Si no cumple con ninguna de las condiciones, el programa debe imprimir un mensaje que lo indique. """

EDAD_MINIMA_PARA_ENTRAR = 6
ESTATURA_MINIMA_PARA_ENTRAR = 1.5

edad = int(input("Edad: "))
estatura = float(input("Estatura: "))

if edad > EDAD_MINIMA_PARA_ENTRAR or estatura > ESTATURA_MINIMA_PARA_ENTRAR:
    print("Puede acceder!")
else:
    print("Lo siento, no cumple con los requisitos para la atraccion")
    