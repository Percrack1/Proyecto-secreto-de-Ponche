from abc import ABC, abstractmethod

class Gama(ABC):

    @abstractmethod
    def tipo_gama(self):
        pass


class Electrodomésticos:

    def __init__(self, id, marca, modelo, precio):

        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):

        return (f"\n •ID: {self.id}" f"\n •Marca: {self.marca}" f"\n •Modelo: {self.modelo}" f"\n •Precio: {self.precio}")


class Lavadora(Electrodomésticos, Gama):

    def __init__(self, id, marca, modelo, precio, capacidad_carga, consumo_agua, ciclos_lavado):

        super().__init__(id, marca, modelo, precio)

        self.capacidad_carga = capacidad_carga
        self.consumo_agua = consumo_agua
        self.ciclos_lavado = ciclos_lavado

    def __str__(self):

        return (super().__str__() + f"\n •Capacidad de carga: {self.capacidad_carga}" + f"\n •Consumo agua: {self.consumo_agua}" + f"\n •Ciclos fr lavado: {self.ciclos_lavado}")

    def tipo_gama(self):

        if self.capacidad_carga <= 10 and self.ciclos_lavado <= 3:
            return "Baja"

        elif self.capacidad_carga <= 15 and self.ciclos_lavado <= 5:
            return "Media"

        else:
            return "Alta"


class Refrigerador(Electrodomésticos, Gama):

    def __init__(self, id, marca, modelo, precio, no_puertas, metros_cubicos, pies_capacidad):

        super().__init__(id, marca, modelo, precio)

        self.no_puertas = no_puertas
        self.metros_cubicos = metros_cubicos
        self.pies_capacidad = pies_capacidad

    def __str__(self):

        return (super().__str__() + f"\n •Numero puertas: {self.no_puertas}" + f"\n •Metros cubicos: {self.metros_cubicos}" + f"\n •Capacidad de almacenamiento: {self.pies_capacidad}")

    def tipo_gama(self):

        if self.no_puertas == 1 and self.metros_cubicos <= 10:
            return "Baja"

        elif self.no_puertas == 2 and self.metros_cubicos <= 13:
            return "Media"

        else:
            return "Alta"


class Microondas(Electrodomésticos, Gama):

    def __init__( self, id, marca, modelo, precio, potencia, consumo_energia, medidas):

        super().__init__(id, marca, modelo, precio)

        self.potencia = potencia
        self.consumo_energia = consumo_energia
        self.medidas = medidas

    def __str__(self):

        return (super().__str__() + f"\n •Potencia: {self.potencia}" + f"\n •Consumo energia: {self.consumo_energia}" + f"\n •Medidas: {self.medidas}")

    def tipo_gama(self):

        if self.potencia < 1000:
            return "Baja"

        elif self.potencia < 1500:
            return "Media"

        else:
            return "Alta"


def datos():

    while True:

        try:

            entrada = input("\n Ingresa id marca modelo y precio: ")

            if not entrada.strip():
                raise ValueError("No puedes dejar campos vacios")

            datos = entrada.split()

            if len(datos) != 4:
                raise ValueError(f"Se esperaban 4 datos pero ingresaste {len(datos)}. Intentalo de nuevo")

            id = int(datos[0])
            marca = datos[1]
            modelo = datos[2]
            precio = float(datos[3])

            return id, marca, modelo, precio

        except ValueError as e:
            print("Error:", e)


def mostrar(objeto):

    print("\n====================")
    print(objeto)
    print("Gama:", objeto.tipo_gama())
    print("====================")


electrodomesticos = []

while True:

    print("\n========= MENU =========")
    print("1. Instanciar")
    print("2. Desplegar")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ")


    if opcion == "1":

        print("\n 1. Lavadora")
        print("2. Refrigerador")
        print("3. Microondas")

        op = input("Seleccione tipo: ")


        if op == "1":

            try:

                id, marca, modelo, precio = datos()

                capacidad_carga = int(input("Capacidad de carga: "))

                consumo_agua = float(input("Consumo de agua: "))

                ciclos_lavado = int(input("Ciclos de lavado: "))

                lavadora = Lavadora( id, marca, modelo, precio, capacidad_carga, consumo_agua, ciclos_lavado)

                electrodomesticos.append(lavadora)

                print("Lavadora registrada")

            except ValueError:
                print("Error en los datos")


        elif op == "2":

            try:

                id, marca, modelo, precio = datos()

                no_puertas = int(input("Numero de puertas: "))

                metros_cubicos = float(input("Metros cubicos: "))

                pies_capacidad = int(input("Capacidad en pies cubicos: "))

                refri = Refrigerador(id, marca, modelo, precio, no_puertas, metros_cubicos, pies_capacidad)

                electrodomesticos.append(refri)

                print("Refrigerador registrado")

            except ValueError:
                print("Error en los datos")


        elif op == "3":

            try:

                id, marca, modelo, precio = datos()

                potencia = int(
                    input("Potencia: ")
                )

                consumo = float(
                    input("Consumo energia: ")
                )

                medidas = input("Medidas: ")

                micro = Microondas(id, marca, modelo, precio, potencia, consumo, medidas)

                electrodomesticos.append(micro)

                print("Microondas registrado")

            except ValueError:
                print("Error en los datos")

        else:
            print("Tipo invalido")


    elif opcion == "2":

        if not electrodomesticos:
            print("No hay objetos registrados")

        else:

            for obj in electrodomesticos:
                mostrar(obj)


    elif opcion == "3":

        print("Programa finalizado")
        break

    else:
        print("Opcion invalida")