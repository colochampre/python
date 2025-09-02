import sys
import os
# Añadir el directorio padre al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from TP_02.ej_1 import *


# ----------------------------- Caja Corriente -------------------------------
class CuentaCorriente(Cuenta):
    def __init__(self, numero_cuenta, titular, cuil, cbu, alias, saldo, descubierto=0.0):
        super().__init__(numero_cuenta, titular, cuil, cbu, alias, saldo)
        self.__descubierto = descubierto  # Monto máximo de descubierto permitido (>=0)


    def __str__(self):
        base = super().__str__()
        return f"{base}\nDescubierto máximo: {self.descubierto_formateado}"


    @property
    def descubierto(self) -> float:
        return self.__descubierto
    

    @property
    def descubierto_formateado(self) -> str:
        return f'${self.__descubierto:.2f}'


    @staticmethod
    def __validar_descubierto(valor: float) -> float:
        v = a_numero(valor)
        if v < 0:
            print("El descubierto no puede ser negativo.")
            return 0.0
        return v
    

    def cambiar_descubierto(self, nuevo_valor: float) -> None:
        self.__descubierto = CuentaCorriente.__validar_descubierto(nuevo_valor)
        print(f"Nuevo descubierto máximo: {self.descubierto_formateado}")


    def extraer(self, monto: float) -> bool:
        monto = pedir_monto_hasta_valido(monto)
        saldo_actual = self.saldo
        limite = saldo_actual + self.__descubierto
        if monto > limite:
            print("Limite de descubierto excedido.")
            return False
        self._Cuenta__saldo = saldo_actual - monto
        self._Cuenta__imprimir_evento_linea("Extracción", monto)
        return True


# ----------------------------- Caja de Ahorro -------------------------------
class CuentaAhorro(Cuenta):
    pass


# --------------------------------- Programa ---------------------------------
cuenta_2 = CuentaCorriente(
    numero_cuenta="12345678901234",
    titular="Juan Perez",
    cuil="20-12345678-9",
    cbu="1234567890123456789012",
    alias="juan.perez",
    saldo=1000.0,
    descubierto=500.0
)

print(cuenta_1)
