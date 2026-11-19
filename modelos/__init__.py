
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: __init__.py
# DESCRIPCION: Organizacion de las clases del paquete modelos.
# =====================================================

# Importamos la clase abstracta Entidad.
from modelos.entidad import Entidad

# Importamos la clase Cliente.
from modelos.cliente import Cliente

# Importamos la clase abstracta Servicio.
from modelos.servicio import Servicio

# Importamos los tres servicios especializados.
from modelos.reserva_sala import ReservaSala
from modelos.alquiler_equipo import AlquilerEquipo
from modelos.asesoria import Asesoria

# Importamos la clase Reserva.
from modelos.reserva import Reserva

# Importamos las excepciones personalizadas.
from modelos.excepciones import (
    ErrorSoftwareFJ,
    ClienteInvalidoError,
    ClienteNoEncontradoError,
    ServicioNoEncontradoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    ReservaNoEncontradaError,
    OperacionNoPermitidaError,
    ParametroFaltanteError,
    CalculoInconsistenteError,
    ReservaCanceladaError,
    ReservaDuplicadaError
)
