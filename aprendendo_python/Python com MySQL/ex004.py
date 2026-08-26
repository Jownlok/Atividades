# Aprendendo a criar chave primária

import pymysql

conexao = pymysql.connect(host='localhost', user='root', password='', database='notesmy')

#Execução de comandos, o cursor é uma intrução que permite executar comandos SQL no banco de dados
cursor = conexao.cursor()
cursor.execute('CREATE TABLE tabelateste(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50), idade INT(3) NOT NULL)')