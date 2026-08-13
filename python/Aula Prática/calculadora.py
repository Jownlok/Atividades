def menu():
    print('|----------Calculadora Simples----------|')
    print('| [1]Soma                               |')
    print('| [2]Subtração                          |')
    print('| [3]Multiplicação                      |')
    print('| [4]Divisão                            |')
    print('| [5]Sair                               |')

def valida_op(perg, min, max):
    while True:
        try:
            op = int(input(perg))
            if op < min or op > max:
                continue
            else:
                return op
        except ValueError:
            print('Digite um número válido.')

def valida_qnt(perg, min, max):
    while True:
        try:
            qnt = int(input(perg))
            if qnt < min or qnt > max:
                continue
        except ValueError:
            print('Digite um número válido.')
        else:
            return qnt
        
soma = 0
while True:
    menu()
    op = valida_op('>>', 1,5)
    print()
    quantidade = valida_qnt('Quantos números deseja calcular?', 2, 10)

while True
    if op == 1:
        resultado = 0

        for i in range(quantidade):
            num = float(input('>> '))
            resultado += num

        print(f'\nTotal: {resultado}')


    elif op == 2:
        resultado = float(input('>> '))

        for i in range(quantidade - 1):
            num = float(input('>> '))
            resultado -= num

        print(f'\nTotal: {resultado}')


    elif op == 3:
        resultado = 1

        for i in range(quantidade):
            num = float(input('>> '))
            resultado *= num

        print(f'\nTotal: {resultado}')


    elif op == 4:
        resultado = float(input('>> '))

        for i in range(quantidade - 1):
            num = float(input('>> '))
            resultado /= num

        print(f'\nTotal: {resultado}')


    elif op == 5:
        print('Encerrando o programa . . .')
        break