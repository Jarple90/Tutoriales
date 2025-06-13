
### Regular Expressions ###

import re

my_string = "Esta es la lección sobre expresiones regulares"
my_other_string = "Esta no es la lección de file handing"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
star, end = match.span()
print(my_string[star:end])


match = re.match("Esta es la lección", my_other_string)
# if not (match == None): #Formas de comprobarlo
# if match is not None: #Otra forma de comprobarlo
if match != None:
    print(match)
    stard, end = match.span()
    print(my_string[star:end])

# print(re.match("Esta es la lección", my_other_string))

# Search 

search = re.search("Esta es la lección", my_string, re.I)
print(search)
star, end = search.span()
print(my_string[star:end])

# findall

findall = re.findall("lección", my_string, re.I)
print(findall)

# split

print(re.split(":", my_string))

# sub

print(re.sub("expresiones", "x", my_string))

# patterns

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "jarptgd@gmail.com"
pattern = r"^[a-zA-z0-9_.+-]+@[a-zA-z0-9]+\.[a-zA-z0-9-.]+$"

print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "jarptgd@gmail.com"
print(re.findall(pattern, email))