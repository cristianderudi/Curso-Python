""" Alfredo , estaba viendo el ejemplo de tuplas , me tope con la funcion x , capaz que si se hubiera llamado con otro nombre
no me hubiera dado cuenta :) , pero me detuve ahi y empezaron a aparecer varios porque , antes habia usado funciones , 
y simplemente las use , funcionaban asi y segui ,  no me habia preguntado eso,  que te paso mas abajo como preguntas, son 
todas preguntas  , y queria saber si es asi , o no . Gracias  
"""


def fun(n): # esta x tiene el valor 4 recibio pasada como argumento y ahora es parametro, todavia seria la x original
    n = 1000
    """ esta x , la contenedora de 1000 , no es la misma que la de arriba, no es que la de arriba cambio de valor,  es "OTRA" x , 
    seria una copia o x[1] o x[...] o como se llame , pero no esta contenida en el mismo lugar de memoria o contenedor que la x del parametro  """
    return n 
    """ esta que retorna , es la copia (o como se llame ) , no la original , esto pasa porque se originan "copias, no se si es el termino tecnico"
    por el tema de que la variables y los strig , son INMUTABLES , sino no seria asi """

def fun1(tupla):
    tupla += (4,)
    return tupla

def modi(z):
    z.append(24555414)


def main():
    lis = [4]
    modi(lis)
    print(lis)

    """    
        renglon = ("producto 1",3,100)
        
        renglones = (renglon,renglon,renglon)

        print(renglones)

        total = 0
        for renglon in renglones:
            importe = renglon[1]*renglon[2]
            total += importe
            print(renglon,importe)
        print("total: ",total)

        t = (1,2,3)
        t = fun1(t)
        
        x = 4 # aca empezaria la vida original de la x
        x = fun(x) # aca la x se mantiene original y va al parametro 

        x=fun(x) , si en vez de la declaracion de arriba , lo hubiera declarado como en esta linea,  la x ANTES del = , no es la misma x 
        ,que la que se le esta pasando en el argumento de la declaracion . Por otro lado siempre que se reciba de un return 
        , y se necesite el valor RETORNADO , producto del proceso de esa funcion ,hay que recibirla , en otra variable , justamente para recibir 
        esa copia con el nuevo valor del proceso , sino estaria recibiendo la x original y si es INMUTABLE , se romperia la ley de Python 
        Seria que el argumento, variable o string, sale , pero jamas vuelve el mismo , siempre se recibe otra , llamese igual o no , es OTRA 
        print('x:',x) 
        # aca se estaria usando , la misma x , no se estaria recibiendo nada del return, esta x , siempre estubo aca , no se proceso en la funcion.   
        """
    
main()













