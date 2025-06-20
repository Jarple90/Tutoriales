#Conectar MongoDB con VSC mediante la extension MongoDB for vs code
# Luengo en nuestro caso teniamos el programa descargado y creado un localhost:27017 por lo que se ha podido conectar a los ejercicios del Máster

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db_client = client["usuarios_db"]  # Aquí seleccionas la base de datos
