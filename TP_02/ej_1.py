# -------------------------------- Utilidades --------------------------------
def limpiar_texto(valor) -> str:
    """A texto, sin espacios a los bordes; None -> ''."""
    return "" if valor is None else str(valor).strip()

def colapsar_espacios(s: str) -> str:
    return " ".join(limpiar_texto(s).split())

def solo_digitos(s: str) -> str:
    """Solo 0-9 (quita puntos, guiones, espacios, etc.)."""
    return "".join(ch for ch in str(s) if ch.isdigit())

def a_numero(valor) -> float:
    try:
        return float(str(valor).replace(",", "."))
    except ValueError:
        raise ValueError("Número inválido")

def es_cadena_n_digitos(s: str, n: int) -> bool:
    return len(s) == n and s.isdigit()

def es_enumerado(valor: str, dominio: set[str]) -> bool:
    return limpiar_texto(valor).upper() in dominio

def es_monto_no_cero(x: float) -> bool:
    """True si |x| > 0."""
    return abs(x) > 0

def validar_numero_cuenta14(s: str) -> str:
    """14 dígitos exactos, sin separadores."""
    d = solo_digitos(s)
    if not es_cadena_n_digitos(d, 14):
        raise ValueError("numero_cuenta debe tener 14 dígitos (0 -9).")
    return d

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
        raise ValueError("cuil debe tener 11 dígitos.")
    return d

_ALIAS_RE = re.compile(r"^[A-Za-z0-9.\-]{6,20}$")

def validar_alias(s: str) -> str:
    """6–20 chars alfanuméricos, punto o guion."""
    s = limpiar_texto(s)
    if not _ALIAS_RE.fullmatch(s):
        raise ValueError("alias inválido: 6-20 [A-Za-z0-9 . -].")
    return s

def validar_monto_no_cero(monto) -> float:
    """Convierte y valida que el valor absoluto sea > 0. Devuelve float."""
    x = a_numero(monto)
    if not es_monto_no_cero(x):
        raise ValueError("El monto debe ser distinto de 0.")
    return x

# ------------------------------- Clase Cuenta -------------------------------
class Cuenta:
    def __init__(self, numero_cuenta, titular, cuil, cbu, alias, saldo):
        self.__numero_cuenta = validar_numero_cuenta14(numero_cuenta) # 14 dígitos numéricos
        self.__titular = str(titular) # 1-100 caracteres
        self.__cuil = str(cuil) # xx-xxxxxxxx-x
        self.__cbu = str(cbu) # 22 dígitos numéricos
        self.__alias = str(alias) # 3-20 caracteres
        self.__saldo = float(saldo)

    def __str__(self):
        return f"{self.numero_cuenta}, {self.titular}, {self.__cuil}, {self.__cbu}, {self.__alias}, {self.__saldo}"

    # Getters
    @property
    def numero_cuenta(self) -> str:
        return f'CA ${self.__numero_cuenta}'

    @property
    def titular(self) -> str:
        return " ".join(p.capitalize() for p in self.__titular.split())

    @property
    def cuil(self) -> str:
        ''' Devuelve "AA-BBBBBBBB-C" a partir de 11 digitos'''
        a = self.digitos[:2]
        b = self.digitos[2:10]
        c = self.digitos[10]
        return f'{a}-{b}-{c}'
        
    @property
    def cbu(self) -> str:
        return self.__cbu

    @property
    def alias(self) -> str:
        return self.__alias

    @property
    def saldo(self) -> float:
        return self.__saldo

    # Setters
    @numero_cuenta.setter
    def numero_cuenta(self, nuevo_numero_cuenta):
        self.__numero_cuenta = validar_numero_cuenta14(nuevo_numero_cuenta)

    @titular.setter
    def titular(self, nuevo_titular):
        self.__titular = normalizar_titular(nuevo_titular)

cuenta_1 = Cuenta('e', '', '39999999', '123456789012345678901234', 'JUAN.PEREZ', 0.0)

print(cuenta_1)
