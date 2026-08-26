#Dicionários armazenam dados no formato chave-valor. Mutável e não ordenado, busca mais rápida;
#Uso para mapear identificadores, registros de banco de dados e contadores;
dados_user = {'Nome': 'Ana', 'Idade': 19, 'Cidade': 'São Paulo' }
print(dados_user['Nome'])
print(dados_user.keys())

if 'Estado' not in dados_user:
    dados_user['Estado'] = 'São Paulo' 
print(dados_user)    