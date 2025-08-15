# Ejercicio 4.1 - for con paso positivo
for i in range(5, 21, 3):
    print(i, end=" ")

print("\n")

# Ejercicio 4.2 - for con paso negativo
for i in range(10, 0, -1):
    print(i, end=" ")

print("\n")

# Ejercicio 4.3 - while
contador = 0
num = int(input("Ingrese un numero (0 para salir): "))
while True:
    if num == 0:
        break
    contador += 1
    num = int(input("Ingrese un numero (0 para salir): "))

print(f"Cantidad de numeros ingresados distintos de 0: {contador}")
