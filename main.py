
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: main.py
# DESCRIPCION: Programa principal del sistema.
# =====================================================

# Importamos las clases del sistema.
from modelos.cliente import Cliente
from modelos.reserva import Reserva
from modelos.reserva_sala import ReservaSala
from modelos.alquiler_equipo import AlquilerEquipo
from modelos.asesoria import Asesoria

# Importamos las excepciones personalizadas.
from modelos.excepciones import (
    ErrorSoftwareFJ,
    ClienteNoEncontradoError,
    ServicioNoEncontradoError,
    ReservaNoEncontradaError,
    ReservaDuplicadaError
)

# Importamos el logger.
from utils.logger import LoggerSoftwareFJ


# =====================================================
# CLASE PRINCIPAL PARA ADMINISTRAR EL SISTEMA
# =====================================================

class GestorSistema:

    # Constructor.
    def __init__(self):

        # Listas privadas para almacenar los objetos.
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

        # Registramos el inicio del sistema.
        LoggerSoftwareFJ.registrar_evento(
            "Sistema integral Software FJ iniciado."
        )

    # -------------------------------------------------
    # REGISTRAR CLIENTES
    # -------------------------------------------------

    def registrar_cliente(self, cliente):

        # Verificamos que no exista otro cliente con el mismo documento.
        for existente in self.__clientes:

            if existente.documento == cliente.documento:
                raise ErrorSoftwareFJ(
                    "Ya existe un cliente con ese documento."
                )

        # Guardamos el cliente.
        self.__clientes.append(cliente)

        # Registramos el evento.
        LoggerSoftwareFJ.registrar_evento(
            f"Cliente registrado: {cliente.nombre}"
        )

        return "Cliente registrado correctamente."

    # -------------------------------------------------
    # BUSCAR CLIENTES
    # -------------------------------------------------

    def buscar_cliente(self, documento):

        for cliente in self.__clientes:

            if cliente.documento == documento:
                return cliente

        raise ClienteNoEncontradoError(
            "No se encontro el cliente solicitado."
        )

    # -------------------------------------------------
    # REGISTRAR SERVICIOS
    # -------------------------------------------------

    def registrar_servicio(self, servicio):

        # Evitamos registrar dos servicios con el mismo identificador.
        for existente in self.__servicios:

            if existente.identificador == servicio.identificador:
                raise ErrorSoftwareFJ(
                    "Ya existe un servicio con ese identificador."
                )

        # Guardamos el servicio.
        self.__servicios.append(servicio)

        # Registramos el evento.
        LoggerSoftwareFJ.registrar_evento(
            f"Servicio registrado: {servicio.nombre}"
        )

        return "Servicio registrado correctamente."

    # -------------------------------------------------
    # BUSCAR SERVICIOS
    # -------------------------------------------------

    def buscar_servicio(self, identificador):

        for servicio in self.__servicios:

            if servicio.identificador == identificador:
                return servicio

        raise ServicioNoEncontradoError(
            "No se encontro el servicio solicitado."
        )

    # -------------------------------------------------
    # CREAR RESERVAS
    # -------------------------------------------------

    def crear_reserva(
        self,
        identificador,
        documento_cliente,
        identificador_servicio,
        duracion,
        parametros_servicio=None
    ):

        # Verificamos que no exista la reserva.
        for reserva in self.__reservas:

            if reserva.identificador == identificador:
                raise ReservaDuplicadaError(
                    "Ya existe una reserva con ese identificador."
                )

        # Buscamos el cliente.
        cliente = self.buscar_cliente(documento_cliente)

        # Buscamos el servicio.
        servicio = self.buscar_servicio(identificador_servicio)

        # Creamos el objeto reserva.
        reserva = Reserva(
            identificador,
            cliente,
            servicio,
            duracion,
            parametros_servicio
        )

        # Guardamos la reserva.
        self.__reservas.append(reserva)

        # Registramos el evento.
        LoggerSoftwareFJ.registrar_evento(
            f"Reserva creada: {identificador}"
        )

        return reserva

    # -------------------------------------------------
    # BUSCAR RESERVAS
    # -------------------------------------------------

    def buscar_reserva(self, identificador):

        for reserva in self.__reservas:

            if reserva.identificador == identificador:
                return reserva

        raise ReservaNoEncontradaError(
            "No se encontro la reserva solicitada."
        )

    # -------------------------------------------------
    # LISTAR CLIENTES
    # -------------------------------------------------

    def listar_clientes(self):
        return self.__clientes.copy()

    # -------------------------------------------------
    # LISTAR SERVICIOS
    # -------------------------------------------------

    def listar_servicios(self):
        return self.__servicios.copy()

    # -------------------------------------------------
    # LISTAR RESERVAS
    # -------------------------------------------------

    def listar_reservas(self):
        return self.__reservas.copy()


# =====================================================
# PROGRAMA PRINCIPAL
# =====================================================

if __name__ == "__main__":

    # Creamos el gestor del sistema.
    sistema = GestorSistema()

    print("=" * 55)
    print("SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
    print("=" * 55)

    # -------------------------------------------------
    # 1. REGISTRO DE CLIENTES
    # -------------------------------------------------

    print("\n1. REGISTRO DE CLIENTES")

    try:

        cliente = Cliente(
            "C001",
            "Carlos Perez",
            "1234567890",
            "carlos@gmail.com",
            "3001234567"
        )

        print(sistema.registrar_cliente(cliente))

    except Exception as error:

        print("Error al registrar cliente:", error)

        LoggerSoftwareFJ.registrar_error(
            "Error al registrar cliente",
            error
        )

    # Probamos registrar un cliente invalido.
    try:

        cliente_invalido = Cliente(
            "C002",
            "",
            "9876543210",
            "correo@gmail.com",
            "3001234567"
        )

        sistema.registrar_cliente(cliente_invalido)

    except Exception as error:

        print("Error controlado de cliente:", error)

        LoggerSoftwareFJ.registrar_error(
            "Error al intentar registrar un cliente invalido",
            error
        )

    # -------------------------------------------------
    # 2. REGISTRO DE SERVICIOS
    # -------------------------------------------------

    print("\n2. REGISTRO DE SERVICIOS")

    try:

        # Creamos la sala con capacidad y disponibilidad.
        sala = ReservaSala(
            "S001",
            "Sala de reuniones",
            50000,
            20,
            True
        )

        # Creamos el equipo con cantidad y disponibilidad.
        equipo = AlquilerEquipo(
            "S002",
            "Computador portatil",
            30000,
            10,
            True
        )

        # Creamos la asesoria con especialidad y disponibilidad.
        asesoria = Asesoria(
            "S003",
            "Asesoria de software",
            80000,
            "Desarrollo de software",
            True
        )

        # Registramos los tres servicios.
        print(sistema.registrar_servicio(sala))
        print(sistema.registrar_servicio(equipo))
        print(sistema.registrar_servicio(asesoria))

    except Exception as error:

        print("Error al registrar servicios:", error)

        LoggerSoftwareFJ.registrar_error(
            "Error al registrar servicios",
            error
        )

    # -------------------------------------------------
    # 3. CREACION Y PROCESAMIENTO DE RESERVAS
    # -------------------------------------------------

    print("\n3. CREACION Y PROCESAMIENTO DE RESERVAS")

    # Reserva de sala.
    try:

        reserva1 = sistema.crear_reserva(
            "R001",
            "1234567890",
            "S001",
            2,
            {"personas": 5}
        )

        reserva1.confirmar()

        costo1 = reserva1.procesar(
            impuesto=19,
            descuento=0
        )

        print("Reserva de sala procesada correctamente.")
        print("Costo total:", costo1)

    except Exception as error:

        print("Error en reserva de sala:", error)

        LoggerSoftwareFJ.registrar_error(
            "Error al procesar reserva de sala",
            error
        )

    # Reserva de equipo.
    try:

        reserva2 = sistema.crear_reserva(
            "R002",
            "1234567890",
            "S002",
            3,
            {"cantidad": 2}
        )

        reserva2.confirmar()

        costo2 = reserva2.procesar(
            impuesto=0,
            descuento=10
        )

        print("Reserva de equipo procesada correctamente.")
        print("Costo total:", costo2)

    except Exception as error:

        print("Error en reserva de equipo:", error)

        LoggerSoftwareFJ.registrar_error(
            "Error al procesar reserva de equipo",
            error
        )

    # Reserva de asesoria.
    try:

        reserva3 = sistema.crear_reserva(
            "R003",
            "1234567890",
            "S003",
            2,
            {"complejidad": "avanzado"}
        )

        reserva3.confirmar()

        costo3 = reserva3.procesar(
            impuesto=19,
            descuento=5
        )

        print("Reserva de asesoria procesada correctamente.")
        print("Costo total:", costo3)

    except Exception as error:

        print("Error en reserva de asesoria:", error)

        LoggerSoftwareFJ.registrar_error(
            "Error al procesar reserva de asesoria",
            error
        )

    # -------------------------------------------------
    # 4. PRUEBAS DE ERRORES
    # -------------------------------------------------

    print("\n4. PRUEBAS DE ERRORES")

    # Buscar cliente inexistente.
    try:

        sistema.buscar_cliente("9999999999")

    except Exception as error:

        print("Error controlado al buscar cliente:", error)

        LoggerSoftwareFJ.registrar_error(
            "Error al buscar un cliente inexistente",
            error
        )

    # Buscar servicio inexistente.
    try:

        sistema.buscar_servicio("S999")

    except Exception as error:

        print("Error controlado al buscar servicio:", error)

        LoggerSoftwareFJ.registrar_error(
            "Error al buscar un servicio inexistente",
            error
        )

    # Crear reserva con servicio inexistente.
    try:

        sistema.crear_reserva(
            "R004",
            "1234567890",
            "S999",
            2
        )

    except Exception as error:

        print("Error controlado al crear reserva:", error)

        LoggerSoftwareFJ.registrar_error(
            "Error al crear una reserva con un servicio inexistente",
            error
        )

    # -------------------------------------------------
    # 5. PRUEBAS DE CANCELACION
    # -------------------------------------------------

    print("\n5. PRUEBAS DE CANCELACION")

    # Creamos una reserva pendiente.
    try:

        reserva_cancelada = sistema.crear_reserva(
            "R005",
            "1234567890",
            "S001",
            2,
            {"personas": 5}
        )

        # Cancelamos la reserva.
        print(reserva_cancelada.cancelar())

        print("Estado actual:", reserva_cancelada.estado)

    except Exception as error:

        print("Error durante la cancelacion:", error)

        LoggerSoftwareFJ.registrar_error(
            "Error durante la prueba de cancelacion",
            error
        )

    # Intentamos confirmar una reserva cancelada.
    try:

        reserva_cancelada.confirmar()

    except Exception as error:

        print(
            "Error controlado al confirmar una reserva cancelada:",
            error
        )

        LoggerSoftwareFJ.registrar_error(
            "Intento de confirmar una reserva cancelada",
            error
        )

    # -------------------------------------------------
    # 6. INTENTO DE CANCELAR UNA RESERVA PROCESADA
    # -------------------------------------------------

    print("\n6. PRUEBA DE CANCELACION DE RESERVA PROCESADA")

    try:

        reserva1.cancelar()

    except Exception as error:

        print(
            "Error controlado al cancelar una reserva procesada:",
            error
        )

        LoggerSoftwareFJ.registrar_error(
            "Intento de cancelar una reserva procesada",
            error
        )

    # -------------------------------------------------
    # 7. CONSULTA DE INFORMACION
    # -------------------------------------------------

    print("\n7. CONSULTA DE INFORMACION DE RESERVAS")

    try:

        print(reserva1.obtener_informacion())

        print("\n")

        print(reserva_cancelada.obtener_informacion())

    except Exception as error:

        print("Error al consultar informacion:", error)

        LoggerSoftwareFJ.registrar_error(
            "Error al consultar informacion de reservas",
            error
        )

    # -------------------------------------------------
    # 8. RESUMEN FINAL DEL SISTEMA
    # -------------------------------------------------

    print("\n8. RESUMEN FINAL DEL SISTEMA")

    print("Total de clientes:", len(sistema.listar_clientes()))
    print("Total de servicios:", len(sistema.listar_servicios()))
    print("Total de reservas:", len(sistema.listar_reservas()))

    print("\nESTADO DE LAS RESERVAS")

    for reserva in sistema.listar_reservas():

        print(
            reserva.identificador,
            "-",
            reserva.estado
        )

    print("\nEl sistema finalizo las pruebas correctamente.")

    print("=" * 55)
