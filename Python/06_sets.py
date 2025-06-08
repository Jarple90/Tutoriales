### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"José Antonio", "Romero Pérez", 35} #Un set no es una estructura ordenada
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Snow Ice")
print(my_other_set)

print("Snow Ice" in my_other_set)  # Devuelve True si el elemento está en el set
print("Snow Ice" not in my_other_set)  # Devuelve False si el elemento está en el set
print("Snow Fire" in my_other_set) # Devuelve False si el elemento no está en el set

my_other_set.remove("Snow Ice")  # Elimina el elemento del set
print(my_other_set)

my_other_set.clear()  # Elimina todos los elementos del set
print(len(my_other_set))  # Devuelve 0 porque el set está vacío

del my_other_set  # Elimina el set
#print(my_other_set)  # Esto generará un error porque el set ya no existe

my_set = {"José Antonio", "Romero Pérez", 35, "Snow Ice"}
my_list = list(my_set)  # Convierte el set a una lista
print(my_list)  # Imprime la lista convertida desde el set      
print(my_list[0])  # Imprime el primer elemento de la lista

my_other_set = {"Snow Fire", "Snow Thunder", "Snow Water"}

my_new_set = my_set.union(my_other_set)  # Une dos sets
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set))  # Devuelve los elementos que están en my_new_set pero no en my_set




