# https://www.mysql.com/ vas a dowload, y buscas la versión más resiente, sistema operativo necesario y requerimientos


"""
🧠 1. Conexión directa con SQL (modo clásico)
🔍 ¿Qué es?
Es conectarte directamente al motor de MySQL usando comandos SQL. Lo haces desde:

La consola (mysql>)

Visual Studio Code con extensiones como SQLTools

MySQL Workbench

🧰 ¿Para qué sirve?
Crear bases de datos y tablas

Insertar, consultar, modificar y borrar datos

Administrar usuarios y permisos

Hacer consultas complejas (JOIN, GROUP BY, etc.)

🧪 Ejemplo:

CREATE DATABASE tienda;
USE tienda;

CREATE TABLE productos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50),
  precio DECIMAL(10,2)
);

INSERT INTO productos (nombre, precio)
VALUES ('Camiseta', 19.99);

SELECT * FROM productos;

🐍 2. Conexión desde Python (modo programático)
🔍 ¿Qué es?
Es usar Python como intermediario para conectarte a MySQL. Usas librerías como:

mysql-connector-python (oficial)

PyMySQL

SQLAlchemy (ORM)

🧰 ¿Para qué sirve?
Crear aplicaciones que usen bases de datos (web, escritorio, scripts)

Automatizar tareas (cargar CSVs, generar informes)

Integrar datos con Pandas, APIs, dashboards, etc.

🧪 Ejemplo básico en Python:

import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="tienda"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM productos")

for fila in cursor.fetchall():
    print(fila)

conexion.close()

🧭 ¿Cuál usar y cuándo?
Situación	Mejor opción
Practicar SQL puro	SQL directo
Crear estructuras y probar queries	SQL directo
Automatizar tareas o apps	Python + MySQL
Integrar con Pandas o APIs	Python + MySQL

"""

### Interfaz gráfica GUI ###

### MySQL Workbench ###

# Cuando logras conectar al servidor MySQL

{
"mysqlOptions": {
    "authProtocol": "default",
    "enableSsl": "Disabled"
},
"previewLimit": 50,
"server": "localhost",
"port": 3306,
"driver": "MySQL",
"name": "Local MySQL",
"database": "mi_primeradbmysql",
"username": "root"
}


### Automatizar e integrar ###

"""
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",  # ← cámbiala por la real (ojo no se publica por razones de confidencialidad a mi propia persona :)
    database="mi_primeradbmysql"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM clientes")

for fila in cursor.fetchall():
    print(fila)

cursor.close()
conexion.close()
"""
### PhPmy admin
### Devart
### SQL pro studio