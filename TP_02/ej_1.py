# -------------------------------- Utilidades --------------------------------
def limpiar_texto(valor) -> str:
    return ''if valor is None else str(valor).strip()

def es_numero_cuenta_valida(cuenta:str) -> bool:
    return len(cuenta) == 5 and cuenta.isdigit()

def pedir_numero_cuenta_valido(valor) -> str:
    s = limpiar_texto(valor)
    while not es_numero_cuenta_valida(s):
        if s:
            print('Error: El numero de cuenta debe tener 14 dígitos numéricos.')
        s = limpiar_texto(input('Ingrese numero de cuenta (14 dígitos numéricos): '))
    return s

def colapsar_espacios(texto:str) -> str:
    return ' '.join(texto.split())

def es_nombre_valido(nombre:str) -> bool:
    if not (3 <= len(nombre) <= 80):
        return False
    permitidos = set(" -'áéíóúÁÉÍÓÚüÜñÑ")
    return all(c.isalpha() or c in permitidos for c in nombre)

def pedir_nombre_valido(valor=None, input=input) -> str:
    s = colapsar_espacios(limpiar_texto(valor))
    while not es_nombre_valido(s):
        if s:
            print('Error: El nombre debe tener entre 1 y 100 caracteres y solo letras, espacios, guiones y apóstrofes.')
        s = colapsar_espacios(limpiar_texto(input('Ingrese nombre (1-100 caracteres): ')))
    return s

def solo_digitos(texto:str) -> str:
    return ''.join(c for c in texto if c.isdigit())

def es_identificador_11_valido(digitos:str) -> bool:    
    return len(digitos) == 11 and digitos.isdigit()

def pedir_identificador_11_valido(valor, input=input) -> str:
    d = solo_digitos(limpiar_texto(valor))
    while not es_identificador_11_valido(d):
        if d:
            print('Error: El identificador debe tener 11 dígitos numéricos.')
        d = solo_digitos(limpiar_texto(input('Ingrese identificador (11 dígitos numéricos): ')))
    return d

def es_cbu_valido(cbu:str) -> bool:
    return len(cbu) == 22 and cbu.isdigit()

def pedir_cbu_valido(valor) -> str:
    s = limpiar_texto(valor)
    while not es_cbu_valido(s):
        if s:
            print('Error: El CBU debe tener 22 dígitos numéricos.')
        s = limpiar_texto(input('Ingrese CBU (22 dígitos numéricos): '))
    return s

def a_numero(monto) -> float:
    try:
        return float(str(monto).replace(',', '.'))
    except ValueError:
        return 0.0 # Forzar error

def es_monto_no_cero(monto) -> bool:
    return abs(monto) >= 0.0

def pedir_monto_valido(valor, input=input) -> float:
    m = a_numero(valor)
    while not es_monto_no_cero(m):
        if str(valor). not in (None, '', '0', '0.0'):
            print('Error: El monto debe ser un número mayor a cero.')
        monto = input('Ingrese monto (mayor a cero): ')
        m = a_numero(monto)
    return m

def formatear_monto(monto:float) -> str:
    signo = '+' if monto >= 0 else '-'
    return f'{signo}{abs(monto):.2f}'

# ------------------------------- Clase Cuenta -------------------------------
class Cuenta:

    def __init__(self, numero_cuenta, titular, cuil, cbu, alias, saldo):
        self.__numero_cuenta = pedir_numero_cuenta_valido(numero_cuenta) # 5 dígitos numéricos
        self.__titular = str(titular) # 1-100 caracteres
        self.__cuil = str(cuil) # xx-xxxxxxxx-x
        self.__cbu = str(cbu) # 22 dígitos numéricos
        self.__alias = str(alias) # 3-20 caracteres
        self.__saldo = float(saldo)

    # Getters
    @property
    def numero_cuenta(self) -> str:
        return self.__numero_cuenta

    @property
    def numero_cuenta_formateada(self) -> str:
        return f'LEG-{self.__numero_cuenta}'

    @property
    def titular(self) -> str:
        return self.__titular

    @property
    def titular_formateado(self) -> str: # Capitaliza cada nombre del titular. Ej: Pepe Argento
        return " ".join(p.capitalize() for p in self.__titular.split())

    @property
    def cuil(self) -> str:
        return self.__cuil
        
    @property
    def cuil_formateado(self) -> str:
        ''' Devuelve "AA-BBBBBBBB-C" a partir de 11 digitos'''
        a = digitos[:2]
        b = digitos[2:10]
        c = digitos[10]
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
    @titular.setter
    def titular(self, nuevo_titular):
        self.__titular = nuevo_titular

    
