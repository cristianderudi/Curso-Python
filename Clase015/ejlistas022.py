"""
- 22) Dada una lista de palabras, crear una función que 
    devuelva una nueva lista con las palabras que son palíndromos 
    (se leen igual de izquierda a derecha y de derecha a izquierda).
"""

def fun(lista_palabras:list)->list:
    
    nueva = []
    for palabra in lista_palabras:
        if palabra == palabra[::-1]:
            nueva.append(palabra)
    return nueva

def main():
    texto = 'El dormitorio es desmantelado y oscuro Hayah un balcón queuq mira al poniente'
    lista_palabras = texto.lower().split()
    nueva = fun(lista_palabras)
    print(nueva)
main()