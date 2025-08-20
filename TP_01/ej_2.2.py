# Ejercicio 2.2 - Sistema para la UTN
class Estudiante:
    def __init__(self, nombre:str, legajo:int, ingreso:int, carrera:str) -> None:
        self.nombre = nombre
        self.legajo = legajo
        self.ingreso = ingreso
        self.carrera = carrera

# Getters
    def getNombre(self) -> str:
        return self.nombre
    def getLegajo(self) -> int:
        return self.legajo
    def getIngreso(self) -> int:
        return self.ingreso
    def getCarrera(self) -> str:
        return self.carrera

# Setters
    def setNombre(self, nuevo_nombre:str) -> None:
        self.nombre = nuevo_nombre
    def setLegajo(self, nuevo_legajo:int) -> None:
        self.legajo = nuevo_legajo
    def setIngreso(self, nuevo_ingreso:int) -> None:
        self.ingreso = nuevo_ingreso
    def setCarrera(self, nueva_carrera:str) -> None:
        self.carrera = nueva_carrera

# Instanciar una lista de 6 estudiantes
estudiantes = [
    Estudiante("Juan", 101, 2022, "ITI"),
    Estudiante("Maria", 102, 2023, "ITI"),
    Estudiante("Pedro", 103, 2022, "ITI"),
    Estudiante("Ana", 104, 2024, "TUP"),
    Estudiante("Luis", 105, 2025, "TUP"),
    Estudiante("Pepe", 106, 2024, "TUP")
]

# Mostrar la lista cargada
def mostrarLista(estudiantes):
    orden = 1
    print(f"{"#":>2}  {"Nombre":<6} | {"Legajo":<6} | {"Ingreso":<7} | {"Carrera":<7}")
    for i in estudiantes:
        print(f"{orden:>2}. {i.getNombre():<6} | {i.getLegajo():<6} | {i.getIngreso():<7} | {i.getCarrera():<7}")
    orden += 1

mostrarLista(estudiantes)

print("\n", end="")

# Mostrar los legajos de los estudiantes de la TUP
legajos_tup = []

for i in estudiantes:
    if i.getCarrera() == "TUP":
        legajos_tup.append(i.getLegajo())

print(f"Legajos de los estudiantes de la TUP: {legajos_tup}", end="\n\n")

# Cambiar la carrera de un estudiante
print(f"Antes: {estudiantes[0].getNombre()} - {estudiantes[0].getCarrera()}")

estudiantes[0].setCarrera("TUP")
print(f"Despues: {estudiantes[0].getNombre()} - {estudiantes[0].getCarrera()}", end="\n\n")

mostrarLista(estudiantes)
