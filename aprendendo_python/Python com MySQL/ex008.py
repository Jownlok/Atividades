#OrdemBy
import pymysql
conec = pymysql.connect(host='localhost', user='root', password='', database='notesmy')
cursor = conec.cursor()

con_sql = 'SELECT * FROM tabelateste ORDER BY nome DESC'

cursor.execute(con_sql)

resultado = cursor.fetchall()

for x in resultado:
    print(x)