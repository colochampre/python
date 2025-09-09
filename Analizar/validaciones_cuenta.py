# Validaciones de datos de entrada
# Por un lado, funciones booleanas es_xxx_valido(valor) -> bool
# Por otro, funciones pedir_xxx_hasta_valido(valor_inicial) -> valor_valido
# que usan las funciones booleanas para repetir el pedido hasta
# que se ingresa un valor válido
# Los separamos por clase para mejor visualizacion

from helpers import limpiar_texto, solo_digitos


# --- cuentas ---
def es_numero_cuenta_valido(valor=None) -> bool:
    if valor is None:
        return False
    return len(valor) == 14 and valor.isdigit()


def es_cbu_valido(valor=None) -> bool:
    if valor is None:
        return False
    return len(valor) == 22 and valor.isdigit()


def es_alias_valido(valor=None) -> bool:
    if valor is None:
        return False
    if 6 <= len(valor) <= 20:
        if all(ch.isalnum() or ch in "-." for ch in valor):
            return True
    return False


def es_monto_valido(valor=None) -> bool:
    try:
        return float(valor) > 0.0
    except (ValueError, TypeError):
        return False


def es_saldo_inicial_valido(valor) -> bool:
    try:
        return float(valor) >= 0.0
    except (ValueError, TypeError):
        return False


# --- pedir hasta válido individuales ----
# --- Cuenta(numero, cbu, alias, saldo) ---
def pedir_numero_cuenta_hasta_valido(valor=None) -> str:
    numero = solo_digitos(limpiar_texto(valor))
    while not es_numero_cuenta_valido(numero):
        print("Número de cuenta inválido.")
        numero = input("Vuelva a intentarlo: ")
        numero = solo_digitos(limpiar_texto(numero))
    return numero


def pedir_cbu_hasta_valido(valor=None) -> str:
    cbu = solo_digitos(limpiar_texto(valor))
    while not es_cbu_valido(cbu):
        print("CBU inválido.")
        cbu = input("Vuelva a intentarlo: ")
        cbu = solo_digitos(limpiar_texto(cbu))
    return cbu


def pedir_alias_hasta_valido(valor=None) -> str:
    alias = limpiar_texto(valor)
    while not es_alias_valido(alias):
        print("Alias inválido.")
        alias = input("Vuelva a intentarlo: ")
        alias = limpiar_texto(alias)
    return alias


def pedir_monto_hasta_valido(valor=None) -> float:
    monto = limpiar_texto(valor)
    while not es_monto_valido(monto):
        print("Monto inválido.")
        monto = input("Vuelva a intentarlo: ")
        monto = limpiar_texto(monto)
    return float(monto)


def pedir_saldo_inicial_hasta_valido(valor=None) -> float:
    saldo = limpiar_texto(valor)
    while not es_saldo_inicial_valido(saldo):
        print("Saldo inicial inválido.")
        saldo = input("Vuelva a intentarlo: ")
        saldo = limpiar_texto(saldo)
    return float(saldo)


# --- pedir hasta válido genérico (loop sin exceptions hacia afuera) ---
# def pedir_hasta_valido(msg_inicial, msg_error, fn_valida, postproc=lambda x: x):
#     valor = postproc(input(msg_inicial))
#     while not fn_valida(valor):
#         print(msg_error)
#         valor = postproc(input("Vuelva a intentarlo: "))
#     return valor
