
        
        
 # generadores yield
        
def generate_gretings():
    yield 'hello'
    yield 'world'
    yield 'hola'
    
    
greetings = generate_gretings()

for greeting in greetings:
    print(greeting)
    


def generate_naturales(n):
    i = 0
    while i < n:
        yield i
        i += 1

for numero in generate_naturales(5):
    print(numero)
    
# diferencias entre bucle for y yield 

numbers = [i for i in range(6)]

for number in numbers:
    print(number)
else:
    print('The loop stops at', number)
    
# ejemplo con yield

def generate_numbers():
    for i in range(6):
        yield i

for tst in generate_numbers():
    print(tst)
    
    


x = 'hello'
x[0]