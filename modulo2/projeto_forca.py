
qtde = int(input("digite a quantidade de jogadores: "))
tentativas = 6
lista_dicionarios = []
palavra = 'uva'


def acertarErrarJogo(lista_dicionarios, jogador, letra, palavra):
    acerto = 0
    for l in range(len(palavra)):
        if letra.upper() == palavra[l].upper():
            lista_dicionarios[jogador]["letrasAcertadas"][l] = letra
            acerto += 1
    if acerto > 0 and '_' in lista_dicionarios[jogador].get("letrasAcertadas"):
        letra = input("Digite uma letra jogador " + lista_dicionarios[jogador].get("nome") + ": ")
        return acertarErrarJogo(lista_dicionarios, jogador, letra, palavra)
    elif acerto == 0:
        atualizarErro = lista_dicionarios[jogador].get("erros")
        atualizarErro = atualizarErro + 1
        lista_dicionarios[jogador].update(erros=atualizarErro)
        return 1
    else:
        return 0



def jogo():
    for i in range(qtde):
        nomeJogador = input("Digite o nome do jogador: ")
        lista_dicionarios.append({"nome": nomeJogador, "erros": 0, "letrasAcertadas": ['_']*len(palavra)})

    var = 0
    ganhou = False
    index = 0

    while var < (qtde * tentativas) and ganhou == False:
        letra = input("Digite uma letra jogador " + lista_dicionarios[index].get("nome") + ": ")
        if lista_dicionarios[index].get("erros") < 6:
            retorno = acertarErrarJogo(lista_dicionarios, index, letra, palavra)

            if not '_' in lista_dicionarios[index].get("letrasAcertadas"):
                print("O jogador "+ lista_dicionarios[index].get("nome") + " venceu o jogo!")
                ganhou = True
            else:
                var = var + retorno
                index = index + 1
                if (index >= qtde):
                    index = 0
        else:
            print("O jogador " + lista_dicionarios[index].get("nome") + " já esgotou sua quantidade de tentativas")

        if var == (qtde * tentativas):
            print("Não houveram ganhadores. Game Over!")

jogo()





