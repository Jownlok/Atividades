# List é mupavel, ordenada e permite elementos duplicados, usada para armazenar sequência de dados, filas simples, históricos
# ou items dinâmicos;
frutas = ['maçã', 'laranja', 'banana']
print(frutas[0])
print(len(frutas))
frutas.append('Uva') #Adiciona Uva a lista
print(frutas)
frutas.insert(3,'manga') #adiciona manga a posição 3
print(frutas)
frutas.remove('banana')#remove item
print(frutas)
frutas.pop(0) #remove e retorna item
print(frutas)