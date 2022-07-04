def funcaoDict1():
    lista_dicionarios = []

    dicionario_banco1 = {
        "id": "999.999.999-99",
        "password": "@#$dassdsad#43a5$¨%&¨&57"
    }

    dicionario_banco2 = {
        "id": "888.888.888-88",
        "password": "@#$12323213ad#43a5$¨%&¨&57"
    }

    dicionario_banco3 = {
        "id": "777.777.777-777",
        "password": "@2354ad#43a5$¨%&¨&"
    }

    lista_dicionarios.append(dicionario_banco1)
    lista_dicionarios.append(dicionario_banco2)
    lista_dicionarios.append(dicionario_banco3)

    # print(lista_dicionarios)
    # print(lista_dicionarios[1].get("id"))

    print(lista_dicionarios[2])
    lista_dicionarios[2].update(password="1234")
    print(lista_dicionarios[2])

#######################################################################################################################




def exercicioDict(lista_dicionarios, dicionario_banco1, dicionario_banco2):
    lista_dicionarios.append(dicionario_banco1)
    lista_dicionarios.append(dicionario_banco2)

    for dicionario in lista_dicionarios:
        for chave, valor in dicionario.items():
            if chave == "conta":
                print(valor[1])

def exercicioDictRetorno(lista_dicionarios, dicionario_banco1, dicionario_banco2):
    lista_retorno = []
    lista_dicionarios.append(dicionario_banco1)
    lista_dicionarios.append(dicionario_banco2)

    for dicionario in lista_dicionarios:
        for chave, valor in dicionario.items():
            if chave == "conta":
                lista_retorno.append(valor[1])

    return lista_retorno


lista_dicionarios1 = []

dicionario_banco = {
    "id": "999.999.999-99",
    "password": "@#$dassdsad#43a5$¨%&¨&57",
    "conta": [33, 22]
}

dicionario_bancoI = {
    "id": "888.888.888-88",
    "password": "@#$12323213ad#43a5$¨%&¨&57",
    "conta": [1, 2]
}


# exercicioDict(lista_dicionarios1, dicionario_banco, dicionario_bancoI)
# lista = exercicioDictRetorno(lista_dicionarios1, dicionario_banco, dicionario_bancoI)
# print(lista)

#######################################################################################################################
# dicionario_banco1 = {
#     "id": "999.999.999-99",
#     "password": "@#$dassdsad#43a5$¨%&¨&57",
#     "conta": [33, 22],
#     "populacao":[
#         {"habitantes": 1200000,
#         "praia": "sim",
#         "regiao": "nordeste",
#         "gentilico": "ludovicense"},
#         {"habitantes": 2722000,
#         "praia": "nao",
#         "regiao": "sudeste",
#         "gentilico": "belorizontino"}
#     ]
# }
#
# for chave, valor in dicionario_banco1.items():
#     for indice in range(len(valor)):
#         if chave == "populacao":
#             print(valor[indice].get("habitantes"))
#             print(valor[indice].get("praia"))
#             print(valor[indice].get("regiao"))
#             print(valor[indice].get("gentilico"))




# print(dicionario_banco1.get("populacao")[0].get("regiao"))



# import metodos.funcoes as obj
#
# print(obj.soma(1, 10))

# from metodos.funcoes import subtracao, soma
#
# print(subtracao(2,1))
# print(soma(2,1))


class Pessoa:
    # Atributos
    nome = ''
    idade = 0
    sexo = ''
    cpf = 0
    peso = 0
    altura = 0.0

    def inicializador(self, nome, idade, sexo, cpf, peso, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.peso = peso
        self.altura = altura

    def getNome(self):
        print(self.nome)

    def getIdade(self):
        print(self.idade)

    def getPeso(self):
        print(self.peso)

    def altura1(self):
        print(self.altura)

    def getTodosDados(self):
        print(self.nome)
        print(self.idade)
        print(self.sexo)
        print(self.cpf)
        print(self.peso)
        print(self.altura)

    def getNomeIdade(self):
        print(self.nome + str(self.idade))

# var = True
#
# while var:
sexo = input("Digite o sexo da pessoa: ")
# if (sexo.upper() != 'F'):
#     var = False
#     print("Você está querendo criar um objeto de uma pessoa do sexo masculino e isso não é permitido")
# else:
nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idadee da pessoa: "))
cpf = int(input("Digite o cpf da pessoa: "))
peso = int(input("Digite o peso da pessoa: "))
altura = float(input("Digite a altura da pessoa: "))

pessoaResilia = Pessoa()
# pessoaResilia.inicializador("Taty", 30, "F", 00000000000, 50, 1.90)
pessoaResilia.inicializador(nome, idade, sexo, cpf, peso, altura)
pessoaResilia.getNomeIdade()
pessoaResilia.altura1()

pessoaResilia.getTodosDados()








