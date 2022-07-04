def funcaoMedia():
    n1 = 5
    n2 = 6
    n3 = 10

    media = (n1 + n2 + n3)/3

    print(media)

def funcaoMediaLendoTeclado():
    n1 = int(  input("Digite a primeira nota: ")  )
    n2 = int(input("Digite a segunda nota: ")   )
    n3 = int(input("Digite a terceira nota: ")  )

    media = (n1 + n2 + n3)/3

    texto = "Terminei o calculo da media"
    print(texto)

    print(media)

funcaoMediaLendoTeclado()


##################################
def funcaoAprovadoReprovado():
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))
    n3 = int(input("Digite a terceira nota: "))

    media = (n1 + n2 + n3) / 3

    if media > 7 or media == 7:
        print("O valor da média é %.2f" % media)
        print("O aluno foi Aprovado")
    else:
        print("O valor da média é ", media)
        print("O aluno foi Reprovado")

##################################################

def inflacionou():
    alimento = input("Digite o nome do alimento: ")

    if alimento == 'tomate' or alimento == 'laranja' or alimento == 'limão':

        valorSemanaAnteriorAlimento = float(input("Digite o valor do alimento na semana passada: "))
        valorSemanaAtualAlimento = float(input("Digite o valor do alimento na semana atual: "))

        if valorSemanaAtualAlimento > valorSemanaAnteriorAlimento:
            print("O " + alimento + " aumentou " + str(valorSemanaAtualAlimento - valorSemanaAnteriorAlimento) + " reais" )
        elif valorSemanaAtualAlimento < valorSemanaAnteriorAlimento:
            print("O " + alimento + " diminuiu " + str(valorSemanaAnteriorAlimento - valorSemanaAtualAlimento) + " reais")
        elif valorSemanaAtualAlimento == valorSemanaAnteriorAlimento:
            print("Não houve alteração no preço do " + alimento)
    else:
        print(alimento + " indisponível na feira")

def And():
    alimento1 = input("Digite o nome do alimento: ")
    alimento2 = input("Digite o nome do outro alimento: ")

    if alimento1 == 'tomate' and alimento2 == 'laranja':
        print("São iguais")
    else:
        print("São diferentes")


# testeAnd()




# lista = ['tomate', 'limão', 'laranja']

# print(lista[0])
# print(lista[1])
# print(lista[2])


# for indice in lista:
#     print(indice)

# for i in range(3):
#     print(str(i) + " " + lista[i])

# print(lista)




############################################

def somaValores(valor1, valor2):
    return valor1 + valor2

def multiplicaValor(valor):
    return valor * 2


# v1 = int(input("Digite o primeiro valor "))
# v2 = int(input("Digite o segundo valor "))
#
# print(somaValores(v1, v2))
#
# result = somaValores(v1, v2)
#
# result = multiplicaValor(result)
#
# print(result)


###################################################

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15, 16, 17, 18,19,20]
# soma = 0
#
# for v in lista:
#     soma = soma + v
#     print(soma)

# print(soma)


def somaLista(listaValores):
    soma = 0
    for valor in listaValores:
        soma = soma + valor

    return soma


# lista = []
#
# for i in range(10):
#     lista.append(int(input("Digite o valor desejado: ")))
#     # print(lista)
#
# # print(somaLista(lista))
# resultado = somaLista(lista)
#
# resultado = resultado / 2
#
# print(resultado)

