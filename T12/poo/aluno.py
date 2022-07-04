class Aluno():
    # Atributos
    _nome = ''
    idade = 0
    sexo = ''
    cpf = 0
    n1 = 0
    n2 = 0
    n3 = 0

    def inicializador(self, nome, idade, sexo, cpf, n1, n2, n3):
        self._nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def printTudo(self):
        print(self._nome)
        print(self.idade)
        print(self.sexo)
        print(self.cpf)
        print(self.n1)
        print(self.n2)
        print(self.n3)

    def getNomeIdade(self):
        print(self._nome + ' ' + str(self.idade))

    def getNome(self):
        return self._nome

