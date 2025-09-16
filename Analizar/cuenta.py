from cliente import Cliente

from helpers import ahora_str, pasar_a_numero 

from validaciones_cuenta import (
    pedir_alias_hasta_valido,
    pedir_cbu_hasta_valido,
    pedir_numero_cuenta_hasta_valido,
    pedir_saldo_inicial_hasta_valido,
    pedir_monto_hasta_valido
)


class Cuenta:
    def __init__(self, numero, cbu, alias, cliente: Cliente, saldo=0.0) -> None:
        self.__numero_cuenta = pedir_numero_cuenta_hasta_valido(numero)
        self.__cbu = pedir_cbu_hasta_valido(cbu)
        self.__alias = pedir_alias_hasta_valido(alias)
        self.__cliente = cliente
        self.__saldo = pedir_saldo_inicial_hasta_valido(saldo)

    # --- getters ---
    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def numero_cuenta_formateado(self):
        return f"$ {self.__numero_cuenta}"

    @property
    def cbu(self):
        return self.__cbu

    @property
    def alias(self):
        return self.__alias

    @property
    def cliente(self):
        return self.__cliente  # objeto Cliente

    @property
    def saldo(self):
        return self.__saldo

    @property
    def saldo_formateado(self):
        return f"${self.__saldo:.2f}"


    @alias.setter
    def alias(self, valor):
        self.__alias = valor

    def ver_saldo(self):
        print("#Consulta de saldo:")
        print(f"#Cliente: {self.cliente.nombre_formateado} – N°: {self.numero_cuenta_formateado}")
        print(f"#Saldo: {self.saldo_formateado}")
    
    def detalle_producto(self):
        return f"Producto: Cuenta."

    def informe_datos(self):
        print("Consulta de datos:")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"N°: {self.numero_cuenta_formateado} - Alias: {self.alias} - CBU: {self.cbu}")

    def __imprimir_movimiento(self, ch, monto):
        motivo = input("Motivo de la operación: ").strip()
        print(
            f"Movimiento ejecutado:\n"
            f"N° {self.numero_cuenta_formateado} - Cliente: {self.cliente.nombre_formateado}\n"
            f"Fecha: {ahora_str()} - Motivo: {motivo} - Monto: {ch}{monto:.2f}"
        )

    def depositar(self, monto) -> bool:
        mv = pedir_monto_hasta_valido(monto)
        self.__saldo += mv
        self.__imprimir_movimiento("+", mv)
        return True

    def extraer(self, monto) -> bool:
        mv = pedir_monto_hasta_valido(monto)
        if mv > self.__saldo:
            print("Fondos insuficientes.")
            return False
        self.__saldo -= mv
        self.__imprimir_movimiento("-", mv)
        return True

    def __str__(self) -> str:
        return (
            f"Cuenta N°: {self.__numero_cuenta} - CBU: {self.__cbu}\n"
            f"Alias: {self.__alias}\n"
            f"Cliente: {self.cliente.nombre_formateado}\n"
            f"Saldo: {self.saldo_formateado}"
            )


class CuentaAhorro(Cuenta):

    @property
    def numero_cuenta_formateado(self):
        return f"CA $ {self.numero_cuenta}"


class CuentaCorriente(Cuenta):
    def __init__(self, numero, cbu, alias, cliente, saldo=0.0, descubierto=0.0) -> None:
        super().__init__(numero, cbu, alias, cliente, saldo)
        self.__descubierto = self.__validar_descubierto(descubierto)

    @staticmethod
    def __validar_descubierto(valor) -> float:
        v = pasar_a_numero(valor)
        if v < 0.0:
            print("El descubierto no puede ser negativo. Se ajusta a 0.0")
            v = 0.0
        return v

    @property
    def numero_cuenta_formateado(self):
        return f"CC $ {self.numero_cuenta}"

    @property
    def descubierto(self):
        return self.__descubierto

    @property
    def descubierto_formateado(self):
        return f"${self.__descubierto:.2f}"

    def cambiar_descubierto(self, nuevo_valor):
        self.__descubierto = self.__validar_descubierto(nuevo_valor)
        print(f"Nuevo descubierto: {self.descubierto_formateado}")

    def extraer(self, monto) -> bool:
        mv = pasar_a_numero(monto)
        while not (mv > 0.0):
            print("Ingrese un monto válido (> 0).")
            mv = pasar_a_numero(input("Vuelva a intentarlo: "))
        saldo_actual = self.saldo
        limite = saldo_actual + self.__descubierto
        if mv > limite:
            print("Límite de descubierto excedido.")
            return False

        # Ajuste del saldo y salida formateada (usa helpers de base)
        self._Cuenta__saldo = saldo_actual - mv
        super()._Cuenta__imprimir_movimiento("-", mv)
        return True

    def detalle_producto(self):
        return f"Producto: Cuenta Corriente (descubierto {self.descubierto_formateado})."

    def informe_datos(self):
        print("Consulta de datos:")
        print(f"Cliente: {self.cliente.nombre_formateado}")
        print(f"CUIL: {self.cliente.cuil_formateado}")
        print(f"N°: {self.numero_cuenta_formateado} - Alias: {self.alias} - CBU: {self.cbu}")

    def ver_saldo(self):
        print("#Consulta de saldo:")
        print(f"#Cliente: {self.cliente.nombre_formateado} – N°: {self.numero_cuenta_formateado}")
        print(f"#Saldo: {self.saldo_formateado} – Descubierto: {self.descubierto_formateado}")
