<h1 align="center"> Ticket UM </h1>
<i align="center">

![Covers Subjects](https://github.com/Lucas16AR/TicketUM/assets/83615373/34b568dc-3b36-4078-bf35-03ae554e3cac)

API diseñada como parte de la materia Aseguramiento de la Calidad del Software (ACS) de la Universidad de Mendoza.

</i>

## About
Aplicación creada para el registro y gestión de invitados de diferentes eventos. Esta es una solución de software que tiene como objetivo permitir la gestión de eventos, facilitando la creación, inscripción y administración de estos. Este sistema está diseñado para ser accesible tanto desde una aplicación web como desde una aplicación móvil (que se desarrollará en el futuro por un equipo externo).

## Propósito

El propósito de este documento es delinear los requisitos para la solución de inscripción a eventos que se desarrollará para una empresa/cliente en concreto. Este documento será utilizado por todos los stakeholders, incluidos desarrolladores y testers.

## Contrato de la API

El desarrollo de la API se realizó de acuerdo con los requerimientos y especificaciones acordadas con el cliente, las cuales se documentaron utilizando Swagger. Este contrato define los endpoints disponibles, los métodos HTTP que se pueden usar, los parámetros requeridos y opcionales, así como las respuestas esperadas.

Usted podrá encontrar nuestro contrato en el apartado de documentación, ubicado en la carpeta `docs`.

La documentación incluye:

- **Endpoints**: Lista de todos los endpoints disponibles en la API.
- **Métodos HTTP**: GET, POST, PUT, DELETE, etc.
- **Parámetros**: Detalles sobre los parámetros requeridos y opcionales para cada endpoint.
- **Respuestas**: Descripción de las respuestas esperadas, incluidos los códigos de estado HTTP y los formatos de respuesta.

## Instalación y Ejecución

Sigue estos pasos para instalar y ejecutar la aplicación TicketUM en tu entorno local:

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- virtualenv (opcional pero recomendado)

### Instrucciones de ejecución

#### Paso 1: Clonar el repositorio

Clona este repositorio en tu máquina local usando Git:

```bash
git clone https://github.com/Lucas16AR/TicketUM.git
cd Ticketum
```

#### Paso 2: Crear un entorno virtual y activarlo

```bash
cd ticketum
python3 -m venv .
source bin/activate # En Windows usar `Scripts\activate`
```

#### Paso 3: Instalar Dependencias

```sh
pip install -r requirements.txt
```

#### Paso 4: Configurar variables de entorno

Actualice la configuración de variables en un archivo `.env` para que coincida con la configuración de su base de datos y Flask Mail.

```
# Database configuration
DB_NAME = "db_name_example"
DB_USER = "db_user_example"
DB_PASSWORD = "db_password_example"
DB_HOST = "db_host_example"
DB_PORT = "db_port_example"
DB_ENGINE = "db_engine_example:////" # sqlite for default
DB_PATH = "db/path/to/your/folder"
SV_PORT = 5000

# Mail configuration
# IMPORTANT: You need to enable less secure apps in your gmail account
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "your-mail-here@example.com"
MAIL_PASSWORD = "your-password-here"
```
#### Paso 5: Aplicar Migraciones

```sh
flask db init
flask db migrate -m "Initial Migration"
flask db upgrade
```

#### Paso 6: Ejecutar el servidor de desarrollo de la API

```sh
python3 app.py
```

## Creditos
- Desarrolladores: 
     * [<i>Lucas Galdame</i>](https://github.com/Lucas16AR)
     * [<i>Nicolas Mayoral</i>](https://github.com/NKAmazing)
     * [<i>Enzo Fernandez</i>](https://github.com/EnzoFer)

- Instructor: <i>**Mario Cuevas**</i>

- Institution: [<i>Universidad de Mendoza - Facultad de Ingenieria</i>](https://um.edu.ar/ingenieria/)

![um-cover](https://user-images.githubusercontent.com/83615373/235419081-c36fcb36-c412-4317-b40a-7cad5e937339.png)
