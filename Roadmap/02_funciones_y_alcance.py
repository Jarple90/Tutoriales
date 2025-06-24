"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

### Funciones definidas por el usuario ###

# Función simple: muestra un saludo fijo
def greet():
    print("Hola, python, soy José Antonio Romero Pérez")

greet()

# Función con retorno: devuelve un saludo como cadena de texto
def return_greet():
    return "Hola, Python, sigo siendo José Antonio Romero Pérez"

# Sobrescribimos greet con el valor retornado (¡ojo con esto!)
greet = return_greet()
print(return_greet())

# Función con un argumento: personaliza el saludo
def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet("José Antonio")

# Función con varios argumentos
def args_greet(greet, name):
    print(f"{greet}, {name}")

args_greet("Hello", "José Antonio")

# Función con argumento predeterminado
def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")

default_arg_greet("Romero")   # Usa el nombre proporcionado
default_arg_greet()           # Usa el valor por defecto

# Función con varios argumentos y retorno
def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hi", "José Antonio"))

# Función que devuelve múltiples valores
def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Función con número variable de argumentos (posicionales)
def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "José Antonio", "Snow Ice", "Prueba")

# Función con número variable de argumentos con palabra clave
def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"Hola, {value} ({key})!")

variable_key_arg_greet(
    language="Python",
    name="José Antonio",
    alias="Snow Ice",
    age=35
)

### Funciones dentro de funciones ###

# Función externa que contiene otra función
def outer_function():
    def inner_function():
        print("Función interna: Hola, Python!")
    inner_function()

outer_function()

### Funciones integradas del lenguaje (built-in) ###

print(len("José Antonio"))  # Devuelve la longitud de la cadena
print(type(35))             # Muestra el tipo de dato
print(" José Antonio".upper())  # Convierte la cadena a mayúsculas

### Variables locales y globales ###

global_var = "Python"  # Variable global

def hello_python():
    local_var = "Hola"  # Variable local, solo accesible dentro de la función
    print(f"{local_var}, {global_var}")

print(global_var)
# print(local_var)  # Esto produciría un error, ya que local_var no existe fuera de la función
hello_python()

### Extra: Versión FizzBuzz personalizada ###

# Imprime números del 1 al 100 con condiciones especiales
def print_numbers(text1, text2) -> int:
    count = 0  # Contador de cuántos números NO son múltiplos de 3 o 5
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text1 + text2)
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else:
            print(number)
            count += 1
    return count  # Devuelve cuántos números normales se imprimieron

print_numbers("Fizz", "Buzz")
