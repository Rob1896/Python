
# este codigo imprime solo 2 opciones
# si el email esta correcto y si el email no esta correcto
email = input('Type your email address: ')
for i in email:
    if i == '@':
        print("you are ok")
        break
else:
    print("you are not ok")
    

# ejemplo usando for
# este ejemplo pide email al user  hasta que este correcto
# tienes 3 intentos sino aparece un error de locked 

for i in range(3): # el range es el rango de veces que el usuario tiene para meter el correo despues de ese rango sino se cumple salta el else 
    email = input('type your email address: ')
    if '@' not in email:
        print('error: Invalid email address,  try again')
    else:
        print('access verfied, your email is: ' + email)
        break
else:
    print('access locked stupid idiot') 

#ejemplo con while 
while True:
    email = input('type your email here: ')
    if '@' not in email:
        print('invalid email')
    else:
        print('valid email, your email is: ' + email)
        break


# mismo ejemplo pero con 2 condiciones
while True:
    email = input('type your email here: ')
    if '@' not in email or '.com' not in email:
        print('invalid email')
    else:
        print('valid email, your email is: ' + email)
        break