import pymysql
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'test'
)

cursor = conexao.cursor()

#Atualizações de uma tabela
# com_sql = "UPDATE pessoa set nome = 'João' where id = 1"
# cursor.execute(com_sql)
# conexao.commit()

con_sql = 'select * from pessoa'
cursor.execute(con_sql)
for i in cursor.fetchall():
    print(i)