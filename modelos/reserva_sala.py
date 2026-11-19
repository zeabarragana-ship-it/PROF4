
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: reserva_sala.py
# DESCRIPCION: Gestion del servicio de reserva de salas.
# =====================================================

# Importamos la clase Servicio para aplicar herencia.
from modelos.servicio import Servicio

# Importamos las excepciones personalizadas.
from modelos.excepciones import (
    ParametroFaltanteError,
    CalculoInconsistenteError
)


# Creamos la clase ReservaSala que hereda de Servicio.
class ReservaSala(Servicio):

    # Constructor de la clase ReservaSala.
    def __init__(self, identificador, nombre, precio_base,
                 capacidad, disponible=True):

        # Inicializamos los atributos heredados.
        super().__init__(identificador, nombre, precio_base, disponible)

        # Validamos que la capacidad sea un numero entero.
        if isinstance(capacidad, bool) or not isinstance(capacidad, int):
            raise ParametroFaltanteError(
                "La capacidad de la sala debe ser un numero entero."
            )

        # Verificamos que la capacidad sea mayor que cero.
        if capacidad <= 0:
            raise CalculoInconsistenteError(
                "La capacidad debe ser mayor que cero."
            )

        # Guardamos la capacidad como atributo privado.
        self.__capacidad = capacidad

    # Propiedad para consultar la capacidad de la sala.
    @property
    def capacidad(self):
        return self.__capacidad

    # Implementamos la validacion del servicio.
    # Este metodo sobrescribe el metodo abstracto de Servicio.
    def validar(self):

        # Ejecutamos primero las validaciones de la clase padre.
        super().validar()

        # Verificamos que la capacidad sea valida.
        if self.__capacidad <= 0:
            raise CalculoInconsistenteError(
                "La capacidad de la sala no es valida."
            )

        # Indicamos que todas las validaciones fueron correctas.
        return True

    # Implementamos la validacion de parametros de la sala.
    def validar_parametros(self, **parametros):

        # Obtenemos el numero de personas solicitado.
        personas = parametros.get("personas")

        # Verificamos que se haya indicado la cantidad de personas.
        if personas is None:
            raise ParametroFaltanteError(
                "Debe indicar la cantidad de personas."
            )

        # Verificamos que sea un numero entero positivo.
        if isinstance(personas, bool) or not isinstance(personas, int) or personas <= 0:
            raise CalculoInconsistenteError(
                "La cantidad de personas debe ser un entero positivo."
            )

        # Comprobamos que la sala tenga suficiente capacidad.
        if personas > self.__capacidad:
            raise CalculoInconsistenteError(
                "La cantidad de personas supera la capacidad de la sala."
            )

        # Devolvemos True si los parametros son correctos.
        return True

    # Implementamos el calculo del costo de la reserva de sala.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        # Verificamos que la duracion sea numerica y positiva.
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise CalculoInconsistenteError(
                "La duracion debe ser un numero mayor que cero."
            )

        # Verificamos que el impuesto sea un porcentaje valido.
        if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100:
            raise CalculoInconsistenteError(
                "El impuesto debe estar entre 0 y 100."
            )

        # Verificamos que el descuento sea un porcentaje valido.
        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise CalculoInconsistenteError(
                "El descuento debe estar entre 0 y 100."
            )

        # Calculamos el costo inicial segun las horas de uso.
        subtotal = self.precio_base * duracion

        # Aplicamos el descuento al subtotal.
        subtotal_con_descuento = subtotal - (subtotal * descuento / 100)

        # Calculamos el impuesto sobre el valor descontado.
        valor_impuesto = subtotal_con_descuento * impuesto / 100

        # Sumamos el impuesto al subtotal.
        costo_total = subtotal_con_descuento + valor_impuesto

        # Verificamos que el resultado sea valido.
        if costo_total < 0:
            raise CalculoInconsistenteError(
                "El calculo del costo genero un resultado negativo."
            )

        # Devolvemos el costo final.
        return round(costo_total, 2)

    # Implementamos la descripcion especifica del servicio.
    def describir_servicio(self):

        # Devolvemos una descripcion de la reserva de sala.
        return (
            f"Reserva de sala: {self.nombre}. "
            f"Capacidad maxima: {self.__capacidad} personas. "
            f"Precio por hora: ${self.precio_base:.2f}."
        )
