# if condição:
#     o que deve ser feito dentro da condição

# result = 1

# if result > 1:
#     print(result)
# if result == 1:
#     print('O valor é igual a 1')
# if result > 0:
#     print('O valor é maior que 0')
# else:
#     print('O valor não é maior que 1')


# v = 1
# while v <= 10:
#     if v % 2 == 0:
#         print(v)
#     v = v + 1


# condicao = True
# v = 1

# while condicao:
#     print(v)
#     if v == 1000:
#         condicao = False
#     v = v + 1


# l = ['Luiza', 'Matheus', 'Laura','Gustavo','Mariana']

# print(l[2])


# para imprimir os valores
# for valor in l:
#     print(valor)

# para imprimir as posições
# for valor in range(len(l)):
#     print(valor)
#     print(l[valor])

# for indice, valor in enumerate(l):
#     print(str(indice))
#     print(str(valor))


# lista_de_lista = []

# l = ['Luiza', 'Matheus', 'Laura']
# l2 = ['Janayna','Gustavo','Mariana']
# l3 = ['Diego', 'Marcus', 'Ives']

# lista_de_lista.append(l)
# lista_de_lista.append(l2)
# lista_de_lista.append(l3)

# print(lista_de_lista)


# for indice, valor in enumerate(lista_de_lista):
#     for indice2, valor2 in enumerate(valor):
#         print(str(indice2) + " " + valor2)

# 19/07 -----------------------------------------------------------------------------------------------------

# Listas
lista = ['Soja', 'Eletro', 'Carro']

# Pilhas - Last in first out (LIFO)
# 'Arroz'
# lista.insert(0, 'Arroz')
# print(lista)

# lista.pop(0)
# lista.pop(0)

# print(lista)



# Filas - First in first out (FIFO)
lista2 = ['Diego', 'Mariana', 'Matheus', 'José']

# lista2.append('Laura')

# print(lista2)

# lista2.pop(0)

# print(lista2)

# Tuplas
# t = ('a', 'b', 'c')

# print('h' in t)


# Dicionários
# dicionario = {'nome': 'Guilherme',
#                 'idade':'32',
#                 'cpf':'12345678900'}

# # print(dicionario.values())

# print(dicionario['idade'])
# print(dicionario.get('idade'))


# dicionario['naturalidade'] = 'rio de janeiro'

# dicionario.update({'idade':'33'})
# print(dicionario)


# dicionario = {'cidade': 'São Luis',
#           'estado': 'MA',
#             'regiao': 'NE',
#             'outros': [1, 2, 3,1, 2, 3,1, 2, 3,1, 2, 3,1, 2, 3,1, 2, 3,1, 2, 3,1, 2, 3,1, 2, 3,1, 2, 3]}

# print(dicionario)

# for valor in dicionario.get('outros'):
#     print(valor)


# dicionario = {'cidade': 'São Luis',
#           'estado': 'MA',
#             'regiao': 'NE',
#             'vizinhos': [{'nome': 'x',
#                         'populacao': 50000,
#                         'limite': 'norte',
#                         'outros': [1, 45, 22, 33]},

#                         {'nome': 'y',
#                         'populacao': 100000,
#                         'limite': 'sul',
#                         'outros': [11, 25, 52, 73]}
#                         ]
#             }
# # Imprimir todos os valores da chave outros de todos os vizinhos
# for valor in dicionario.get('vizinhos'):
#     for valor2 in valor.get('outros'):
#         print(valor2)


# 20/07 --------------------------------------------------------------------------------------

# idade != 00
# outras perguntas

# idade = ''
# condicao = True

# while condicao:
#   idade = input('Digite a idade: ')
#   if idade == '00':
#     condicao = False

#   if condicao == True:
#     x = input('Primeira pergunta: ')
#     y = input('Segunda pergunta: ')
#   else:
#     print('Idade 00 digitada. Programa encerrado.')
#   print(' ')



import pandas as pd


dicionario = {
  'x': ['a', 'b'],
  'y': ['m', 'f'],
  'r1': [1, 2],
  'r2': [2, 2],
  'r3': [1, 1],
  'r4': [2, 2]
}

lista = [
  {'x': 'a', 'y': 'm', 'r1': 1,'r2': 2,'r3': 1,'r4': 1},
  {'x': 'b', 'y': 'f', 'r1': 2,'r2': 2,'r3': 1,'r4': 2}
]



df = pd.DataFrame(lista)

df.to_csv('teste.csv')

print(df.head())


# class Pai(object):
#   def __init__(self):
#     print('Classe pai foi montada')


# class Filha(Pai):
#   def __init__(self):
#     super().__init__()


# f = Filha()


