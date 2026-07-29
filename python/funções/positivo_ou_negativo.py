def valores (x):
    """
    Descubra se o número é positivo ou negativo com 1 parâmetro; 
    """
    if valor >= 1:
        print(f'{valor} é positivo')
    else:
        print(f'{valor} é negativo')

def menu ():
    print('-------------------------------------------')   
    print('Descubra se o número é positivo ou negativo')
    print('Descobrir [1]')
    print('Sair [2]')
    print('-------------------------------------------')


while True:
    menu()
    op = int(input('Digite a opção escolhida: '))
    if op == 1:
        print('Opção escolhida 1')
        valor = float(input('Digite o valor a ser descoberto: '))
        print('-----------------------------')
        valores(valor)
        print('-----------------------------')
    elif op == 2:
        print('Encerrando programa: ')
        break
help(valores)