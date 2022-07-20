class Aluno:
    # Atributos
    _nome = ''
    idade = 0
    sexo = ''
    cpf = 0
    n1 = 0
    n2 = 0
    n3 = 0

    def __init__(self, nome, idade, sexo, cpf, n1, n2, n3):
        self._nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def getTodosDados(self):
        print(self._nome)
        print(self.idade)
        print(self.sexo)
        print(self.cpf)

    def getNomeIdade(self):
        print(self._nome + str(self.idade))
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
        return self.nome
