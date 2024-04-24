


import datetime

x = datetime.datetime.now()
print(x) #imprime la fecha y hora con segundos y microsegundos

#Return the year and name of weekday:
import datetime

x = datetime.datetime.now()

print(x.year) #imprime el ano
print('esto es un separador')
print(x.strftime("%A")) #imprime el dia


#To create a date, we can use the datetime()
# The datetime() class requires three parameters to create a date: year, month, day.

import datetime

x = datetime.datetime(2024, 4, 1)

print(x)

# The datetime object has a method for formatting date objects into readable strings.
#The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
# see the diferent formats in the dates page on my one note

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%c"))

e = datetime.datetime.now() # imprime la fecha de hoy con la hora 
print(e)
print(e.strftime("%c")) #imrpime el dia con la fecha y la hora
