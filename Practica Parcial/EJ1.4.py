class Alumno:
    def __init__(self, nombre, nota):
        self.__nombre = nombre
        self.__nota = nota

    @property
    def nombre(self):
        return self.__nombre

    @property
    def nota(self):
        return self.__nota

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @nota.setter
    def nota(self, nueva_nota):
        try:
            valor = float(nueva_nota)
            if valor > 0 and valor < 10:
                self.__nota = valor
            else:
                raise Exception("Error: La nota debe estar entre 0 y 10")
        except (TypeError, ValueError):
            print("Error: La nota debe ser un numero")
            return

a1 = Alumno("Juan", 0)
a1.nota = "22"
print(f"Nombre: {a1.nombre} | Nota: {a1.nota}")