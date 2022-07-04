from aluno import Aluno

class Escola():
    nomeEscola = ''
    qtdTurmas = 0
    alunos = []

    def inicializador(self, alunos, nomeEscola, qtdTurmas):
        self.alunos = alunos
        self.nomeEscola = nomeEscola
        self.qtdTurmas = qtdTurmas

    def printEscola(self):
        print(self.nomeEscola)
        print(self.qtdTurmas)

    def printAlunosEscola(self):
        for i, j in enumerate(self.alunos):
            print(j.getNome() + " " + str(j.cpf) + " " + str(j.idade))



listaAlunos = []
objAluno = Aluno()
objAluno.inicializador("Aluno1", 18, "F", 00000, 7, 8, 9)
listaAlunos.append(objAluno)

objAluno = Aluno()
objAluno.inicializador("Aluno2", 23, "M", 00000, 10, 8, 9)
# objAluno.printTudo()
listaAlunos.append(objAluno)

objEscola = Escola()
objEscola.inicializador(listaAlunos, "ResiliaT12", 1)

objEscola.printAlunosEscola()