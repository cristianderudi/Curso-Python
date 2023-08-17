""" Ejercicio 034
Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del salario bruto por cada año de antigüedad. También se le realizan los siguientes descuentos:

* Jubilación: 11%
* Obra Social: 3%
* Sindicato: 3%

Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)
Estado Civil: Soltero/Casado Sueldo básico: $ 999.99 Antigüedad: 99 años

Descuentos:

* Jubilación - 999,99
* Obra Social - 999,99
* Sindicato - 999,99
Sueldo Neto 999,99 """

# Constantes
INCREMENTO_SOLTERO = 0.05
INCREMENTO_CASADO = 0.07
DESCUENTO_JUBILACION = 0.11
DESCUENTO_OBRA_SOCIAL = 0.03
DESCUENTO_SINDICATO = 0.03

# Entrada de datos
sueldo_basico = float(input("Ingrese sueldo básico: "))
antiguedad = int(input("Ingrese antigüedad en años: "))
estado_civil = input("Ingrese estado civil (S: Soltero / C: Casado): ").upper()

# Cálculo del incremento por antigüedad
if estado_civil == "S":
    incremento_antiguedad = sueldo_basico * INCREMENTO_SOLTERO * antiguedad
elif estado_civil == "C":
    incremento_antiguedad = sueldo_basico * INCREMENTO_CASADO * antiguedad

# Cálculo del salario bruto
salario_bruto = sueldo_basico + incremento_antiguedad

# Cálculo de los descuentos
descuento_jubilacion = salario_bruto * DESCUENTO_JUBILACION
descuento_obra_social = salario_bruto * DESCUENTO_OBRA_SOCIAL
descuento_sindicato = salario_bruto * DESCUENTO_SINDICATO

# Cálculo del sueldo neto
sueldo_neto = salario_bruto - descuento_jubilacion - descuento_obra_social - descuento_sindicato

# Salida de datos
print(f"Estado Civil: {'Soltero' if estado_civil == 'S' else 'Casado'}")
print(f"Sueldo básico: $ {sueldo_basico:.2f}")
print(f"Antigüedad: {antiguedad} años")
print("\nDescuentos:")
print(f"Jubilación - ${descuento_jubilacion:.2f}")
print(f"Obra Social - ${descuento_obra_social:.2f}")
print(f"Sindicato - ${descuento_sindicato:.2f}")
print(f"\nSueldo Neto ${sueldo_neto:.2f}")