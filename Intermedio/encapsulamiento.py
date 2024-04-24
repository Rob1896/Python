


class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
        
    
persona = Persona('Peggy', 'Miranda',5) #estos valores si pueden ser cambiados

print(persona.nombre) 
persona.apellido = 'Mercado' # aqui modifique el valor inicial que era Miranda a Mercado
print(persona.apellido)





#como evitar que suceda:
#los _ solo sirven como generalidad, no quiere decir que NO se puede modificar, si se puede  pero NO DEBERIA modificarse 

class Personas:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre # doble _
        self._apellido = apellido #un solo _ 
        self._edad = edad
        
        
    
persona = Personas('Maggie', 'Miranda',5)


print(persona._apellido) #con un solo _ si se puede acceder pero no se puede cambiar ya que es "privado"
#para acceder a ese atributo privado desde afuera se hace asi:
print(persona._Personas__nombre) 






# los dobles guion bajo se llaman name mangling
# no se puede acceder desde fuera de la funcion porque da error

class Personas:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        
        
    
persona = Personas('Maggie', 'Miranda',5) # estos son los valores que NO pueden ser cambiados 

print(persona.__nombre) ## esto va a dar error porque lleva doble __ por eso no se puede acceder 
print(persona._Personas__nombre) # para acceder correctamente se usa este metodo






# los atributos que tienen __ no se pueden acceder desde afuera de la clase como normalmente se hace
# tampoco se pueden modificar esos atributos como normalmente se hace
# la idea de usar los __ es que hace los atributos "privados" y no se acceden desde fuera de la clase y tampoco los pueden modificar 
class Personas:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
 # el  getter se usa para acceder desde afuera de la clase:      
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
        
    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_apellido(self,apellido):
        self.__apellido = apellido
    
    def set_edad(self,edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print('La edad no puede ser negativa')
    

    
persona = Personas('Maggie', 'Miranda',5)



"""si quisiera acceder a algo se hace asi: persona.apellido pero da error porque tiene __"""
#con el getter se accede asi:
print(persona.get_apellido())
print(persona.get_nombre())
print(persona.get_edad())

#si quiero modificar algo se hace asi:
'''persona.__apellido = 'Garcia'  pero esta da error porque el atributo es "privado"'''
#modifico los atributos 
persona.set_apellido('Garcia')
persona.set_nombre('Luna')
persona.set_edad(10)
#nuevos atributos:
print(persona.get_apellido())
print(persona.get_nombre())
print(persona.get_edad())


# segunda forma de hacerlo  y es la mas comun en python usando @property que viene siendo como un decorador

class Personas:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
    
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def edad(self):
        return self.__edad
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido
    
    @edad.setter
    def edad(self,edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print('La edad no puede ser negativa')
    
    

    
persona = Personas('Maggie', 'Miranda',5)




print(persona.nombre)
print(persona.apellido)
print(persona.edad)

persona.set_nombre('peggy')
persona.set_apellido('Mercado')
persona.set_edad(4)

print(persona.nombre)
print(persona.apellido)
print(persona.edad)


#mismo ejemplo pero agregando strings a los atributos

class Personas:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    def get_nombre(self):
        print(f'Nombre: {self.__nombre}.')
        return self.__nombre

    def get_apellido(self):
        print(f'Apellido: {self.__apellido}.')
        return self.__apellido

    def get_edad(self):
        print(f'Edad: {self.__edad}.')
        return self.__edad
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_apellido(self,apellido):
        self.__apellido = apellido
    
    def set_edad(self,edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print('La edad no puede ser negativa')

persona1 = Personas('Peggy', 'Miranda',5) 

persona1.get_apellido()
persona1.get_nombre()
persona1.get_edad()


persona1.set_apellido('Smith')
persona1.set_nombre('Petunia')
persona1.set_edad(2)

persona1.get_apellido()
persona1.get_nombre()
persona1.get_edad()


################3

class Pokemon:
   
    def __init__(self, name, level, health, color, fuerza):
        self.__name = name
        self.__level = level
        self.__health = health
        self.__color = color
        self.__fuerza = fuerza
        
    @property
    def name(self):
        return  f'Name: {self.__name}'
    
    @property
    def level(self):
        return f'Level: {self.__level}'
    
    @property
    def health(self):
        return f'Health:  {self.__health}'
    
    @property
    def color(self):
        return f'Color: {self.__color}'
    
    @property
    def fuerza(self):
        return f'Fuerza: {self.__fuerza}'
    
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @level.setter
    def level(self, level):
        self.__level = level
    
    @health.setter
    def health(self, health):
        self.__health = health
    
    @color.setter
    def color(self, color):
        self.__color = color
    
    @fuerza.setter
    def fuerza(self, fuerza):
        self.__fuerza = fuerza
        
    def rango(self):
        if self.__fuerza >= 500:
            return 'Rango 1'
        elif self.__fuerza >= 400:
            return 'Rango 2'
        elif self.__fuerza >= 300:
            return 'Rango 3'
        else:
            return 'Rango 0'
    
    
pokemon1= Pokemon('Pikachu', 300, 250, 'Amarillo', 525)
pokemon2= Pokemon('Charmander', 300, 250, 'Rojo', 325)

print(pokemon1.name)
print(pokemon1.level)
print(pokemon1.health)
print(pokemon1.color)
print(pokemon1.rango())

print('Pokemon numero 2')


print(pokemon2.name)
print(pokemon2.level)
print(pokemon2.health)
print(pokemon2.color)
print(pokemon2.rango())



        
    




    
        
        
    
 
 
 


