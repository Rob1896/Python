#Imprime «Hola Mundo» si a es mayor a b

a = 10
b = 5

if a > b:
    print("Hola Mundo")




#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.


age = int(input("What is your age:"))
if age >= 18:
        print('you are older')
else:
    print('you are not older')
    

# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

age = int(input("edad: "))
ingreso = int(input("escriba su ingreso mensual: "))
if age >= 16 and ingreso >= 1000:
    print('debe pagar impuesto')
else:
    print('no debe pagar impuesto')
    
    

name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)

# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad = int(input("Cual es tu edad: "))
if age <= 4:
    print("Su entrada es gratis")
elif age <= 18:
    print("Costo de la entrad 5")
else:
    print("Costo de la entrada 10")
    
# otra forma de hacerlo

edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "€.")



# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
#Renta	Tipo impositivo
#Menos de 10000€	5%
#Entre 10000€ y 20000€	15%
#Entre 20000€ y 35000€	20%
#Entre 35000€ y 60000€	30%
#Más de 60000€	45%


renta = int(input("Cual es su renta Anual: "))
if renta < 10000:
    impuesto = '5%'
elif renta > 10000  and renta < 20000:
    impuesto = '15%'
elif renta > 20000 and renta < 35000:
    impuesto = '20%'
elif renta > 35000 and renta < 65000:
    impuesto = '30%'
elif renta >  65000:
    impuesto = '45%'
print('Su impuesto es de:', impuesto, 'pelucholares')



# Imprime «Hola Mundo» si a es mayor a b.

a = 10
b = 5

if a > b:
    print("Hola Mundo")



    






