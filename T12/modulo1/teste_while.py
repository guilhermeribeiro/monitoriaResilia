tamanhoFor = int(input("Digite a quantidade de pessoas: "))

sexoFeminino = 0
qtdePessoas = 0
acumuladoSalario = 0
menorIdade = 0
maiorIdade = 0
parada = 0

while parada < tamanhoFor:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo: ")
    salario = float(input("Digite o salário: "))

    # Condição c) = quantidade de mulheres na região
    if sexo.upper() == 'F':
        sexoFeminino = sexoFeminino + 1

    # Condição a) = média de salário do grupo
    qtdePessoas = qtdePessoas + 1
    acumuladoSalario = acumuladoSalario + salario

    # Condição b) = maior e menor idade do grupo
    if menorIdade == 0 and maiorIdade == 0:
        maiorIdade = idade
        menorIdade = idade

    if idade > maiorIdade:
        maiorIdade = idade

    if idade < menorIdade:
        menorIdade = idade

    parada = parada + 1
    print(" ")


if(qtdePessoas > 0):
    print(acumuladoSalario/qtdePessoas)
    print(maiorIdade)
    print(menorIdade)
    print(sexoFeminino)





# parada = 0
#
# while parada < tamanhoFor:
#     print(parada)
#     parada = parada + 1