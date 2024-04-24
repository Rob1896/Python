#funciones de retorno de funciones 
#closure functions 

def add_ten():
    def function(n):
        return n + 10
    return function

result1 = add_ten() # va vacio porque no lleva parametros al definirla 
print(result1(3))


def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  
print(closure_result(10)) 


#ejemplo 2 con parametro en la funcion
def add_five(n):
    def add(num):return num + n
    return add

resultado = add_five(5)

print(resultado(10))
print(resultado(45))


# crea una funcion que duplique o triplique un valor dado

def multiplicador(n):
    def funcion(x): return x * n
    return funcion

# grabo la funcion "multiplicador" en una variable y le paso los parametros en este caso el valor de "n"
# recordar la idea de la funcion multiplicar x * n
duplicar = multiplicador(2) # este 2 es el varlor de N a diferencia de la anterior(linea 20) SI lleva parametro por eso el 2
triplicar = multiplicador(3) # este 3 es el varlor de N

print(duplicar(10)) # este 10 es el valor de X o sea lo que voy a duplicar
print(triplicar(10)) # este 10 es el valor de X o sea lo que voy a triplicar 
print(multiplicador(2)(4))


# crear funcion que sume 10 a un valor dado 
# mismo ejemplo pero sumando 
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


test = sum_ten(4)
print(test(5))
print(test(10)) # suma 10 + 10 + 4
#mismo resultado, la direfencia es que no toma en cuenta el "sum_ten(4)" 
print((sum_ten(4)(10))) # suma 4 + 10 + 10 o sea hace la operacion del "return" directo  

#ejemplo 4
def make_incrementer(n):
    def increment(x):
        return x + n
    return increment

increment_by_5 = make_incrementer(5)
print(increment_by_5(10))  # Devuelve 15
print(increment_by_5(7))   # Devuelve 12

# ejemplo
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

multiply_by_3 = make_multiplier(3)
print(multiply_by_3(5))   # Devuelve 15
print(multiply_by_3(8))   # Devuelve 24


#jemplo 
def make_power_function(exponent):
    def power(x):
        return x ** exponent
    return power

square = make_power_function(2)
print(square(4))   # Devuelve 16
print(square(9))   # Devuelve 81



def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3)) 





 