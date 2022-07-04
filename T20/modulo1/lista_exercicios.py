'''
    Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721
'''
def reverso(numero):
    concat = ''
    for i in list(str(numero))[::-1]:
        if concat == '':
            concat = i
        else:
            concat+=i
    return int(concat)


def reverso2(numero):
    concat = ''
    for i in reversed(str(numero)):
        if concat == '':
            concat = i
        else:
            concat+=i
    return int(concat)

'''
    Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
        taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem 
        e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''
def somaImposto(custo, taxaImposto):
    return custo + custo * taxaImposto/100

print(somaImposto(100, 80))


'''
    Faça um programa que peça uma nota, entre zero e dez. 
    Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
def avaliaNota():
    nota = int(input('Digite uma nota: '))
    while nota >= 0 or nota <= 10
