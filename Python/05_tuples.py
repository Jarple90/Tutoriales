### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "José Antonio", "Romero Pérez")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])


print(my_tuple.count("José Antonio")) # Cuenta cuántas veces aparece un elemento dentro de la tupla
print(my_tuple.index("José Antonio")) # Devuelve el índice de la primera aparición del elemento dentro de la tupla
print(my_tuple.index("Romero Pérez")) # Devuelve el índice de la primera aparición del elemento dentro de la tupla

# Error al intentar modificar un elemento de la tupla
# my_tuple[0] = 36 # TypeError: 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6]) # Slicing de tuplas


my_tuple = list(my_tuple) # Convierte la tupla en una lista
print(type(my_tuple))


my_tuple[2] = "Romero"
my_tuple.insert(1,"Azul")
my_tuple = tuple(my_tuple) # Convierte la lista en una tupla
print(my_tuple)
print(type(my_tuple))

# del my_tuple # Elimina la tupla 
# print(my_tuple) # NameError: name 'my_tuple' is not defined

