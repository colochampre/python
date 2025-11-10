class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = str(titular)
        self.__saldo = float(saldo)

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            return
        self.__saldo = saldo

cuenta1 = CuentaBancaria("Juan", 1000)
cuenta1.saldo = -10.0
print(cuenta1.saldo)
