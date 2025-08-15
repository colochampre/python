# Ejercicio 3.1 - if sin else
num = int(input("Ingrese un numero: "))

if num > 10:
    print(f"El numero {num} es mayor que 10")

# Ejercicio 3.2 - if con else
num = int(input("Ingrese un numero: "))

if num % 2 == 0:
    print(f"El numero {num} es par")
else:
    print(f"El numero {num} es impar")

# Ejercicio 3.3 - if anidado
nota = int(input("Ingrese un numero (0-100): "))

if nota >= 0 and nota <= 100:
    if nota >= 70:
        print("Aprobado", end=" ")
        if nota >= 90:
            print("con honores")
    else:
        print("Desaprobado")
else:
    print(f"El numero {nota} no esta entre 0 y 100")
