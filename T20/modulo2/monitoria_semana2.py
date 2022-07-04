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

apresentacaoPilha()