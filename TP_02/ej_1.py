import re
from datetime import datetime


# -------------------------------- Utilidades --------------------------------
def limpiar_texto(valor) -> str:
    """A texto, sin espacios a los bordes; None -> ''."""
    return "" if valor is None else str(valor).strip()


def colapsar_espacios(s: str) -> str:
    return " ".join(s.split())


def solo_digitos(s: str) -> str:
    """Solo 0-9 (quita puntos, guiones, espacios, etc.)."""
    return "".join(ch for ch in str(s) if ch.isdigit())


def es_cadena_n_digitos(s: str, n: int) -> bool:
    return len(s) == n and s.isdigit()


def es_nombre_valido(s: str) -> bool:
    if not (1 <= len(s) <= 100):
        return False
    permitidos = set(" -'áéíóúÁÉÍÓÚñÑ")
    return all(ch.isalpha() or ch in permitidos for ch in s)


_ALIAS_RE = re.compile(r"^[A-Za-z0-9.\-]{6,20}$")


def es_alias_valido(s: str) -> bool:
    return _ALIAS_RE.fullmatch(s)


def a_numero(valor) -> float:
    try:
        return float(str(valor).replace(",", "."))
    except ValueError:
        return 0.0


def es_monto_no_cero(x: float) -> bool:
    return x > 0


def pedir_numero_cuenta_hasta_valido(valor_inicial=None, input_fn=input) -> str:
    d = colapsar_espacios(limpiar_texto(valor_inicial))
    while not es_cadena_n_digitos(d, 14):
        if d:
            print("El numero de cuenta debe tener 14 dígitos (0-9).")
        d = solo_digitos(limpiar_texto(input_fn("Ingrese el numero de cuenta (14 dígitos): ")))
    return d.upper()


def pedir_titular_hasta_valido(valor_inicial=None, input_fn=input) -> str:
    s = colapsar_espacios(limpiar_texto(valor_inicial)) # reutilizamos
    while not es_nombre_valido(s):
        if s:
            print("Nombre inválido: use letras, espacios, '-' o ''', hasta 100 caracteres.")
        s = colapsar_espacios(limpiar_texto(input_fn("Ingrese nombre completo: ")))
    return s.upper()


def pedir_cuil_hasta_valido(valor_inicial=None, input_fn=input) -> str:
    d = solo_digitos(limpiar_texto(valor_inicial))
    while not es_cadena_n_digitos(d, 11):
        if d:
            print("El CUIL debe tener 11 dígitos (0-9).")
        d = solo_digitos(limpiar_texto(input_fn("Ingrese el CUIL (11 dígitos): ")))
    return d


def pedir_cbu_hasta_valido(valor_inicial=None, input_fn=input) -> str:
    s = solo_digitos(limpiar_texto(valor_inicial))
    while not es_cadena_n_digitos(s, 22):
        if s:
            print("El CBU debe tener 22 dígitos (0-9).")
        s = solo_digitos(limpiar_texto(input_fn("Ingrese el CBU (22 dígitos): ")))
    return s


def pedir_alias_hasta_valido(valor_inicial=None, input_fn=input) -> str:
    s = colapsar_espacios(limpiar_texto(valor_inicial))
    while not es_alias_valido(s):
        if s:
            print("Alias inválido: 6-20 [A-Za-z0-9 . -].")
        s = colapsar_espacios(limpiar_texto(input_fn("Ingrese el alias: ")))
    return s


def pedir_monto_hasta_valido(valor_inicial=None, input_fn=input) -> float:
    if valor_inicial is not None:
        m = a_numero(valor_inicial)
        if es_monto_no_cero(m):
            return m
    while True:
        valor_ingresado = input_fn("Ingrese monto (positivo o negativo, ≠ 0):")
        m = a_numero(valor_ingresado)
        if es_monto_no_cero(m):
            return m
        print("Monto inválido. Debe ser distinto de 0.")


def normalizar_titular(s: str) -> str:
    """Guarda MAYÚSCULAS; Longitud 1..100; colapsa espacios."""
    s = colapsar_espacios(s)
    if not (1 <= len(s) <= 100):
        raise ValueError("titular inválido: 1-100 caracteres.")
    permitidos = set(" -'áéíóúÁÉÍÓÚñÑ")
    if not all(ch.isalpha() or ch in permitidos for ch in s):
        raise ValueError("titular inválido: use letras, espacios, ' -' o '''.")
    return s.upper()


def normalizar_cuil(s: str) -> str:
    """Devuelve 11 dígitos (sin separadores)."""
    d = solo_digitos(s)
    if not es_cadena_n_digitos(d, 11):
        raise ValueError("El CUIL debe tener 11 dígitos.")
    return d


def ahora_str() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M')


# ------------------------------- Clase Cuenta -------------------------------
class Cuenta:
    def __init__(self, numero_cuenta, titular, cuil, cbu, alias, saldo):
        self.__numero_cuenta = pedir_numero_cuenta_hasta_valido(numero_cuenta) # 14 dígitos numéricos
        self.__titular = pedir_titular_hasta_valido(titular) # 1-100 caracteres
        self.__cuil = pedir_cuil_hasta_valido(cuil) # xx-xxxxxxxx-x
        self.__cbu = pedir_cbu_hasta_valido(cbu) # 22 dígitos numéricos
        self.__alias = pedir_alias_hasta_valido(alias) # 6-20 caracteres
        self.__saldo = pedir_monto_hasta_valido(saldo)


    def __str__(self):
        return f"Titular: {self.titular} - CUIL: {self.cuil_formateado}\n"\
        f"N° de cuenta: {self.numero_cuenta_formateado} - Alias: {self.alias} - CBU: {self.cbu}"


    # Getters
    @property
    def numero_cuenta(self) -> str:
        return self.__numero_cuenta


    @property
    def titular(self) -> str:
        return " ".join(p.capitalize() for p in self.__titular.split())


    @property
    def cuil(self) -> str:
        return self.__cuil


    @property
    def cuil_formateado(self) -> str:
        return Cuenta.formatear_cuil(self.__cuil)
        
    
    @property
    def cbu(self) -> str:
        return self.__cbu


    @property
    def alias(self) -> str:
        return self.__alias


    @property
    def saldo(self) -> float:
        return self.__saldo


    @staticmethod
    def formatear_cuil(digitos:str) -> str:
        """Devuelve 'AA-BBBBBBBB-C' a partir de 11 dígitos."""
        a = digitos[:2]
        b = digitos[2:10]
        c = digitos[10]
        return f'{a}-{b}-{c}'


    @staticmethod
    def formatear_numero_cuenta(digitos:str) -> str:
        return f'CA $ {digitos}'


    @property
    def titular(self):
        return self.__titular


    @property
    def cuil(self):
        return self.__cuil


    # Metodos
    @staticmethod
    def imprimir_evento_linea(motivo: str, monto: float) -> str:
        return f"Fecha: {ahora_str()} – Motivo: {motivo} – Importe: {monto:.2f}"


    def retirar_monto(self):
        monto = pedir_monto_hasta_valido()
        if monto > self.saldo:
            print("Error: Saldo insuficiente")
        else:
            self.__saldo -= monto
            print(self.imprimir_evento_linea("Retiro", monto))


    def depositar_monto(self):
        monto = pedir_monto_hasta_valido()
        if monto < 0:
            print("Error: Monto inválido")
        else:
            self.__saldo += monto
            print(self.imprimir_evento_linea("Depósito", monto))

    def consultar_saldo(self): # Nombre del titular: XXXX – N° de cuenta: CA $ XXXX – Saldo: XXXX.XX
        print(f"Nombre del titular: {self.titular} – N° de cuenta: CA $ {self.formatear_numero_cuenta(self.numero_cuenta)} – Saldo: ${self.saldo:.2f}")


# --------------------------------- Programa ---------------------------------
cuenta_1 = Cuenta('21100000000037', '', '22399999993', '0110030330123456749017', 'a', '1000.0')


def mostrar_menu():
    print("\nMenu")
    print("1. Consultar datos de la cuenta")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Consultar saldo")
    print("5. Salir", end="\n\n")


while True:
    mostrar_menu()
    opcion = input("Ingrese una opcion (1-5): ")
    if opcion == "1":
        print(cuenta_1)
    elif opcion == "2":
        cuenta_1.retirar_monto()
    elif opcion == "3":
        cuenta_1.depositar_monto()
    elif opcion == "4":
        cuenta_1.consultar_saldo()
    elif opcion == "5":
        break
    else:
        print("Opcion no valida")
