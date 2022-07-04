def complete_series(lista):
    lista.sort()
    lista_saida = []

    for i in range(len(lista)):
        if lista[i] == lista[i+1]:
            lista_saida.append(0)
            return lista_saida

        elif lista[i] + 1 == lista[i+1]:
            lista_saida.append(lista[i])

        else:
            lista_saida.append(lista[i])
            distancia = (lista[i+1] - lista[i]) - 1
            for j in range(distancia):
                lista_saida.append(lista[i] + (j+1))

    lista_saida.insert(0, 0)
    return lista_saida


lista = [0, 1, 3]

print(complete_series(lista))