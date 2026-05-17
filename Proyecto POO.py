from abc import ABC, abstractmethod

class Gama(ABC):
    @abstractmethod
    def tipo_gama(self):
        pass

class Electrodomésticos():
    def __init__(self, id, marca, modelo, precio):
        self.id=id
        self.marca=marca
        self.modelo=modelo
        self.precio=precio

    def __str__(self):
        return f"\n •{self.id} \n •{self.marca} \n •{self.modelo} \n •{self.precio}"

class Lavadora(Gama, Electrodomésticos):
    pass

class Refrigerador(Gama, Electrodomésticos):
    pass

class Microondas(Gama, Electrodomésticos):
    pass

a = Electrodomésticos(1,2,3,4)
print(a)