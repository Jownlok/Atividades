# Operadores Aritméticos: +, -, *, /, //(divisão inteira, retorna apenas o inteiro), **, %
#Ordem de Procedência: 1 = Parenteses, 2 = Exponenciação, 3 = Multiplicação e Divisão, 4 = Adição e Subtração
# pow(4,3) = 64, uma função que retorna o valor de 4 elevado a 3
#============================================================================================================

#nome = input('Qual é o seu nome? ')         |
#print(f'Prazer em te conhecer {nome:>20}!') |Antes do nome vai ter um espaço de 20 caracteres, alinhado a direita
#Saída = Prazer em te conhecer                 Luis!

numero = 0
total = 0
quantidade = int(input('Digite a quantidade de números que deseja somar: '))
for x in range(quantidade):
    numero = float(input(f'Digite o número {x+1}: '))
    total = total + numero
print(f'A soma dos números é: {total}')