### Lambdas en Python ###

# Una función lambda es una función anónima que se define con la palabra clave `lambda`.
# Se utiliza para crear funciones pequeñas y rápidas sin necesidad de definirlas con `def`.

sum_two_values = lambda first_value, second_value: first_value + second_value # Esta función toma dos argumentos y devuelve su suma.
print(sum_two_values(2, 3)) # Llamada a la función lambda, devuelve 5

multiply_values = lambda first_value, second_value: first_value * second_value - 2  # Esta función toma dos argumentos, multiplica y resta 2.
print(multiply_values(2, 3))  # Llamada a la función lambda, devuelve 4

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value 

print(sum_three_values(2)(3, 4))  # Llamada a la función lambda dentro de otra función, devuelve 9

def sum_value_and_lambda(value, sum_two_values):
    return lambda first_value, second_value: first_value + second_value + value 

print(sum_three_values(2)(3, 4))  # Llamada a la función lambda dentro de otra función, devuelve 9



