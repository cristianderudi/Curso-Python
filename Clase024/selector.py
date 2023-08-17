import os

SALIR = 99

class Selector:
    def __init__(self,opciones):
        self.opciones = opciones.split(",")        
    
    def selec(self):
        largo = self.largoLinea() + 10
        os.system("CLS")
        print("-"*largo)
        print(self.opciones[0])#TITULO
        print("-"*largo)
        ult = 0
        for x in range(1,len(self.opciones)):
            print("(" + str(x) + ")       "+self.opciones[x])
            ult = x
        print("-"*largo)
        print("("+str(ult+1) + ")    SALIR")
        print("-"*largo)
        rta = int(input("INGRESE UNA OPCION: "))
        if rta == ult+1:
            return 99

        return rta 
    
    def largoLinea(self):
        mayor = -1
        for palabra in self.opciones:
            if len(palabra) > mayor:
                mayor = len(palabra)
        return mayor

def main():
    s = Selector("Menu Principal,Altas,Bajas,Modificaciones,Listado,Otra opcion,otra,otra Mas")
    
    opcion = s.selec()
    while opcion != 99:
        if opcion == 1:
            pass
        elif opcion== 2:
            pass
        elif opcion ==3:
            pass
        elif opcion ==4:
            cadena_opciones = "PANTALLA 2,OPCION1,OPCION2,OPCION3,OPCION4"
            opcion = Selector(cadena_opciones).selec()
            while opcion != 99:
                opcion = Selector(cadena_opciones).selec()
            
        elif opcion ==5:
            pass
        else:
            pass
        opcion = s.selec()

if __name__ == "__main__":
    main()
