### Type Hints ###

my_string_variable = "My String Variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

my_typed_variable: str = "My typed String Variable"
my_typed_variable
print(my_string_variable)
print(type(my_string_variable))

my_typed_variable: int = 5
print(my_string_variable)
print(type(my_string_variable))

# Buenas prácticas de indicar que type hints para cuando se vaya a realziar FAST API, aunque Python tenga tipado (dinámico), esto ayudará a su lectura y posibles errores

# Instalar Fast API  
"""
Primero es con cd entrar a la carpeta donde queremos levantar nuestro servidor y usar pip install "fastapi[standard]"
"""