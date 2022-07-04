# nome = "Jonas"
# horario = input('Digite o período da facul: \n [M] Mat \n [V] Vesp \n[N] Not\n ')

# condicao = True

# while condicao:
#     if horario == 'M':
#         print("Bom dia " + nome)
#         condicao = False
#     elif horario == 'V':
#         print("Boa tarde " + nome)
#         condicao = False
#     elif horario == 'N':
#         print("Boa noite " + nome)
#         condicao = False
#     else:
#         print('Valor inválido. Digite novamente \n')
#         horario = input('Digite o período da facul: \n [M] Mat \n [V] Vesp \n[N] Not\n ')



# def soma(v1, v2):
#     return v1 + v2


# def main():
#     x = int(input('Digite um valor: '))
#     y = int(input('Digite outro valor: '))
#     print(soma(x, y))


# main()

# 07/06 --------------------------------------------------------------------------

# import math

# N = 500 #int(input('Digite o tamanho da população: '))
# p = 0.5
# e = 0.05 #float(input('Digite a margem de erro: '))
# ie = 80 #int(input('Digite o intervalo de confiança (80, 85, 90, 95, 99): '))


# if ie == 80:
#     z = 1.28
# elif ie == 85:
#     z = 1.44
# elif ie == 90:
#     z = 1.65
# elif ie == 95:    
#     z = 1.96
# elif ie == 99:
#     z = 2.58

# # print(z**2)

# # print((((z**2) * (p*(1-p)))/ (e**2)))

# # print((1+ (((z**2)*(p*(1-p)))/(e**2)*N)))

              
# tam_amostra = (((z**2) * (p*(1-p)))/(e**2))/ (1+ (z**2)*(p*(1-p)) / ((e**2)*N))


# print(math.ceil(tam_amostra))



# Idade
# Sexo
# Salario
# idade máxima
# idade minima

# idade = 0
# idade_min = 1000
# idade_max = 0
# sexo_f = 0
# salario_acumulado = 0
# qtd_salario = 0

# while idade >= 0:
#     idade = int(input('Digite a idade: '))

#     if idade > -1:
#         if idade > idade_max:
#             idade_max = idade
#         if idade < idade_min:
#             idade_min = idade

#         sexo = input('Digite o sexo (M ou F): ')
#         salario = float(input('Digite o salario: '))
#         print('\n')

#         if sexo == 'F':
#             sexo_f += 1
        
#         if salario > 0:
#             salario_acumulado += salario
#             qtd_salario += 1

# print(salario_acumulado/qtd_salario)
# print(sexo_f)
# print(idade_min)
# print(idade_max)

# 08/06 ----------------------------------------------------------------------------------------

# and (&) - e lógico
# or (|)- ou lógico
# not (~ versões antigas do python)- não lógico


# x = 1
# y = 2
# z = True
# a = False
# b = False

# Exemplo 1
# if not (x >= 1) | (y == 3):
#     print('Entrei na condição 1')
# else:
#     print('Entrei na condição 2')

# Exemplo 2
# if x >= 1:
#     print('Entrei na condição 1')
# elif y == 2:
#     print('Entrei na condição 2')
# else:
#     print('Não entrei na condição 2')

# Exemplo 3
# if ((x>y) | a) and z | (x+y)==3:
#     print('Entrei na 1')
# else:
#     print('Entrei na 2')

# Exemplo 4
# if not ((x>y) | a) and (z and (x+y)>=3):
#     print('Entrei na 1')
# else:
#     print('Entrei na 2')


# # Exemplo 5
# x = 10
# y = 1
# z = True
# a = True
# b = False
# string = 'x'

# if not (y < x) and z | b:
#     print('Entrei na 1')
# else:
#     print('Entrei na 2')
# if (x > y) and 'x' == 'x':
#     print('Entrei nesse aqui')
# elif not a and b:
#     print('Entrei nesse outro')
# else:
#     print('Nem no aqui, nem no outro')

# 09/06 -----------------------------------------------

# valor1 = int(input('primeiro: '))
# valor2 = int(input('segundo: '))

# def soma(v1, v2):
#     return v1 + v2

# print(soma(valor1,valor2))

s = 'Guilherme'

print(s[:5])



