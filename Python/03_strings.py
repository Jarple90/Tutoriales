### Strings ###

my_string = "Hola Python"
my_other_string = "¿Qué vas a aprender hoy?"

print(len(my_string))  # Longitud de la cadena
print(len(my_other_string))  # Longitud de la otra cadena

print(my_string + " " + my_other_string)  # Concatenación de cadenas

my_new_line_string = "Este es un string con tabulación \ncon salto de línea"
print(my_new_line_string)  # Imprimir el string con tabulación y salto de línea

my_tab_string = "\tEste es un string con tabulación con tabulación"
print(my_tab_string)  # Imprimir el string con tabulación

my_scape_string = "\\tEste es un string con un \\n escapadas"
print(my_scape_string)  # Imprimir el string con caracteres escapados

# Formateo

name, surname, age = "José Antonio", "Romero Pérez", 35
print("Mi nombre es %s %s y tengo %d años." % (name, surname, age))  # Formateo con el operador %
print("Mi nombre es {} {} y tengo {} años.".format(name, surname, age))  # Formateo con el método format
print(f"Mi nombre es {name} {surname} y tengo {age} años.")  # Formateo con f-strings (Python 3.6+)

# desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language  # Desempaquetado de caracteres
print(a)
print(e)

# Division de caracteres

language_slice = language[0:3]  # División de caracteres (slice)
print(language_slice)  # Imprimimos la división de caracteres

laguage_slice = language[1:]  # División de caracteres desde el segundo carácter
print(language_slice)  # Imprimimos la división de caracteres desde el segundo carácter

language_slice = language[-2:]  # División de caracteres desde el penúltimo carácter
print(language_slice)  # Imprimimos la división de caracteres desde el penúltimo carácter

language_slice = language[0:6:2]  # División de caracteres con paso
print(language_slice)  # Imprimimos la división de caracteres con paso

# Revere de caracteres
language_reverse = language[::-1]  # Inversión de caracteres
print(language_reverse)  # Imprimimos la inversión de caracteres

# Funciones de cadenas

print(language.capitalize())  # Mayúscula en la primera letra
print(language.upper())  # Mayúsculas en toda la cadena
print(language.lower())  # Minúsculas en toda la cadena
print(language.count("o"))  # Contamos ocurrencias de un carácter
print(language.find("t"))  # Encontramos la posición de un carácter
print(language.isnumeric)()  # Verificamos si la cadena es numérica
print(language.upper().isupper())  # Verificamos si la cadena está en mayúsculas
print("1".isnumeric())  # Verificamos si la cadena "1" es numérica
print(language.startswith("P"))  # Verificamos si la cadena comienza con "P"
print(language.endswith("n"))  # Verificamos si la cadena termina con "n"
print(language.replace("P", "J"))  # Reemplazamos un carácter por otro
print(language.split("t"))  # Dividimos la cadena en una lista por el carácter "t"   
print("Py" == "Py")  # Comparamos dos cadenas




