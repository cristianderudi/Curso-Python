from random import randint

PIEDRA = 1
PAPEL = 2
TIJERA = 3

 


class Gesto:
    def __init__(self) -> None:
        self.__gesto = randint(1,3)

    def __eq__(self, otro: object) -> bool:
        if otro is None:
            return False
        elif not isinstance(otro,Gesto):
            return False
        return self.__gesto == otro.__gesto
        

    def getgesto(self):
        return self.__gesto

    def __str__(self) -> str:
        cadena = str(super())

        if self.__gesto == PIEDRA:
            cadena = '[PIEDRA]'
        elif self.__gesto == PAPEL:
            cadena = '[PAPEL]'
        elif self.__gesto == TIJERA:
            cadena = '[TIJERA]'
            
        return cadena

class Jugador:
    def __init__(self,nombre) -> None:
        self.__nombre = nombre
        self.__mano = Gesto()

    def hacer_gesto(self)->None:    
        self.__mano = Gesto()

    def getnombre(self)->str:
        return self.__nombre

    def getmano(self)->Gesto:
        return self.__mano

    def __str__(self) -> str:
        return f'{self.__nombre} {str(self.__mano)}'


class PiedraPapelTijera:
    def __init__(self,nombre_jug1:str,nombre_jug2:str) -> None:
        self.__jug1:Jugador = Jugador(nombre_jug1)
        self.__jug2:Jugador = Jugador(nombre_jug2)

    def jugar(self)->None:
        terminar = False
        victorias_jug1 = 0
        victorias_jug2 = 0
         
        while not terminar:
            self.__jug1.hacer_gesto()
            print(str(self.__jug1))
            self.__jug2.hacer_gesto()
            print(str(self.__jug2))

            ganador,por_que_gana = self.__quien_gana()

            if self.__jug1 is ganador:
                victorias_jug1 += 1
                print(f"Gana la mano: {ganador.getnombre()} {por_que_gana}")
            elif self.__jug2 is ganador:
                victorias_jug2 += 1
                print(f"Gana la mano: {ganador.getnombre()} ")
            else:
                print("Empate!!!")   

            if victorias_jug1 == 2 or victorias_jug2 == 2:
                terminar = True             

        print(f"GANADORRRRRR ==> {ganador.getnombre()}")

    def __quien_gana(self)->Jugador:
        jugador_ganador = None
        texto = "Empate"
        g1 = self.__jug1.getmano().getgesto()
        g2 = self.__jug2.getmano().getgesto()

        if g1 == g2:
            jugador_ganador = None
            texto = "Empate"
        elif g1 == PIEDRA and g2 == TIJERA:
            jugador_ganador = self.__jug1
            texto = "Piedra rompe tijera"
        elif g1 == PAPEL and g2 == PIEDRA:
            jugador_ganador = self.__jug1

        elif g1 == TIJERA and g2 == PAPEL:
            jugador_ganador = self.__jug1 
        else:
            jugador_ganador = self.__jug2

        return jugador_ganador,texto
            
        
        

def main():
    juego = PiedraPapelTijera("Juan","Pinchame")
    juego.jugar()
    #g = Gesto()
    # print(g)
    # j = Jugador("Pepe")
    # print(j)
    a = 2
    b = a
    print( isinstance(a,(int,float)))
    print(a is b)      

main()





    














