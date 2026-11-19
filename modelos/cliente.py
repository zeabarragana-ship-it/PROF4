
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: cliente.py
# DESCRIPCION: Gestion y validacion de los clientes.
# =====================================================

# Importamos la clase abstracta Entidad.
from modelos.entidad import Entidad

# Importamos las excepciones personalizadas.
from modelos.excepciones import ClienteInvalidoError


# Creamos la clase Cliente que hereda de Entidad.
class Cliente(Entidad):

    # Constructor de la clase Cliente.
    def __init__(self, identificador, nombre, documento, correo, telefono):

        # Inicializamos los atributos de la clase padre.
        super().__init__(identificador)

        # Guardamos los datos personales como atributos privados.
        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono

        # Validamos los datos del cliente al momento de crearlo.
        self.validar()

    # Propiedad para consultar el nombre del cliente.
    @property
    def nombre(self):
        return self.__nombre

    # Propiedad para modificar el nombre del cliente.
    @nombre.setter
    def nombre(self, nuevo_nombre):

        # Verificamos que el nombre sea un texto valido.
        if not isinstance(nuevo_nombre, str) or not nuevo_nombre.strip():
            raise ClienteInvalidoError("El nombre no puede estar vacio.")

        # Guardamos el nombre sin espacios innecesarios.
        self.__nombre = nuevo_nombre.strip()

    # Propiedad para consultar el documento.
    @property
    def documento(self):
        return self.__documento

    # Propiedad para consultar el correo.
    @property
    def correo(self):
        return self.__correo

    # Propiedad para modificar el correo.
    @correo.setter
    def correo(self, nuevo_correo):

        # Verificamos que el correo tenga un formato basico valido.
        if not isinstance(nuevo_correo, str) or "@" not in nuevo_correo or "." not in nuevo_correo:
            raise ClienteInvalidoError("El correo electronico no es valido.")

        # Guardamos el correo en minusculas.
        self.__correo = nuevo_correo.strip().lower()

    # Propiedad para consultar el telefono.
    @property
    def telefono(self):
        return self.__telefono

    # Propiedad para modificar el telefono.
    @telefono.setter
    def telefono(self, nuevo_telefono):

        # Verificamos que el telefono contenga solamente numeros.
        if not str(nuevo_telefono).isdigit():
            raise ClienteInvalidoError("El telefono debe contener solamente numeros.")

        # Verificamos que tenga entre 7 y 15 digitos.
        if not 7 <= len(str(nuevo_telefono)) <= 15:
            raise ClienteInvalidoError("El telefono debe tener entre 7 y 15 digitos.")

        # Guardamos el telefono como texto.
        self.__telefono = str(nuevo_telefono)

    # Metodo para validar todos los datos del cliente.
    def validar(self):

        # Validamos que el nombre sea correcto.
        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise ClienteInvalidoError("El nombre del cliente es obligatorio.")

        # Validamos que el documento contenga solamente numeros.
        if not str(self.__documento).isdigit():
            raise ClienteInvalidoError("El documento debe contener solamente numeros.")

        # Validamos que el documento tenga una longitud adecuada.
        if not 5 <= len(str(self.__documento)) <= 15:
            raise ClienteInvalidoError("El documento debe tener entre 5 y 15 digitos.")

        # Validamos el formato basico del correo electronico.
        if not isinstance(self.__correo, str) or "@" not in self.__correo or "." not in self.__correo:
            raise ClienteInvalidoError("El correo electronico no es valido.")

        # Validamos el numero de telefono.
        if not str(self.__telefono).isdigit():
            raise ClienteInvalidoError("El telefono debe contener solamente numeros.")

        # Validamos la longitud del telefono.
        if not 7 <= len(str(self.__telefono)) <= 15:
            raise ClienteInvalidoError("El telefono debe tener entre 7 y 15 digitos.")

        # Si todos los datos son correctos, devolvemos True.
        return True

    # Metodo para mostrar la informacion del cliente.
    def mostrar_informacion(self):

        # Devolvemos los datos principales del cliente.
        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono}"
        )

    # Metodo especial para representar el objeto como texto.
    def __str__(self):

        # Devolvemos el nombre y el documento del cliente.
        return f"{self.__nombre} - Documento: {self.__documento}"
