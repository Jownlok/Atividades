# Aprendendo a criar chave primária

import pymysql

conexao = pymysql.connect(host='localhost', user='root', password='', database='notesmy')

#Execução de comandos, o cursor é uma intrução que permite executar/métodos comandos SQL no banco de dados
cursor = conexao.cursor()
cursor.execute('ALTER TABLE tabelateste DROP COLUMN id')