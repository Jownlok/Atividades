# Dissecando uma Variável
palavra = input('Digite uma palavra: ')
tipo = type(palavra)
print(f'O tipo é {tipo}')
print('Só tem espaço?', palavra.isspace())
print('É alfabético?', palavra.isalpha())
print('É alfanúmerico?', palavra.isalnum())
print('Está em maiúsculo?', palavra.isupper())