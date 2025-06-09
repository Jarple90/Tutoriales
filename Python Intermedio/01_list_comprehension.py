### List Comprehension para Python ###

my_original_list = [35,35, 15, 25, 45, 60, 75, 80, 90]
my_list = []

my_range = range(10)  # Creamos un rango de números del 0 al 6
print(list(my_range))  # Imprimimos el rango como una lista

my_list = [i for i in range(10)]
print(my_list)  # Imprimimos la lista creada con list comprehension

my_list = [i+ 1 for i in range(10)]
print(my_list)  # Imprimimos la lista creada con list comprehension

my_list = [i * 2 for i in range(10)]
print(my_list)  # Imprimimos la lista creada con list comprehension

my_list = [i * i for i in range(10)]
print(my_list)  # Imprimimos la lista creada con list comprehension

def sum_five(number):
    return number +5 # Función que suma 5 a un número

