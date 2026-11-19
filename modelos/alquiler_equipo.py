
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: alquiler_equipo.py
# DESCRIPCION: Gestion del servicio de alquiler de equipos.
# =====================================================

# Importamos la clase Servicio para aplicar herencia.
from modelos.servicio import Servicio

# Importamos las excepciones personalizadas.
from modelos.excepciones import (
    ParametroFaltanteError,
    CalculoInconsistenteError
)


# Creamos la clase AlquilerEquipo que hereda de Servicio.
class AlquilerEquipo(Servicio):

    # Constructor de la clase.
    def __init__(self, identificador, nombre, precio_base,
                 cantidad_disponible, disponible=True):

        # Inicializamos los atributos de la clase padre.
        super().__init__(identificador, nombre, precio_base, disponible)

        # Verificamos que la cantidad sea un numero entero.
        if isinstance(cantidad_disponible, bool) or not isinstance(cantidad_disponible, int):
            raise CalculoInconsistenteError(
                "La cantidad disponible debe ser un numero entero."
            )

        # Verificamos que existan equipos disponibles.
        if cantidad_disponible < 0:
            raise CalculoInconsistenteError(
                "La cantidad disponible no puede ser negativa."
            )

        # Guardamos la cantidad como atributo privado.
        self.__cantidad_disponible = cantidad_disponible

    # Propiedad para consultar la cantidad disponible.
    @property
    def cantidad_disponible(self):
        return self.__cantidad_disponible

    # Implementamos la validacion general del servicio.
    def validar(self):

        # Ejecutamos las validaciones de la clase padre.
        super().validar()

        # Verificamos que la cantidad disponible no sea negativa.
        if self.__cantidad_disponible < 0:
            raise CalculoInconsistenteError(
                "La cantidad disponible no es valida."
            )

        # Indicamos que el servicio es valido.
        return True

    # Validamos los parametros necesarios para alquilar equipos.
    def validar_parametros(self, **parametros):

        # Obtenemos la cantidad de equipos solicitados.
        cantidad = parametros.get("cantidad")

        # Verificamos que se haya indicado una cantidad.
        if cantidad is None:
            raise ParametroFaltanteError(
                "Debe indicar la cantidad de equipos que desea alquilar."
            )

        # Verificamos que la cantidad sea un entero positivo.
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise CalculoInconsistenteError(
                "La cantidad de equipos debe ser un entero positivo."
            )

        # Verificamos que existan suficientes equipos.
        if cantidad > self.__cantidad_disponible:
            raise CalculoInconsistenteError(
                "No hay suficientes equipos disponibles."
            )

        # Devolvemos True si los parametros son correctos.
        return True

    # Calculamos el costo del alquiler de equipos.
    def calcular_costo(self, duracion, impuesto=0, descuento=0,
                       cantidad=1):

        # Verificamos que la duracion sea numerica y positiva.
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise CalculoInconsistenteError(
                "La duracion del alquiler debe ser mayor que cero."
            )

        # Verificamos que la cantidad sea un entero positivo.
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise CalculoInconsistenteError(
                "La cantidad de equipos debe ser un entero positivo."
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

        # Calculamos el subtotal segun duracion y cantidad.
        subtotal = self.precio_base * duracion * cantidad

        # Aplicamos el descuento.
        subtotal_con_descuento = subtotal - (
            subtotal * descuento / 100
        )

        # Calculamos el valor del impuesto.
        valor_impuesto = subtotal_con_descuento * impuesto / 100

        # Sumamos el impuesto para obtener el costo final.
        costo_total = subtotal_con_descuento + valor_impuesto

        # Verificamos que el resultado no sea negativo.
        if costo_total < 0:
            raise CalculoInconsistenteError(
                "El calculo del alquiler genero un costo negativo."
            )

        # Devolvemos el costo final redondeado.
        return round(costo_total, 2)

    # Describimos el servicio de alquiler de equipos.
    def describir_servicio(self):

        # Devolvemos la informacion del servicio.
        return (
            f"Alquiler de equipos: {self.nombre}. "
            f"Cantidad disponible: {self.__cantidad_disponible}. "
            f"Precio por dia: ${self.precio_base:.2f}."
        )
