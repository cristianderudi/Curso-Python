"""
Ejercicio 011
Escribir un programa que permita resolver el siguiente problema:
Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).
Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido previamente."""


socio1 = (input("Ingrese nombre del primer socio: "))
socio2 = (input("Ingrese nombre del segundo socio: "))
socio3 = (input("Ingrese nombre del tercer socio: "))

capital_socio1 = int(input(f"Ingrese capital de {socio1}: "))
capital_socio2 = int(input(f"Ingrese capital de {socio2}: "))
capital_socio3 = int(input(f"Ingrese capital de {socio3}: "))

valor_total_aportado = capital_socio1 + capital_socio2 + capital_socio3

porcentaje_inversion_persona1 = round((capital_socio1 / valor_total_aportado) * 100, 2)
porcentaje_inversion_persona2 = round((capital_socio2 / valor_total_aportado) * 100, 2)
porcentaje_inversion_persona3 = round((capital_socio3 / valor_total_aportado) * 100, 2)

print(f"El total aportado por los socios es de $ {valor_total_aportado}")
print(f"El porcentaje aportado por {socio1} es de {porcentaje_inversion_persona1}%")
print(f"El porcentaje aportado por {socio2} es de {porcentaje_inversion_persona2}%")
print(f"El porcentaje aportado por {socio3} es de {porcentaje_inversion_persona3}%")