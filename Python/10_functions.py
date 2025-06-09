### Functions en python###

def my_function():
    print("Esto es una función")

my_function() # Llamada a la función
my_function() # Llamada a la función
my_function() # Llamada a la función

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(5,7) # Llamada a la función
sum_two_values(10,20) # Llamada a la función

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values("Hola ", "Python") # Llamada a la función
sum_two_values(5.5, 7.5) # Llamada a la función

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

sum_two_values_with_return(10, 5)  # Llamada a la función

my_result = sum_two_values_with_return(10, 5)  # Llamada a la función
print(my_result)  # Imprime el resultado de la función

def print_name(name, surname):
    print(f"{name},{surname}")

print_name(surname ="Romero Pérez", name = "José Antonio")

def print_name_with_default(name, surnname, alias = "Sin alias"):
    print(f"{name}, {surnname}, {alias}")

print_name_with_default("José Antonio", "Romero Pérez", "Snow Ice")

def print_texts(*texts):
    for texts in texts:
        print(texts.upper())

print_texts("Hola", "Python", "Snow Ice")  #Llamada a la función con múltiples argumentos
print_texts("Hola")  # Esto funcionará correctamente




