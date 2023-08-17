





CAMINO = "CLASE019/"
ARCHIVO_LOCALIDADES = "LOCALIDADES.CSV"
ARCHIVO_NOMBRES_FEMENINIOS = "NOMBRESFEMENINOS.TXT"
ARCHIVO_NOMBRES_MASCULINOS = "NOMBRESMASCULINOS.TXT"
ARCHIVO_APELLIDOS = "APELLIDOS.TXT"
import random

def obtener_lista(nombre_archivo:str)->list:
    try:
        with open(file=nombre_archivo,mode='r',encoding='utf-8') as archivo:
            return [linea.rstrip() for linea in archivo]
    except IOError as e:
        raise RuntimeError(f"Error: {nombre_archivo}\nPython ==> {e}")

def obtener_dicc(nombre_archivo:str)->dict:
    pass

def crear_lista_personas(cantidad_personas:int)->list:
    femeninos = obtener_lista(ARCHIVO_NOMBRES_FEMENINIOS)
    masculinos = obtener_lista(ARCHIVO_NOMBRES_MASCULINOS)
    apellidos = obtener_lista(ARCHIVO_APELLIDOS)
    dic_provincias = obtener_dicc(ARCHIVO_LOCALIDADES)
    lista_personas = []
    
    for x in range(cantidad_personas):
        
        dni = random.randint(15000000,49999999)
        sexo = random.choice("MF")
        edad = random.randint(18,75)
        provincia = random.choice(dic_provincias.keys())
        localidad = random.choice(dic_provincias[provincia])
        if sexo == 'M':
            nombre = ' '.join(random.choices(masculinos,random.randint(1,3)))
        else:
            nombre = ' '.join(random.choices(femeninos,random.randint(1,3)))    
        apellido =  ' '.join(random.choices(apellidos,random.randint(1,2)))  
        calle =   random.choice(dic_provincias[random.choice(dic_provincias.keys())])
        altura = str(random.randint(50,9999))
        ubicacion = random.choice(["Casa",f"Dto {random.randint(1,20)}",f"Dto{random.choice('ABCDEFGH')}"])
        mail = f"{nombre.split()[0]}@.{random.choice(['com','com.ar'])}"
        lista_personas.append({dni,apellido,nombre,sexo,edad,provincia,localidad,calle,altura,ubicacion,mail})
    return lista_personas    
    # dict(zip(titulos,linea.rstrip().split(',')))


def main():
    lista_personas = crear_lista_personas(1000)



main()






