










CAMINO = "Clase016/"



def llenar_desde_archivo(nombre_archivo:str) -> list:
    lista_enteros = []

    archivo = open(file=nombre_archivo,mode='r',encoding='utf-8')
    for linea in archivo:
        lista_cadenas = linea.rstrip().split(',')
        for cadena in lista_cadenas:
            numero = int(cadena)
            lista_enteros.append(numero)
        
    archivo.close()

    return lista_enteros


def mostrar_lista(lista:list) -> None:   
    for indice,dato in enumerate(lista):
        print(f"lista[{indice}] = {dato}")



def main():
    lista = llenar_desde_archivo(CAMINO + "numeros2.txt")
    mostrar_lista(lista)
    print("range de len lista: ",list(range(len(lista))))
    print("enumerate lista: ",list(enumerate(lista)))
    




main()



