def menu():
    print('  Bem-vindo a Loja de Gelados do João Vitr ')
    print('------------------Cardápio-----------------')
    print('-------------------------------------------')
    print('-----|Tamanho |Cupuaçu (CP)| Açai    |-----')
    print('-----|  P    |  R$ 9,00   | R$ 11,00 |-----')
    print('-----|  M    |  R$ 14,00  | R$ 16,00 |-----')
    print('-----|  G    |  R$ 18,00  | R$ 20,00 |-----')
    print('-------------------------------------------')

def valida_sabor(escolha):
    while escolha not in ['cp', 'ac']:
        print('Sabor inválido. Tente novamente')
        escolha = input('Entre com o sabor desejado (CP/AC): ').lower()
    return escolha

def valida_tamanho(escolha):
    while escolha not in ['p', 'm', 'g']:
        print('Tamanho inválido. Tente novamente')
        escolha = input('Entre com o tamanho desejado (P/M/G): ')
    return escolha

def valor_total(sabor, tamanho, total):
    if tamanho == 'p' and sabor == 'cp':
        total = total + 9
        print(f'Você pediu um {sabor} no tamanho {tamanho}: R$9,00')
    elif tamanho == 'm' and sabor == 'cp':
        total = total + 14
        print(f'Você pediu um {sabor} no tamanho {tamanho}: R$14,00')
    elif tamanho == 'g' and sabor == 'cp':
        total = total + 18
        print(f'Você pediu um {sabor} no tamanho {tamanho}: R$18,00')
    elif tamanho == 'p' and sabor == 'ac':
        total = total + 11
        print(f'Você pediu um {sabor} no tamanho {tamanho}: R$11,00')
    elif tamanho == 'm' and sabor == 'ac':
        total = total + 16
        print(f'Você pediu um {sabor} no tamanho {tamanho}: R$16,00')
    elif tamanho == 'g' and sabor == 'ac':
        total = total + 20
        print(f'Você pediu um {sabor} no tamanho {tamanho}: R$20,00')
    return total
        
def valida_op(op):
    while op not in ['s', 'n']:
        print('Opção de escolha errada. Tente novamente')
        op = input('Deseja mais alguma coisa? (S/N): ').lower()
    return op

#Programa Principal
menu()
acumulador = 0

while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ').lower()
    sabor = valida_sabor(sabor)
    tamanho = input('Entre com o tamanho desejado (P/M/G): ').lower()
    tamanho = valida_tamanho(tamanho)
    acumulador = valor_total(sabor, tamanho, acumulador)
    op = input('Deseja mais alguma coisa? (S/N): ').lower()
    op = valida_op(op)
    if op == 's':
        continue
    elif op == 'n':
        print(f'O valor total a ser pago: R$ {acumulador:.2f}')
        break





