data = [
    {"id":1, "nome": "Maria", "salario": 4500.03},
    {"id":2, "nome": "José", "salario": 6500.05},
    {"id":3, "nome": "Antonio", "salario": 3409.98},
    {"id":4, "nome": "Ana", "salario": 5093.34},
    {"id":5, "nome": "Mariana", "salario": 3458.54},
    {"id":6, "nome": "Ana", "salario": 10932.59},
]
total = 0
for item in data:
    total = total+item['salario'] 

print(f' Média = {total/len(data):.2f}')

#OU ---------------------------------------------------------------------------------------

import pandas as pd

df = pd.DataFrame(data)
media = df['salario'].mean()
print(f'Média Pandas = {media:.2f}')