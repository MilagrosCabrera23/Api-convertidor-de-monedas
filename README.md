# API de Conversión de Monedas 📊

 ## 📝 Descripción del Proyecto

Esta es una API RESTful robusta y eficiente, construida con FastAPI y SQLAlchemy, diseñada para proporcionar servicios de conversión de monedas en tiempo real (o con datos históricos, si los incluyes). La API permite a los usuarios:

🔹Consultar tipos de cambio: Obtener las tasas de conversión entre diferentes divisas.

🔹Realizar conversiones: Calcular el valor de una cantidad de dinero de una moneda a otra.

🔹Gestión de usuarios: Permitir el registro y la gestión básica de usuarios para un posible historial de conversiones o límites de uso.

El objetivo principal es ofrecer un servicio de conversión de divisas fiable y fácil de integrar para aplicaciones de terceros, sitios web o herramientas internas.

## Características Clave
🔹API RESTful: Diseño siguiendo principios REST para una fácil integración.

🔹FastAPI: Alto rendimiento, fácil de usar y con autogeneración de documentación interactiva (Swagger UI/ReDoc).

🔹SQLAlchemy ORM: Manejo eficiente de la base de datos con un ORM potente y flexible.

🔹Modular y Escabable: Arquitectura en capas para una clara separación de responsabilidades, facilitando el mantenimiento y la adición de nuevas funcionalidades.

🔹Validación de Datos: Uso de Pydantic para una validación estricta de los datos de entrada y salida.

🔹Manejo de Errores: Respuestas claras para errores comunes (ej. moneda no válida, usuario no encontrado).

🔹Contenedorización: Configuración para Docker.

### Tecnologías Utilizadas
Python 3.9+
FastAPI
SQLAlchemy (ORM)
Uvicorn (Servidor ASGI)
Pydantic (Validación de datos)
MYSQL
Git / GitHub
pip (Gestor de paquetes)

### Estructura del Proyecto
La aplicación sigue una Arquitectura en Capas para una óptima separación de responsabilidades:
```
├── app/
│   ├── api/
│   │   ├── dependencies/    # Inyección de dependencias (ej. get_db)
│   │   ├── routers/        # Endpoints de la API (definición de rutas)
│   ├── core/               # Configuración global, excepciones
│   ├── crud/               # Operaciones directas a la base de datos (CRUD)
│   ├── database/           # Configuración de la conexión DB y ORM
│   ├── models/             # Modelos de SQLAlchemy (tablas de DB)
│   ├── schemas/            # Modelos Pydantic (validación de datos de entrada/salida)
│   ├── services/           # Lógica de negocio y orquestación
└── main.py             # Punto de entrada de la aplicación FastAPI
├── venv/                   # Entorno virtual
├── .env                    # Variables de entorno
├── .gitignore              # Archivos a ignorar por Git
├── bd_users.sql            # (Opcional) Script SQL para inicializar DB
├── README.md               # Este archivo
└── requirements.txt        # Dependencias del proyecto
```
 
### Instalación y Ejecución
Sigue estos pasos para configurar y correr la API en tu máquina local:

##### Prerrequisitos
Python 3.9+ instalado.
Un gestor de paquetes Python (preferiblemente pip o Poetry).


## 1. Clonar el repositorio:
```
Bash
git clone https://github.com/MilagrosCabrera23/Api-convertidor-de-monedas.git
cd tu-repo
```
### 2.Crear y activar un entorno virtual:
```
Bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar las dependencias:
```
Bash
pip install -r requirements.txt
(Si usas Poetry, sería poetry install)

#### 4.Configurar las variables de entorno:
Crea un archivo .env en la raíz del proyecto (al mismo nivel que requirements.txt) y añade la configuración necesaria de tu base de datos. Ejemplo:

DATABASE_URL="sqlite:///./app/sql_app.db" # O tu URL de PostgreSQL/MySQL
```

### 5.CEjecutar la API
```
Bash
uvicorn main:app --reload
```
La API estará disponible en http://127.0.0.1:8000.

##  Documentación de la API
FastAPI genera automáticamente documentación interactiva:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc


## Endpoints Disponibles
## A - /users/

### 1 - POST /users/
 Crea un nuevo usuario.
- **Método:** `POST`
- **Body**: JSON con los campos: email (string), password (string).
- **Respuesta:** JSON con el id y email del usuario creado.
- **Validaciones** El email debe ser único. 

### 2 - GET /users/
Obtiene la lista de todos los usuarios.
- **Método:** `GET`
- **Respuesta**: JSON con una lista de objetos de usuario (cada uno con id y email).

### 3- GET /users/{user_id}
Obtiene un usuario por ID.
- **Método:** `GET`
- **Parámetros de ruta:**user_id (integer)
- **Respuesta**: JSON con una lista de objetos de usuario (cada uno con id y email).


### 4- DELETE /users/{user_id}
Elimina un usuario por ID.
- **Método:** `DELETE`
- **Parámetros de ruta:**user_id (integer)
- **Respuesta**: JSON con el id y email del usuario eliminado.


### B: /convert/ 
### 1 -GET /convert/
Convierte una cantidad de dinero de una moneda de origen a una moneda de destino.
- **Método:** `GET`
- **Parámetros de ruta:**
- from_currency: Código de la moneda de origen (ej. USD, EUR, ARS).
- to_currency: Código de la moneda de destino (ej. EUR, JPY, CLP).
- amount: Cantidad numérica a convertir.
- **Respuesta**: JSON con los detalles de la conversión.




## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

