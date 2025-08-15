# Ejercicio 2.1 - Acumulador de suma
total = 0
for i in range(100): # 0-99
    total += i + 1   # 1-100
    
print(total)

# Ejercicio 2.2 - Contador de pares
pares = 0
nums = [1, 2, 3, 4, 5, 6]

for i in nums:
    if i % 2 == 0:
        pares += 1

print(f"Cantidad de pares: {pares}")

# Ejercicio 2.3 - Tabla de multiplicar
num = int(input("Ingrese un numero: "))

for i in range(10):
    print(f"{num}x{i + 1} = {num * (i + 1)}")
