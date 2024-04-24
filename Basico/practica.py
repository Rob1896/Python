#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla.

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(subjects)

print(type(subjects))


#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla.

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for subject in subjects:
    print("Yo estudio " + subject)
    
supermarket = ['frijoles','aceite','arroz','leche','azucar']
for super in supermarket:
    print('la lista del super: ', super)
    
#Escribí un programa que solicite al usuario que ingrese su nombre. 
#A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, [usuario]”, donde “[usuario]” se reemplazará por el nombre que el usuario haya ingresado.
    

name = input("ingrese su nombre: ")
print('Welcome', name)

# Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable. 
# A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. 
# En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario. 
# Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el resultado de la operación.

num1 = int(input('ingrese un numero entero: '))
num2 = float(input('ingrese un numero con decimales: '))
sum = num1 + num2
print('el resultado de la suma es: ', sum)


# Escribí un programa que solicite al usuario dos números y los almacene en dos variables. 
# En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
#A continuación, el programa debe solicitar al usuario que ingrese un tercer número, 
# el cual se debe almacenar en una nueva variable. 
# Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.

a = int(input("ingrese un numero: "))
b = int(input("ingrese numero: "))
c = a + b
e = int(input("ingrese otro numero: "))
print(e * c)

#####
n1=int(input("Ingresá un número:"))
n2=int(input("Ingresá otro número:"))
suma=n1+n2
print("Suman:", suma)
n3=int(input("Ingresá un nuevo número:"))
print("Multiplicación de la suma por el último número:",suma*n3)

#Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta 
# y la cantidad de litros de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro

km = int(input("ingrese kilometros recorrido:"))
gas = int(input("ingrese litros consumidos:"))

print("el consumo de combustible por kilómetro es: ", km/gas)


#Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit 
# (debe permitir decimales) y le muestre el equivalente en grados Celsius. 
# La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_


Fahrenheit=float(input("Ingresá una temperatura expresada en Fahrenheit:"))
print((5/9) * (Fahrenheit-32))


#Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle el promedio de los tres.

n= int(input("Número 1: "))
n2= int(input("Número 2: "))
n3= int(input("Número 3: "))
promedio= n+n2+n3/3
print(' el promedio es: ', promedio)

n1=float(input("Primer número:"))
n2=float(input("Segundo número:"))
n3=float(input("Tercer número:"))
print("El promedio de los tres es", (n1+n2+n3)/3)

# Escribí un programa que solicite al usuario un número y le reste el 15%, 
# almacenando todo en una única variable. A continuación, mostrar el resultado final en pantalla.

precio = int(input('Ingrese el precio: '))
print('el descuento sera el de 15%, precio final: ', precio - (precio*15)/100)

# solucion mia

valor = 260
porcentaje = 15

descuento = (porcentaje/100)* valor
resultado = valor - descuento
print('El descuento sera de: ', resultado)


#Escribí un programa que solicite al usuario el ingreso de dos palabras, 
# las cuales se guardarán en dos variables distintas. 
# A continuación, almacená en una variable la concatenación de la primera palabra,
# más un espacio, más la segunda palabra. Mostrá este resultado en pantalla.


word1= input('Ingrese una palabra: ')
word2= input('Ingrese otra palabra')
frase = word1 + ' ' + word2
print(frase)

# Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año
# y almacene ese número en una variable. 
# A continuación mostrar en pantalla un valor de verdad (True o False) que indique si el usuario ha visto más de 3 shows.

shows=int(input("Shows vistos en el último año:"))
print(shows>3)



#Escribí un programa que le solicite al usuario su edad y la guarde en una variable. 
# Que luego solicite la cantidad de artículos comprados en una tienda y la guarde en otra variable. 
# Finalmente, mostrar en pantalla un valor de verdad (True o False) que indique si el usuario es mayor de 18 años de edad y además compró más de 1 artículo.

edad = int(input('Ingrese su edad: '))
articulo = int(input('Cuantos articulos compro: '))

print(edad>18 and articulo > 3)



#Escribí un programa que, dada una cadena de texto por el usuario, 
# imprima True si la cantidad de caracteres en la cadena es un número par, o False si no lo es.

cadena=input("Ingresá una frase:")
longitud=len(cadena)
print(longitud%2 == 0)

#Escribí un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables, 
# y que luego imprima True si la primera palabra es menor que la segunda o False si no lo es.

word1= input('Ingrese una palabra: ')
word2 = input('ingrese otra palabra: ')
print(word1<word2)


#  Escribí un programa que solicite al usuario el ingreso de dos números diferentes y muestre en pantalla al mayor de los dos.