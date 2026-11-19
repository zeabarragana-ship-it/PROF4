
# PROYECTO: SOFTWARE FJ
# ARCHIVO: excepciones.py
# DESCRIPCION: Excepciones personalizadas del sistema.


# Clase base para todos los errores personalizados.
# Hereda de Exception, que es la clase general de errores de Python.
class ErrorSoftwareFJ(Exception):

    # Constructor de la excepcion personalizada.
    def __init__(self, mensaje):

        # Guardamos el mensaje que explica el error.
        self.mensaje = mensaje

        # Enviamos el mensaje a la clase Exception.
        super().__init__(mensaje)


# Excepcion para datos incorrectos de un cliente.
class ClienteInvalidoError(ErrorSoftwareFJ):
    pass


# Excepcion cuando un cliente no se encuentra registrado.
class ClienteNoEncontradoError(ErrorSoftwareFJ):
    pass


# Excepcion cuando un servicio no existe.
class ServicioNoEncontradoError(ErrorSoftwareFJ):
    pass


# Excepcion cuando un servicio no esta disponible.
class ServicioNoDisponibleError(ErrorSoftwareFJ):
    pass


# Excepcion cuando se intenta crear una reserva incorrecta.
class ReservaInvalidaError(ErrorSoftwareFJ):
    pass


# Excepcion cuando no se encuentra una reserva.
class ReservaNoEncontradaError(ErrorSoftwareFJ):
    pass


# Excepcion cuando se intenta realizar una operacion no permitida.
class OperacionNoPermitidaError(ErrorSoftwareFJ):
    pass


# Excepcion cuando faltan parametros obligatorios.
class ParametroFaltanteError(ErrorSoftwareFJ):
    pass


# Excepcion cuando se presenta un problema al calcular un costo.
class CalculoInconsistenteError(ErrorSoftwareFJ):
    pass


# Excepcion cuando se intenta confirmar una reserva cancelada.
class ReservaCanceladaError(ErrorSoftwareFJ):
    pass


# Excepcion cuando se intenta realizar una reserva duplicada.
class ReservaDuplicadaError(ErrorSoftwareFJ):
    pass
