### Lists ###

my_list = list()  # Creamos una lista vacía
my_other_list = []  # Otra forma de crear una lista vacía

print(len(my_list))  # Imprimimos la longitud de la lista (debería ser 0) porque está vacía

my_list = [35,35, 15, 25, 45, 60, 75, 80, 90]  # Creamos una lista con varios números

print(my_list)  # Imprimimos la lista de números
print(len(my_list))  # Imprimimos la longitud de la lista (debería ser 9)

my_other_list = [35, 1.77, "José Antonio", "Romero Pérez"]  # Creamos una lista con diferentes tipos de datos

print(type(my_other_list))  # Imprimimos el tipo de la lista (debería ser <class 'list'>)

print(type(my_list))  # Imprimimos la lista con diferentes tipos de datos
print(type(my_other_list))  # Imprimimos el tipo de la lista con diferentes tipos de datos

print(my_other_list[0])  # Imprimimos el primer elemento de la lista (35)
print(my_other_list[1])  # Imprimimos el segundo elemento de la lista (1.77)        
print(my_other_list[2])  # Imprimimos el tercer elemento de la lista ("José Antonio")
print(my_other_list[3])  # Imprimimos el cuarto elemento de la lista ("Romero Pérez")
print(my_other_list[-1])  # Imprimimos el último elemento de la lista ("Romero Pérez")
print(my_other_list[-2])  # Imprimimos el penúltimo elemento de la lista ("José Antonio")
print(my_other_list[-3])  # Imprimimos el antepenúltimo elemento de la lista (1.77)

print(my_other_list.count(35))  # Imprimimos el número de elementos de la lista (debería ser 4)

age, height, name, surname = my_other_list  # Asignamos los valores de la lista a variables
print(name)  # Imprimimos el nombre (José Antonio)

## name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]  # Asignamos los valores de la lista a variables de forma individual
## print(age)  # Imprimimos la edad

print(my_list + my_other_list)  # Concatenamos las dos listas e imprimimos el resultado

my_other_list.append("Snow Ice")  # Añadimos un nuevo elemento al final de la lista
print(my_other_list)  # Imprimimos la lista con el nuevo elemento añadido

my_other_list.insert(1, "Azul") # Insertamos un nuevo elemento en la posición 1 de la lista
print(my_other_list)  # Imprimimos la lista con el nuevo elemento insertado

my_other_list.remove("Azul")  # Eliminamos el elemento "Azul" de la lista, ojo, si hay varios elementos "Azul", solo elimina el primero
print(my_other_list)  # Imprimimos la lista después de eliminar el elemento "Azul"

# del my_other_list[1]  # Eliminamos el elemento en la posición 1 de la lista se usa para eliminar un elemento sin devolverlo
# print (my_other_list.pop(1))  # Imprimimos el elemento eliminado (en este caso, "1.77") pop se usa para eliminar un elemento y devolverlo

my_new_list = my_list.copy()  # Creamos una copia de la lista my_list

my_list.clear()  # Limpiamos la lista my_list, dejándola vacía
print(my_list)  # Imprimimos la lista my_list (debería estar vacía)
print(my_new_list)  # Imprimimos la lista my_new_list (debería ser una copia de my_list)

my_new_list.reverse()  # Invertimos el orden de los elementos en my_new_list
print(my_new_list)  # Imprimimos la lista my_new_list (debería estar invertida)

my_new_list.sort()  # Ordenamos los elementos de my_new_list
print(my_new_list)  # Imprimimos la lista my_new_list (debería estar ordenada)