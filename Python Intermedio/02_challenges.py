### Challenges en Python en Retos de Programación de Mouredev ###

"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
"""

def fizzbuzz(): # Función que imprime los números del 1 al 100 con las condiciones especificadas
    for index in range(1,101): # Itera desde 1 hasta 100
        if index % 3 == 0 and index % 5 == 0: # Comprueba si es múltiplo de 3 y 5
            print("fizzbuzz") # Imprime "fizzbuzz" si es múltiplo de 3 y 5
        elif index % 3 == 0: # Comprueba si es múltiplo de 3
            print("fizz") # Imprime "fizz" si es múltiplo de 3
        elif index % 5 == 0: # Comprueba si es múltiplo de 5
            print("buzz") # Imprime "buzz" si es múltiplo de 5
        else: # Si no es múltiplo de 3 ni de 5
            print(index) # Imprime el número actual

fizzbuzz() # Llama a la función fizzbuzz para ejecutar el programa

"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower(): # Comprueba si las palabras son iguales
        return False # Si son iguales, no son anagramas
    return sorted(word_one.lower()) == sorted(word_two.lower()) # Compara las palabras ordenadas en minúsculas
    
print(is_anagram("amor", "roma")) # Imprime True, ya que "amor" y "roma" son anagramas

"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    prev = 0 # Inicializa el primer número de Fibonacci
    next = 1 # Inicializa el segundo número de Fibonacci
    for index in range(0,50): # Itera 50 veces para imprimir los primeros 50 números de Fibonacci
        print(prev)

        fib = prev + next # Calcula el siguiente número de Fibonacci
        prev = next # Actualiza el valor del número anterior
        next = fib # Actualiza el valor del siguiente número de Fibonacci

fibonacci()

"""
#4 ¿ES UN NÚMERO PRIMO?
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 *
""" 
def is_prime():

    for number in range(1, 101): # Itera desde 1 hasta 100

        if number >= 2: # Comprueba si el número es menor que 2 

            is_divisible = False # Inicializa la variable is_divisible como False
    
            for index in range(2, number): # Itera desde 2 hasta el número dado
                if number % index == 0: # Comprueba si el número es divisible por 2
                    is_divisible = True # Si es divisible, cambia is_divisible a True
                    break # Sale del bucle si encuentra un divisor
            
            if not is_divisible: # Si is_divisible es False, significa que el número es primo
                print(number) # Imprime el número primo encontrado
    
is_prime() # Llama a la función is_prime para ejecutar el programa

"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(text):
    text_len = len(text) # Obtiene la longitud del texto
    reversed_text = "" # Inicializa una cadena vacía para almacenar el texto invertido
    for index in range(0,text_len): # Itera desde 0 hasta la longitud del texto
        reversed_text += text[text_len - index - 1] # Añade el carácter en la posición inversa al resultado
    return reversed_text 
print(reverse("Hola mundo")) #  Imprime el resultado de la función reverse con el texto "Hola mundo"