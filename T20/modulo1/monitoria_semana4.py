'''
    Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721
'''
def funcReverso(numero):
    concat = ''
    for i in list(str(numero))[::-1]:
        if concat == '':
            concat = i
        else:
            concat = concat + i
    
    return int(concat)

def funcReversoSimples(numero):
    return str(numero)[::-1]

def funcReverso2(numero):
    concat = ''
    for i in reversed(str(numero)):
        if concat == '':
            concat = i
        else:
            concat = concat + i
    
    return int(concat)


#def zeros(n):


# print(funcReverso2(127))

# from calculadora import *

# print(divisao(2,6))

