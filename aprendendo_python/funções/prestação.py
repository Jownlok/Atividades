def valor_pagamento(valor, dias_atraso):
    if dias_atraso == 0:
        return valor
    else:
        multa = valor * 0.03
        juros = valor * (0.001 * dias_atraso)
        return valor + multa + juros


quantidade = 0
total = 0

while True:
    valor = float(input("Digite o valor da prestação (0 para encerrar): "))

    if valor == 0:
        break

    dias = int(input("Digite a quantidade de dias em atraso: "))

    pagamento = valor_pagamento(valor, dias)

    print(f"Valor a pagar: R$ {pagamento:.2f}\n")

    quantidade += 1
    total += pagamento

print("\n----- RELATÓRIO DO DIA -----")
print(f"Quantidade de prestações pagas: {quantidade}")
print(f"Valor total recebido: R$ {total:.2f}")

# USO DE IA PARA CORREÇÃO E MELHORIAS DO CÓDIGO