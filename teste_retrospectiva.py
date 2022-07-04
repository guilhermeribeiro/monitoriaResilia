import pandas as pd

google = pd.read_excel('C:\\Users\\guilh\\Downloads\\Análise Retrospectiva - PROADI HIAE (respostas).xlsx')
ar = pd.read_excel('C:\\Users\\guilh\\Downloads\\divisão_imagens_analisadas_médicos.xlsx', sheet_name="Modelo 1" )
tb = pd.read_excel('C:\\Users\\guilh\\Downloads\\divisão_imagens_analisadas_médicos.xlsx', sheet_name="Modelo 2" )


ar = ar[(ar["Unnamed: 5"] == "Sim") | (ar["Unnamed: 5"] == "SIM")]
tb = tb[(tb["Unnamed: 5"] == "Sim") | (tb["Unnamed: 5"] == "SIM")]

final = pd.concat([ar, tb]).reset_index()


final1 = google.merge(ar, left_on='zz', right_on='Unnamed: 3', how='left')
final2 = google.merge(tb, left_on='zz', right_on='Unnamed: 3', how='left')


print(google[~google['zz'].isin(final["Unnamed: 3"])]['zz'].drop_duplicates())





