class Pai():
    def teste_heranca(self):
        print('Eu sou pai da filha')


class Filha(Pai):
    def teste_heranca(self):
        print('Eu sou a filha e mãe da neta')


class Neta(Filha):
    def __init__(self):
        # super().teste_heranca()
        super().teste_heranca()


f = Neta()