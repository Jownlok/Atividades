#Visualizando a tabela pelo python
import pymysql
conexao = pymysql.connect(host='localhost', user='root', password='', database='notesmy')
cursor = conexao.cursor()
cursor.execute("SHOW TABLES") #SHOW TABLES = mostrar tabelas

for x in cursor: #Em x no cursor, ele vai mostrar todas as tabelas que estão no banco de dados
    print(x)