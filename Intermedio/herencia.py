"""En Python, las herencias se refieren a la capacidad de una clase de heredar atributos y métodos de otra clase. 
Esto permite la reutilización de código y la creación de una jerarquía de clases 
donde las clases hijas pueden extender o modificar el comportamiento de las clases padre."""



class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enMarcha = True
        
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
    
        

class Furgoneta(Vehiculo):
    pass

furgoneta1 = Furgoneta('Volvo', 'LEVC')


furgoneta1.estado()


         

    