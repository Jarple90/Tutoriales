# Variables (buenas prácticas)

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

my_float_variable = 3.14
print(my_float_variable)

print(my_string_variable, my_int_variable, my_bool_variable, my_float_variable)

# Transformación de tipos de variables

my_int_variable = int(my_float_variable)
print(my_int_variable)

print(my_string_variable,type(my_int_variable), my_bool_variable, my_float_variable)

# Concatenación de variables en un print
print(type(my_string_variable), type(my_int_variable), type(my_bool_variable), type(my_float_variable)) #si lo hacemos solo con un type nos daría un error Traceback type() takes 1 or 3 argumentes

print("Este es el valor de:", my_float_variable)
#Funcion len() o contar caracteres de una cadena

print(len(my_string_variable))  # Longitud de la cadena

# Variables en una sola línea
name, surname, alias, age = "José Antonio", "Romero Pérez", "Romero or Snow Ice", 35
print("Me llamo", name, surname, "pero me conocen como", alias, "y tengo", age, "años.")

#Inputs
"""
name = input ('What is your name?')  #Machacamos el valor y reasignando el valor
age = input ('What is your age?')    #Reasignamos el valor

print(name)
print(age)

"""
#Cambiar su tipo de dato

name= 35
age = "José Antonio"

print(name)
print(age)

# Forzamos el tipo de dato

address: str = "My address"
address = 35
print(type(address)) 
