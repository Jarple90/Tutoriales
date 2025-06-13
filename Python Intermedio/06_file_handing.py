### File Handing en Python ###

# r " → Abre el archivo solo para leer. Genera error si el archivo no existe.
# "r+" → Permite leer y escribir sin borrar el contenido. Error si el archivo no existe.
# "w" → Sobrescribe el archivo o lo crea si no existe. Borra todo el contenido previo.
#"w+" → Permite escribir y leer, pero borra todo el contenido del archivo antes de escribir.
#"a" → Abre el archivo solo para agregar contenido al final. No borra lo existente.
#"a+" → Permite leer y agregar contenido al final sin borrar lo anterior.

# .txt file

import os

txt_file = open(r"R:\PROYECTOS\Python Intermedio\my_file.txt", "r+") # Abre el texto, hay que tener en cuenta el disco duro al principio y la ruta

# print(txt_file.read())
# print(txt_file.read(10))
# print(txt_file.readline())


# Abrir y leer el archivo
with open(r"R:\PROYECTOS\Python Intermedio\my_file.txt", "r+", encoding="utf-8") as txt_file:
    contenido = txt_file.read()
    print(contenido)  # Mostrar contenido antes de escribir
    
    txt_file.write("\nAunque he trabajado en muchos sectores")  # Agregar nueva línea
    txt_file.seek(0)  # Mover el cursor al inicio después de escribir
    print(txt_file.readline())  # Leer la primera línea después de escribir


# **CERRAR el archivo automáticamente con `with open()`**
print("El archivo 'my_file.txt' ha sido cerrado correctamente.")

# **CREAR otro archivo y escribir contenido**
with open(r"R:\PROYECTOS\Python Intermedio\my_other_file.txt", "w", encoding="utf-8") as my_other_file:
    my_other_file.write("Este es un nuevo archivo.\n")
    my_other_file.write("Aquí seguiré practicando la manipulación de archivos.\n")
    my_other_file.write("¡Python es genial!")

print("El archivo 'my_other_file.txt' ha sido creado exitosamente.")

#os.remove # añadimos la ruta y eliminaría el archivo

import json


# Datos de ejemplo para guardar en el archivo JSON

data = {
    "nombre": "Jose Antonio",
    "apellido": "Romero Perez",
    "edad": 35,
    "profesion": "Data Scientist en formación" "Workday HCM en Estructura y Servicing"
}

# Crear y escribir en el archivo JSON

with open(r"R:\PROYECTOS\Python Intermedio\json_file.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent= 4)  # Guardar el diccionario en formato JSON con sangría

print("El archivo JSON ha sido creado exitosamente.")

json_dict = json.load(open(r"R:\PROYECTOS\Python Intermedio\json_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["nombre"])

# csv. file

# import csv

# .xlsx file

# import xlrd # se debe instalar el modulo

# xml 

# import xml


