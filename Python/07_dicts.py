### Dictionaries en Python	###


my_dict = dict() # Una forma de crear un diccionario
my_other_dict = {} # Otra forma de crear un diccionario

print(type(my_dict)) # Imprime <class 'dict'>
print(type(my_other_dict)) # Imprime <class 'dict'>

my_other_dict = {"Nombre": "José Antonio", "Apellido": "Romero Pérez", "Edad": 35, 1: "Python"} # Un diccionario puede tener claves de diferentes tipos, como cadenas, enteros, etc.
my_dict = {"Nombre": "José Antonio", "Apellido": "Romero Pérez", "Edad": 35, 1: "Python"} # Otra tipo de diccionario con claves y valores

my_dict = {
    "Nombre": "José Antonio",
    "Apellido": "Romero Pérez",
    "Edad": 35,
    "Lenguajes": {"Python", "JavaScript", "C++"},
    1: 1.78
} # Otra forma de crear un diccionario con varios tipos de datos y un conjunto como valor

print(my_other_dict)
print(my_dict)

print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle José Antonio"
print(my_dict)

# del my_dict["Calle"]
# print(my_dict)

print("José Antonio" in my_dict) # Da false porque la clave es "Nombre"
print("Snow Ice" in my_dict) # Da false porque no existe la clave

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
#print(my_dict.fromkeys(("Nombre", 1)))

my_list =["Nombre", 1, "Apellido"]

my_new_dict = my_other_dict.fromkeys(("Nombre",1,"Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,("José Antonio", "Romero Pérez"))
print(my_new_dict)

my_values= my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(dict.fromkeys(list(my_new_dict.values())).keys()) # esto devuelve las claves de un diccionario con los valores únicos
print(tuple(my_new_dict)) # esto devuelve las claves de un diccionario con los valores únicos
print(set(my_new_dict)) # esto devuelve las claves de un diccionario con los valores únicos
