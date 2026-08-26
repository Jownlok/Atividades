def exibir_tabuleiro():
    print("\n     1  2  3")
    print('\n  1|  |   |   |')
    print('\n  2|  |   |   |')
    print('\n  3|  |   |   |')

#Programa Principal
while True:
    exibir_tabuleiro()
    op = int(input("[x]Escolha uma posição (1-1) a (3-3): "))