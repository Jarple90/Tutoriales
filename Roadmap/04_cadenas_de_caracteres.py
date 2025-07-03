
### EJERCICIO ###
""" 
* Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""

"""
Operaciones
"""

s1 = "Hola"
s2 = "Python"
# Concatenación
print(s1 + ", " + s2 + "!")

# Repetición
print(s1 * 5)

# Indexación 

print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud

print(len(s1))
print(len(s2))

# Slicing (porción)

print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Búsqueda 
print("l" in s1)
print("f" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# División 
print(s2.split("t"))