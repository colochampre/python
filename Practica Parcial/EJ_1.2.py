class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    @property 
    def nombre(self):
        return self.__nombre

    @property 
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor a 0")

p1 = Producto("Producto 1", 100)
p1.precio = -100
print(p1.precio)

