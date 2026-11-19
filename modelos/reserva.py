
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: reserva.py
# DESCRIPCION: Gestion integral de las reservas.
# =====================================================

# Importamos datetime para registrar la fecha de la reserva.
from datetime import datetime

# Importamos la clase abstracta Entidad.
from modelos.entidad import Entidad

# Importamos las excepciones personalizadas.
from modelos.excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    ServicioNoDisponibleError,
    CalculoInconsistenteError
)

# Importamos el sistema de registro de eventos y errores.
from utils.logger import LoggerSoftwareFJ


# Creamos la clase Reserva que hereda de Entidad.
class Reserva(Entidad):

    # Constructor de la clase Reserva.
    def __init__(
        self,
        identificador,
        cliente,
        servicio,
        duracion,
        parametros_servicio=None
    ):

        # Inicializamos los atributos de la clase padre.
        super().__init__(identificador)

        # Guardamos el cliente asociado a la reserva.
        self.__cliente = cliente

        # Guardamos el servicio asociado a la reserva.
        self.__servicio = servicio

        # Guardamos la duracion de la reserva.
        self.__duracion = duracion

        # Guardamos los parametros adicionales del servicio.
        self.__parametros_servicio = (
            parametros_servicio.copy()
            if parametros_servicio is not None
            else {}
        )

        # Definimos el estado inicial de la reserva.
        self.__estado = "PENDIENTE"

        # Inicializamos el costo de la reserva.
        self.__costo = None

        # Registramos la fecha y hora de creacion.
        self.__fecha_reserva = datetime.now()

        # Validamos la informacion de la reserva.
        self.validar()

        # Registramos la creacion de la reserva.
        LoggerSoftwareFJ.registrar_evento(
            f"Reserva {self.identificador} creada correctamente."
        )

    # Propiedad para consultar el cliente.
    @property
    def cliente(self):
        return self.__cliente

    # Propiedad para consultar el servicio.
    @property
    def servicio(self):
        return self.__servicio

    # Propiedad para consultar la duracion.
    @property
    def duracion(self):
        return self.__duracion

    # Propiedad para consultar el estado.
    @property
    def estado(self):
        return self.__estado

    # Propiedad para consultar el costo.
    @property
    def costo(self):
        return self.__costo

    # Propiedad para consultar la fecha de la reserva.
    @property
    def fecha_reserva(self):
        return self.__fecha_reserva

    # Implementamos el metodo abstracto validar.
    def validar(self):

        # Verificamos que exista un cliente.
        if self.__cliente is None:
            raise ReservaInvalidaError(
                "La reserva debe tener un cliente."
            )

        # Verificamos que el cliente tenga el metodo validar.
        if not callable(getattr(self.__cliente, "validar", None)):
            raise ReservaInvalidaError(
                "El cliente proporcionado no es valido."
            )

        # Validamos los datos del cliente.
        self.__cliente.validar()

        # Verificamos que exista un servicio.
        if self.__servicio is None:
            raise ReservaInvalidaError(
                "La reserva debe tener un servicio."
            )

        # Verificamos que el servicio tenga los metodos necesarios.
        if not callable(getattr(self.__servicio, "calcular_costo", None)):
            raise ReservaInvalidaError(
                "El servicio proporcionado no es valido."
            )

        # Verificamos que la duracion sea un numero positivo.
        if (
            isinstance(self.__duracion, bool)
            or not isinstance(self.__duracion, (int, float))
            or self.__duracion <= 0
        ):
            raise ReservaInvalidaError(
                "La duracion debe ser mayor que cero."
            )

        # Verificamos que los parametros adicionales sean un diccionario.
        if not isinstance(self.__parametros_servicio, dict):
            raise ReservaInvalidaError(
                "Los parametros deben estar en un diccionario."
            )

        # Validamos los parametros especificos del servicio.
        self.__servicio.validar_parametros(
            **self.__parametros_servicio
        )

        # Indicamos que la reserva es valida.
        return True

    # Metodo para confirmar una reserva.
    def confirmar(self):

        # Verificamos que la reserva no este cancelada.
        if self.__estado == "CANCELADA":
            raise OperacionNoPermitidaError(
                "No se puede confirmar una reserva cancelada."
            )

        # Verificamos que no haya sido procesada.
        if self.__estado == "PROCESADA":
            raise OperacionNoPermitidaError(
                "La reserva ya fue procesada."
            )

        # Verificamos que el servicio este disponible.
        if not self.__servicio.disponible:
            raise ServicioNoDisponibleError(
                "El servicio no esta disponible."
            )

        # Volvemos a validar la reserva.
        self.validar()

        # Actualizamos el estado.
        self.__estado = "CONFIRMADA"

        # Registramos la confirmacion.
        LoggerSoftwareFJ.registrar_evento(
            f"Reserva {self.identificador} confirmada."
        )

        # Devolvemos un mensaje.
        return "La reserva fue confirmada correctamente."

    # Metodo para cancelar una reserva.
    def cancelar(self):

        # No permitimos cancelar reservas procesadas.
        if self.__estado == "PROCESADA":
            raise OperacionNoPermitidaError(
                "No se puede cancelar una reserva procesada."
            )

        # No permitimos cancelar dos veces.
        if self.__estado == "CANCELADA":
            raise OperacionNoPermitidaError(
                "La reserva ya esta cancelada."
            )

        # Actualizamos el estado.
        self.__estado = "CANCELADA"

        # Registramos la cancelacion.
        LoggerSoftwareFJ.registrar_evento(
            f"Reserva {self.identificador} cancelada."
        )

        # Devolvemos un mensaje.
        return "La reserva fue cancelada correctamente."

    # Metodo para procesar una reserva y calcular su costo.
    def procesar(self, impuesto=0, descuento=0):

        # Verificamos que la reserva este confirmada.
        if self.__estado != "CONFIRMADA":
            raise OperacionNoPermitidaError(
                "Solo se pueden procesar reservas confirmadas."
            )

        # Utilizamos try para controlar errores.
        try:

            # Verificamos que el servicio este disponible.
            if not self.__servicio.disponible:
                raise ServicioNoDisponibleError(
                    "El servicio ya no esta disponible."
                )

            # Copiamos los parametros adicionales del servicio.
            parametros_calculo = self.__parametros_servicio.copy()

            # Eliminamos personas porque solo se utiliza para validar la sala.
            parametros_calculo.pop("personas", None)

            # Calculamos el costo utilizando el metodo del servicio.
            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto,
                descuento,
                **parametros_calculo
            )

            # Verificamos que el costo sea un numero valido.
            if (
                isinstance(self.__costo, bool)
                or not isinstance(self.__costo, (int, float))
                or self.__costo < 0
            ):
                raise CalculoInconsistenteError(
                    "El costo calculado no es valido."
                )

        # Capturamos los errores durante el procesamiento.
        except Exception as error:

            # Registramos el error en el archivo de logs.
            LoggerSoftwareFJ.registrar_error(
                f"Error al procesar la reserva {self.identificador}",
                error
            )

            # Lanzamos una excepcion personalizada.
            # from error conserva la causa original.
            raise ReservaInvalidaError(
                "No fue posible procesar la reserva."
            ) from error

        # Este bloque se ejecuta si no ocurre ningun error.
        else:

            # Cambiamos el estado de la reserva.
            self.__estado = "PROCESADA"

            # Registramos el procesamiento exitoso.
            LoggerSoftwareFJ.registrar_evento(
                f"Reserva {self.identificador} procesada. "
                f"Costo total: ${self.__costo:.2f}"
            )

            # Devolvemos el costo final.
            return self.__costo

        # Este bloque se ejecuta siempre.
        finally:

            # Registramos el final del intento de procesamiento.
            LoggerSoftwareFJ.registrar_evento(
                f"Finalizo el intento de procesamiento "
                f"de la reserva {self.identificador}."
            )

    # Metodo para consultar toda la informacion de la reserva.
    def obtener_informacion(self):

        # Mostramos el costo si ya fue calculado.
        costo_texto = (
            f"${self.__costo:.2f}"
            if self.__costo is not None
            else "Pendiente de calculo"
        )

        # Devolvemos la informacion completa.
        return (
            f"Reserva: {self.identificador}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duracion: {self.__duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: {costo_texto}\n"
            f"Fecha: {self.__fecha_reserva}"
        )

    # Metodo especial para representar la reserva como texto.
    def __str__(self):

        # Devolvemos el identificador y el estado.
        return (
            f"Reserva {self.identificador} - "
            f"Estado: {self.__estado}"
        )
