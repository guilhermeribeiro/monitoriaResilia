def complete_series(seq):
    repetido = set(seq)
    if len(repetido) != len(seq):
      return [0]
    maior_valor = max(seq)
    contador = []
    for valor in range(maior_valor + 1):
      contador.append(valor)
    return contador

seq = [0, 1, 3]

print(complete_series(seq))