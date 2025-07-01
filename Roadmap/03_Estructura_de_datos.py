"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""
### Listas en Python ###

my_list = ["José Antonio", "Snow Ice", "Snow", "Fire"]
print(my_list)

my_list.append("FireStorm") # Insercción
print(my_list)

my_list.remove("Snow") #eliminación
print(my_list)
print(my_list[1]) # Acceso
my_list[1] = "Romero" # Actualización
my_list.sort() # Ordenación
print(my_list)

# Tuplas

my_tuple = ("José Antonio", "Romero", "Snow Ice", 35)
print(my_tuple[1]) # Solo puedo hacer Acceso no se puede modificar una tupla
print(my_tuple[3]) # Si quieres ordenarlo tiene que ser todo texto my_tuple = tuple(sorted(my_tuple))
print(type(my_tuple))

# Sets 

my_set = {"José Antonio", "Romero", "Snow Ice", 35} # Optimización de datos y facil de encontrar los valores, pero su orden es "aleatorio", eso sí nos sirve para que no esten duplicados
print(my_set)
my_set.add("jarptgd@gmail.com")
print(my_set)
my_set.remove("jarptgd@gmail.com")
print(type(my_set))
print(my_set)
# my_set = set(sorted(my_set) No se puede ordenar

# Diccionario

my_dict: dict = {
    "name":"José Antonio", 
    "surname":"Romero", 
    "alias": "Snow Ice", 
    "age": "34"
    }
print(my_dict["name"]) #Acceso
print(type(my_dict))

my_dict["email"] = "jarptgd@gmail.com" # Insercción
print(my_dict)

my_dict["age"] = "35" # Actualización
print(my_dict)

del my_dict["surname"] # Eliminación
print(my_dict)

my_dict = dict(sorted(my_dict.items()))
print(my_dict)

### Extra ###

def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos.")

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(
                        f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")


my_agenda()