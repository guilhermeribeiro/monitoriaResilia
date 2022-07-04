import psycopg2

# Criar a conexão com o banco com os dados de acesso
    # host
    # nome do banco (database)
    # nome do usuario (user)
    # senha (passworod)
# Criar um cursor com essa conexão para poder executar os comandos SQL
# Executar comandos SQL
# Manipular os resultados

con = psycopg2.connect(host='localhost', database='resilia', user='postgres', password='admin')

cur = con.cursor()

cur.execute('select * from pizzaria.tb_pizza')

for desc in cur.description:
    print(desc[0])

print('\n')
rs = cur.fetchall()

for rec in rs:
    print(rec[1] + ' ' + str(rec[4]))