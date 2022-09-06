'''
    # Entidade: Carro
    # Atributos:
        - cor;
        - placa;
        - modelo;
        - marca;
        - qtde_portas;
        - ano_fabricacao;
        - motorizacao;
        - cambio;
        - potencia;
'''
class Carro():
    __cor = ''
    __placa = ''
    __modelo = ''
    __marca = ''
    __qtde_portas = 0
    __ano_fabricacao = 0
    __motorizacao = 0.0
    __cambio = ''
    __potencia = 0
    __valor = 0

    def __init__(self, ano_fabricacao, modelo, marca, cor, placa, qtde_portas, motorizacao, cambio, potencia, valor):
        self.__ano_fabricacao = ano_fabricacao
        self.__modelo = modelo
        self.__marca = marca
        self.__cor = cor
        self.__placa = placa
        self.__qtde_portas = qtde_portas
        self.__motorizacao = motorizacao
        self.__cambio = cambio
        self.__potencia = potencia
        self.__valor = valor
    
    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_valor(self):
        return self.__valor

    #valor + 20% do valor dele
    # valor * 0.2 + valor    
    def valor_financiamento(self):
        return self.get_valor() * 0.2 + self.get_valor()


c = Carro(2022, 'creta', 'hyundai', 'preto', 'ABC-12D4', 5, 2.0, 'AT', 167, 160000)
#c2 = Carro(2022, 'h20', 'hyundai', 'branco', 'XYZ-12D4', 5, 1.0, 'AT', 110, 80000)

print(c.get_modelo())

c.set_modelo('ix35')

print(c.get_modelo())

print(c.valor_financiamento())

#print(c2.get_modelo())

    