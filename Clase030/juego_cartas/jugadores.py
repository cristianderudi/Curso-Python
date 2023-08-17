"""
Modulo que contiene las clases que representan a los jugadores de cartas.

- JugadorCartas: Clase abstracta que representa un jugador de cartas.

- JugadorBlackjack: Clase que representa un jugador de blackjack.

- Cliente: Clase que representa un cliente del casino.

- Croupier: Clase que representa el croupier del casino.

- JugadorHumano: Clase que representa un jugador humano.

- JugadorComputadora: Clase que representa un jugador bot.

"""

from cartas import Carta, CartaPoker
from mazos import Mazo, MazoBlackJack
from txtcolores import strclr
from utilidades import leer_entero
from abc import ABC, abstractmethod
from random import shuffle,randint
import sys
sys.path.append('recursos/')


class JugadorCartas(ABC):
    """
    Clase abstracta que representa un jugador de cartas.

    Args:
        ABC ([type]): [description]

    """

    def __init__(self, nombre: str, mano: Mazo) -> None:
        """
        Inicializa un jugador con un nombre y una mano.

        Args:
            nombre (str): Nombre del jugador.
            mano (Mazo): Mano del jugador.
        """
        super().__init__()  # Llama al constructor de la clase base
        self.__nombre: str = nombre
        self.__mano: Mazo = mano

    def poner(self, carta: Carta, index: int = -1) -> None:
        """
        Pone una carta en la mano del jugador.

        Args:
            carta (Carta): Carta a poner.
            index (int, optional): Indice donde poner la carta. Defaults to -1.
            Si index es -1 la carta se pone al final de la mano.
            De lo contrario se pone en la posicion index.
        """
        self.__mano.poner(carta, index)

    def sacar(self, index: int = 0) -> Carta:
        """
        Saca una carta de la mano del jugador.

        Args:
            index (int, optional): Indice de la carta a sacar. Defaults to 0.
        """
        return self.__mano.sacar(index)

    def tieneCartas(self) -> bool:
        """
        Indica si el jugador tiene cartas en su mano.
        """
        return not self.__mano.isvacio()

    def getNombre(self) -> str:
        """
        Devuelve el nombre del jugador.
        """
        return self.__nombre

    def getMano(self) -> Mazo:
        """
        Devuelve la mano del jugador.
        """
        return self.__mano

    def __str__(self) -> str:
        return f"{self.__nombre} ==> {self.__mano}"


class JugadorBlackjack(JugadorCartas):
    """
    Clase abstracta que representa un jugador de blackjack.
    """

    def __init__(self, nombre: str) -> None:
        """
        Inicializa un jugador de blackjack con un nombre y una mano.            
        """
        super().__init__(nombre, MazoBlackJack())
        self.__color = 15

    def setColor(self, color: int) -> None:
        """
        Establece el color del jugador.
        """
        self.__color = color

    def getColor(self) -> int:
        """
        Devuelve el color del jugador.
        """
        return self.__color

    def poner(self, carta: CartaPoker, index: int = -1) -> None:
        """
        Pone una carta en la mano del jugador.
        Método delegado de la clase MazoBlackJack.
        """
        self.getMano().poner(carta, index)

    def sacar(self, index: int = 0) -> CartaPoker:
        """
        Saca una carta de la mano del jugador.
        Método delegado de la clase MazoBlackJack.
        """
        return self.getMano().sacar(index)

    def tieneBlackJack(self) -> bool:
        """
        Indica si el jugador tiene blackjack.
        """
        return len(self.getMano()) == 2 and self.getMano().suma() == 21

    def getMano(self) -> MazoBlackJack:
        """
        Devuelve la mano del jugador.
        """
        return super().getMano()

    @abstractmethod
    def sePlanta(self) -> bool:
        """
        Indica si el jugador se planta.
        """
        pass


class Croupier(JugadorBlackjack):
    def __init__(self) -> None:
        super().__init__("Sr Croupier")
        self.setColor(154)

    def sePlanta(self) -> bool:
        """
        El croupier se planta si su mano suma 17 o más.
        Sobreescribe el método de la clase base.
        """
        suma = self.getMano().suma()
        print(f"{str(self)} ({suma})")
        
        if suma >= 21:
            print(strclr("SE PASO",196))
            return True
        else:
            
            if suma >= 17:
                print(strclr("SE PLANTA",15))
                return True
        return False

    def __str__(self) -> str:
        return f"{strclr(self.getNombre(),self.getColor())} ==> {self.getMano()}"


class Cliente(JugadorBlackjack):
    """
    Clase que representa un cliente de un casino.
    """
    colores = [10, 11, 12, 13, 14, 32, 125, 175, 201]

    def __init__(self, nombre: str, fichas: int) -> None:
        """
        Inicializa un cliente con un nombre y una mano.

        Args:
            nombre (str): Nombre del cliente.
            fichas (int): Fichas del cliente.
        """
        super().__init__(nombre)  # Llama al constructor de la clase base

        self.__fichas:int = fichas
        shuffle(Cliente.colores)
        self.setColor(Cliente.colores.pop(0))

    def getFichas(self) -> int:
        """
        Devuelve las fichas del cliente.
        """
        return self.__fichas

    def ganarFchas(self, fichas: int) -> None:
        """
        Gana fichas.

        Args:
            fichas (int): Fichas a ganar.
        """
        self.__fichas += fichas

    def perderFichas(self, fichas: int) -> None:
        """
        Pierde fichas.

        Args:
            fichas (int): Fichas a perder.
        """
        self.__fichas -= fichas

    @abstractmethod
    def apostar(self) -> int:
        pass

    def __str__(self) -> str:
        return f"{strclr(self.getNombre(),self.getColor())} ==> {self.getMano()} $[{self.getFichas()}]  ({self.getMano().suma()})"


class JugadorHumano(Cliente):
    """
    Clase que representa un jugador humano.
    """

    def __init__(self, nombre: str, fichas: int) -> None:
        super().__init__(nombre, fichas)
    
    def __leer_sino(self,cartel:str)->bool:
        return input(f"¿{cartel}?[S/N]: ").upper() == 'S'
    
    def sePlanta(self) -> bool:
        """
        Sobreescribe el método de la clase base.
        """
        print(str(self))
        suma = self.getMano().suma()
        if suma >= 21:
            print(strclr("SE PASO",196))
            return True
        return self.__leer_sino("Se planta")
    
    def apostar(self) -> int:
        print(str(self))
        return leer_entero('Cuanto apuesta: ',1,self.getFichas())


class JugadorComputadora(Cliente):
    """
    Clase que representa un jugador computadora.
    """
    FRENETICO = 100
    TRANQUILO = 1
    def __init__(self, nombre: str, fichas: int) -> None:
        super().__init__(nombre, fichas)
        self.__personalidad:int = self.__obtener_personalidad()

    def __obtener_personalidad(self)->int:
        return randint(self.TRANQUILO,self.FRENETICO)

    def __pensar(self)->int:
        return randint(self.TRANQUILO,self.FRENETICO)

    def sePlanta(self) -> bool:
        print(str(self))
        suma = self.getMano().suma()
        if suma > 21:
            print(strclr("SE PASO",196))
            return True
        pensamiento = self.__pensar()
        if pensamiento < self.__personalidad:
            respuesta = 'N'
        else:
            respuesta = 'S'
        print(f'Se planta [S/N]: {respuesta}')
        return respuesta == 'S'    

    def apostar(self) -> int:
        print(str(self))
        cantidad = 0
        if self.__pensar() < self.__personalidad:
            cantidad = randint(self.getFichas()//2,self.getFichas())
        else:
            cantidad = randint(1,self.getFichas()//2)
        print(f'Cuanto apuesta: {cantidad}')
        return cantidad

def test():
    mazo = MazoBlackJack()
    mazo.llenar()
    mazo.mezclar()
    jh = JugadorHumano("Pepe", 100)
    jh.poner(mazo.sacar())
    jh.poner(mazo.sacar())
    jh.poner(mazo.sacar())
    jh.poner(mazo.sacar())
    print(jh)
    cr = Croupier()
    cr.poner(mazo.sacar())
    cr.poner(mazo.sacar())
    cr.getMano().destapar(0)
    print(cr)
    cr.poner(mazo.sacar())
    print(cr)

    jc = JugadorComputadora("Computadora", 100)
    jc.poner(mazo.sacar())
    jc.poner(mazo.sacar())
    print(jc)


if __name__ == '__main__':
    test()
