### Exception Handling en Python ###

#   print(10 + "10") # TypeError: es un error de tipo, no se puede sumar un entero con una cadena

#numberOne = 5
#numberTwo = 10
#numberTwo = "10"  # Cambiamos el tipo de numberTwo a cadena


#if type (numberOne) == int:
#   print(numberOne + numberTwo)
#else:
#   print("numberOne no es un entero") # TypeError: numberOne es un entero, pero numberTwo es una cadena


#try:
#   print(numberOne + numberTwo)  # Intentamos sumar un entero con una cadena
#   print("No se ha producido ningún error")  # Esta línea no se ejecutará si hay un error
#except:
#   print("La ejecución ha sido exitosa, no se ha producido ningún error")  # Esta línea se ejecutará si hay un error

# Try except else
#try:
#    print(numberOne + numberTwo)  # Intentamos sumar un entero con una cadena
#    print("No se ha producido ningún error")  # Esta línea no se ejecutará si hay un error
#except:
    # es opcional, pero se recomienda especificar el tipo de error
#    print("Se ha producido un error")
#else:
#    print("La ejecución ha sido exitosa, no se ha producido ningún error")
#finally:
    # Esta línea se ejecutará siempre, haya o no habido un error
#    print("Esto se ejecuta siempre, haya o no habido un error")

# Excepciónes por tipo
#try:
#    print(numberOne + numberTwo)  # Intentamos sumar un entero con una cadena
#    print("No se ha producido ningún error")  # Esta línea no se ejecutará si hay un error
#except ValueError:
#    print("La ejecución ha sido exitosa, no se ha producido ningún error")  # Esta línea se ejecutará si hay un error
#except TypeError as error:
#    print("Se ha producido un error de tipo ValueError")

# Captura de la información de la excepción

#try:
#    print(numberOne + numberTwo)  # Intentamos sumar un entero con una cadena
#    print("No se ha producido ningún error")  # Esta línea no se ejecutará si hay un error
#except ValueError as error:
#    print(error)
#except Exception as my_random_error_name:
#    print(my_random_error_name)

