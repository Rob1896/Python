'''Claro, *args y **kwargs son usados para manejar un número variable de argumentos en funciones de Python. 
*args se usa para pasar una lista de argumentos posicionales,
mientras que **kwargs se usa para pasar un diccionario de argumentos de palabra clave. Por ejemplo:'''


#ejemplo 2
def myfunc(*args):
    return sum(args)*.05

print(myfunc(40,60,20))


#ejemplo 3
def suma(*args):
    total = 0
    for num in args:
        total += num
    return total

resultado = suma(1, 2, 3, 4, 5)
print(resultado)  # Output: 15

#ejemplo 4 **kwargs

def detalles_persona(**kwargs):
    for key, value in kwargs.items():
        print(key + ":", value)

detalles_persona(nombre="Juan", edad=30, ciudad="Madrid")


#ejempl 4 **kwargs

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
    else:
        print("I don't like fruit")
        
myfunc(fruit='pineapple')

#ejemplo usando args y kwargs
def imprimir_detalles(*args, **kwargs):
    print("Argumentos posicionales:")
    for arg in args:
        print(arg)
    
    print("\nArgumentos de palabra clave:")
    for key, value in kwargs.items():
        print(key + ":", value)

imprimir_detalles("Hola", "Mundo", saludo="¡Hola!", despedida="Adiós")



#ejemplo 2  
def ejemplo(*args, **kwargs):
    for arg in args:
        print("Argumento posicional:", arg)
    
    for key, value in kwargs.items():
        print("Argumento de palabra clave:", key, "=", value)

# Usando *args y **kwargs
ejemplo(1, 2, 3, nombre="Juan", edad=30)