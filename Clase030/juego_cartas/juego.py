from jugadores import Croupier, JugadorHumano, JugadorComputadora, Cliente
from random import randint,shuffle
from typing import List
from txtcolores import strclr
from cartas import CartaPoker
from mazos import MazoBlackJack
from os import system
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
        shuffle(self.__jugadores)
        

    def __juego_hay_jugadores(self) -> None:
        return len(self.__jugadores) > 0

    def __jugadores_repartir_dos_cartas(self):
        for jugador in self.__jugadores:
            jugador.poner(self.__mazo.sacar())
            jugador.poner(self.__mazo.sacar())
    
    def __croupier_repartir_dos_cartas(self)->None:
        carta = self.__mazo.sacar()
        carta.tapar()
        self.__croupier.poner(carta)
        self.__croupier.poner(self.__mazo.sacar())
    
    def __jugadores_apuestan(self)->None:
        print(self.__croupier)
        self.__las_apuestas.clear()
        for jugador in self.__jugadores:            
            self.__las_apuestas.append(jugador.apostar())

    def __jugadores_juegan(self)->None:
        for jugador in self.__jugadores:            
            while not jugador.sePlanta():                
                jugador.poner(self.__mazo.sacar())

    def __croupier_juega(self)->None:
        self.__croupier.getMano().destapar(0)
        while not self.__croupier.sePlanta():            
            self.__croupier.poner(self.__mazo.sacar())
        #print(f"{str(self.__croupier)} ({self.__croupier.getMano().suma()})")
        system('pause')

    def __jugadores_se_descartan(self)->None:
        for jugador in self.__jugadores:
            while not jugador.getMano().isvacio():
                self.__mazo.poner(jugador.getMano().sacar())
    def __croupier_se_descarta(self)->None:
        while not self.__croupier.getMano().isvacio():
            self.__mazo.poner(self.__croupier.getMano().sacar())
    
    def __juego_repartir_premios(self):
        system("cls")
        print(strclr("-"*80,16))
        print(strclr("REPARTIR PREMIOS".center(80),16))
        print(strclr("-"*80,16))
        suma_jugadores = 0
        suma_croupier = self.__croupier.getMano().suma()
        print(f"{self.__croupier} ==> ",end='')
        if suma_croupier > 21:
            # SE PASO EL CROUPIER
            print(strclr("SE PASO",self.__color_alerta))
            for jugador in self.__jugadores:
                index = self.__jugadores.index(jugador)
                suma_jugadores = jugador.getMano().suma()
                if suma_jugadores > 21:
                    print(jugador,"Pierde! Se paso")                    
                    jugador.perderFichas(self.__las_apuestas[index])
                else:
                    print(jugador,"Gana! se paso el croupier")
                    jugador.ganarFchas(self.__las_apuestas[index])
        else:
            print(f'{strclr("PUNTOS CROUPIER: ",self.__color_alerta)} ({suma_croupier})')
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
                            jugador.ganarFchas(self.__las_apuestas[index])
                        else:
                            print(jugador,"Pierde! Gana el Croupier")                    
                            jugador.perderFichas(self.__las_apuestas[index])
        system("pause")
        system("cls")
            
    def __juego_retirar_jugadores(self)->None:
        pass
    
    def jugar(self):
        while self.__juego_hay_jugadores():
            self.__mazo.mezclar()
            self.__jugadores_repartir_dos_cartas()
            self.__croupier_repartir_dos_cartas()
            self.__jugadores_apuestan()
            self.__jugadores_juegan()
            self.__croupier_juega()
            self.__juego_repartir_premios()
            self.__jugadores_se_descartan()
            self.__croupier_se_descarta()
            self.__juego_retirar_jugadores()

def test():
    juego = BlackJack("Compu_Ana,Compu_Rosa")
    juego.agregar_jugador(JugadorHumano('Raul', 1000))
    juego.agregar_jugador(JugadorHumano('Alfredo', 1000))
    juego.jugar()


if __name__ == '__main__':
    test()
