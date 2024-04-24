# los nombres de las clases van con la primera letra en mayus y sin espacios


class Carro:
    def __init__(self, marca, modelo,year, color):
        #atributos
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.color = color
    #crear los metodos:
    def aceleracion(self):
        print(self.modelo + " acelera de 0 a 100km en 6 segundos")
#instanciar la clase
car1 = Carro('Ford', 'mustang', 2020, 'Azul marino')
car2 = Carro('Chevrolet', 'camaro',2020,'Amarillo')



print(car1.marca, car1.modelo, car1.year,  car1.color + " son las caracteristicas seleccionadas")
print(car2.marca, car2.modelo, car2.year, car2.color  + " son las caracteristicas seleccionadas")


car1.aceleracion()
car2.aceleracion()


# Mismo codigo pero sin los prints de las lienas 18 y 19

class Carro:
    def __init__(self, marca, modelo,year, color):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.color = color
        
       
    def aceleracion(self):
        print(self.modelo + " acelera de 0 a 100km en 6 segundos")
    def caracteristica(self):
       print(self.marca + " " + self.modelo + " son las caracteristicas del auto elejido")

car1 = Carro('Ford', 'mustang', 2020, 'Azul marino')
car2 = Carro('Chevrolet', 'camaro',2020,'Amarillo')




car1.caracteristica()
car1.aceleracion()
car2.caracteristica()
car2.aceleracion()

"""una clase puede tener atributos de clase y atributos de instancia
ejemplos:"""

class Pikachu:
    
    # atributo de clase
    tipo = ' electrico'
    
    #atributo de instancia 
    def __init__(self, name, level, health, colour, force):
        self.name = name
        self.level = level
    
        self.health = health
        self.colour = colour
        self.force = force
        
    def attack(self):
        print(f'my {self.name} attach with  {self.level} and genertes a lot damage')
        
        
pikachu1 = Pikachu('maggie', 450, 100, 'black', 700)

pikachu1.attack()

print(f'my pikachu type{pikachu1.tipo} called {pikachu1.name} with {pikachu1.level} and {pikachu1.force} is a winner')

# se pueden modificar los atributos
pikachu1.level = 500

print(f'my pikachu type{pikachu1.tipo} called {pikachu1.name} with {pikachu1.level} and {pikachu1.force} is a winner')

    





# clase 2

class Perro:
    def __init__(self, nombre, edad, raza, peso):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
    
    #metodos:
    def ladrar(self):
        print(self.nombre + " esta ladrando")
    def comer(self):
        print(self.nombre + " esta comiendo ")
        
mi_perro = Perro('Magie', 5, 'Daschund', 3)
mi_perro2 = Perro('Peggy', 3, 'Daschund',5)

print("es de raza: ", mi_perro.raza)
print('es de raza: ',mi_perro2.raza)

print('el perro se llaman: ', mi_perro.nombre)
print('el perro se llaman: ', mi_perro2.nombre)

mi_perro.comer()
mi_perro2.comer()

mi_perro.ladrar()
mi_perro2.ladrar()


# clase 3

class Person:
    def __init__(self, name, surname, alias="Sin alias"):  # puedo agregar los valores desde aca
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Rob", "Mercado")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()


new_person = Person('Maggie','Mayers','gordita')
print(new_person.full_name)
print(new_person.get_name())
new_person.walk()


# clase 4
# creando clase con personaje de juego


class Personaje:
    #atributos
    def __init__(self, name, power, level, defense, life_level):  
        self.name = name
        self.power = power
        self.level = level
        self.defense = defense
        self.life_level = life_level
    # metodos:
    def atributos(self):
        print('Name: ', self.name)
        print('Power: ', self.power)
        print('Level: ', self.level)
        print('Defense: ', self.defense)
        print('Life level: ', self.life_level)
        
    def level_up(self,  fuerza, level):
        self.level = self.level + fuerza
        self.defense = self.defense + level
    
    def available(self):
        if self.level > 8 and self.defense > 50:
            return True

        else:
            return False
    
    def welcome_message(self):
        if self.available():
            print(f"Welcome {self.name} to the game!")
            return
        else:
            print(f"You are not ready {self.name}. Come back when you are stronger!")
        
    
        
        
        

# le paso los atributos grabando en una variable
#instanciar clase
My_skin = Personaje('Carter', 'Run fast', 3, 23, 'high')
Enemy =  Personaje('Kitty CaT', 'attack your face',2, 66, 'high')


# forma de acceder a los atributos:
print('your skin is ' + My_skin.name)
print(My_skin.name, 'has a level: ' + str(My_skin.level))
My_skin.atributos()
My_skin.level_up(3,7)
My_skin.atributos()
print(My_skin.available())
My_skin.welcome_message()


Enemy.atributos()
print(Enemy.available())




class Libro:
    
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author
        self.info = f'Book title: {title}, published date: {year} and author: {author}'
        
    def infomation(self):
        print('The book information is: ', self.info)
        
        
        
    
        
book3 = Libro('The shinning', 1977,'Stephen King')

book3.infomation()
print(book3.title)
print(book3.author)
print(book3.info)



class Carro:
    def __init__(self, marca, modelo,year, color):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.color = color
        
       
    def aceleracion(self):
        print(self.modelo + " acelera de 0 a 100km en 6 segundos")
    def caracteristica(self):
       print(self.marca + " " + self.modelo + " son las caracteristicas del auto elejido")

car1 = Carro('Ford', 'mustang', 2020, 'Azul marino')
car2 = Carro('Chevrolet', 'camaro',2020,'Amarillo')


car1.aceleracion()



class books:
    
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author
        
        
    def info(self):
        print(self.title + " " + str(self.year) + " " + self.author)
        

book1 = books('Tokio Blues', 2013,'Murakami')


book1.info()

