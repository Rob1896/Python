g = 25

if g > 10 and g < 20:
    print('g is between 10 and 20')
elif g > 20 and g < 30:
    print('g is old enough')


while True: #Creamos el ciclo infinito
    opcion = (input("""Elige una fruta para tu desayuno: 
    1- Manzanas
    2- Bananas
    3- Nada
    """))#Creamos un input para
        #que el usuario ingrese su opción y la almacenamos en "opcion"
        
############################################-2-##################################################       
    if opcion == '1': #Condicionales según la opción que eligió!
        print ("Has seleccionado manzanas")
    elif opcion == '2':
        print ("Has seleccionado bananas")
    elif opcion == '3':
        print ("Has seleccionado nada")
    else:
        print ("Debes seleccionar una opcion (1, 2 o 3)")
        
        
    numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5