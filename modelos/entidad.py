
# PROYECTO: SOFTWARE FJ
# ARCHIVO: entidad.py
# DESCRIPCION: Clase abstracta general del sistema.

# Importamos ABC y abstractmethod para crear clases abstractas.
from abc import ABC, abstractmethod

# Importamos datetime para registrar fechas y horas.
from datetime import datetime


# Creamos la clase abstracta Entidad.
# ABC indica que esta clase no se debe instanciar directamente.
class Entidad(ABC):

    # Constructor de la clase.
    # Recibe un identificador para cada entidad del sistema.
    def __init__(self, identificador):

        # Verificamos que el identificador sea un texto.
        if not isinstance(identificador, str):

            # Generamos un error si el identificador no es texto.
            raise ValueError("El identificador debe ser un texto.")

        # Verificamos que el identificador no esté vacío.
        if not identificador.strip():

            # Generamos un error si el identificador está vacío.
            raise ValueError("El identificador no puede estar vacío.")

        # Guardamos el identificador como atributo privado.
        # Los dos guiones bajos aplican encapsulamiento.
        self.__identificador = identificador.strip()

        # Registramos automáticamente la fecha de creación.
        self.__fecha_creacion = datetime.now()

    # Creamos una propiedad para consultar el identificador.
    @property
    def identificador(self):

        # Devolvemos el identificador privado.
        return self.__identificador

    # Creamos una propiedad para consultar la fecha de creación.
    @property
    def fecha_creacion(self):

        # Devolvemos la fecha de creación.
        return self.__fecha_creacion

    # Definimos un método abstracto.
    # Las clases hijas estarán obligadas a implementarlo.
    @abstractmethod
    def validar(self):

        # pass indica que la implementación estará en las clases hijas.
        pass

    # Método para mostrar información general de la entidad.
    def obtener_informacion(self):

        # Devolvemos el identificador y la fecha de creación.
        return (
            f"Identificador: {self.__identificador} | "
            f"Fecha de creación: {self.__fecha_creacion}"
        )
