from validaciones_cliente import (
    pedir_nombre_hasta_valido,
    pedir_cuil_hasta_valido,
    pedir_mail_hasta_valido,
    pedir_telefono_hasta_valido,
    pedir_direccion_hasta_valida,
    pedir_dni_hasta_valido
    )


class Cliente:
    def __init__(self, nombre, cuil, mail, telefono, direccion):
        self.__nombre = pedir_nombre_hasta_valido(nombre)
        self.__cuil = pedir_cuil_hasta_valido(cuil)
        self.__mail = pedir_mail_hasta_valido(mail)
        self.__telefono = pedir_telefono_hasta_valido(telefono)
        self.__direccion = pedir_direccion_hasta_valida(direccion)

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def nombre_formateado(self):
        return " ".join(self.__nombre.split()).capitalize()

    @property
    def cuil(self):
        return self.__cuil
    
    @property
    def cuil_formateado(self):
        return f"{self.__cuil[:2]}-{self.__cuil[2:11]}-{self.__cuil[-1]}"

    @property
    def mail(self):
        return self.__mail
    
    @property
    def telefono(self):
        return self.__telefono
    
    @property
    def direccion(self):
        return self.__direccion
    
    @property
    def direccion_formateado(self):
        return " ".join(self.__direccion.split()).lower()

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = pedir_nombre_hasta_valido(valor)

    @mail.setter
    def mail(self, valor):
        self.__mail = pedir_mail_hasta_valido(valor)
    
    @telefono.setter
    def telefono(self, valor):
        self.__telefono = pedir_telefono_hasta_valido(valor)
    
    @direccion.setter
    def direccion(self, valor):
        self.__direccion = pedir_direccion_hasta_valida(valor)

    def __str__(self) -> str:
        # Detalle base común a cualquier cliente
        datos_personales = f"Nombre: {self.nombre_formateado}, CUIL: {self.cuil_formateado}"
        cotacto = f"Mail: {self.mail}, Tel: {self.telefono}, Dir: {self.direccion_formateado}"
        return f"{datos_personales}\n{cotacto}"


class PersonaFisica(Cliente):
    def __init__(self, nombre, cuil, mail, telefono, direccion, dni):
        super().__init__(nombre, cuil, mail, telefono, direccion)
        self.__dni = pedir_dni_hasta_valido(dni)

    @property
    def dni(self):
        return self.__dni

    def informe_datos(self):
        print("#Datos del cliente:")
        print(f"nombre: {self.nombre_formateado}")
        print(f"dni: {self.__dni}")
        print(f"cuil: {self.cuil_formateado}") 
        print(f"mail: {self.__mail}")
        print(f"tel: {self.__telefono}")    
        print(f"dir: {self.direccion_formateado}") 


    def __str__(self) -> str:
        datos_personales = f"Nombre: {self.nombre_formateado}, DNI: {self.dni}, CUIL: {self.cuil_formateado}"
        cotacto = f"Mail: {self.mail}, Tel: {self.telefono}, Dir: {self.direccion_formateado}"
        return f"{datos_personales}\n{cotacto}"


class Empresa(Cliente):
    def __init__(self, nombre_juridico, cuil, mail, telefono, direccion, nombre_fantasia):
        super().__init__(nombre_juridico, cuil, mail, telefono, direccion)
        self.__nombre_fantasia = pedir_nombre_hasta_valido(nombre_fantasia)

    @property
    def nombre_juridico(self):
        return self.nombre  # reutiliza el atributo de Cliente

    @property
    def nombre_fantasia(self):
        return self.__nombre_fantasia

    @nombre_fantasia.setter
    def nombre_fantasia(self, valor):
        self.__nombre_fantasia = pedir_nombre_hasta_valido(valor)

    def informe_datos(self):
        print("#Datos del cliente:")
        print(f"nombre fantasía: {self.nombre_fantasia}")
        print(f"Nombre juridico: {self.nombre_formateado}")
        print(f"cuil: {self.cuil_formateado}") 
        print(f"mail: {self.__mail}")
        print(f"tel: {self.__telefono}")    
        print(f"dir: {self.direccion_formateado}")

    def __str__(self) -> str:
        base = super().__str__()  # reutiliza contacto + estado [+ alta]
        return f"{self.__nombre_fantasia}/n{base}"
    