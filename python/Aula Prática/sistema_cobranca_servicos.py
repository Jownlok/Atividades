def menu():
    print('Bem vindo a Copiadora do João Vitor')
    print()
    print('Entre com o tipo de serviço desejado')
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')


def menu2():
    print()
    print('Deseja adicionar algum serviço?')
    print('1 - Encadernação Simples - R$ 15,00')
    print('2 - Encadernação Capa Dura - R$ 40,00')
    print('0 - Não desejo mais nada')


def escolha_servico(servico):
    while servico not in ['dig', 'ico', 'ipb', 'fot']:
        print('Escolha inválida, entre com o tipo do serviço novamente')
        servico = input('>> ').lower()
    return servico


def num_pagina():
    while True:
        try:
            numerop = int(input('Entre com o número de páginas: '))

            if numerop > 20000:
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, entre com o número de páginas novamente.\n')
                continue

            return numerop

        except ValueError:
            print('Digite um número inteiro válido.\n')


def validando_servico(servico):
    if servico == 'dig':
        return 0.20
    elif servico == 'ipb':
        return 0.40
    elif servico == 'ico':
        return 1.00
    elif servico == 'fot':
        return 0.20   # altere se o valor da fotocópia for diferente


def servico_extra():
    while True:
        try:
            op = int(input('>> '))

            if op == 1:
                return (servico_total * n_paginas) + 15

            elif op == 2:
                return (servico_total * n_paginas) + 40

            elif op == 0:
                return servico_total * n_paginas

            else:
                print('Escolha apenas 0, 1 ou 2.')

        except ValueError:
            print('Digite apenas um número (0, 1 ou 2).')


# Programa Principal
while True:

    menu()

    servico = input('>> ').lower()
    servico = escolha_servico(servico)

    servico_total = validando_servico(servico)

    n_paginas = num_pagina()

    menu2()

    total = servico_extra()

    print()

    if servico == 'dig':
        print(f'Total: R$ {total:.2f} (Serviço: R$0,20 x {n_paginas})')

    elif servico == 'ipb':
        print(f'Total: R$ {total:.2f} (Serviço: R$0,40 x {n_paginas})')

    elif servico == 'ico':
        print(f'Total: R$ {total:.2f} (Serviço: R$1,00 x {n_paginas})')

    elif servico == 'fot':
        print(f'Total: R$ {total:.2f} (Serviço: R$0,20 x {n_paginas})')

    break