def menu():
    print('-' * 30)
    print('Descubra o horário PM ou AM')
    print('-' * 30)
    print('Descobrir [1]')
    print('Sair [Qualquer outro número]')
    print('-' * 30)

def descobrir(hora):
    if hora >= 13:
        global valor
        valor = 'A'
        return valor
    else: 
        valor = 'P'
        return valor
    
def dizer(valor, hora):
    if valor == 'A':
        hora = hora - 12
        print(f'O horário é {hora}:00 A.M')
    else:
        hora = hora + 12
        print(f'O horário é {hora}:00 P.M')

while True:
    menu()
    op = int(input('Escolha a opção: '))
    if op == 1:
        hora = int(input('Digite a hora em números inteiros: '))
        descobrir(hora)
        dizer(valor, hora)
    else:
        print('Encerrando . . .')
        break