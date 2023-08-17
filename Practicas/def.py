def main():
    fecha = int(19851217)
    anio = fecha//10000
    dia = fecha%100
    mes = (fecha//100)%100

    print(f"{dia}/{mes}/{anio}")
main()