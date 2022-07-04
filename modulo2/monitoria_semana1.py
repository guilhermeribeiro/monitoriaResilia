def estruturaFila():
    fila = [10, 22, 15, 11, 40, 80, 71, 51]
    print(fila.pop(0))
    print(fila.pop(0))
    fila.append(60)
    fila.append(90)
    fila.append(100)
    print(fila.pop(0))
    print(fila)

# estruturaFila()


def estruturaPilha():
    pilha = [10, 22, 15, 11, 40, 80, 71, 51]
    print(pilha.pop(0))
    pilha.insert(0, 50)
    pilha.insert(0,91)
    print(pilha)

# estruturaPilha()

#######################################################################################################################



# O menor tempo é o primeiro
# o segundo menor tempo é o segundo
# o maior tempo é o terceiro


# def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
#     if tempo_chegada1 < tempo_chegada2 and tempo_chegada1 < tempo_chegada3:
#         if tempo_chegada2 < tempo_chegada3:
#             return f"1 - {tempo_chegada1} minutos\n2 - {tempo_chegada2} minutos\n3 - {tempo_chegada3} minutos\n"
#         else:
#             return f"1 - {tempo_chegada1} minutos\n2 - {tempo_chegada3} minutos\n3 - {tempo_chegada2} minutos\n"
#     elif tempo_chegada2 < tempo_chegada1 and tempo_chegada2 < tempo_chegada3:
#         if tempo_chegada1 < tempo_chegada3:
#             return  f"1 - {tempo_chegada2} minutos\n2 - {tempo_chegada1} minutos\n3 - {tempo_chegada3} minutos\n"
#         else:
#             return f"1 - {tempo_chegada2} minutos\n2 - {tempo_chegada3} minutos\n3 - {tempo_chegada1} minutos\n"
#     elif tempo_chegada3 < tempo_chegada1 and tempo_chegada3 < tempo_chegada2:
#         if tempo_chegada1 < tempo_chegada2:
#             return f"1 - {tempo_chegada3} minutos\n2 - {tempo_chegada1} minutos\n3 - {tempo_chegada2} minutos\n"
#         else:
#             return f"1 - {tempo_chegada3} minutos\n2 - {tempo_chegada2} minutos\n3 - {tempo_chegada1} minutos\n"


def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
    if tempo_chegada1 < tempo_chegada2 and tempo_chegada1 < tempo_chegada3:
        if tempo_chegada2 < tempo_chegada3:
            return f"1 - {nome_corredor1} - {tempo_chegada1} minutos\n2 - {nome_corredor2} - {tempo_chegada2} minutos\n3 - {nome_corredor3} - {tempo_chegada3} minutos\n"
        else:
            return f"1 - {nome_corredor1} - {tempo_chegada1} minutos\n2 - {nome_corredor3} - {tempo_chegada3} minutos\n3 - {nome_corredor2} - {tempo_chegada2} minutos\n"
    elif tempo_chegada2 < tempo_chegada1 and tempo_chegada2 < tempo_chegada3:
        if tempo_chegada1 < tempo_chegada3:
            return f"1 - {nome_corredor2} - {tempo_chegada2} minutos\n2 - {nome_corredor1} - {tempo_chegada1} minutos\n3 - {nome_corredor3} - {tempo_chegada3} minutos\n"
        else:
            return f"1 - {nome_corredor2} - {tempo_chegada2} minutos\n2 - {nome_corredor3} - {tempo_chegada3} minutos\n3 - {nome_corredor1} - {tempo_chegada1} minutos\n"
    elif tempo_chegada3 < tempo_chegada1 and tempo_chegada3 < tempo_chegada2:
        if tempo_chegada1 < tempo_chegada2:
            return f"1 - {nome_corredor3} - {tempo_chegada3} minutos\n2 - {nome_corredor1} - {tempo_chegada1} minutos\n3 - {nome_corredor2} - {tempo_chegada2} minutos\n"
        else:
            return f"1 - {nome_corredor3} - {tempo_chegada3} minutos\n2 - {nome_corredor2} - {tempo_chegada2} minutos\n3 - {nome_corredor1} - {tempo_chegada1} minutos\n"


# t1 = int(input('Digite o tempo do primeiro competidor: '))
# t2 = int(input('Digite o tempo do segundo competidor: '))
# t3 = int(input('Digite o tempo do terceiro competidor: '))
# nome1 = input('Digite o nome do primeiro competidor: ')
# nome2 = input('Digite o nome do segundo competidor: ')
# nome3 = input('Digite o nome do terceiro competidor: ')
#
# print(podio_olimpico(t1, t2, t3, nome1, nome2, nome3))

'''
    Elaborar um algoritmo que cria duas listas de 10 posições e faça multiplicação
    dos elementos de mesmo índice, colocando o resultado em uma terceira lista que 
    deve ser mostrada como saída.
'''
def exercicioAula():
    lista1 = [2, 3, 4, 5, 6, 7 ,8, 9, 10, 11]
    lista2 = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    lista3 = [0]*10

    for i in range(10):
        # lista3.append(lista1[i] * lista2[i])
        lista3[i] = (lista1[i] * lista2[i])

    print(lista3)

'''
    Elabore um algoritmo que:
        - Leia uma lista de quinze números;
        - Remova os elementos ímpares;
        - Ordene e exiba em tela o menor e o maior valor
'''
def exercicioRemoveImpares():
    lista = []
    for i in range(3):
        lista.append(int(input('Digite um número: ')))

    indice = 0
    tamanhoLista = len(lista)

    while indice < tamanhoLista:
        if lista[indice] % 2 > 0: # [2]
            lista.remove(lista[indice])
            tamanhoLista = len(lista)
            if indice > 0:
                indice -= 1
        else:
            indice += 1

            # [2 3]
            # [2]

    if len(lista) > 0:
        lista.sort()
        print(lista[0])
        print(lista[-1])
    else:
        print('A lista está vazia pois todos os elementos eram ímpares e foram removidos.')

exercicioRemoveImpares()

















