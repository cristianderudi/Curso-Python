""" Ejercicio 015
Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada, más el 5% del valor_adicional de esas ventas. 
Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes.
Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor_adicional total de las mismas.
¿Sobran datos? ¿Qué datos sobran? """


# Parámetros de la inmobiliaria
SALARIO_BASE = 150000
COMISION_FIJA = 500

# Datos de entrada
nombre_vendedor = input("Ingrese nombre del vendedor: ")
cantidad_ventas= int(input("Ingrese la cantidad de ventas que realizó: "))
valor_total_ventas = float(input("Ingrese el valor total de las ventas: "))

# Cálculo del salario
total_comisiones = COMISION_FIJA * cantidad_ventas
bono_ventas = valor_total_ventas * 0.05
salario_total = SALARIO_BASE + total_comisiones + bono_ventas

# Resultado
print(f"El salario de {nombre_vendedor} en este mes es de: ${round(salario_total)}")
