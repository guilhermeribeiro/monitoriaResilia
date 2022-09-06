class Pai():
    nome = 'Nome Pai'
    idade = 99

    def __init__(self):
        print('Classe pai foi criada')



class Filha(Pai):
    escola = 'Resilia'
    teste = 'somente teste'

    def __init__(self):
        super().__init__()



f = Filha()

print(f.nome)