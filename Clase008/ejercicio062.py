"""
## Ejercicio 062

### Un entrenador le ha propuesto a un atleta recorrer una ruta de cinco kilómetros durante 10 días para determinar si es apto para la prueba de 5 kilómetros que se desarrollará en el Parque. No se sabe si está apto y para eso nos piden que hagamos el siguiente programa.
### Nos ingresan por cada día de entrenamiento tiempo de la prueba en minutos (entero mayor que 0 y menor a 100)
### Para considerarlo apto debe cumplir las siguientes condiciones:
- Que en ninguna de las pruebas haga un tiempo mayor a 20 minutos. 
- Que al menos en una de las pruebas realice un tiempo menor de 15 minutos.
- Que su promedio sea menor o igual a 18 minutos.
### Se pide:
- Diseñar un algoritmo para registrar los datos y decidir si es apto para la competencia.
- Sólo en caso de estar apto, informar el promedio y el número de día en el que realizó el
menor tiempo 
"""



CANTIDAD_DIAS_ENTRENAMIENTO = 3
mayor_20 = False
menor_15 = False
suma_tiempos = 0
for dia in range(CANTIDAD_DIAS_ENTRENAMIENTO):# [0,1,2,3,4,5,6,7,8,9]

    """    tiempo = int(input(f"Día: {dia+1} Ingrese Tiempo [0..100]: "))
        while tiempo < 0 or tiempo > 100: # MIENTRAS ERROR
            print(f"Error: El dato no es un numero entre {0} y {100}")
            tiempo = int(input(f"Día: {dia+1} Ingrese Tiempo [0..100]: "))
    """
    # PRINCIPIO VALIDAR EL TIEMPO
    ok = False
    while not ok:  # MIENTRAS ERROR        
        tiempo = int(input(f"Día: {dia+1} Ingrese Tiempo [0..100]: "))   
        if tiempo < 0 or tiempo > 100:     
            print(f"Error: El dato no es un numero entre {0} y {100}")
        else:
            ok = True
    # FIN DE VALIDAR TIEMPO
    suma_tiempos += tiempo
    
    if tiempo > 20:
        mayor_20 = True

    if tiempo < 15:
        menor_15 = True

    
# FIN FOR
promedio = suma_tiempos/CANTIDAD_DIAS_ENTRENAMIENTO
apto =  promedio >= 18 and menor_15 and not mayor_20  
if apto:
    print("Dale!!")
else:
    print("No apto!!")         
        