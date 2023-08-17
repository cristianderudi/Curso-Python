import random

from os import system



PIEDRA = 1
NOMBRE_PIEDRA = "PIEDRA"
PAPEL = 2
NOMBRE_PAPEL = "PAPEL"
TIJERA = 3
NOMBRE_TIJERA = "TIJERA"
LAGARTO = 4
NOMBRE_LAGARTO = "LAGARTO"
SPOCK = 5
NOMBRE_SPOCK = "SPOCK"

class Gesto(object):
    def __init__(self) -> None:
        self.__gesto = self.__gesto_random()

    def __gesto_random(self):
        return random.randint(1,5)
    
    def getgesto(self) -> int:
        return self.__gesto
    
    def __str__(self) -> str:
        if self.__gesto == PIEDRA:
            return NOMBRE_PIEDRA
        elif self.__gesto == PAPEL:
            return NOMBRE_PAPEL
        elif self.__gesto == TIJERA:
            return NOMBRE_TIJERA
        elif self.__gesto == LAGARTO:
            return NOMBRE_LAGARTO
        else:
            return NOMBRE_SPOCK

class Jugador(object):
    def __init__(self,nombre:str=None,motivo:str=None) -> None:
        self.__nombre = nombre
        self.__mano = Gesto()
        self.__motivo = motivo

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value,Jugador):
            return False
        return __value.getnombre() == self.getnombre()

    def hacer_gesto(self) -> None:
        self.__mano = Gesto()
        
    def getnombre(self) -> str:  
        return self.__nombre

    def getmotivo(self) -> str:  
        return self.__motivo
    
    def setmotivo(self,motivo:str)->None:
        self.__motivo = motivo

    def getmano(self) -> Gesto:
        return self.__mano

    def __str__(self) -> str:
        return f"{self.__nombre:8} ==> [{str(self.__mano)}]"     

class Juego(object):
    def __init__(self,nomb_jug_1:str,nomb_jug_2:str) -> None:
        self.__jug1 = Jugador(nomb_jug_1)
        self.__jug2 = Jugador(nomb_jug_2)    
    
    def __quien_gana(self) -> Jugador:
        gesto1 = self.__jug1.getmano().getgesto() 
        gesto2 = self.__jug2.getmano().getgesto()
        ganador = Jugador()
        if gesto1 == gesto2:
            ganador.setmotivo("Empate") 
            
        elif gesto1 == PIEDRA and (gesto2 == TIJERA or gesto2 == LAGARTO):
            ganador = self.__jug1
            ganador.setmotivo("Tijera corta al lagarto") 
        
        elif gesto1 == PAPEL and (gesto2 == PIEDRA or gesto2 == SPOCK):
            ganador = self.__jug1
            ganador.setmotivo("Piedra mata a Spock") 
        elif gesto1 == TIJERA and (gesto2 == PAPEL or gesto2 == LAGARTO):
            ganador = self.__jug1
            ganador.setmotivo("ñladkjsdfañlkasñdfkasñ") 
            return self.__jug1
        elif gesto1 == LAGARTO and (gesto2 == PAPEL or gesto2 == SPOCK):
            ganador = self.__jug1
            ganador.setmotivo("ajmksskamxams lagarto") 
        elif gesto1 == SPOCK and (gesto2 == TIJERA or gesto2 == PIEDRA):
            ganador = self.__jug1
            ganador.setmotivo("Tijera corta al lagarto") 
       
        ganador = self.__jug2
        ganador.setmotivo()
        return self.__jug2

    def jugar(self) -> None:
        puntos_jugador1 = 0
        puntos_jugador2 = 0
        terminar = False
        ganador = Jugador()
        
        while not terminar:
            self.__jug1.hacer_gesto()
            print(self.__jug1)
            self.__jug2.hacer_gesto()
            print(self.__jug2)

            ganador = self.__quien_gana() #agragar por que gano

            if ganador == self.__jug1:
                puntos_jugador1 += 1
                print(f"Gana {ganador.getnombre() } {ganador.getmotivo()}\n")
                # agregar por que
            elif ganador == self.__jug2:
                print(f"Gana {ganador.getnombre() } {ganador.getmotivo()}\n")
                puntos_jugador2 += 1
            else:
                print(f"Empate\n")
            
            if puntos_jugador1 == 4 or puntos_jugador2 == 4:
                terminar = True
        winer = f"Ganador {ganador.getnombre()}" 
        print(f"{'*'*30}\n{winer.center(30)}\n{'*'*30}\n")
       
def main():
    system("cls")
    Juego('Juan','Pinchame').jugar() 
    
main()
