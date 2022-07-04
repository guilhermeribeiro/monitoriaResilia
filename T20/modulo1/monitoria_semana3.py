'''
    Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
     se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
'''
from re import X


def func(arg):
    if arg > 0:
        return 'P'
    else:
        return 'N'

'''
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
'''
def func2():
    numero = 2345
    print(len(str(numero)))

def func3():
    numero = 2345
    count = 1
    for i in range(numero):
        if i == 10:
            count+=1
        elif i == 100:
            count+=1
        elif i == 1000:
            count+=1
    print(count)


'''
Faça um programa para imprimir para um n informado pelo usuário. 
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
'''

def func4(n):
    for i in range (n):
        for j in range(i+1):
            print(str(j+1)+ " ")

# func4(10)




# 14/06 ----------------------------------------------------------------------------------------------------------------
# 1,9 -> 8
# 4,17 -> 12
def teste(inicio, fim):
    l = list(range(inicio, fim+1))

    for i, j in enumerate(l):
        if j % 5 == 0:
            resultado = j / 5
            if resultado % 2 != 0:
                l.remove(j)
    
    return len(l)

# print(teste(4, 17))

def teste2(inicio, fim):
    count = 0
    for i in range(inicio, fim+1):
        valor = str(i)
        if valor.__contains__("5"):
            continue
        count+=1
    
    return count

# print(teste2(55, 61))

'''
    Faça um programa com uma função chamada somaImposto. A função irá ler dois parâmetros formais: 
        taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem 
        e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''
def somaImposto2(custo, imposto):   
    return custo + custo * imposto/100
    
def somaImposto():
    custo = int(input('Digite o custo do produto: '))
    imposto = int(input('Digite o imposto sobre o produto (%): '))

    print(custo + custo * imposto/100)
    
# somaImposto()


# 15/06 -------------------------------------------------------------------------------


def retornaComprimento(frase):
    l = frase.split(' ')
    tam = 0
    for i, j in enumerate(l):
        if i == 0:
            tam = len(j)
        elif len(j) < tam:
            tam = len(j)
    
    return tam


# p = 'caminho tiver sido incluído'

# print(retornaComprimento(p))


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 10

# print(fibonacci(n))

condicao = True

while condicao:
    condicao2 = True
    x = input('Variavel qualquer: ')
    y = input('Variavel dois qualquer: ')

    if y == 'a':
        while condicao2:
            print('to na condicao 2')
            z = input('Variavel 3 qualquer: ')

            if z == 's':
                condicao = False
                condicao2 = False
            elif z == 's2':
                condicao2 = False
            else:
                print('Ainda to aqui no segundo while')

    else:
        print('y não foi igual a letra "a"')





