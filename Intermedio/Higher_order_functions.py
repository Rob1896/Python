# es una funcion que acepta otra funcion como argumento
# va a aplicar la funcion que acepta como argumento  a elementos iterables como una lista
# ver explicacion en el onenote 


#Filter
# filtra elementos de una secuencia segun el filtro que haga:

list1 = [1,2,3,4,5,6,7,8,9,10]
evens = filter(lambda x: x % 2 == 0, list1)
print(list(evens))

# usando funcion:
def numeros(number):
    return number % 2 == 0

print(list(filter(numeros, list1)))

#usando lambda:
even_numbers = list(filter(lambda x: x % 2 == 0 ,list1))
print(even_numbers)


#ejemplo 2    


lista = list(range(14))
pares = filter(lambda x: x % 2 == 0, lista) #filtro: crear una lista de numeros pares en base a otra lista existente 
print(list(pares))

#ejemplo 3

words = ['ana','apolo','australia','papaya','carro','agua','gato']

def words_with_a(word):
    return word[0] == 'a'

print(list(filter(words_with_a, words)))

# usando lambda
list_with_a = list(filter(words_with_a, words))
print(list_with_a)


#map
# aplica una funcion a cada elemento iterable(lista por ejemplo)
# y devuelve otra lista con los resultados

#ejemplo

list_name = ['roberto','alyssa','peggy','maggie']
new_list = list(map(str.capitalize, list_name)) #primera letra mayusculas
list2 = list(map(str.upper, list_name)) #todas las letras en mayusculas

print(new_list)
print(list2)


#ejmplo 2
fruits = ['apple', 'orange', 'banana', 'grapes',]
print(list(map(str.capitalize, fruits)))
print(list(map(str.upper, fruits)))


#add a sufix _fruits to the list using a function


fruits = ['apple', 'orange', 'banana', 'grapes',]

#se crea la funcion
def add_sufix(fruit):
    sufix = '_fruits'
    return fruit + sufix # esto concatena con la variable

new_list = list(map(add_sufix,fruits)) # aqui aplico la funcion a cada fruta de la lista
print(new_list)

#mismo ejemplo pero sin la funcion
fruits = ['apple', 'orange', 'banana', 'grapes',]
print(list(map(lambda x: x + '_fruits',fruits)))
print(list(map(lambda x: 'fruits_' + x, fruits)))


# otra ejemplo de hacerlo sin funcion
# grabando el lambda en una variable:

resultado = list(map(lambda x: x + '_fruits',fruits))
print(resultado)

# tambien se puede crear la lista en el print usando la variable
animals = ['dog', 'cat', 'elefant','tiger']

uper = map(lambda x: x + '_fruits',animals)
print(list(uper))
 

#ejemplo 4
numbers = [1,2,3,4,5]
double = map(lambda x:  x * 2,numbers)
print(list(double)) # creo la lista con el resultado del map 

# ejemplo 5
my_nums = [1,2,3,4,5]
def square(num):
    return num**2
# aqui el map aplica la funcion a cada elemento de la lista de my numbs
d = list(map(square,my_nums)) # le digo que aplique la funcion square a cada numero de my_nums
print(d)

#ejemplo sin usar la funcion
r = map(lambda x: x**2,my_nums)
print(list(r))


numbers = [2, 5, 10, 21, 3, 30]
def multiply_two(number):
    return number * 2
print(list(map(multiply_two, numbers)))

#mismo ejemplo que el anterior solo que sin la funcion
# desventaja: no se puede reutilizar por eso se recomienda hacer la funcion
numbers = [2, 5, 10, 21, 3, 30]
print(list(map(lambda x: x * 2, numbers)))



