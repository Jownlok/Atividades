# Criando tabelas

import pymysql

conexao = pymysql.connect(
    host='localhost', 
    user='root', 
    password='', 
    database='notesmy',
    ) #Database a mesma que está no SGBD
cursor = conexao.cursor()
cursor.execute('CREATE TABLE users(email VARCHAR(120) UNIQUE, password VARCHAR(20))') #Criei a tabela users com as colunas email e password
        
