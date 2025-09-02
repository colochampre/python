from TP_02.ej_1 import *


# ----------------------------- Caja Corriente -------------------------------
class CuentaCorriente(Cuenta):
    def __init__(self, numero_cuenta, titular, cuil, cbu, alias, saldo, descubierto=0.0):
        super().__init__(numero_cuenta, titular, cuil, cbu, alias, saldo)
        self.__descubierto = descubierto  # Monto máximo de descubierto permitido (>=0)


    @property
    def descubierto(self) -> float:
        return self.__descubierto


    @staticmethod
    def __validar_descubierto(valor: float) -> float:
        v = a_numero(valor)
        if v < 0:
            print("El descubierto no puede ser negativo.")
            return 0.0
        return v

# ----------------------------- Caja de Ahorro -------------------------------
class CuentaAhorro(Cuenta):
    def __init__(self, numero_cuenta, titular, cuil, cbu, alias, saldo):
        super().__init__(numero_cuenta, titular, cuil, cbu, alias, saldo)
