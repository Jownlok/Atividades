def soma_imposto(custo, taxa_imposto):
    global taxa_nova
    taxa_nova = custo * (taxa_imposto / 100)
    global total
    total = custo + taxa_nova
    return(total )

custo = float(input('Digite o custo do item escolhido: '))
taxa_imposto = int(input('Digite a taxa de imposto em números inteiros: '))
soma_imposto(custo, taxa_imposto)
print(f'O total a ser pago é R${total} ...')
print('Encerrando . . .')

