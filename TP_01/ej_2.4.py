# Ejercicio 2.4 - Sistema para aerolineas
class Vuelo:
    def __init__(self, codigo:str, origen:str, destino:str, fecha:str, precio:float) -> None:
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.precio = precio

# Getters
    def getCodigo(self) -> str:
        return self.codigo

    def getOrigen(self) -> str:
        return self.origen

    def getDestino(self) -> str:
        return self.destino

    def getFecha(self) -> str:
        return self.fecha

    def getPrecio(self) -> float:
        return self.precio

# Setters
    def setCodigo(self, nuevo_codigo:str) -> None:
        self.codigo = nuevo_codigo

    def setOrigen(self, nuevo_origen:str) -> None:
        self.origen = nuevo_origen

    def setDestino(self, nuevo_destino:str) -> None:
        self.destino = nuevo_destino

    def setFecha(self, nuevo_fecha:str) -> None:
        self.fecha = nuevo_fecha

    def setPrecio(self, nuevo_precio:float) -> None:
        self.precio = nuevo_precio

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
    if i.getOrigen() == ORIGEN_FILTRO and i.getPrecio() < PRECIO_LIMITE:
        codigos.append(i.getCodigo())

print(f"Vuelos desde {ORIGEN_FILTRO} por menos de ${PRECIO_LIMITE}: {codigos}")

# Mostrar el vuelo más barato
def mostrarMasBarato(vuelos:list) -> None:
    codigo_barato = vuelos[0].getCodigo()
    precio_barato = vuelos[0].getPrecio()

    for i in vuelos:
        if i.getPrecio() < precio_barato:
            codigo_barato = i.getCodigo()
            precio_barato = i.getPrecio()
    print(f"El vuelo más barato es: {codigo_barato} - ${precio_barato:.2f}")

# Cambiar el precio de un vuelo
def cambiarPrecio(vuelo:Vuelo, nuevo_precio:float) -> None:
    print(f"Antes: {vuelo.getCodigo()} - ${vuelo.getPrecio():.2f}")
    vuelo.setPrecio(nuevo_precio)
    print(f"Despues: {vuelo.getCodigo()} - ${vuelo.getPrecio():.2f}", end="\n\n")

mostrarMasBarato(vuelos)
cambiarPrecio(vuelos[0], 100000)
mostrarMasBarato(vuelos)
