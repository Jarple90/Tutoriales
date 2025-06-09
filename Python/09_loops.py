### Loops en python, bucles, ciclos, iteracciones... ###

# While

my_condition = 0

while my_condition < 9:  # Mientras la condición sea verdadera
    print(my_condition) # Se puede ver el incremento, imprimir el texto de salida repitiendo...
    my_condition += 1  # Incrementa la condición
else: # Es opcional y se ejecuta al finalizar el bucle
    print("El bucle ha terminado") # Se ejecuta al finalizar el bucle

print("Fin del bucle while") # Se ejecuta al finalizar el bucle

while my_condition < 19:
    my_condition += 3 # Incrementa la condición en 3
    if my_condition == 15:
        print("Mi condición es igual a 15")
        break  # Sale del bucle si la condición es igual a 15, si quieres que continue, usa continue
    print("Mi condición es menor que 19")

# For

my_list = [35, 35, 33, 34, 35, 32, 33]  # Lista de números

for element in my_list: # Recorre cada elemento de la lista
    print(element)  # Imprime el elemento actual

my_tuple = (35, 1.76, "José Antonio", "Romero Pérez", "Snow Ice") # Tupla de datos

for element in my_tuple:  # Recorre cada elemento de la tupla
    print(element)  # Imprime el elemento actual

my_set = {"José Antonio","Romero Pérez", 35}

for element in my_set:  # Recorre cada elemento del conjunto
    print(element)  # Imprime el elemento actual

my_dict = {"Nombre": "José Antonio", "Apellido": "Romero Pérez", "Edad": 35, "Altura": 1.76}  # Diccionario de datos

for element in my_dict:  # Recorre cada clave del diccionario
    print(element)  # Imprime la clave actual
    if element == "Edad":  # Si la clave es "Edad"
        continue
    print("Se ejecuta")
else:
    print("El bucle ha terminado")