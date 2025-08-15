# Ejercicio 6.1 - Menú de validación
def menu():
    while True:
        print("""
        Menu
        1. Edad
        2. Nombre
        3. Carrera
        0. Salir
        """)
        opcion = int(input("Ingrese una opcion: "))

        match opcion:
            case 0:
                break
            case 1:
                try:
                    edad = int(input("Ingrese su edad: "))
                    if edad > 0 and edad < 120:
                        print("Edad validada")
                    else:
                        print("Edad fuera de rango")
                except ValueError:
                    print("Error: Entrada invalida")
            case 2:
                nombre = input("Ingrese su nombre: ").strip()
                if nombre:
                    print("Nombre validado")
                else:
                    print("Error: Nombre vacío")
            case 3:
                carrera = input("Ingrese su carrera: ").strip()
                if carrera:
                    print("Carrera validada")
                else:
                    print("Error: Carrera vacía")
            case _:
                print("Opcion no disponible")

    print("Saliendo...")

menu()