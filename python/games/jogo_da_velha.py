def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]


def exibir_tabuleiro(tabuleiro):
    print("\n  0   1   2")
    for i, linha in enumerate(tabuleiro):
        print(f"{i} " + " | ".join(linha))
        if i < 2:
            print("  " + "---+" * 2 + "---")
    print()


def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):
            return True
        if all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False


def tabuleiro_cheio(tabuleiro):
    return all(celula != " " for linha in tabuleiro for celula in linha)


def jogar():
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"

    print("--- JOGO DA VELHA ---")
    print("Digite a linha (0-2) e a coluna (0-2) separadas por espaço.\n")

    while True:
        exibir_tabuleiro(tabuleiro)

        # Entrada do jogador
        try:
            jogada = input(
                f"Jogador [{jogador_atual}], informe linha e coluna: "
            ).split()
            if len(jogada) != 2:
                print("⚠️ Digite dois números (ex: 1 2)!")
                continue

            linha, coluna = int(jogada[0]), int(jogada[1])

            if linha not in range(3) or coluna not in range(3):
                print("⚠️ Posição fora do tabuleiro! Use valores de 0 a 2.")
                continue

            if tabuleiro[linha][coluna] != " ":
                print("⚠️ Posição já ocupada! Escolha outra.")
                continue

        except ValueError:
            print("⚠️ Entrada inválida! Digite números inteiros.")
            continue

        # Marca a jogada
        tabuleiro[linha][coluna] = jogador_atual

        # Verifica fim de jogo
        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"🎉 Parabéns! O Jogador [{jogador_atual}] venceu!\n")
            break

        if tabuleiro_cheio(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("🤝 Empate! Deu velha.\n")
            break

        # Alterna o jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"


if __name__ == "__main__":
    jogar()