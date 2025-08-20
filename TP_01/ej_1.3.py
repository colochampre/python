# Ejercicio 1.3 - Definición de clases
class Dispositivo:
    def __init__(self, marca:str, modelo:str, anio:int, precio:float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

# Instanciar una lista de 6 dispositivos
dispositivos = [
    Dispositivo("Marca A", "A", 2020, 1000),
    Dispositivo("Marca A", "B", 2021, 1200),
    Dispositivo("Marca B", "M1", 2022, 1100),
    Dispositivo("Marca C", "A1", 2023, 1400),
    Dispositivo("Marca C", "A2", 2024, 1600),
    Dispositivo("Marca D", "Mk1", 2025, 2100)
]

# Mostrar la lista de dispositivos y sus precios
print("Dispositivos (Modelo, Precio):")
for i in dispositivos:
    print(f"{i.modelo}, ${i.precio:.0f}")
