# Ejercicio 2.1 - Atributos y formas recomendadas de accederlos
class Articulo:
    def __init__(self, nombre:str, precio:float, stock:int, categoria:str) -> None:
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

# Getters
    def getNombre(self) -> str:
        return self.nombre

    def getPrecio(self) -> float:
        return self.precio

    def getStock(self) -> int:
        return self.stock

    def getCategoria(self) -> str:
        return self.categoria

# Setters
    def setNombre(self, nuevo_nombre:str) -> None:
        self.nombre = nuevo_nombre

    def setPrecio(self, nuevo_precio:float) -> None:
        self.precio = nuevo_precio

    def setStock(self, nuevo_stock:int) -> None:
        self.stock = nuevo_stock

    def setCategoria(self, nueva_categoria:str) -> None:
        self.categoria = nueva_categoria

# Instanciar una lista de 5 articulos
articulos = [
    Articulo("Yerba", 3500.0, 50, "Alimentos"),
    Articulo("Arroz", 2300.0, 100, "Alimentos"),
    Articulo("Cafe", 8200.0, 100, "Alimentos"),
    Articulo("Detergente", 4200.0, 60, "Limpieza"),
    Articulo("Lavandina", 3000.0, 80, "Limpieza")
]

# Mostrar nombre de articulos por mas de $4000
PRECIO_CARO = 4000
articulos_caros = []

for i in articulos:
    if i.getPrecio() > PRECIO_CARO:
        articulos_caros.append(i.getNombre())

print(f"Articulos por mas de ${PRECIO_CARO}: {articulos_caros}")

# Cambiar el precio de un articulo
print(f"Antes: {articulos[0].getNombre()} ${articulos[0].getPrecio():.2f}")

articulos[0].setPrecio(3800.0)
print(f"Despues: {articulos[0].getNombre()} ${articulos[0].getPrecio():.2f}")
