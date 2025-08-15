import math

# Ejercicio 6.2 - Calculadora de áreas y perímetros
def menu():
    area = 0
    perimetro = 0

    while True:
        print("""
        Menu
        1. Circulo
        2. Triangulo
        3. Rectangulo
        0. Salir
        """)

        try:
            opcion = input("Ingrese una opcion: ")
        except ValueError:
            print("Error: Entrada invalida")
            continue

        match opcion:
            case "0":
                break
            case "1":
                try:
                    radio = float(input("Ingrese el radio del circulo: "))
                except ValueError:
                    print("Error: Entrada invalida")
                    continue
                if radio > 0:
                    area = math.pi * radio ** 2
                    perimetro = 2 * math.pi * radio
                else:
                    print("Error: El radio debe ser mayor a 0")
            
            case "2":
                try:
                    base = float(input("Ingrese la base del triangulo: "))
                    altura = float(input("Ingrese la altura del triangulo: "))
                except ValueError:
                    print("Error: Entrada invalida")
                    continue
                if base > 0 and altura > 0:
                    area = (base * altura) / 2
                    perimetro = base + altura + math.sqrt(base ** 2 + altura ** 2)
                else:
                    print("Error: La base y la altura deben ser mayores a 0")
            case "3":
                try:
                    base = float(input("Ingrese la base del rectangulo: "))
                    altura = float(input("Ingrese la altura del rectangulo: "))
                except ValueError:
                    print("Error: Entrada invalida")
                    continue
                if base > 0 and altura > 0:
                    area = base * altura
                    perimetro = 2 * (base + altura)
                else:
                    print("Error: La base y la altura deben ser mayores a 0")
            case _:
                print(f"Opcion '{opcion}' no disponible")

        if area > 0 and perimetro > 0:
            print(f"Area: {area:.2f}")
            print(f"Perimetro: {perimetro:.2f}")

    print("Saliendo...")

menu()
