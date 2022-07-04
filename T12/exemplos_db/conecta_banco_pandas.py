import psycopg2
import pandas as pd

con = psycopg2.connect(host='localhost', database='resilia', user='postgres', password='admin')

cur = con.cursor()

cur.execute('select * from pizzaria.tb_pizza')

rs = cur.fetchall()

df = pd.DataFrame(rs, columns=['id_pizza','nome','desc','cat','preco'])

print(df)

print(df.query('preco > 55.0'))


