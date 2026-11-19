
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: asesoria.py
# DESCRIPCION: Gestion del servicio de asesoria especializada.
# =====================================================

# Importamos la clase Servicio para aplicar herencia.
from modelos.servicio import Servicio

# Importamos las excepciones personalizadas.
from modelos.excepciones import (
    ParametroFaltanteError,
    CalculoInconsistenteError
)


# Creamos la clase Asesoria que hereda de Servicio.
class Asesoria(Servicio):

    # Constructor de la clase Asesoria.
    def __init__(self, identificador, nombre, precio_base,
                 especialidad, disponible=True):

        # Inicializamos los atributos de la clase padre.
        super().__init__(identificador, nombre, precio_base, disponible)

        # Verificamos que la especialidad sea un texto valido.
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ParametroFaltanteError(
                "La especialidad de la asesoria es obligatoria."
            )

        # Guardamos la especialidad como atributo privado.
        self.__especialidad = especialidad.strip()

    # Propiedad para consultar la especialidad.
    @property
    def especialidad(self):
        return self.__especialidad

    # Implementamos la validacion general del servicio.
    def validar(self):

        # Ejecutamos las validaciones de la clase padre.
        super().validar()

        # Verificamos que la especialidad no este vacia.
        if not self.__especialidad.strip():
            raise ParametroFaltanteError(
                "La especialidad de la asesoria no puede estar vacia."
            )

        # Indicamos que el servicio es valido.
        return True

    # Validamos los parametros de la asesoria.
    def validar_parametros(self, **parametros):

        # Obtenemos el nivel de complejidad.
        complejidad = parametros.get("complejidad")

        # Verificamos que se haya indicado la complejidad.
        if complejidad is None:
            raise ParametroFaltanteError(
                "Debe indicar el nivel de complejidad de la asesoria."
            )

        # Definimos los niveles de complejidad permitidos.
        niveles_validos = ["basico", "intermedio", "avanzado"]

        # Comprobamos que el nivel sea un texto.
        if not isinstance(complejidad, str):
            raise CalculoInconsistenteError(
                "El nivel de complejidad debe ser un texto."
            )

        # Convertimos el nivel a minusculas para compararlo.
        complejidad = complejidad.strip().lower()

        # Verificamos que el nivel este permitido.
        if complejidad not in niveles_validos:
            raise CalculoInconsistenteError(
                "La complejidad debe ser basica, intermedia o avanzada."
            )

        # Devolvemos True si los parametros son correctos.
        return True

    # Calculamos el costo de la asesoria.
    def calcular_costo(self, duracion, impuesto=0, descuento=0,
                       complejidad="basico"):

        # Verificamos que la duracion sea numerica y positiva.
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise CalculoInconsistenteError(
                "La duracion de la asesoria debe ser mayor que cero."
            )

        # Verificamos que el impuesto sea valido.
        if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100:
            raise CalculoInconsistenteError(
                "El impuesto debe estar entre 0 y 100."
            )

        # Verificamos que el descuento sea valido.
        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise CalculoInconsistenteError(
                "El descuento debe estar entre 0 y 100."
            )

        # Definimos los multiplicadores por nivel de complejidad.
        multiplicadores = {
            "basico": 1.0,
            "intermedio": 1.5,
            "avanzado": 2.0
        }

        # Comprobamos que la complejidad sea un texto.
        if not isinstance(complejidad, str):
            raise CalculoInconsistenteError(
                "La complejidad debe ser un texto."
            )

        # Normalizamos el nivel de complejidad.
        complejidad = complejidad.strip().lower()

        # Verificamos que el nivel exista en los multiplicadores.
        if complejidad not in multiplicadores:
            raise CalculoInconsistenteError(
                "El nivel de complejidad no es valido."
            )

        # Calculamos el subtotal segun las horas y la complejidad.
        subtotal = (
            self.precio_base
            * duracion
            * multiplicadores[complejidad]
        )

        # Aplicamos el descuento.
        subtotal_con_descuento = subtotal - (
            subtotal * descuento / 100
        )

        # Calculamos el impuesto.
        valor_impuesto = subtotal_con_descuento * impuesto / 100

        # Sumamos el impuesto para obtener el costo final.
        costo_total = subtotal_con_descuento + valor_impuesto

        # Verificamos que el costo no sea negativo.
        if costo_total < 0:
            raise CalculoInconsistenteError(
                "El calculo de la asesoria genero un costo negativo."
            )

        # Devolvemos el costo final redondeado.
        return round(costo_total, 2)

    # Describimos el servicio de asesoria.
    def describir_servicio(self):

        # Devolvemos la informacion de la asesoria.
        return (
            f"Asesoria especializada: {self.nombre}. "
            f"Especialidad: {self.__especialidad}. "
            f"Precio por hora: ${self.precio_base:.2f}."
        )
