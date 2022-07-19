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


lista_de_lista = []

l = ['Luiza', 'Matheus', 'Laura']
l2 = ['Janayna','Gustavo','Mariana']
l3 = ['Diego', 'Marcus', 'Ives']

lista_de_lista.append(l)
lista_de_lista.append(l2)
lista_de_lista.append(l3)

print(lista_de_lista)


for indice, valor in enumerate(lista_de_lista):
    for indice2, valor2 in enumerate(valor):
        print(str(indice2) + " " + valor2)







