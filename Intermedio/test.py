'''Herencia con clases o metodos"privados" y heredando la clase padre de otro file'''


from herencia2 import Avatar  # se importa la clase padre desde el otro file

class Pikachu(Avatar): #el nombre de la clase padre se coloca en la clase hija entre () para que herede la clase
    
    tipo = 'electric'
    
   
   
   # nombre, health, color, level
    def __init__(self, name, health, color, level, amperaje):
        super().__init__(nombre = name, health = health, color = color, level = level)
       
        self.__amperaje = amperaje
      
     
    @property
    def amperaje(self):
       print("Amperaje:" , self.__amperaje)
        
        
    @property
    def level(self):
        print("Level: " ,self._Avatar_level)
    
    @level.setter
    def level(self, level):
        if level >= 0 and  level <= 700:
            self._Avatar_level = level
        else:
           return "Level cannot be higer than 700", "\nlevel cannot be negative"
            
            
    @property
    def health(self):
        print('Health: ', self._Avatar_health)
    
    @health.setter
    def health(self, health):
        if health >= 0 and health <= 100:
            self._Avatar_health = health
        else:
            return "Health cannot be higer than 100", "\nHealth cannot be negative"
            

            
            
            

pikachu1 = Pikachu('pikachu', 90, 'Amarillo', 400, 250)

print(pikachu1.nombre)
print(pikachu1.color)
print(pikachu1.level)
print(pikachu1.health)
print(pikachu1.amperaje)

    
    
        
        
        
        
    







        
    