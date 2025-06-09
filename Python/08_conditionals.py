
### Conditionals en Python ###

my_condition = False # Cambia a True para probar la condición

if my_condition: # Si la condición es verdadera por defecto
    print("Se ejectuta la condición del if")

print("La ejecución continúa")

my_condition = 5 * 2 

if my_condition == 10: # Si la condición es verdadera por defecto
    print("Se ejectuta la condición del if con my_condition y es verdadera = 5 * 2")

if my_condition > 10: # Si la condición es verdadera por defecto
    print("Es mayor que 10")
else: # Si la condición es falsa por defecto
    print("Es menor o igual que 10")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("No es mayor que 10 o no es menor que 20")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 9:
    print("Es igual a 9")
else:
    print("No es mayor que 10 o no es menor que 20")

my_string = ""

if not my_string:  # Verifica si la cadena está vacía
    print("La cadena está vacía")

if my_string == "Mi cadena de textoooo": # Verifica si la cadena es igual a otra
    print("Estas cadenas de texto son iguales")


