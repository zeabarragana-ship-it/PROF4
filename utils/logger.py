
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: logger.py
# DESCRIPCION: Sistema de registro de eventos y errores.
# =====================================================

# Importamos logging para registrar eventos y errores.
import logging

# Importamos os para trabajar con rutas de archivos.
import os

# Importamos traceback para obtener detalles de los errores.
import traceback


# Obtenemos la ruta de la carpeta principal del proyecto.
RUTA_PROYECTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Definimos la ruta donde se guardara el archivo de registros.
RUTA_LOGS = os.path.join(RUTA_PROYECTO, "logs.log")


# Configuramos el sistema de registros.
logging.basicConfig(
    filename=RUTA_LOGS,                  # Archivo donde se guardaran los registros.
    level=logging.INFO,                  # Nivel minimo de registro.
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",                    # Permite guardar caracteres especiales.
    force=True                           # Aplica esta configuracion al proyecto.
)


# Creamos una clase para administrar los registros.
class LoggerSoftwareFJ:

    # Metodo para registrar eventos importantes.
    @staticmethod
    def registrar_evento(mensaje):

        # Utilizamos try para controlar posibles errores al registrar.
        try:

            # Guardamos el evento como informacion.
            logging.info(mensaje)

        # Capturamos cualquier error inesperado.
        except Exception as error:

            # Mostramos el error si no se puede registrar.
            print(f"Error al registrar evento: {error}")

    # Metodo para registrar errores del sistema.
    @staticmethod
    def registrar_error(mensaje, error=None):

        # Intentamos registrar el error.
        try:

            # Si recibimos una excepcion, registramos su informacion.
            if error is not None:

                # Guardamos el mensaje y los detalles de la excepcion.
                logging.error(
                    f"{mensaje}: {error}",
                    exc_info=(
                        type(error),
                        error,
                        error.__traceback__
                    )
                )

            # Si no recibimos una excepcion, registramos solamente el mensaje.
            else:

                logging.error(mensaje)

        # Capturamos errores durante el registro.
        except Exception as error_logger:

            # Mostramos el problema sin detener el programa.
            print(f"Error interno del logger: {error_logger}")

    # Metodo para registrar advertencias.
    @staticmethod
    def registrar_advertencia(mensaje):

        # Intentamos guardar la advertencia.
        try:

            # Registramos el mensaje como advertencia.
            logging.warning(mensaje)

        # Controlamos errores del sistema de registro.
        except Exception as error:

            # Informamos el problema por pantalla.
            print(f"Error al registrar advertencia: {error}")

    # Metodo para registrar excepciones con su seguimiento.
    @staticmethod
    def registrar_excepcion(mensaje):

        # Intentamos registrar la excepcion.
        try:

            # Guardamos el mensaje y el seguimiento completo del error.
            logging.error(
                mensaje + "\n" + traceback.format_exc()
            )

        # Controlamos cualquier error del registro.
        except Exception as error:

            # Informamos el problema sin detener la aplicacion.
            print(f"Error al registrar excepcion: {error}")
