# 04/07 -----------------------------------------------------------------------
# import math

# var = 13.499999

# print(math.floor(var))
# print(math.ceil(var))
# print(round(var))


# Fila -> FIFO (First in First out) -> O primeiro elemento que entra na fila é o primeiro a sair
def apresentacaoFila():
    fila = ['Patrick', 'Matheus', 'Diego']
    print(fila.pop(0))
    print(fila)
    fila.append('Joãozinho')
    print(fila)

# apresentacaoFila()


# Pilha -> LIFO (Last in First out) -> O último elemento que entra na pilha é o primeiro a sair
def apresentacaoPilha():
    pilha = ['Container carne', 'Container Miojo', 'Container Frango']
    print(pilha.pop(0))
    print(pilha)
    pilha.insert(0, 'Container milho')
    print(pilha)

# apresentacaoPilha()

# 05/07 ----------------------------------------------------------------------------------------------------------------------

def funcaoToDo():
    qtd_candidatos = int(input('Digite a quantidade de candidados: '))
    count = 0
    lista_candidatos = []

    while count < qtd_candidatos:
        lista_notas = []
        e = int(input('Digite a nota da entrevista do candidato: '))
        t = int(input('Digite a nota do teste teórico do candidato: '))
        p = int(input('Digite a nota do teste prático do candidato: '))
        s = int(input('Digite a nota da avaliação de softskills do candidato: '))

        lista_notas.append(e)
        lista_notas.append(t)
        lista_notas.append(p)
        lista_notas.append(s)

        lista_candidatos.append(lista_notas)

        count += 1

    print(lista_candidatos)

'''
    Próximos passos do TO-DO

    1) Criar a função que irá filtrar a lista_candidatos de acordo com os parâmetros passados de notas (e,t,p,s);
    2) Percorrer a lista de candidatos e criar uma lógica para verificar se cada uma das notas dos candidatos da lista são maiores
    ou iguais as respectivas notas passadas como parâmetro pelo usuário;
    3) Se um determinado candidato estiver com TODAS as notas dentro da condição citada no item 2), este candidato com suas
    respectivas notas deverão ser adicionados a uma lista final.
    4) Imprimir lista final com a formatação exigida na questão.

'''

'''
    1) Explicação do exemplo 4,4,8,8
    NOTA E:
    1
    2
    3
    5

    NOTA T:
    1
    2
    3
    5

    NOTA P:
    1
    5
'''

lista = [[1, 2, 5, 9], [10, 7, 8, 5]]

lista_limiar = [1,4,5,2]


for i, j in enumerate(lista):
    for indice, valor in enumerate(j):
        if valor >= lista_limiar[indice]:
            print(valor)
            
    print("")    

# var = 'e5_t10_p8_s8'

# lista = var.split('_')

# print(lista)

# lista[0] = lista[0].replace("e", "")
# lista[1] = lista[1].replace("t", "")
# lista[2] = lista[2].replace("p", "")
# lista[3] = lista[3].replace("s", "")

# print(lista)

# lista = [int(x) for x in lista]

# print(lista)
