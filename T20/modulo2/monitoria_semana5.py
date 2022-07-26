class Carro():
    __ano_fabricacao = 0
    __cor = ''
    __modelo = ''
    __cambio = ''
    __arcond = True
    __marca = ''
    __qtde_combustivel = 0
    __valor = 0

    def __init__(self, ano_fabricacao, cor, modelo, cambio, arcond, marca, qtde_combustivel, valor):
        self.__ano_fabricacao = ano_fabricacao
        self.__cor = cor
        self.__modelo = modelo
        self.__cambio = cambio
        self.__arcond = arcond
        self.__marca = marca
        self.__qtde_combustivel = qtde_combustivel
        self.__valor = valor
    
    def get_ano_fabricacao(self):
        return self.__ano_fabricacao
    
    def set_ano_fabricacao(self, ano_fabricacao):
        self.__ano_fabricacao = ano_fabricacao
    
    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor

    def valor_financiamento(self):
        return self.get_valor() * 0.15 + self.get_valor()


car = Carro('2022', 'prata', 'hb20', 'at', True, 'hyundai', 45, 70000)
car2 = Carro('2022', 'preto', 'hrv', 'at', True, 'honda', 60, 140000)

print(car.get_ano_fabricacao())

car.set_ano_fabricacao('2021')

print(car.get_ano_fabricacao())

print(car.valor_financiamento())

lista_carros = []

lista_carros.append(car)
lista_carros.append(car2)

print(lista_carros)