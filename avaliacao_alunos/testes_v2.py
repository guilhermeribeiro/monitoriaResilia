'''
    Crie um programa que leia dois números do teclado e passe esses valores para uma função que irá checar qual deles é
    maior, qual deles é menor ou se eles são iguais.
'''

def avaliaNumeros(a, b):
    if a > b:
        print('O valor 1 é maior que o valor 2')
    elif a < b:
        print('O valor 2 é maior que o valor 1')
    else:
        print('Os valores são iguais')



# valor1 = int(input("Ler o valor 1: "))
# valor2 = int(input("Ler o valor 2: "))
# print(avaliaNumeros(valor1, valor2))


'''
    Crie um programa que leia três notas de um aluno do teclado e uma função que calcule a média delas, transformando o 
    resultado em um valor percentual tendo como intervalo de referência o valor de 0 (0%) a 10 (100%).
'''

def mediaPercentual(a, b, c):
    return ((a+b+c)/3)*10


valor1 = int(input("Ler o valor 1: "))
valor2 = int(input("Ler o valor 2: "))
valor3 = int(input("Ler o valor 3: "))
print(mediaPercentual(valor1, valor2, valor3))