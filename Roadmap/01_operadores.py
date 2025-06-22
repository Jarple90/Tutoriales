### Operadores en Python ###

# Operadores aritméticos
x = 7
y = 3

print(f"Suma: 7 + 3 = {7 + 3}")                 # Modo matemático: print(f"Suma: x + y = {x + y}")
print(f"Resta: 7 - 3 = {7 - 3}")                # Modo matemático: print(f"Resta: x - y = {x - y}")
print(f"Multiplicación: 7 * 3 = {7 * 3}")       # Modo matemático: print(f"Multiplicación: x * y = {x * y}")
print(f"División: 7 / 3 = {7 / 3}")             # Modo matemático: print(f"División: x / y = {x / y}")
print(f"Módulo: 7 % 3 = {7 % 3}")               # Modo matemático: print(f"Módulo: x % y = {x % y}")
print(f"Exponentes: 7 ** 3 = {7 ** 3}")         # Modo matemático: print(f"Exponentes: x ** y = {x ** y}")
print(f"División entera: 7 // 3 = {7 // 3}")    # Modo matemático: print(f"División entera: x // y = {x // y}")


# Operadores de comparación 

x = 7
y = 2

print(f"Igualdad: 7 == 2 → {7 == 2}")              # Modo matemático: print(f"Comparación: x == y → {x == y}")
print(f"Desigualdad: 7 != 2 → {7 != 2}")           # Modo matemático: print(f"Comparación: x != y → {x != y}")
print(f"Mayor que: 7 > 2  → {7 > 2}")              # Modo matemático: print(f"Comparación: x > y  → {x > y}")
print(f"Menor que: 7 < 2  → {7 < 2}")              # Modo matemático: print(f"Comparación: x < y  → {x < y}")
print(f"Mayor o igual que: 7 >= 2 → {7 >= 2}")     # Modo matemático: print(f"Comparación: x >= y → {x >= y}")
print(f"Menor o igual que: 7 <= 2 → {7 <= 2}")     # Modo matemático: print(f"Comparación: x <= y → {x <= y}")

# Operadores Lógicos

x = 7
y = 2
z = 10

print(f"AND: 7 > 2 and 7 < 10 → {7 > 2 and 7 < 10}")    # Modo matemático: print(f"AND: x > y and x < z → {x > y and x < z}")
print(f"OR ||: 7 < 2 or 7 < 10 → {7 < 2 or 7 < 10}")    # Modo matemático: print(f"OR: x < y or x < z → {x < y or x < z}")
print(f"NOT: not(7 > 2) → {not(7 > 2)}")                # Modo matemático: print(f"NOT: not(x > y) → {not(x > y)}")

# Operardores de asignación 

x = 7
y = 2

print(f"x = 7")                  # Modo matemático: asignación inicial → x = 7
print(f"x += 2 → {x + 2}")       # Modo matemático: x = x + y → print(f"x += y → {x + y}")
print(f"x -= 2 → {x - 2}")       # Modo matemático: x = x - y → print(f"x -= y → {x - y}")
print(f"x *= 2 → {x * 2}")       # Modo matemático: x = x * y → print(f"x *= y → {x * y}")
print(f"x /= 2 → {x / 2}")       # Modo matemático: x = x / y → print(f"x /= y → {x / y}")
print(f"x %= 2 → {x % 2}")       # Modo matemático: x = x % y → print(f"x %= y → {x % y}")
print(f"x **= 2 → {x ** 2}")     # Modo matemático: x = x ** y → print(f"x **= y → {x ** y}")
print(f"x //= 2 → {x // 2}")     # Modo matemático: x = x // y → print(f"x //= y → {x // y}")

# Operadores de identidad
x = 7
y = 2
z = x

print(f"x is z → {x is z}")       # Modo matemático: print(f"x is z → {x is z}")     → ¿x es el mismo objeto que z?
print(f"x is y → {x is y}")       # Modo matemático: print(f"x is y → {x is y}")     → ¿x es el mismo objeto que y?
print(f"x is not y → {x is not y}") # Modo matemático: print(f"x is not y → {x is not y}") → ¿x NO es el mismo objeto que y?

# Operadores de pertenecia

x = 7
y = 2
lista = [1, 3, 7, 10]

print(f"7 in [1, 3, 7, 10] → {7 in [1, 3, 7, 10]}")         # Modo matemático: print(f"x in lista → {x in lista}")
print(f"2 not in [1, 3, 7, 10] → {2 not in [1, 3, 7, 10]}") # Modo matemático: print(f"y not in lista → {y not in lista}")

# Funciona con cadenas de texto también

texto = "python"
print(f"'py' in 'python' → {'py' in texto}")      # Modo matemático: print(f"'py' in texto → {'py' in texto}")

# Operadores de bit 

x = 7  # binario: 0111
y = 2  # binario: 0010

print(f"x & y = {x & y}")      # Modo matemático: print(f"x & y = {x & y}")     → AND bit a bit: 0111 & 0010 = 0010 → 2
print(f"x | y = {x | y}")      # Modo matemático: print(f"x | y = {x | y}")     → OR bit a bit: 0111 | 0010 = 0111 → 7
print(f"x ^ y = {x ^ y}")      # Modo matemático: print(f"x ^ y = {x ^ y}")     → XOR bit a bit: 0111 ^ 0010 = 0101 → 5
print(f"~x = {~x}")            # Modo matemático: print(f"~x = {~x}")           → NOT bit a bit: ~0111 = ...1000 (complemento a dos) → -8
print(f"x << 1 = {x << 1}")    # Modo matemático: print(f"x << 1 = {x << 1}")   → Desplazamiento a la izquierda: 0111 → 1110 → 14
print(f"x >> 1 = {x >> 1}")    # Modo matemático: print(f"x >> 1 = {x >> 1}")   → Desplazamiento a la derecha: 0111 → 0011 → 3

"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

# Condicionales

x = 7
y = 2

if x > y:
    print("7 es mayor que 2")                  # Modo matemático: if x > y: print("x es mayor que y")

if x == 7 and y == 2:
    print("x es 7 y y es 2")                   # Modo matemático: if x == 7 and y == 2: print("...")

if x != y:
    print("7 y 2 son diferentes")              # Modo matemático: if x != y: print("x y y son diferentes")

if x < 10:
    print("7 es menor que 10")                 # Modo matemático: if x < 10: print("x es menor que 10")

if y in [1, 2, 3]:
    print("2 está en la lista")                # Modo matemático: if y in lista: print("y está en la lista")

if not (x < y):
    print("7 no es menor que 2")               # Modo matemático: if not(x < y): print("x no es menor que y")

if x > y:
    print("x es mayor que y")
else:
    print("x no es mayor que y")               # Modo matemático: estructura condicional if...else

# o más completo:
if x == y:
    print("x es igual a y")
elif x > y:
    print("x es mayor que y")
else:
    print("x es menor que y")

# Iterativas 

# Recorriendo una lista
lista = [1, 2, 3]
for elemento in lista:
    print(f"Elemento: {elemento}")  # Modo matemático: for elemento in lista: print(f"Elemento: {elemento}")

# Usando range()
for i in range(3):
    print(f"Iteración número: {i}")  # Modo matemático: for i in range(n): print(...)

# Usando contador 

contador = 0
while contador < 3:
    print(f"Contador: {contador}")  # Modo matemático: while contador < 3: print(...)
    contador += 1                   # Modo matemático: contador = contador + 1

# Ejemplo completo con números concretos 

for i in range(1, 4):
    print(f"7 * {i} = {7 * i}")      # Modo matemático: print(f"x * i = {x * i}")

"""
Extra
"""

for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 == 0:
        print(number)