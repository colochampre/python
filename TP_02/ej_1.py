import re

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

def pedir_numero_cuenta_hasta_valido(valor_inicial=None, input_fn=input) -> str:
    d = colapsar_espacios(limpiar_texto(valor_inicial))
    while not es_cadena_n_digitos(d, 14):
        if d:
            print("El numero de cuenta debe tener 14 dígitos (0-9).")
        d = solo_digitos(limpiar_texto(input_fn("Ingrese el numero de cuenta (14 dígitos): ")))
    return d.upper()

def es_nombre_valido(s: str) -> bool:
    if not (1 <= len(s) <= 100):
        return False
    permitidos = set(" -'áéíóúÁÉÍÓÚñÑ")
    return all(ch.isalpha() or ch in permitidos for ch in s)

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

_ALIAS_RE = re.compile(r"^[A-Za-z0-9.\-]{6,20}$")

def validar_alias(s: str) -> str:
    """6-20 chars alfanuméricos, punto o guion."""
    s = limpiar_texto(s)
    if not _ALIAS_RE.fullmatch(s):
        raise ValueError("Alias inválido: 6-20 [A-Za-z0-9 . -].")
    return s

def a_numero(valor) -> float:
    try:
        return float(str(valor).replace(",", "."))
    except ValueError:
        return 0.0

def es_monto_no_cero(x: float) -> bool:
    """True si |x| > 0."""
    return abs(x) > 0

def pedir_monto_hasta_valido(valor_inicial=None, input_fn=input) -> float:
    m = a_numero(valor_inicial)
    while not es_monto_no_cero(m):
        if str(valor_inicial) not in (None, "", "0", "0.0"):
            print("Monto inválido. Debe ser distinto de 0.")
        valor_inicial = input_fn("Ingrese monto (positivo o negativo, ≠ 0):")
    m = a_numero(valor_inicial)
    return m

# ------------------------------- Clase Cuenta -------------------------------
class Cuenta:
    def __init__(self, numero_cuenta, titular, cuil, cbu, alias, saldo):
        self.__numero_cuenta = pedir_numero_cuenta_hasta_valido(numero_cuenta) # 14 dígitos numéricos
        self.__titular = pedir_titular_hasta_valido(titular) # 1-100 caracteres
        self.__cuil = pedir_cuil_hasta_valido(cuil) # xx-xxxxxxxx-x
        self.__cbu = pedir_cbu_hasta_valido(cbu) # 22 dígitos numéricos
        self.__alias = validar_alias(alias) # 3-20 caracteres
        self.__saldo = pedir_monto_hasta_valido(saldo)

    def __str__(self):
        return f"Titular: {self.titular} - CUIL: {self.cuil_formateado}\n"\
        f"N° de cuenta: {self.numero_cuenta_formateado} - Alias: {self.alias} - CBU: {self.cbu}"

    # Getters
    @property
    def numero_cuenta(self) -> str:
        return self.__numero_cuenta

    @property
    def numero_cuenta_formateado(self) -> str:
        return Cuenta.formatear_numero_cuenta(self.__numero_cuenta)

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

    @property
    def saldo_formateado(self) -> str:
        return f"${self.__saldo:.2f}"

    @staticmethod
    def formatear_cuil(digitos:str) -> str:
        """Devuelve 'AA-BBBBBBBB-C' a partir de 11 dígitos."""
        a = digitos[:2]
        b = digitos[2:10]
        c = digitos[10]
        return f'{a}-{b}-{c}'

    @staticmethod
    def formatear_numero_cuenta(digitos:str) -> str:
        return f'CA ${digitos}'

    # Setters
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nuevo_titular):
        self.__titular = normalizar_titular(nuevo_titular)

    @property
    def cuil(self):
        return self.__cuil

    @cuil.setter
    def cuil(self, nuevo_cuil):
        self.__cuil = normalizar_cuil(nuevo_cuil)

    # Metodos
    def retirar_monto(self):
        monto = float(input("Ingrese el monto a retirar: "))
        if monto > self.saldo:
            print("Error: Saldo insuficiente")
        else:
            self.__saldo -= monto
            self.informar_movimiento(monto)

    def depositar_monto(self):
        monto = float(input("Ingrese el monto a depositar: "))
        if monto < 0:
            print("Error: Monto inválido")
        else:
            self.__saldo += monto
            self.informar_movimiento(monto)

    def informar_movimiento(self, monto): # N° de cuenta: CA $ XXXX – Nombre del titular: XXXX – Fecha: XXXX – motivo: XXXX – Monto: XXXX
        print(f"N° de cuenta: {self.numero_cuenta_formateado} – Nombre del titular: {self.titular} – Fecha: {datetime.now().strftime('%Y-%m-%d')} – motivo: {monto} – Monto: {monto}")

# --------------------------------- Programa ---------------------------------
cuenta_1 = Cuenta('21100000000037', '', '', '0110030330123456749017', 'JAMON.JUGO.NUTRIA', '1000.0')

def mostrar_menu():
    print("\nMenu")
    print("1. Consultar datos de la cuenta")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Consultar saldo")
    print("5. Salir")
    return input("Ingrese una opcion: ")

while True:
    opcion = mostrar_menu()
    if opcion == "1":
        print(cuenta_1)
    elif opcion == "2":
        cuenta_1.retirar_monto()
    elif opcion == "3":
        cuenta_1.depositar_monto()
    elif opcion == "4":
        print(cuenta_1.saldo_formateado)
    elif opcion == "5":
        break
    else:
        print("Opcion no valida")
