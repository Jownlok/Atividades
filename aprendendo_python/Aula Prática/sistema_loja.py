print('Bem-vindo a Loja do João Vitor')
valor_unitario = float(input('Entre com o valor unitário do produto: '))
quantidade = int(input('Entre com a quantidade do produto: '))
valor_total = valor_unitario * quantidade

if valor_total < 2500:
    desconto = valor_total 
    print(f'O valor SEM desconto: R${valor_total:.2f}')
    print(f'O valor COM desconto: R${desconto:.2f}')
elif valor_total >= 2500 and valor_total < 6000:
    desconto = valor_total - (valor_total * 0.04)   
    print(f'O valor SEM desconto: R${valor_total:.2f}')
    print(f'O valor COM desconto: R${desconto:.2f}')
elif valor_total >= 6000 and valor_total < 10000:
    desconto = (valor_total * 0.07) - valor_total
    print(f'O valor SEM desconto: R${valor_total:.2f}')
    print(f'O valor COM desconto: R${desconto:.2f}')
elif valor_total >= 10000:
    desconto = (valor_total * 0.11) - valor_total
    print(f'O valor SEM desconto: R${valor_total:.2f}')
    print(f'O valor COM desconto: R${desconto:.2f}')