# son funciones cortas y anonimas
# no se definen con Def sino con lambda y no llevan nombre por eso son anonimas

#ejemplo
# los : son los mimos : como si fuera a hacer una funcion if: en la parte de abajo, solo que aca esta en la misma linea
square = lambda num: num **2  
print(square(4))



#ejemplo 2
x = lambda a : a + 10
print(x(5))

#ejemplo 3
x = lambda a, b : a * b
print(x(5, 6))

#ejemplo 4 

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))