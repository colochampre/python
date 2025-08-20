# Ejercicio 1.4 - Definición de clases
class Vuelo:
    def __init__(self, codigo:str, origen:str, destino:str, fecha:str, precio:float) -> None:
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.precio = precio

# Instanciar una lista de 6 vuelos
vuelos = []

for i in range(6):
    codigo = input("Codigo del vuelo (ej: AR123):").strip()
    origen = input("Origen del vuelo (ej EZE):").strip().upper()
    destino = input("Destino del vuelo (ej: COR/MDZ):").strip()
    fecha = input("Fecha (AAAA-MM-DD):").strip()
    while True:
        try:
            precio = float(input("Precio (en pesos):").strip().replace(",", "."))
            break
        except ValueError:
            print("Error: Entrada invalida")
            continue
    vuelos.append(Vuelo(codigo, origen, destino, fecha, precio))
    print("\n")

# Mostrar codigos de vuelo desde EZE con precio menor a 200000
ORIGEN_FILTRO = "EZE"
PRECIO_LIMITE = 200000
codigos = []

for i in vuelos:
    if i.origen == ORIGEN_FILTRO and i.precio < PRECIO_LIMITE:
        codigos.append(i.codigo)

print(f"Vuelos desde {ORIGEN_FILTRO} por menos de ${PRECIO_LIMITE}: {codigos}")

