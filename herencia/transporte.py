
class Transporte:
    
    pasajeros:int

    def avanzar(self)-> str:
        return "el transporte esta en movimiento"

    def detener(self)->str:
        
        return "el transporte se detuvo"
    

class Automovil(Transporte):
        combustible: str

carro: Automovil = Automovil()
print(carro.avanzar())

class Avion(Transporte):
     def avanzar(self)->str:
          return "el avion avanzando!"
     
avion:Avion =Avion()
print(avion.avanzar())