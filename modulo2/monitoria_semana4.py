class Carro():
    _cor = ''
    capacidadeTanque = 0
    qtdeCombustivel = 0
    consumoMedio = 0

    def previsaoKm(self):
        return self.qtdeCombustivel * self.consumoMedio

    def atualizaTanque(self, qtdeKm):
         return self.qtdeCombustivel - (qtdeKm/self.consumoMedio)

    def getCor(self):
        return self._cor

    def getCapacidadeTanque(self):
        return self.capacidadeTanque

    def getConsumoMedio(self):
        return self.consumoMedio

    def getQtdeCombustivel(self):
        return self.qtdeCombustivel

    def setCor(self, novaCor):
        self._cor = novaCor

    def setCapacidadeTanque(self, novaCapacidadeTanque):
        self.capacidadeTanque = novaCapacidadeTanque

    def setConsumoMedio(self, novoConsumoMedio):
        self.consumoMedio = novoConsumoMedio

    def setQtdeCombustivel(self, novaQtdeCombustivel):
        self.qtdeCombustivel = novaQtdeCombustivel

    def __init__(self, modelo, cor):
        self.modelo = modelo
        self._cor = cor

objCarro = Carro("corsa", "preto")


# objCarro = Carro("Corsa", "prata")
# objCarro.setCor("Azul")
# objCarro.setCapacidadeTanque(45)
# objCarro.setConsumoMedio(12)
# objCarro.setQtdeCombustivel(45)
# print(objCarro.atualizaTanque(220))
#
# print(objCarro.getCor())
# print(objCarro.getConsumoMedio())
# print(objCarro.getCapacidadeTanque())
# print(objCarro.previsaoKm())