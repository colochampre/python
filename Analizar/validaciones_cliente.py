# Validaciones de datos de entrada de la cuenta Cliente
# Por un lado, funciones booleanas es_xxx_valido(valor) -> bool
# Por otro, funciones pedir_xxx_hasta_valido(valor_inicial) -> valor_valido
# que usan las funciones booleanas para repetir el pedido hasta
# que se ingresa un valor válido
# Los separamos por clase para mejor visualización

from helpers import limpiar_texto, colapsar_espacios, solo_digitos


def es_nombre_valido(valor=None) -> bool:
    permitidos = set(
       "abcdefghijklmnopqrstuvwxyz"
       "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
       "áéíóúüñÁÉÍÓÚÜÑ"
       "àèìòùÀÈÌÒÙ"
       "âêîôûÂÊÎÔÛ"
       "äëïöüÿÄËÏÖÜŸ"
       "ãõÃÕ"
       "çÇ"
       " -'."
    )
    if valor is None:
        return False
    if 2 <= len(valor) <= 50:
        return all(ch in permitidos for ch in valor)
    return False
    # El nombre puede tener letras (con tildes y eñes)
    # y algunos caracteres especiales
    # Se limita a 50 caracteres por abarcar la mayoria de los casos prácticos


def es_cuil_valido(valor=None) -> bool:
    if valor is None:
        return False
    return len(valor) == 11 and valor.isdigit()
    # El CUIL es un número de 11 dígitos sin guiones ni espacios


def es_mail_valido(valor=None) -> bool:
    if valor is None:
        return False
    return 5 <= len(valor) <= 120 and ("@" in valor and "." in valor)
    # Un mail se construye con el esquema local@dominio
    # El estándar RFC 5321 define un máximo de 64 caracteres para local
    # y un máximo de 255 caracteres para dominio. Total 232 por el @
    # Aquí se limita a 120 caracteres que cubre la mayoria
    # de los casos prácticos


def es_telefono_valido(valor=None) -> bool:
    if valor is None:
        return False
    return 8 <= len(valor) <= 15 and str(valor).isdigit()
# La UIT-T define la recomendación E.164 con un máximo de 15 dígitos
# sin contar el + y un mínimo de 8 dígitos (sin contar el código de país)


def es_direccion_valida(valor=None) -> bool:
    permitidos = set(
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "01234567890"
        "áéíóúüñÁÉÍÓÚÜÑ"
        "àèìòùÀÈÌÒÙ"
        "âêîôûÂÊÎÔÛ"
        "äëïöüÿÄËÏÖÜŸ"
        "ãõÃÕ"
        "çÇ"
        " -'."
        ",#º°/"
    )
    if valor is None:
        return False
    if 2 <= len(valor) <= 120:
        return all(ch in permitidos for ch in valor)
    return False
    # La dirección en cualquier parte del mundo puede tener
    # letras (con tildes y eñes), números y varios caracteres especiales
    # Se limita a 120 caracteres por abarcar la mayoria de los casos prácticos


def es_dni_valido(valor=None) -> bool:
    if valor is None:
        return False
    return len(valor) in (6, 7, 8) and valor.isdigit()
    # El DNI en Argentina tiene 6 o 8 dígitos sin puntos ni espacios


# ---- pedir hasta válido individuales ----
# ---- CLiente(nombre, cuil, mail, telefono, dirección) ----
def pedir_nombre_hasta_valido(valor=None) -> str:
    nombre = colapsar_espacios(limpiar_texto(valor))
    while not es_nombre_valido(nombre):
        print("Nombre inválido.")
        nombre = input("Vuelva a intentarlo: ")
        nombre = colapsar_espacios(limpiar_texto(nombre))
    return nombre.upper()
    # Se devuelve con la primera letra de cada palabra en mayúscula


def pedir_cuil_hasta_valido(valor=None) -> str:
    cuil = solo_digitos(limpiar_texto(valor))
    while not es_cuil_valido(cuil):
        print("CUIL inválido.")
        cuil = input("CUIL (11 dígitos, sin guiones ni espacios): ")
        cuil = solo_digitos(limpiar_texto(cuil))
    return cuil


def pedir_mail_hasta_valido(valor=None) -> str:
    mail = limpiar_texto(valor)
    while not es_mail_valido(mail):
        print("Mail inválido.")
        mail = limpiar_texto(input("Vuelva a intentarlo: "))
    return mail.lower()


def pedir_telefono_hasta_valido(valor=None) -> str:
    telefono = solo_digitos(limpiar_texto(valor))
    while not es_telefono_valido(telefono):
        print("Teléfono inválido.")
        telefono = solo_digitos(limpiar_texto(input("Vuelva a intentarlo: ")))
    return telefono


def pedir_direccion_hasta_valida(valor=None) -> str:
    direccion = colapsar_espacios(limpiar_texto(valor))
    while not es_direccion_valida(direccion):
        print("Dirección inválida.")
        direccion = input("Vuelva a intentarlo: ")
        direccion = colapsar_espacios(limpiar_texto(direccion))
    return direccion.upper()


def pedir_dni_hasta_valido(valor=None) -> str:
    dni = solo_digitos(limpiar_texto(valor))
    while not es_dni_valido(dni):
        print("DNI inválido.")
        dni = input("DNI (6 a 8 dígitos, sin puntos ni espacios): ")
        dni = solo_digitos(limpiar_texto(dni))
    return dni

# --- pedir hasta válido genérico (loop sin exceptions hacia afuera) ---
# def pedir_hasta_valido(msg_inicial, msg_error, fn_valida, postproc=lambda x: x):
#     valor = postproc(input(msg_inicial))
#     while not fn_valida(valor):
#         print(msg_error)
#         valor = postproc(input("Vuelva a intentarlo: "))
#     return valor
