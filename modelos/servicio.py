
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: servicio.py
# DESCRIPCION: Clase abstracta que representa los servicios
# ofrecidos por la empresa Software FJ.
# =====================================================

# Importamos ABC y abstractmethod para crear clases abstractas.
from abc import ABC, abstractmethod

# Importamos la clase Entidad para establecer la herencia.
from modelos.entidad import Entidad

# Importamos las excepciones personalizadas del sistema.
from modelos.excepciones import (
    ServicioNoDisponibleError,
    CalculoInconsistenteError,
    ParametroFaltanteError
)


# Creamos la clase abstracta Servicio.
# Hereda de Entidad para reutilizar sus atributos y metodos.
class Servicio(Entidad):

    # Constructor de la clase Servicio.
    def __init__(self, identificador, nombre, precio_base, disponible=True):

        # Inicializamos los atributos de la clase padre.
        super().__init__(identificador)

        # Verificamos que el nombre sea un texto valido.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ParametroFaltanteError(
                "El nombre del servicio es obligatorio."
            )

        # Verificamos que el precio sea un numero.
        if isinstance(precio_base, bool) or not isinstance(precio_base, (int, float)):
            raise CalculoInconsistenteError(
                "El precio debe ser un valor numerico."
            )

        # Verificamos que el precio sea mayor que cero.
        if precio_base <= 0:
            raise CalculoInconsistenteError(
                "El precio debe ser mayor que cero."
            )

        # Verificamos que la disponibilidad sea verdadera o falsa.
        if not isinstance(disponible, bool):
            raise ValueError(
                "La disponibilidad debe ser True o False."
            )

        # Guardamos el nombre como atributo privado.
        self.__nombre = nombre.strip()

        # Guardamos el precio base como atributo privado.
        self.__precio_base = float(precio_base)

        # Guardamos el estado de disponibilidad.
        self.__disponible = disponible

    # Propiedad para consultar el nombre del servicio.
    @property
    def nombre(self):
        return self.__nombre

    # Propiedad para consultar el precio base.
    @property
    def precio_base(self):
        return self.__precio_base

    # Propiedad para consultar la disponibilidad.
    @property
    def disponible(self):
        return self.__disponible

    # Metodo para cambiar la disponibilidad del servicio.
    def cambiar_disponibilidad(self, estado):

        # Comprobamos que el estado sea de tipo booleano.
        if not isinstance(estado, bool):
            raise ValueError(
                "El estado debe ser True o False."
            )

        # Actualizamos la disponibilidad del servicio.
        self.__disponible = estado

    # Metodo para verificar si el servicio esta disponible.
    def verificar_disponibilidad(self):

        # Comprobamos si el servicio esta habilitado.
        if not self.__disponible:

            # Generamos una excepcion si no esta disponible.
            raise ServicioNoDisponibleError(
                f"El servicio {self.__nombre} no esta disponible."
            )

        # Si esta disponible, devolvemos True.
        return True

    # Metodo para validar los datos generales del servicio.
    def validar(self):

        # Verificamos que exista el identificador.
        if not self.identificador:
            raise ParametroFaltanteError(
                "El identificador del servicio es obligatorio."
            )

        # Verificamos que exista el nombre.
        if not self.__nombre:
            raise ParametroFaltanteError(
                "El nombre del servicio es obligatorio."
            )

        # Verificamos que el precio sea positivo.
        if self.__precio_base <= 0:
            raise CalculoInconsistenteError(
                "El precio del servicio no es valido."
            )

        # Si todo es correcto, devolvemos True.
        return True

    # Metodo abstracto para calcular el costo del servicio.
    # Cada clase hija implementara su propio calculo.
    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    # Metodo abstracto para describir el servicio.
    # Cada servicio especializado tendra su propia descripcion.
    @abstractmethod
    def describir_servicio(self):
        pass

    # Metodo abstracto para validar parametros especificos.
    # Cada clase hija implementara sus propias validaciones.
    @abstractmethod
    def validar_parametros(self, **parametros):
        pass

    # Metodo para mostrar la informacion general del servicio.
    def mostrar_informacion(self):

        # Devolvemos los datos del servicio en forma de texto.
        return (
            f"Servicio: {self.__nombre} | "
            f"Precio base: ${self.__precio_base:.2f} | "
            f"Disponible: {self.__disponible}"
        )
