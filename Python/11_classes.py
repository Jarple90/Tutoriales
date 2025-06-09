### Clases en python ###

class MyEmptyPerson:
    pass 

print(MyEmptyPerson)
print(MyEmptyPerson()) 

class Person:
    def __init__(self, name, surname):
        pass

my_person = Person("José Antonio", "Romero Pérez")
print(my_person)

class Person:
    def __init__(self, name, surname, alias="sin alias"):
# self.name = name
# self.surname = surname 
# self.__name = name propiedad privada
# self.__surname = surname propiedad privada
        self.full_name = f"{name} {surname},***{alias}***" 
    
    def walk(self):
        print(f"{self.full_name} Está caminando")


my_person = Person("José Antonio", "Romero Pérez")
#print(f"{my_person.name} {my_person.surname}")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("José Antonio", "Romero Pérez", "Snow Ice")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Snow Ice es mi nombre en los videojuegos"
print(my_other_person.full_name)

