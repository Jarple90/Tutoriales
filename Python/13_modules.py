### Modules en Python ###

import module

module.sum(1, 2, 3) # hay que importar el modulo para poder usarlo en este caso module con la funcion sum
module.printvalue("Hola, Python") # se puede usar el nombre del modulo para llamar a la funcion printvalue

from module import sum, printvalue
sum(4, 5, 6) # se puede importar las funciones directamente y usarlas sin el nombre del modulo
printvalue("Hola, Python desde importación directa") # se puede usar la funcion directamente sin el nombre del modulo

import math # se puede importar el modulo math para usar sus funciones matemáticas

print(math.pi) # se puede usar la constante pi del modulo math
print(math.pow(2,3)) # se puede usar la funcion pow del modulo math para elevar un numero a una potencia

from math import pi as pi_value # se puede importar una constante del modulo math con un alias
print(pi_value) # se puede usar la constante pi con el alias pi_value

