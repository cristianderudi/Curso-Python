""" 
Un animal en rehabilitación después de una cirugía requiere ser alimentado y 
monitoreado en un zoológico. Se alimenta 3 veces al día y, en cada tanda
de alimentación, se le da de comer hasta que ya no tenga ganas.
Por cada tanda de comida, se debe ingresar la cantidad de alimento en kg 
(número entero) que se le dio y se le debe preguntar al animal si quiere seguir 
comiendo ('S', 'N'). Se desea conocer:

A. Total de alimento recibido.
B. Promedio de alimento por tanda.
C. Cuál de las 3 comidas fue la que el animal comió más cantidad.
D. Alimento total de la tanda mayor. 
E. Bonus: Cuanto suma el total de kg de la tanda más abundante  
"""

TANDAS = 3
max_comida = -float('inf')
kg_max = -float('inf')
total_kilos = 0
kg_acum_tanda_max = 0  # Contador para sumar kg totales de la tanda mayor

for comida in range(1, TANDAS+1):   
  print(f"* Tanda {comida} de {TANDAS}")
  fin_comida = False    # Máxima Tarzán: mientras no terminar... continuar. La condicion "fin_comida" tiene que 
                        # cambiar de estado en algun momento, para que el león deje de comer. 
                        # Sino, siempre entra al ciclo. Me interesa que deje de comer en algún momento. 
  tot_por_comida = 0
  while not fin_comida:    # Mientras no False >> True (come dentro de una misma tanda). Alt: "while fin_comida == False"
  # while fin_comida == False:  # Es correcto también, pero mejor la forma "while not fin_comida"
    kilos = int(input("Ingrese los kg de alimento: "))
    total_kilos += kilos    # Suma de kg en todas las tandas
    fin_comida = (input("Recibir más alimento? [S/N]: ")).upper() == 'N'  # Boolean condition. Cuando ingreso 'N', fin_comida se convierte en True >>
    tot_por_comida += kilos                                                                          # tanto "while not fin_comida" como "while fin_comida == False" no se cumplen, entonces deja de comer. 
    
    if kilos > kg_max:    # kilos_max = -float('inf') 
      tanda_max = comida    # Como sabe que i es la tanda mayor si no suma los kg en ningun lado? Donde la compara con otras tandas?
      kg_max = kilos
      kg_acum_tanda_max += kilos 
      
  # FIN WHILE fin de una comida
  if tot_por_comida > max_comida:
    max_comida = tot_por_comida
    tanda_max = comida
# FIN FOR
        
informe = f"""
- INFORME DE ALIMENTACION - 
* Total de alimento suministrado: {total_kilos} kg.  
* Promedio de alimento por tanda: {(total_kilos / TANDAS):.2f} kg.
* Tanda de mayor suministro de alimento: {tanda_max}
* Alimento total tanda mayor: {max_comida} kg. 
* Ración máxima en tanda más abundante: {kg_max} kg.
"""
print(informe)

