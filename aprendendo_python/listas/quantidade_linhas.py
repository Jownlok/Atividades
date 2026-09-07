import pandas as pd
data = [
    {"id":1, "nome": "Maria", "salario": 4500.03},
    {"id":2, "nome": "José", "salario": 6500.05},
    {"id":3, "nome": "Antonio", "salario": 3409.98},
    {"id":4, "nome": "Ana", "salario": 5093.34},
    {"id":5, "nome": "Mariana", "salario": 3458.54},
    {"id":6, "nome": "Ana", "salario": 10932.59},
]
print(f'Quantidade de linhas: {len(data)}')

df = pd.DataFrame(data)
quantidade = df.shape[1]
print(f'Quantidade de colunas: {quantidade}')

estatisticas = df['salario'].describe().round(2)
print(f"Principais estatísticas:\n{estatisticas}")
#Maniplando a lista = comandos {'id': 1, 'nome': 'Maria', 'salario': 4500.03}
print(data[0]) =  {'id': 1, 'nome': 'Maria', 'salario': 4500.03}
#Pegando apenas o valor do nome
print(data[0]["nome"]) = Maria
#Percorrendo toda a lista
for pessoa in data:
    print(pessoa) = percorre toda a lista
#Numero de colunas
numero_colunas = len(data[0])
print(f'Número de colunas: {numero_colunas}') 
#Descobrindo o nome das colunas
print(data[0].keys()) = dict_keys(['id', 'nome', 'salario'])