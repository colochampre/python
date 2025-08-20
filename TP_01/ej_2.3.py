# Ejercicio 2.3 - Plataforma de streaming
class Pelicula:
    def __init__(self, titulo:str, director:str, duracion_min:int, genero:str) -> None:
        self.titulo = titulo
        self.director = director
        self.duracion_min = duracion_min
        self.genero = genero
        
# Getters
    def getTitulo(self) -> str:
        return self.titulo
    def getDirector(self) -> str:
        return self.director
    def getDuracionMin(self) -> int:
        return self.duracion_min
    def getGenero(self) -> str:
        return self.genero

# Setters
    def setTitulo(self, nuevo_titulo:str) -> None:
        self.titulo = nuevo_titulo
    def setDirector(self, nuevo_director:str) -> None:
        self.director = nuevo_director
    def setDuracionMin(self, nuevo_duracion_min:int) -> None:
        self.duracion_min = nuevo_duracion_min
    def setGenero(self, nuevo_genero:str) -> None:
        self.genero = nuevo_genero

# Instanciar una lista de 5 películas
peliculas = [
    Pelicula("P1", "DirA", 95, "Drama"),
    Pelicula("P2", "DirB", 120, "Accion"),
    Pelicula("P3", "DirC", 140, "Drama"),
    Pelicula("P4", "DirD", 110, "Comedia"),
    Pelicula("P5", "DirE", 130, "Drama")
]

# Mostrar las películas de Drama
drama = []
for i in peliculas:
    if i.getGenero() == "Drama":
        drama.append(i.getTitulo())

print(f"Peliculas de Drama: {drama}")

print("\n", end="")

# Cambiar la duracion de una película
def cambiarDuracion(pelicula:Pelicula, nueva_duracion:int) -> None:
    print(f"Antes: {pelicula.getTitulo()} - {pelicula.getDuracionMin()}m")
    pelicula.setDuracionMin(nueva_duracion)
    print(f"Despues: {pelicula.getTitulo()} - {pelicula.getDuracionMin()}m", end="\n\n")

cambiarDuracion(peliculas[0], 100)
cambiarDuracion(peliculas[1], 115)
