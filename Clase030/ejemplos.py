
class A(object):
    def __init__(self) -> None:
        self.__xx:int = 0
    
    def getxx(self)->int:
        return self.xx
    
    def setxx(self, xx:int)->None:
        self.xx = xx

    def _pepe(self)->None:
        print("pepe")


class B(A):
    def __init__(self) -> None:
        super().__init__()
        self.__tt:int = 0

    def gettt(self)->int:
        return self.tt
    
    def settt(self, tt:int)->None:
        self.tt = tt



def metodo1(a:int|float)->None:
    a.setxx(10)
    print(a.getxx())


a = B()

a._pepe()


f = list(filter(lambda x: x%2 == 0, [1,2,3,4,5,6,7,8,9,10]))
print(f)

lista_palabras = ["hola", "mundo", "chau", "mundo"]
f = list(filter(lambda x: x == "mundo", lista_palabras))
print(f)


# obtener las palabras con la letra m
f = list(filter(lambda x: "m" in x, lista_palabras))

