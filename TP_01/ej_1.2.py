# Ejercicio 1.2 - Definición de clases
class Cancion:
    def __init__(self, titulo:str, artista:str, duracion:int, genero:str) -> None:
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        self.genero = genero

# Instanciar una lista de 5 canciones
canciones = [
    Cancion("Tema A", "Banda A", 120, "Rock"),
    Cancion("Tema B", "Artista B", 180, "Pop"),
    Cancion("Tema C", "Banda C", 240, "Rock"),
    Cancion("Tema D", "Artista D", 300, "Pop"),
    Cancion("Tema E", "Banda E", 190, "Rock")
]

rock = []
for i in canciones:
    if i.genero == "Rock": # Filtro por genero
        rock.append(i.titulo) # Agregar solo el titulo de la cancion

print("Rock:", rock)
