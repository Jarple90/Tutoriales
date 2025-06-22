"""
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
"""
# 🐍 Proyecto de introducción a Python

# Página oficial: https://python.org

# ---------- COMENTARIOS EN PYTHON ----------

# Comentario de una línea: útil para notas rápidas

"""
Comentario en varias líneas: útil para explicar fragmentos largos
o descripciones de código (también puede usarse con ''').
"""
# ---------- VARIABLES Y TIPOS DE DATOS ----------

# Las variables se crean al asignarles un valor. No es necesario declarar el tipo.

# Cadenas de texto (strings)
x = "mi variable"  # Nombre genérico
my_variable = "Mi variable"
my_string = "Mi cadena de texto"
my_other_string = "Mi otra cadena de texto"

# Entero (int)
my_int = 1

# Números con decimales (float)
my_float = 3.5

# Booleanos (bool): pueden ser True o False
my_bool = False
#my_bool = True  # Esta línea sobrescribe la anterior

# Constantes: en Python no existen formalmente,
# pero por convención se escriben en mayúsculas

MY_CONSTANT = "Mi constante"

# ---------- SALIDA EN CONSOLA ----------

# Mostrar un mensaje personalizado
print("Hola, Python, soy Jose Antonio Romero Perez")

# Mostrar el tipo de cada variable
print(type(my_int))           # <class 'int'>
print(type(my_float))         # <class 'float'>
print(type(my_bool))          # <class 'bool'> (valor actual: True)
print(type(my_string))        # <class 'str'>
print(type(my_other_string))  # <class 'str'>
