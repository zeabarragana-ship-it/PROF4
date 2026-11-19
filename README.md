# SOFTWARE FJ
## FASE 4 - COMPONENTE PRÁCTICO - PRÁCTICAS SIMULADAS

### 1. Descripción del proyecto

Software FJ es un sistema integral de gestión de clientes, servicios y reservas, desarrollado en Python utilizando programación orientada a objetos.

El sistema permite registrar clientes, administrar servicios, crear reservas, calcular costos, confirmar y cancelar reservas, y controlar errores mediante excepciones personalizadas.

### 2. Objetivo

Desarrollar una aplicación modular que aplique los principios de programación orientada a objetos, incluyendo:

- Abstracción.
- Encapsulamiento.
- Herencia.
- Polimorfismo.
- Manejo de excepciones.
- Registro de eventos y errores.

### 3. Servicios disponibles

El sistema ofrece tres servicios especializados:

1. Reserva de salas: permite reservar espacios según su capacidad.
2. Alquiler de equipos: permite alquilar equipos según la cantidad disponible.
3. Asesoría especializada: permite contratar asesorías según su nivel de complejidad.

### 4. Estructura del proyecto

- `main.py`: programa principal y administración del sistema.
- `modelos/entidad.py`: clase abstracta Entidad.
- `modelos/cliente.py`: gestión y validación de clientes.
- `modelos/servicio.py`: clase abstracta Servicio.
- `modelos/reserva_sala.py`: servicio de reserva de salas.
- `modelos/alquiler_equipo.py`: servicio de alquiler de equipos.
- `modelos/asesoria.py`: servicio de asesoría especializada.
- `modelos/reserva.py`: gestión de reservas.
- `modelos/excepciones.py`: excepciones personalizadas.
- `utils/logger.py`: registro de eventos y errores.
- `logs.log`: archivo generado para almacenar los registros del sistema.

### 5. Funcionamiento

El sistema permite:

- Registrar y consultar clientes.
- Registrar y consultar servicios.
- Crear reservas asociadas a clientes y servicios.
- Confirmar y cancelar reservas.
- Procesar reservas y calcular costos.
- Aplicar impuestos y descuentos.
- Validar datos y parámetros.
- Controlar operaciones no permitidas.
- Registrar eventos y errores.

### 6. Manejo de excepciones

Se implementan excepciones personalizadas para controlar errores relacionados con clientes, servicios, reservas, parámetros faltantes y cálculos inconsistentes.

Los errores se capturan para permitir que el programa continúe ejecutándose.

### 7. Almacenamiento de información

Los clientes, servicios y reservas se almacenan en listas en memoria durante la ejecución del programa.

No se utiliza una base de datos. El archivo `logs.log` se utiliza exclusivamente para registrar eventos y errores.

### 8. Requisitos para ejecutar

- Python 3 instalado.
- Visual Studio Code (recomendado).

### 9. Ejecución

Desde la terminal, ubicarse en la carpeta principal del proyecto y ejecutar:

```bash
python main.py
```

### 10. Pruebas realizadas

El programa principal incluye pruebas de:

- Registro correcto e incorrecto de clientes.
- Registro de los tres servicios.
- Creación y procesamiento de reservas.
- Búsqueda de clientes y servicios inexistentes.
- Intentos de creación de reservas inválidas.
- Cancelación de reservas.
- Intentos de realizar operaciones no permitidas.
- Consulta y resumen de las reservas.

### 11. Autor

Proyecto académico desarrollado para la Fase 4 de programación orientada a objetos. Andres Zea