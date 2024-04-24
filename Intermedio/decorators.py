
"""estructrura de un decorador
constan de 3 funciones(A,B y C)
Donde A recibe como parametro a B para devolver C"""



# decorador(funcion A) parametros(funcion B)
def decorador(parametros):
    def funcion_interna(): # funcion_interna(funcion C)
    # lo que va a modificar la funcion:
        print('hola')
        parametros()
        print('adios')
    return funcion_interna


@decorador
def funcion_b(): # esta es recibida por A para devolver C

    print('medio')
    
funcion_b()

# defining a decorator
def hello_decorator(func):
 
    # inner1 is a Wrapper function in 
    # which the argument is called
     
    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")
 
        # calling the actual function now
        # inside the wrapper function.
        func()
 
        print("This is after function execution")
         
    return inner1
 
 
# defining a function, to be called inside wrapper
@hello_decorator
def function_to_be_used():
    print("This is inside the function !!")

function_to_be_used()


# crear un decorador que agregue un texto al inicio y al final de la funcion

def mi_decorador(funcion):
    # Define la función interna del decorador
    def wrapper():
        # Agrega funcionalidad adicional antes de llamar a la función original
        print("Antes de ejecutar la función")
        # Llama a la función original
        funcion()
        # Agrega funcionalidad adicional después de llamar a la función original
        print("Después de ejecutar la función")
    # Devuelve la función interna del decorador
    return wrapper


@mi_decorador # esto es como si fuera: mi_decorador(saludo) que saludo vendria siendo el parametro "funcion" que cree al definir la funcion arriba
def saludo():
    print("Hola mundo")
    
    
saludo() # al llamar la funcion lo que hago es ejecutar el "wrapper" del decorador que es imprimir el texto antes y despues de ejecutar saludo

# ejemplo 2:
#######################
def imprimir_argumentos(funcion):
    def wrapper(*args, **kwargs): #los * van solo al declarar la funcion
        print("Argumentos posicionales:", args) 
        print("Argumentos clave:", kwargs)
        return funcion(*args, **kwargs)
    return wrapper


#si quiero imprimir los args:

@imprimir_argumentos
def suma(a, b):
    return a + b

resultado = suma(31, 5) #se graba la variable con los parametros que le paso a la funcion suma( a y b) 
print("Resultado de la suma:", resultado)


# si quiero imprimir los kwargs
@imprimir_argumentos
def test_function(**kwargs):
    print('aqui deberian estar los argumentos: ',kwargs)
    

test_function(e="testingt",r = "function")

# decorator 3

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper() # "function" ya esta dentro de func, lo que le pase a function mas tarde va a aparecer en mayusculas.
        return make_uppercase

    return wrapper

# como si fuera 'uppercase_decorator(say_something) e imprime el texto en mayuscula.
#'uppercase_decorator(say_something)" es como si fuera 'uppercase_decorator(function) el parametro es 'say_something'
@uppercase_decorator # esto hace que lo que le pase a function lo haga mayuscula, en este caso el texto de la funcion "say_something"
def say_something():
    return 'hello Rob!'

print(say_something())


@uppercase_decorator
def text():
    return 'hello Rob, this is a text string'

print(text())



# ejemplo 2

def decorador(funtion):
    def wrapper():
        print('making wrapper')
        funtion()
        print('made wrapper')
        
    return wrapper

@decorador
def say_something():
    print('hello Rob!')
    
say_something()

@decorador
def text():
    print ('this is a text')

text()


           
#ejemplo 4
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print(f"My arguments are: {arg1}, {arg2}")
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print(f"Cities I love are {city_one} and {city_two}")

cities("Tokyo", "NewYork")    

    

