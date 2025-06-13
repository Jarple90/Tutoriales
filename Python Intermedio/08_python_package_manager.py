### Python Package Manager ###

# PIP https://pypi.org

# pip --version
# pip install --upgrade pip
# pip install numpy
# pip install pandas
# pip install requests
# pip install beautifulsoup4

import numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

# pip unistall pandas para elminar el paquete

# pip install requests

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())


# Arithmetics Package

from mypackages import arithmetics

print(arithmetics.sum_two_values(1,4))