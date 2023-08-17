"""
Ejercicio 002

Define una clase llamada Cuenta, que se inicializa con el nombre del titular de la cuenta como parámetro.

Cada cuenta tendrá un saldo inicial de 0.

La clase Cuenta debe tener los siguientes métodos:

a. acreditar(monto, concepto): Este método permite acreditar un monto en la cuenta. Debe recibir como 
parámetros el monto a acreditar y un concepto que describe la transacción (por ejemplo, "Sueldo", 
"Venta", "Transferencia", etc.). 
El monto acreditado se suma al saldo actual de la cuenta.

b. transferir(monto, otra_cuenta): Este método permite transferir un monto desde la cuenta actual a 
otra cuenta. Debe recibir como parámetros el monto a transferir y la instancia de otra cuenta (otra_cuenta) 
a la cual se desea transferir el dinero. 
Si la cuenta actual tiene saldo suficiente, se realiza la transferencia descontando el monto de la cuenta 
actual y acreditándolo en la otra cuenta.

c. extraer(monto, concepto): Este método permite extraer un monto de la cuenta. Debe recibir como parámetros 
el monto a extraer y un concepto que describe la transacción (por ejemplo, "Compra", "Retiro", etc.). 
El monto extraído se resta del saldo actual de la cuenta. Si el saldo no es suficiente para cubrir el monto 
a extraer, se debe lanzar una excepción.

d. saldo(): Este método devuelve el saldo actual de la cuenta.

Recuerda que al implementar la clase Cuenta, debes tener en cuenta las validaciones necesarias para evitar 
operaciones inválidas y mantener el correcto funcionamiento del sistema de cuentas

A continuación, un ejemplo de cómo se podría utilizar la clase:

# Creamos las cuentas para Pérez y López
c = Cuenta('Pérez')
d = Cuenta('López')

# Acreditamos un sueldo de 100 a la cuenta de Pérez
c.acreditar(100, 'Sueldo')

# Transferimos 30 desde la cuenta de Pérez a la cuenta de López
c.transferir(30, d)

# Extraemos 60 de la cuenta de Pérez por compras
c.extraer(60, 'Shopping')

# Consultamos el saldo de la cuenta de Pérez
saldo_perez = c.saldo()
print("Saldo de la cuenta de Pérez:", saldo_perez)

"""

class Resultado:
    def __init__(self,mensaje,resultado:bool) -> None:        
        self.__mensaje = mensaje
        self.__resultado = resultado
    
    def __str__(self) -> str:
        return f"{self.__mensaje} - Resultado: {self.__resultado}"
    
    def is_ok(self) -> bool:
        return self.__resultado
    

class Cuenta:

    def __init__(self, titular: str = 'Titular') -> None:

        self.__titular = titular

        self.__saldo = 0.0

        self.__registro_operaciones = ()

    def get_saldo(self) -> float:

        return self.__saldo

    def __str__(self) -> str:

        return f"Titular: {self.__titular} - Saldo Actual: $ {self.__saldo}."

    def acreditar(self, monto: float = 0.0, concepto: str = 'Varios') -> Resultado:

        self.__saldo += monto

        self.__registro_operaciones += (monto, concepto)

        return Resultado(f"Se acreditó $ {monto} en la cuenta de {self.__titular}.",True)

    # Preguntar: ¿cómo recibo una instancia de otra cuenta y la modifico?
    def transferir(self,otra_cuenta: 'Cuenta', monto: float , concepto: str = 'Varios' ) -> Resultado:

        if (otra_cuenta is None or not isinstance(otra_cuenta, Cuenta) ):
            raise ValueError("Debe seleccionar una cuenta a la cual transferir.")

        if (monto <= 0):
            raise ValueError("Debe seleccionar un importe para transferir.")

        if (self.__saldo < monto):
            raise ValueError("Saldo insuficiente.")

        self.__saldo -= monto

        self.__registro_operaciones += (monto, concepto)
        otra_cuenta.acreditar(monto, concepto)
        return Resultado(f"Se transfirió $ {monto} a la cuenta de {otra_cuenta.__titular}.",True)

        

    def extraer(self, monto: float = 0.0, concepto: str = 'varios') -> None:

        if (monto <= 0):

            return "Debe seleccionar un importe para extraer."

        if (self.__saldo < monto):

            raise ValueError("Saldo insuficiente.")

        self.__saldo -= monto

        self.__registro_operaciones += (monto, concepto)

        


def main():

    # Creamos las cuentas para Pérez y López
    c = Cuenta('Pérez')
    d = Cuenta('López')

    # Acreditamos un sueldo de 100 a la cuenta de Pérez
    c.acreditar(100, 'Sueldo')

    # Transferimos 30 desde la cuenta de Pérez a la cuenta de López
    r = c.transferir(d, 3000)
    if r.is_ok():
        print("Transferencia exitosa")
    else:
        print(r)
    # Extraemos 60 de la cuenta de Pérez por compras
    c.extraer(60, 'Shopping')

    # Consultamos el saldo de la cuenta de Pérez y de Lopez
    saldo_perez = c.get_saldo()
    print("Saldo de la cuenta de Pérez:", saldo_perez)
    saldo_lopez = d.get_saldo()
    print("Saldo de la cuenta de López:", saldo_lopez)


if __name__ == '__main__':
    main()
