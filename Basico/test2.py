



for i in range(1,11,15):
    print(i)
    
    
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
    
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def multiplicador(n):
    def funcion(x): return x * n
    return funcion

duplicar = multiplicador(2) # este 2 es el varlor de N a diferencia de la anterior SI lleva parametro por eso el 2
triplicar = multiplicador(3) # este 3 es el varlor de N

print(duplicar(10)) # este 10 es el valor de X
print(triplicar(10))
print(multiplicador(2)(4)) # aqui le doy los argumentos de una vez en este caso el valor de x y n
