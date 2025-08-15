import math

# Ejercicio 5.1 - Círculo
pi = math.pi
radio = float(input("Ingrese el radio del circulo: "))

area = pi * radio ** 2
perimetro = 2 * pi * radio

print(f"Area: {area}")
print(f"Perimetro: {perimetro}")

# Ejercicio 5.2 - Triangulo (base y altura)
base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))

if base > 0 and altura > 0:
    area = (base * altura) / 2
    perimetro = base + altura + math.sqrt(base ** 2 + altura ** 2)

    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")
else:
    print("Los valores de la base y la altura deben ser mayores a 0")

# Ejercicio 5.3 - Rectángulo
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

if base > 0 and altura > 0:
    area = base * altura
    perimetro = 2 * (base + altura)

    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")
else:
    print("Los valores de la base y la altura deben ser mayores a 0")
