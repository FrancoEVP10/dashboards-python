# Dashboard con Python, MySQL y Flask

Este proyecto consiste en un dashboard que se conecta a una base de datos MySQL, realiza consultas, y presenta la información mediante gráficos y tablas utilizando Python y Flask. Los gráficos se generan utilizando **Matplotlib** y la interfaz web está diseñada con **Bootstrap** para garantizar que sea responsive y agradable visualmente.

## Características del Proyecto

- **Conexión a MySQL**: El proyecto se conecta a una base de datos MySQL donde almacena datos sobre empleados.
- **Gráficos**:
  - Gráfico de barras que muestra la relación entre la **edad** y el **salario** de los empleados.
  - Gráfico circular que representa la cantidad de empleados por **ciudad**.
- **Visualización de Datos**: La información de los empleados se muestra en una tabla dinámica con un diseño moderno y responsive.
- **Despliegue**: El dashboard es accesible a través de un servidor web Flask.

## Tecnologías Utilizadas

- **Python 3.12.5**
- **Flask** para la creación de la aplicación web.
- **MySQL** como base de datos.
- **MySQL Connector** para la conexión entre Python y MySQL.
- **Pandas** para la manipulación de datos.
- **Matplotlib** para la creación de gráficos.
- **Bootstrap 5** para el diseño responsive de la interfaz web.

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.x**
- **MySQL** (servidor local o remoto)
- **pip** (administrador de paquetes de Python)
- **MySQL Connector** (puede ser instalado a través de pip)
- **Flask**
- **Pandas**
- **Matplotlib**

## Configuración del Proyecto

### 1. Clona el Repositorio

```bash
git clone https://github.com/FrancoEVP10/dashboards-python.git
cd dashboards-python
```

### 2. Configura la Base de Datos MySQL
Crea una base de datos y una tabla para almacenar los datos de los empleados:

1. Abre tu cliente de MySQL e ingresa las siguientes consultas para crear la base de datos y la tabla:
```bash
CREATE DATABASE prueba_dashboard;

USE prueba_dashboard;

CREATE TABLE empleados (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    edad INT,
    ciudad VARCHAR(100),
    salario DECIMAL(10,2)
);

INSERT INTO empleados (nombre, edad, ciudad, salario) VALUES
('Juan Pérez', 30, 'Lima', 2500.50),
('María Gómez', 25, 'Cusco', 2000.00),
('Luis Torres', 35, 'Arequipa', 3000.00),
('Ana Ruiz', 28, 'Lima', 2200.00),
('Pedro Flores', 40, 'Trujillo', 3200.75);
```

### 3. Instala las Dependencias
Primero, crea un entorno virtual (opcional pero recomendado) y activa el entorno:

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual (Windows)
.\venv\Scripts\activate

# Activar el entorno virtual (Linux/Mac)
source venv/bin/activate
```

Luego, instala las dependencias requeridas para ejecutar el proyecto:

```bash
pip install -r requirements.txt
```

Al finalizar la ejecución del proyecto, para desactivar el entorno virtual, ejecutar el siguiente comando:
```bash
# Para desactivar el entorno virtual (Windows/Linux/Mac)
deactivate
```

### 4. Configura la Conexión a la Base de Datos
Edita el archivo app.py y asegúrate de que las credenciales de la base de datos estén configuradas correctamente:

```bash
db_connection = mysql.connector.connect(
    host="localhost",       # Cambia si estás usando un servidor MySQL remoto
    user="tu_usuario",       # Cambia por tu usuario de MySQL
    password="tu_contraseña", # Cambia por tu contraseña de MySQL
    database="prueba_dashboard"
)
```
### 5. Ejecuta la Aplicación
Con todas las dependencias instaladas y la base de datos configurada, ya puedes ejecutar la aplicación Flask:

```bash
python app.py
```

La aplicación se ejecutará en el puerto 5000 de tu máquina local. Abre tu navegador y visita la siguiente URL para acceder al dashboard:

```bash
http://127.0.0.1:5000/
```
