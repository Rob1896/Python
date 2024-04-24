# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
# e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.


name = input("Nombre del usuario: ")
numero = input("Numero del 1 al 10: ")
print((name + "\n") * int(numero))




name = input("Nombre: ")
print(name.lower())
print(name.upper())
print(name.title())



#Escribir un programa que pregunte el nombre del usuario en la consola 
# y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
name = input("Cual es tu nombre: ")
print(name.upper(), ' tiene' , len(name), 'letras')


numero = +3434445519
print(numero)

print(numero[0:3])


# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
# y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este formato en la consola 
# y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])




# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
frase = input("Introduce una frase: ")
print(frase[::-1])

#

frase= input('introduzca frase: ')
vocal = input('introduzca cualquier vocal: ')
print('su frase es: ', 'su vocal: ', vocal.upper())