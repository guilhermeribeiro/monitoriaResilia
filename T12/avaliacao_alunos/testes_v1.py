import pandas as pd

# projeto = pd.read_csv('C:\\Users\\guilh\\Downloads\\Ano-2021.csv', delimiter = ';')
#
# teste = projeto[['txNomeParlamentar', 'ideCadastro']]
#
# teste.drop_duplicates(subset=['txNomeParlamentar'], inplace=True)
#
# teste.groupby(['ideCadastro']).count().query('txNomeParlamentar > 1')


# def soma(a, b):
#   return a + b
#
# valor1 = int(input("Ler o valor 1: "))
# valor2 = int(input("Ler o valor 2: "))
#
# resultado = soma(valor1, valor2)
#
# if resultado == 12:
#     print('Soma igual a 12')
# elif resultado > 12:
#     print('Soma maior que 12')
# else:
#     print('Soma menor que 12')

# '''laranja, uva, morango, melancia'''
#
# lista = ['laranja', 'uva', 'morango', 'melancia']
#
# for i, j in enumerate(lista):
#     palavra = list(j)
#     palavra[0] = str.upper(palavra[0])
#     palavra[-1] = str.upper(palavra[-1])
#     lista[i] = ''.join(palavra)
#
# print(lista)

'''Ler o dataset Walmart utilizando a biblioteca pandas e realizar as seguintes operações:

    1 - Remover as colunas Unemployment e CPI;
    2 - Imprimir a soma das vendas semanais (Weekly_Sales);
    3 - Imprimir a média do preço do combustível (Fuel_Price);

'''

import pandas as pd

projeto = pd.read_csv('C:\\Users\\guilh\\Downloads\\Aula 7_Walmart_Store_sales.csv', delimiter=',')

print(projeto.head())

projeto.drop(columns=['Unemployment', 'CPI'], inplace=True)

# Print para demonstrar que as colunas foram removidas.
print(projeto.head())

print(projeto['Weekly_Sales'].sum())
print(projeto['Fuel_Price'].mean())
