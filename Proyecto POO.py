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
    def __init__(self, id, marca, modelo, precio, capacidad_carga, consumo_agua, ciclos_lavado):
        super().__init__(id, marca, modelo, precio)
        self.capacidad_carga=capacidad_carga
        self.consumo_agua=consumo_agua
        self.ciclos_lavado=ciclos_lavado
    
    def __str__(self):
        return super().__str__() + f"\n •{self.capacidad_carga} \n •{self.consumo_agua} \n •{self.ciclos_lavado}"
    
    def tipo_gama(self):
        if self.capacidad_carga <= 10 and self.ciclos_lavado <= 3:
            return "Baja"
        elif self.capacidad_carga <= 15 and self.ciclos_lavado <= 5:
            return "Media"
        else:
            return "Alta"
    
if __name__ == "__main__":
# Prueba de lavadora gama alta 
    mi_lavadora = Lavadora("LAV-100", "Whirlpool", "RTX 5070", 18500, 20, 60, 12)
    print(mi_lavadora)

class Refrigerador(Gama, Electrodomésticos):
    pass

class Microondas(Gama, Electrodomésticos):
    pass

a = Electrodomésticos(1,2,3,4)
print(a)