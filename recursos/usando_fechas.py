from Fechas import Fecha

x = Fecha()
print(x)
print(x.fecha_larga_dia())
print(f"Dia de la semana {x.getdia_semana()}")
print(x.intfecha())
if x > '3':
    print(Fecha.NOMBRES_DIAS_SEMANAS)