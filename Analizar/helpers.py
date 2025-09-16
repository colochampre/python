# utilidades varias: tomar fecha del sistema,
# limpiar texto para asegurar strings,
# colapsar espacios para que entre palabras hay un solo espacio,
# pasar a número para preparar un string previo a convertirlo en float,
# solo dígitos para descartar cualquir caracter que no sea dígito

from datetime import datetime


def ahora_str() -> str:
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


def limpiar_texto(valor=None) -> str:
    return "" if valor is None else str(valor).strip()


def colapsar_espacios(valor: str) -> str:
    return " ".join(str(valor).split())


def pasar_a_numero(valor) -> float:
    s = str(valor).replace(",", ".")
    try:
        return float(s)
    except (ValueError, TypeError):
        return 0.0


def solo_digitos(valor) -> str:
    return "".join(ch for ch in str(valor) if ch.isdigit())

