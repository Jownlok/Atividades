def menu():
    print('|' + '-' * 10 + 'Calculadora Simples' + '-' * 10 + '|')
    print('[1]Soma')
    print('[2]Sair')
    print('|' + '-' * 40 + '|\n')


def valida_op(perg, min, max):
    while True:
        try:
            op = int(input(perg))
            if op < min or op > max:
                print('Digite um número válido.')
        except ValueError:
            print('Digite um número válido.')
        else:
            return op 

while True:
    menu()
    op = valida_op('>>', 1,2)
    if op == 1:
        resultado = 0
        quantidade = valida_op('Quantos números deseja somar [1-10]: ', 1, 10)
        for i in range(quantidade):
            numero = float(input(f'Digite o {i + 1}º número: '))
            resultado += numero
        print(f'O resultado da soma é: {resultado}\n')
    elif op == 2:
        print('Encerrando o programa. . .')
        break
