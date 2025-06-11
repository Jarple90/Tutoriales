### Higher Order Functions en Python ###

def sum_one(value):
    return value + 1  # Esta función toma un argumento y devuelve su valor más uno.

def sum_five(value):
    return value + 5  # Esta función toma un argumento y devuelve su valor más cinco.

def sum_two_values_and_one_and_value(first_value, second_value, f_sum): # Esta función toma dos valores y una función como argumentos.
    return f_sum(first_value + second_value) # f_sum es una función que se aplica al resultado de la suma de los dos valores.

print(sum_two_values_and_one_and_value(1, 2, sum_one))  # Imprime 4 porque 1 + 2 + 1 = 4
print(sum_two_values_and_one_and_value(1, 2, sum_five))  # Imprime 8 porque 1 + 2 + 5 = 8

### Clousers ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value  # Esta función interna añade 10 al valor recibido y a un valor original.
    return add  # La función sum_ten devuelve la función add, que añade 10 a su argumento.

add_closure  = sum_ten(1)
print(add_closure(5))  # Imprime 16 porque 5 + 10 + 1 = 16
print((sum_ten(5))(5))  # Imprime 20 porque 5 + 10 + 5 = 20

### Built-in Higher Order Functions en python ###

numbers = [5, 20, 35, 4, 50]  # Lista de números del 1 al 5.

### Map ###

def multiply_two(number):
    return number * 2  # Esta función toma un número y lo multiplica por 2.

print(list(map(multiply_two, numbers)))  # Aplica la función multiply_two a cada elemento de la lista numbers.
print(list(map(lambda numbers: numbers * 2, numbers)))  # Utiliza una función lambda para multiplicar cada elemento de numbers por 2.

### Filter ###

# filter() permite filtrar elementos de una lista basándose en una condición.

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False  # Esta función devuelve True si el número es mayor que 10, de lo contrario devuelve False.

print(list(filter(filter_greater_than_ten, numbers)))  # Filtra los números de la lista numbers que son mayores que 10.
print(list(filter(lambda number: number > 10, numbers)))  # Utiliza una función lambda para filtrar los números mayores que 10.

### Reduce ###

# reduce() es una función que aplica una función de reducción a los elementos de una lista, acumulando el resultado.

from functools import reduce  # Importa la función reduce del módulo functools.

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value  # Esta función toma dos valores y devuelve su suma.

print(reduce(sum_two_values, numbers))











