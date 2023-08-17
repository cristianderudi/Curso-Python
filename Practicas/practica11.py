""" Ejercicio 011
Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).
Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido previamente. """




socio1 = (input("Ingrese primer nombre: "))
aporte_socio1 = int(input("Capital aportado: "))

socio2 = (input("Ingrese segundo nombre: "))
aporte_socio2 = int(input("Capital aportado:"))

socio3 = (input("Ingrese tercer nombre: "))
aporte_socio3 = int(input("Capital aportado: "))

aporte_total = aporte_socio1 + aporte_socio2 + aporte_socio3

porcentaje_socio1 = round((aporte_socio1 / aporte_total) * 100,2)
porcentaje_socio2 = round((aporte_socio2 / aporte_total) * 100,2)
porcentaje_socio3 = round((aporte_socio3 / aporte_total) * 100,2)

print(f"Valor total aportado por los socios: $ {aporte_total}")
print(f"Porcentaje aportado por {socio1}= % {porcentaje_socio1}")
print(f"Porcentaje aportado por {socio2}= % {porcentaje_socio2}")
print(f"Porcentaje aportado por {socio3}= % {porcentaje_socio3}")

