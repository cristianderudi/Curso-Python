import copy

class Humano(object):
    cantidad_humanos = 0
    def __init__(self, sexo: str, edad: int) -> None:
        super().__init__()
        Humano.cantidad_humanos += 1
        self.__sexo: str = sexo
        self.__edad: int = edad


    def __str__(self) -> str:
        return f'{self.__sexo},{self.__edad}'
    
    def cuantos_somos(self) -> int:
        return Humano.cantidad_humanos


class Persona(Humano):
    def __init__(self, dni: int, nombre: str, sexo: str, edad: int) -> None:
        super().__init__(sexo, edad)
        self.__dni: str = dni
        self.__nombre: str = nombre    
    
    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre


    def get_dni(self) -> str:
        return self.__dni
    
    def set_dni(self, dni: str) -> None:
        self.__dni = dni

    def __str__(self) -> str:
        return super().__str__() + f',{self.__dni},{self.__nombre}'


class Empleado(Persona):
    def __init__(self, sueldo: float, dni: int, nombre: str, sexo: str, edad: int) -> None:
        super().__init__(dni, nombre, sexo, edad)
        self.__sueldo: float = sueldo

    def get_sueldo(self) -> float:
        return self.__sueldo
    
    def set_sueldo(self, sueldo: float) -> None:
        self.__sueldo = sueldo

    def __str__(self) -> str:
        return super().__str__() + f',{self.__sueldo}'    

class Alumno(Persona):
    def __init__(self, legajo: int, dni: int, nombre: str, sexo: str, edad: int) -> None:
        super().__init__(dni, nombre, sexo, edad)
        self.__legajo: int = legajo

    def get_legajo(self) -> int:
        return self.__legajo
    
    def set_legajo(self, legajo: int) -> None:
        self.__legajo = legajo

    def __str__(self) -> str:
        return super().__str__() + f',{self.__legajo}'

def main():
    h = Humano('M', 25)
    #print(h)

    p = Persona(nombre="Juan", dni=12345678, sexo='M', edad=33)
    #print(p)

    e = Empleado(100000.0, 12345678, 'Juan', 'M', 33)
    #print(e)

    a = Alumno(1234, 12345678, 'Juan', 'M', 33)
    #print(a)
    #print(a.cantidad_humanos)
    #print("Somos: ",a.cuantos_somos())

    x = a

    # print(x)

    lista = [h, p, e, a,x]

    print("Lista original\n"+'\n'.join([str(elemento) for elemento in lista]))

    otra_lista = copy.deepcopy(lista)
    
    print("Otra lista\n"+'\n'.join([str(elemento) for elemento in otra_lista]))

    # otra_lista[2].set_nombre("Pedro")
    print(e.get_nombre())
    e.set_nombre("Pedro")
    print(e.get_nombre())
    otra_lista.pop(3)
    print("-"*50)

    print("\nLista original\n"+'\n'.join([str(elemento) for elemento in lista]))

    
    print("\nOtra lista\n"+'\n'.join([str(elemento) for elemento in otra_lista]))

main()
