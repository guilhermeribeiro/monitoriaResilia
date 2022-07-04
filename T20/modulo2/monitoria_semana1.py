# lista = [10, 2, 19, 30]
# lista2 = ['sdasdsa', 'sadasd', 's']
# lista3 = [3.2, 1.2, 5.9, 324243.32434, 1323.12]
# lista4 = [True, False, False, False, True, True]


# for posicao, valor in enumerate(lista2):
#     print(str(posicao) + " " + str(valor))



# lista = ['sdasAHUOISHAIDUASHDIUASHDASIUDHASIUDHASIUDHASIUDHASDUIAHSDIUHSAIUHSUIdsa', 'sadasd', 's']

# for posicao, valor in enumerate(lista):
#     print(str(posicao) + " " + str(valor))

# lista.remove(lista[-1])
# print(' ')

# for posicao, valor in enumerate(lista):
#     print(str(posicao) + " " + str(valor))



# lista = [10, 2, 19, 30]

# lista.append(25)

# print(lista)

# lista[1] = 30

# print(lista)

# lista.insert(2, 50)

# print(lista)


# Filas
    # - FIFO = First In First Out

# Pilhas
    # - LIFO = Last In First Out


# lista = [10, 2, 19, 30]
# lista2 = ['sdasdsa', 'sadasd', 's']
# lista3 = [3.2, 1.2, 5.9, 324243.32434, 1323.12]
# lista4 = [True, False, False, False, True, True]


# lista_f = [lista, lista2, lista3, lista4]

# print(lista_f[2][-1])


# 29-06 ----------------------------------------------------------------------------------------------------------
# 	1) Lista de 3 a 5 nomes	
# 	2) Lista com 3 nomes	
# 	3) Concatena a lista do item 2 na lista do item 1	
# 	4) Checa se o nome lido de um facilitador está contido na lista concatenada	
		
# 1	['x','y','z']	
# 2	['a', 'b']	
# 3	['x','y','z']['a', 'b']	
# 4	Não está	Digitei 'c'
# 	Está	Digitei 'a'


# lista1 = ['Jaque', 'Mariana', 'Patrick', 'Guilherme']
# lista2 = ['Marisa', 'Karoline', 'Matheus']

# listac = lista1 + lista2

# facilitador = 'Marisa'


# if facilitador in listac:
#     print('O(A) facilitador(a) '+ facilitador + ' está na lista!')
# else:
#     print('O(A) facilitador(a) NÃO está na lista!')


'''
    Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''

from audioop import reverse


def printLista():
    lista = []

    for i in range(5):
        lista.append(input('Digite o valor da posição ' + str(i) + ' : '))

    print(lista)


def printLista2(lista):
    print(lista)


# XASOAJDO = []

# for i in range(5):
#     XASOAJDO.append(input('Digite o valor da posição ' + str(i) + ' : '))

# printLista2(XASOAJDO)


'''
    Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

def media(lista):
    soma_notas = 0
    for i in range(len(lista)):
        soma_notas = soma_notas + lista[i]

    # Outra forma de fazer o for acima
    # for posicao, valor in enumerate(lista):
    #     soma_notas += valor
    print(lista)
    print(soma_notas/len(lista))


def mediaRetorno(lista):
    soma_notas = 0
    for i in range(len(lista)):
        soma_notas = soma_notas + lista[i]

    # Outra forma de fazer o for acima
    # for posicao, valor in enumerate(lista):
    #     soma_notas += valor
    
    return lista, soma_notas/len(lista)



# notas = []

# for i in range(4):
#     notas.append(int(input('Digite o valor da nota ' + str(i+1) + ' : ')))


# notaslidas, media =  mediaRetorno(notas)

# print(notaslidas)
# print(media)


'''
    Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

def printListaInversa(lista):
    lista.reverse()
    print(lista)


def ordernaImprime(lista):
    lista.sort(reverse=True)
    print(lista)


numeros = []

for i in range(5):
    numeros.append(float(input('Digite o numero ' + str(i+1) + ' : ')))


ordernaImprime(numeros)