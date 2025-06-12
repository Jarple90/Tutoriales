### Error Types en Python ###

# SyntaxError

#print "Hola, soy un error de sintaxis" #Error de sintaxis
print ("Hola, soy un error de sintaxis arreglado")

# NameError
language = "Spanish" # realizar para que print no tenga un error, necesitamos definir la variable language
print(language) # Imprime el valor de la variable language si no está definido language, se produce un NameError

# IndexError

my_list = ["Python", "Java", "Switft", "JavaScript", "Dart"]
print(my_list[0]) # Imprime el primer elemento de la lista
print(my_list[1]) # Imprime el segundo elemento de la lista
print(my_list[2]) # Imprime el tercer elemento de la lista
print(my_list[-1])  # Imprime el último elemento de la lista
# print(my_list[5]) # Error de índice, ya que no hay un elemento en la posición 5

# ModuleNotFoundError

# import maths # Descomentar para Error

import math

#AtributeError

# print(math.PI) # Error a no nombrarlo correctamente

print(math.pi)

#KeyError

my_dict = {"Nombre": "José Antonio", "Apellidos": "Romero Pérez", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apellido"]) #Descomentar para Error 
print(my_dict["Apellidos"])

#TypeError
#print(my_list["0"]) # Descomentar para ver el error
print(my_list[0])

#ImportError

#from math import PI # Descomentar para ver el error
from math import pi
print(pi)

# ValueError

my_int = int("10")
# my_int = int("10 años") # No hay forma de transformalo en un entero
print(type(my_int))

# ZeroDivisionError

print(4/2)
# print(4/0)   # Error no se puede dividir entre cero