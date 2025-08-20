# Ejercicio 1.1 - Definición de clases
class Ciudad:
    def __init__(self, nombre:str, provincia:str, poblacion:int) -> None:
        self.nombre = nombre
        self.provincia = provincia
        self.poblacion = poblacion

# Instanciar dos ciudades
la_plata = Ciudad("La Plata", "Buenos Aires", 700000)
mar_del_plata = Ciudad("Mar del Plata", "Buenos Aires", 620000)

# Mostrar atributos de las ciudades
#print(la_plata.nombre, la_plata.provincia, la_plata.poblacion, sep=", ")
#print(mar_del_plata.nombre, mar_del_plata.provincia, mar_del_plata.poblacion, sep=", ")

print(vars(la_plata))
print(vars(mar_del_plata))
