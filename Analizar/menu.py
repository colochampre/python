from cliente import PersonaFisica, Empresa
from cuenta import CuentaAhorro, CuentaCorriente


def construir_cliente():
    print("=== CLIENTE ===")
    print("1) Persona Física")
    print("2) Empresa")
    tipo = input("Elegí tipo (1/2): ").strip()

    if tipo == "2":
        nombre_juridico = input("Razón Social: ")
        nombre_fantasia = input("Nombre de fantasía: ")
        cuil = input("CUIL: ")
        mail = input("Mail: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        return Empresa(mail=mail, telefono=telefono, direccion=direccion, nombre_fantasia=nombre_fantasia, nombre_juridico=nombre_juridico, cuil=cuil)
    else:
        nombre = input("Nombre: ")
        cuil = input("CUIL: ")
        mail = input("Mail: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        dni = input("DNI: ")
        return PersonaFisica(nombre=nombre, cuil=cuil, mail=mail, telefono=telefono, direccion=direccion, dni=dni)


def construir_cuenta(cliente):
    print("\n=== CUENTA ===")
    print("1) Caja de Ahorro")
    print("2) Cuenta Corriente")
    tipo = input("Elegí tipo (1/2): ").strip()
    numero = input("Número de cuenta (14 dígitos): ")
    cbu = input("CBU (22 dígitos): ")
    alias = input("Alias (6..20): ")
    saldo = input("Saldo inicial (>= 0): ")

    if tipo == "2":
        descubierto = input("Descubierto (>= 0): ")
    else:
        descubierto = None

    if tipo == "2":
        return CuentaCorriente(numero, cbu, alias, cliente, saldo, descubierto)
    else:
        return CuentaAhorro(numero, cbu, alias, cliente, saldo)


def menu_operaciones(cuenta):
    print("\n>>> Cuenta creada.")
    print(cuenta)
    print(cuenta.detalle_producto())

    while True:
        print("\n=== MENÚ OPERACIONES ===")
        print("1) Ver datos de la cuenta")
        print("2) Ver saldo")
        print("3) Depositar")
        print("4) Extraer")
        print("5) Cambiar alias")
        print("6) Ver movimientos")
        if hasattr(cuenta, "cambiar_descubierto"):
            print("7) Cambiar descubierto")
        print("0) Salir")

        op = input("Opción: ").strip()
        print()
        
        if op == "1":
            cuenta.informe_datos()
        elif op == "2":
            cuenta.ver_saldo()
        elif op == "3":
            monto = input("Monto a depositar: ")
            cuenta.depositar(monto)
        elif op == "4":
            monto = input("Monto a extraer: ")
            cuenta.extraer(monto)
        elif op == "5":
            nuevo = input("Nuevo alias: ")
            cuenta.alias = nuevo
        elif op == "6":
            cuenta.ver_movimientos()
        elif op == "7" and hasattr(cuenta, "cambiar_descubierto"):
            nuevo = input("Nuevo descubierto: ")
            cuenta.cambiar_descubierto(nuevo)
        elif op == "0":
            print("Fin.")
            break
        else:
            print("Opción inválida.")


def run_menu():
    cliente = construir_cliente()
    cuenta = construir_cuenta(cliente)
    menu_operaciones(cuenta)
