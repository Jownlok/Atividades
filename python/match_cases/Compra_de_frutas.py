# Match-Case: Função recente do python; Igual a switch case de outras linguagens como C++;

from unittest import case


def menu():
    print('Escolha uma fruta:')
    print('1. Maçã')
    print('2. Banana')
    print('3. Laranja')


while True:
    menu()
    opc = int(input('Digite o número da fruta que deseja comprar: '))
    qnt = int(input('Digite a quantidade de frutas que deseja comprar: '))
    match opc:
        case 1:
            total = qnt * 2.50
            print(f'O total a pagar é: R${total:.2f}')
        case 2:
            total = qnt * 1.50
            print(f'O total a pagar é: R${total:.2f}')
        case 3:
            total = qnt * 3.00
            print(f'O total a pagar é: R${total:.2f}')
        case 4:
            print('Saindo do programa...')
            break
        case _:
            print('Opção inválida!')  