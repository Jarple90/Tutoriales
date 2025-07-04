"""
📚 Fundamentos de Bases de Datos Relacionales (BDR)

Son sistemas que organizan datos en tablas, con filas (registros) y columnas (atributos).
Se basan en el modelo relacional de Edgar F. Codd.
Buscan integridad, consistencia, eficiencia y facilidad de consulta.

Características clave:

📌 Atomicidad: cada operación es indivisible
🔁 Consistencia: los datos cumplen reglas definidas
🛡️ Integridad referencial: relaciones entre tablas se mantienen correctamente
🧱 Normalización: estructura optimizada (sin duplicidad, con lógica clara)

🧠 ¿Qué es una Entidad?
Una entidad es cualquier “cosa” del mundo real sobre la cual quieres guardar información.

👉 Ejemplos:

Persona
Producto
Curso
Pedido

Cada entidad se representa como una tabla en la base de datos. Cada fila es una instancia (ej: un usuario específico) Cada columna es un atributo (ej: nombre, edad, correo...)

Y cuando relacionas varias entidades → nacen las relaciones (¡sorpresa!).

🗣️ Lenguajes en SQL (clasificación)
SQL se divide en varios sublenguajes, según lo que necesitas hacer:

Tipo de Lenguaje	Nombre	¿Qué hace?	Ejemplos
📄 Definición	DDL (Data Definition Language)	Crear y modificar estructuras	CREATE, ALTER, DROP
📥 Manipulación	DML (Data Manipulation Language)	Insertar, modificar, eliminar datos	INSERT, UPDATE, DELETE
🔍 Consulta	DQL (Data Query Language)	Obtener datos	SELECT
🔐 Control	DCL (Data Control Language)	Gestionar permisos	GRANT, REVOKE
⚙️ Transacción	TCL (Transaction Control Language)	Controlar transacciones	COMMIT, ROLLBACK, SAVEPOINT

Se añade un último aspecto que una relación puede ser de tipo 1:1, 1:n o n:n
"""
