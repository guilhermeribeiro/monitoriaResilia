# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))
# n3 = float(input("Digite a terceira nota: "))
# n4 = float(input("Digite a quarta nota: "))
#
# media = n1 + n2 + n3 + n4 / 4
#
# print(media)

########################################################################################################################
# sexoFeminino = 0
# qtdePessoas = 0
# acumuladoSalario = 0
# menorIdade = 0
# maiorIdade = 0
#
# while True:
#     idade = int(input("Digite a idade: "))
#
#     if idade < 1:
#         print("Idade negativa. Programa encerrado.")
#         break
#
#     sexo = input("Digite o sexo: ")
#     salario = float(input("Digite o salário: "))
#
#     # Condição c) = quantidade de mulheres na região
#     if sexo.upper() == 'F':
#         sexoFeminino = sexoFeminino + 1
#
#     # Condição a) = média de salário do grupo
#     qtdePessoas = qtdePessoas + 1
#     acumuladoSalario = acumuladoSalario + salario
#
#     # Condição b) = maior e menor idade do grupo
#     if menorIdade == 0 and maiorIdade == 0:
#         maiorIdade = idade
#         menorIdade = idade
#
#     if idade > maiorIdade:
#         maiorIdade = idade
#
#     if idade < menorIdade:
#         menorIdade = idade
#
#     print(" ")
#
# if(qtdePessoas > 0):
#     print(acumuladoSalario/qtdePessoas)
#     print(maiorIdade)
#     print(menorIdade)
#     print(sexoFeminino)

########################################################################################################################

# from metodos.funcoes import soma, subtracao

# def soma (valor1, valor2, variavelBooleana):
#     if variavelBooleana == True:
#         return valor1 + valor2
#     else:
#         return "O valor booleano é falso"
#
#
# v1 = 10
# v2 = 20
# realizaSoma = False
#
# print(soma(v1, v2, realizaSoma))

########################################################################################################################

# def subtrair(valor1, valor2):
#     resultado = valor1 - valor2
#     return resultado
#
# v1 = 30
# v2 = 10
# resultadoSubtracao = subtrair(v1,v2)
# resultadoSubtracao = 10
# print(resultadoSubtracao)

########################################################################################################################

# lista = ['jose', 'joao', 'francisco', 'seu zé']

# for x, y in enumerate(lista):
#     print(x)
#     print(y)

# count = 0
# testeBooleano = True
#
#
# while testeBooleano:
#     count = count + 1
#     print(count)
#
#     if count == 100:
#         testeBooleano = False

########################################################################################################################

# final = 100
# contador = 1
#
# while contador <= final:
#     print(contador)
#     contador = contador + 1

########################################################################################################################

# count = 0
#
# while True:
#     count = count + 1
#     print(count)
#
#     if count == 1000:
#         break

# count = 0
# valorFinal = 100
#
# while count < valorFinal:
#     print(count)
#     # count = count + 1

########################################################################################################################

condicao = True

while condicao:
    sexo = input("Digite o sexo da pessoa [M/F]: ")
    if sexo.upper() == 'M':
        print('Você digitou o sexo masculino corretamente')
        condicao = False
    elif sexo.upper() == 'F':
        print('Você digitou o sexo feminino corretamente')
        condicao = False
    else:
        print("Opção inválida! Digite novamente o sexo")

########################################################################################################################

# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

# def quilosExcedentes(quilosPescados):
#     if quilosPescados > 50:
#         return (quilosPescados - 50)
#     else:
#         return 0
#
#
# quilosPescados = int(input("Digite a quantidade de quilos de peixes pescados por João: "))
#
# print(quilosExcedentes(quilosPescados))
# print(quilosExcedentes(quilosPescados)*4)

# excesso = quilosExcedentes(quilosPescados)
# multa = excesso * 4

# print(excesso)
# print(multa)














