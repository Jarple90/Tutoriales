### Dates ###

from datetime import datetime

now = datetime.now() # Determina la fecha y hora actual

print(now.day) # Imprime la hora actual    
print(now.month) # Imprime el mes actual
print(now.year) # Imprime el año actual
print(now.hour) # Imprime la hora actual
print(now.minute) # Imprime el minuto actual
print(now.second) # Imprime el segundo actual
print(now.strftime("%d/%m/%Y %H:%M:%S")) # Imprime la fecha y hora actual en formato personalizado
print(now.strftime("%A")) # Imprime el nombre del día de la semana
print(now.strftime("%B")) # Imprime el nombre del mes
print(now.strftime("%a")) # Imprime la abreviatura del nombre del día de la semana
print(now.strftime("%b")) # Imprime la abreviatura del nombre del mes

timestamp = now.timestamp() # Convierte la fecha y hora actual a un timestamp
print(timestamp) # Imprime el timestamp actual

year_2025 = datetime(2025, 1, 1) # Crea un objeto datetime para el 1 de enero de 2025
print(year_2025) # Imprime el objeto datetime para el 1 de enero de 2025

def print_date(date):
    print(date.day) # Imprime el día actual  
    print(date.month) # Imprime el mes actual
    print(date.year) # Imprime el año actual
    print(date.hour) # Imprime la hora actual
    print(date.minute) # Imprime el minuto actual
    print(date.second) # Imprime el segundo 
    print(date.timestamp()) # Imprime el timestamp de la fecha


print_date(now) # Llama a la función print_date con la fecha actual

year_2025 = datetime(2025, 1, 1) # Crea un objeto datetime para el 1 de enero de 2025
print_date(year_2025) # Llama a la función print_date con el 1 de enero de 

from datetime import time

current_time = time(15,48,17)# Crea un objeto time con la hora actual
print(current_time) # Imprimimos la hora actual
print(current_time.hour) # Imprimimos la hora actual
print(current_time.minute) # Imprimimos el minuto actual
print(current_time.second) # Imprimimos el segundo actual

from datetime import date

current_date = date.today() # Obtenemos la fecha actual

print(current_date.year) # Imprimimos la fecha actual
print(current_date.month) # Imprimimos el mes actual
print(current_date.day) # Imprimimos el día actual


current_date = date(current_date.year, current_date.month + 1, current_date.day) # Creamos un objeto date con la fecha actual más un mes
print(current_date.month) # Imprimimos la fecha actual más un mes

diff = year_2025 - now # Calculamos la diferencia entre el 1 de enero de 2025 y la fecha actual
print(diff) # Imprimimos la diferencia

diff = year_2025.date() - current_date # Calculamos la diferencia entre el 1 de enero de 2025 y la fecha actual
print(diff) # Imprimimos la diferencia

diff = year_2025.time()

from datetime import timedelta

start_timedelta = timedelta(200,100,100, weeks= 10) # Creamos un objeto timedelta con 200 días, 100 segundos, 100 microsegundos y 10 semanas
end_timedelta = timedelta(100,100,100, weeks= 5) # Creamos un objeto timedelta con 100 días, 100 segundos, 100 microsegundos y 5 semanas
print(end_timedelta - start_timedelta) # Imprimimos la diferencia entre los dos objetos timedelta
print(start_timedelta + end_timedelta) # Imprimimos la suma de los dos objetos timedelta



