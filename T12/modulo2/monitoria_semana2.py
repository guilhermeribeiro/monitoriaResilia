# Elabore um algoritmo que cria duas tuplas de dez posições e faça a multiplicação do s elementos de mesmo indice,
# colocando o resultado e uma tercira tupla que dever sr mostrada como saída.

def multiplicaTuplas():
    nome_da_tupla1 = (1, 2, 3, 4, 5)
    nome_da_tupla2 = (5, 4, 3, 2, 1)
    nome_da_tupla3 = ()

    for i in range(len(nome_da_tupla1)):
        nome_da_tupla3 = nome_da_tupla3 + tuple([nome_da_tupla1[i] * nome_da_tupla2[i]])
        # Fluxo de execução
        # Quando i = 0
            # tupla1[0] * tupla2[0] => 1 * 5 => 5 => tupla3(5)
        # Quando i = 1
        # tupla1[1] * tupla2[1] => 2 * 4 => 8 => tupla3(5, 8)
        # Quando i = 2
        # tupla1[2] * tupla2[2] =>  3 * 3 => 9 => tupla3(5, 8, 9)
    print(nome_da_tupla3)


# multiplicaTuplas()



# frutas = {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25}
#
# print(frutas)
#
# frutas['laranja'] = 10
# frutas['laranja'] = 11
#
#
#
# print(frutas.items())
#
# for fruta, qtd in frutas.items():
#     print(fruta +": "+str(qtd))

def exercicioDict():
    lista_dicionarios = []

    cidade1 = {
            "cidade": "São Paulo",
            "estado": "SP",
            "populacao": 12000000,
            "praia": "nao",
            "regiao": "sudeste",
            "gentilico": "paulistano"
    }

    cidade2 = {
        "cidade": "São Luis",
        "estado": "MA",
        "populacao": 1200000,
        "praia": "sim",
        "regiao": "nordeste",
        "gentilico": "ludovicense"
    }

    cidade3 = {
        "cidade": "Belo Horizonte",
        "estado": "MG",
        "populacao": 2722000,
        "praia": "nao",
        "regiao": "sudeste",
        "gentilico": "belorizontino"
    }

    lista_dicionarios.append(cidade1)
    lista_dicionarios.append(cidade2)
    lista_dicionarios.append(cidade3)

    # print(lista_dicionarios[0])

    for cidade in lista_dicionarios:
        for chave, valor in cidade.items():
            print(chave + ": " + str(valor))
        print("")


# cidade2 = {
#     "cidade": "São Luis",
#     "estado": "MA",
#     "lista": [{
#         "populacao": 1200000,
#         "praia": "sim",
#         "regiao": "nordeste",
#         "gentilico": "ludovicense"}]
# }
#
# cidade3 = {
#     "cidade": "Belo Horizonte",
#     "estado": "MG",
#     "populacao": 2722000,
#     "praia": "nao",
#     "regiao": "sudeste",
#     "gentilico": "belorizontino"
# }



# teste = {( 'Rio Claro', 'SP'):
#      ['População: 210.00', 'Sem praia', 'Sudeste', 'Rio Clarense']}
#
# print(teste[( 'Rio Claro', 'SP')].__getitem__(1))

cidade2 = {
    "cidade": "São Luis",
    "estado": "MA",
    "populacao":[{
        "habitantes": 1200000,
        "praia": "sim",
        "regiao": "nordeste",
        "gentilico": "ludovicense"}],
    "lista": [1, 2, 3]
}

# print(cidade2.get('populacao').get('habitantes'))
# print(cidade2.get("lista")[2])
#
# cidade2.get("populacao")[0].update(praia='não')
# print(cidade2.get("populacao")[0].get("praia"))

cidade1 = {
    "cidade": ["São Luis", "Belo Horizonte"],
    "estado": ["MA", "MG"],
    "populacao":[
        {"habitantes": 1200000,
        "praia": "sim",
        "regiao": "nordeste",
        "gentilico": "ludovicense"},
        {"habitantes": 2722000,
        "praia": "nao",
        "regiao": "sudeste",
        "gentilico": "belorizontino"}
    ]
}

for chaves, valores in cidade1.items():
    for indice in range(len(valores)):
        if chaves == 'populacao':
            print(valores[indice].get("habitantes"))
            print(valores[indice].get("praia"))
            print(valores[indice].get("regiao"))
            print(valores[indice].get("gentilico"))
        else:
            print(chaves + " " + str(valores[indice]))

