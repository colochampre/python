class Persona:
    
    def __init__(self, nombre:str, edad:int):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad


class Estudiante(Persona):
    def __init__(self, nombre, edad, legajo:int):
        super().__init__(nombre, edad)
        self.__legajo = legajo

    @property
    def legajo(self):
        return self.__legajo

    def mostrar_legajo(self) -> None:
        print(f'{self.nombre} {self.edad} {self.legajo}')

e = Estudiante('Pepe', 14, 100)
e.mostrar_legajo()
