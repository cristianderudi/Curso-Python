from jugadores import Croupier, JugadorHumano, JugadorComputadora, Cliente
from random import randint
from typing import List
from txtcolores import strclr
from cartas import CartaPoker
from mazos import MazoBlackJack
import sys
sys.path.append('recursos/')


class BlackJack():

    def __init__(self, nombres: str = None) -> None:
        self.__color_alerta: int = 196
        self.__color_sitema: int = 15
        self.__croupier: Croupier = Croupier()
        self.__jugadores: List[Cliente] = []
        self.__las_apuestas: list[int] = []
        self.__mazo: MazoBlackJack = MazoBlackJack()
        self.__mazo.llenar()
        if nombres:
            for nombre in nombres.split(','):
                self.__jugadores.append(
                    JugadorComputadora(nombre, randint(100, 1000)))

    def agregar_jugador(self, cliente: Cliente) -> None:
        """
        Agrega un jugador al juego.

        Args:
            cliente (Cliente): Cliente a agregar.
        """
        if not isinstance(cliente, Cliente):
            raise TypeError('El jugador debe ser un objeto de tipo Cliente.')
        self.__jugadores.append(cliente)

    def __hay_jugadores(self) -> None:
        return len(self.__jugadores) > 0

    def __repartir_dos_cartas_jugadores(self):
        for jugador in self.__jugadores:
            jugador.poner(self.__mazo.sacar())
            jugador.poner(self.__mazo.sacar())
    
    def __repartir_dos_cartas_croupier(self)->None:
        carta = self.__mazo.sacar()
        carta.tapar()
        self.__croupier.poner(carta)
        self.__croupier.poner(self.__mazo.sacar())
    
    # correccion aquí. 
    # los métodos jugador.apostar no estaban definidos tenian pass.
    def __apostar(self)->int:
        self.__las_apuestas.clear()
        for jugador in self.__jugadores:
            cantidad_fichas =  jugador.apostar()
            # print(f"{jugador.getNombre()} apuesta {cantidad_fichas}")
            print(f"{strclr(jugador.getNombre(),jugador.getColor())} apuesta {cantidad_fichas}")
            self.__las_apuestas.append(cantidad_fichas)

    def __jugadores_juegan(self)->None:
        for jugador in self.__jugadores:
            
            while not jugador.sePlanta():                
                jugador.poner(self.__mazo.sacar())

    def __croupier_juega(self)->None:
        self.__croupier.getMano().destapar(0)
        while not self.__croupier.sePlanta():            
            self.__croupier.poner(self.__mazo.sacar())
        # print(f"{str(self.__croupier)} ({self.__croupier.getMano().suma()})")

    def __descartar(self)->None:
        for jugador in self.__jugadores:
            while not jugador.getMano().isvacio():
                self.__mazo.poner(jugador.getMano().sacar())
        while not self.__croupier.getMano().isvacio():
            self.__mazo.poner(self.__croupier.getMano().sacar())
    
    def __repartir_premios(self):
        suma_jugadores = 0
        suma_croupier = self.__croupier.getMano().suma()
        if suma_croupier > 21:
            # SE PASO EL CROUPIER
            for jugador in self.__jugadores:
                index = self.__jugadores.index(jugador)
                suma_jugadores = jugador.getMano().suma()
                if suma_jugadores > 21:
                    print(jugador,"Pierde! Se paso")                    
                    jugador.perderFichas(self.__las_apuestas[index])
                else:
                    print(jugador,"Gana! se paso el croupier")
                    jugador.ganarFichas(self.__las_apuestas[index])
        else:
            for jugador in self.__jugadores:
                index = self.__jugadores.index(jugador)
                suma_jugadores = jugador.getMano().suma()
                if suma_jugadores > 21:
                    print(jugador,"Pierde! Se paso")                    
                    jugador.perderFichas(self.__las_apuestas[index])
                else:
                    if suma_croupier == suma_jugadores:
                        print(jugador,"Empata!")  
                    else:
                        if suma_jugadores > suma_croupier:                  
                            print(jugador,"Gana! Pierde el croupier")                            
                            jugador.ganarFichas(self.__las_apuestas[index])
                        else:
                            print(jugador,"Pierde! Gana el Croupier")                    
                            jugador.perderFichas(self.__las_apuestas[index])

            

    def jugar(self):      
        while self.__hay_jugadores():           
            print("\n\nHagan sus apuestas Damas y Caballeros")
            self.__mazo.mezclar()
            self.__repartir_dos_cartas_jugadores()
            self.__repartir_dos_cartas_croupier()
            self.__apostar()
            self.__jugadores_juegan()
            self.__croupier_juega()
            self.__repartir_premios()
            self.__descartar()

def test():
    juego = BlackJack()
    juego.agregar_jugador(JugadorHumano('Raul', 1000))
    juego.agregar_jugador(JugadorHumano('Rosa', 1000))
    juego.agregar_jugador(JugadorComputadora('Wallie', 1000))
    juego.jugar()


if __name__ == '__main__':
    test()
