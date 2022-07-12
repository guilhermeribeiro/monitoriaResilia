# lista = [5, 6, 4]

# for i, j in enumerate(lista):
#     print(i)
#     print(j)


# Fila -> FIFO -> First in First out (Primeiro que chega, primeiro que sai)
# fila = ['Laura', 'Sthepanie', 'Matheus']
# fila.append('Marcus')
# print(fila)

# fila.pop(0)

# print(fila)

# Pilha -> LIFO -> Last in First out (último que chega, primeiro que sai)
# pilha = ['Não perecíveis','Peças','Carros']

# pilha.insert(0, 'Celulose')

# print(pilha)

# pilha.pop(0)

# print(pilha)


# Dicionário
# dicionario = {
#     "cidade" : "São Luis",
#     "estado" : "MA",
#     "lista": [{
#         "populacao": 1200000,
#         "praia": "sim",
#         "regiao": "nordeste",
#         "gentilico": "ludovicense"
#     }]
# }

# print(dicionario.get("lista")[0].get("gentilico")  )

# with open('D:\\Arquivo de Programas\\workspace\\monitoriaResilia\\T20\\modulo2\\curriculo_exemplo.txt') as f:
#     lines = f.readlines()
#     print(lines)

# lista = ['Teste', 'T20']
# with open('readme.txt', 'w') as f:
#     for line in lista:
#         f.write(line)
#         f.write('\n')


# 12/07 ---------------------------------------------------------

with open('D:\\Arquivo de Programas\\workspace\\monitoriaResilia\\T20\\modulo2\\curriculo_exemplo.txt', 'r') as f:
     lista_curriculo = f.readlines()

# print(lista_curriculo)

# lista_curriculo = str(lista_curriculo)

# print(lista_curriculo)

# var = 'python'

# print(var in lista_curriculo)

concatena_string = ''

for valor in lista_curriculo:
    concatena_string = concatena_string + valor.replace('\n','') + ' '

# lista_curriculo = str(lista_curriculo)


var = ['python', 'powerbi', 'sql', 'soft']

candidatos_match = 0
count = 0

for i in var:
    if i in concatena_string:
        count = count + 1

print(count)

if count > 0:
    candidatos_match = candidatos_match + 1

print(candidatos_match)

dict1 = {}

dict1["resumo_candidato_x"] = concatena_string

print(dict1)

