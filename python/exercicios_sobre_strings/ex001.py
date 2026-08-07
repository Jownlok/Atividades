def menu():
    print('---------------------')
    print('Comparação de Strings')
    print('[1]Comparar')
    print('[2]Sair')
    print('---------------------')

def valida_op(pergunta, min, max):
    while True:
        try:
            op = int(input(pergunta))
            if op < min or op > max:
                print(f'ERRO! Digite um número entre {min} e {max}.')
            else:
                return op
        except ValueError:
            print('ERRO! Digite um número válido.')

while True:
    menu()
    op = valida_op('>>', 1, 2)
    if op == 1:
        str1 = input('Digite a primeira str: ')
        str2 = input('Digite a segunda str: ')
        
        print(f'Tamanho de {str1}: {len(str1)} caracteres')
        print(f'Tamanho de {str2}: {len(str2)} caracteres')
        um = len(str1)
        dois = len(str2)

        if um == dois:
            print('As duas strings são de tamanhos iguais.')
        else:
            print('As duas strings são de tamanhos diferentes.')

        if str1 == str2:
            print('As duas strings possuem o mesmo conteúdo.')
            print()
        else:
            print('As duas strings possuem conteúdos diferentes.')
            print()
    elif op == 2:
        print('Encerrando programa. . . ')
        break