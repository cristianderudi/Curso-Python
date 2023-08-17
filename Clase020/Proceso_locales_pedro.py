
CAMINO = 'clase018/'
NOMBRE_ARCHIVO = CAMINO +'locales-en-venta-2020-transformado.csv'

def obtener_lista_desde_archivo(nombre_archivo:str)->dict:
    try:
        with open(file=nombre_archivo,mode='r',encoding='utf-8') as archivo:
            titulos = archivo.readline().rstrip().split(',')
            return [ dict(zip(titulos,linea.rstrip().split(','))) for linea in archivo]

    except IOError as e:
        raise Exception(f"Error al intentar leer el archivo: {nombre_archivo} \nPython dice:{e}")

def filtrar_por_barrio(lista:list[dict],nombre_barrio:str)->list[dict]:
    return [   local   for local in lista if local['BARRIO'] == nombre_barrio   ]

def pepe(lista_dic:list[dict],nombre_barrio:str)->list:
    return list(filter(lambda x : x['BARRIO']==nombre_barrio,lista_dic))
    
"""    
    salida = []
    for local in lista:
        if local['BARRIO'] == nombre_barrio:
            salida.append(local)
    return salida
"""

def main():
    try:
        lista_locales = obtener_lista_desde_archivo(NOMBRE_ARCHIVO)
    except Exception as e:
        print("Error: ",e)
    else: 
           
        for local in pepe(lista_locales,"BALVANERA"):
            print(' '.join(local.values()))

main()