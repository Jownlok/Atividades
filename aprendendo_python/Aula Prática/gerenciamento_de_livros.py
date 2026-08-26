def menu():
    print('Bem vindo a Livraria do João Vitor')
    print('----------------------------------')
    print('--------- MENU  PRINCIPAL --------')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livros')
    print('3 - Remover Livro')
    print('4 - Sair')

def cadastrar_livro(id_global):
    print('----------------------------------')
    print('------ MENU CADASTRAR LIVRO ------')
    id = input('Id do livro: ')
    nome = input('Porfavor entre com o nome do livro: ')
    autor = input('Porfavor entre com o autor do livro: ')
    editora = input('Porfavor entre com a editora do livro: ')
    livro = {"id": id,"nome": nome, "autor": autor, "editora": editora}
    return livro

def consultar_livro():
    print()
    print('1 - Consultar Todos')
    print('2 - Consultar por Id')
    print('3 - Consultar por Autor')
    print('4 - Retornar ao Menu')

    while True:
        try:
            opcao = int(input('>> '))
            if opcao in [1, 2, 3, 4]:
                return opcao
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Erro: digite apenas números inteiros.")

def remover_livro(id)

#PROGRAMA PRINCIPAL

lista_livros = []
id_global = 5836107

while True:
    menu()
    op = int(input('>> '))

    if op == 1:
        novo_livro = cadastrar_livro(id_global)
        lista_livros.append(novo_livro)
        print(lista_livros)
    elif op == 2:
        opcao = consultar_livro()
        if opcao == 1:
            print()
            print(f'Lista com todos os livros: {lista_livros}')
        elif opcao == 2:
            print()
            id_busca = input('Digite o Id do livro que deseja consiltar: ')
            encontrado = None
            for livro in lista_livros:
                if livro['id'] == id_busca:
                    encontrado = livro
                    break
            if encontrado:
                print()
                print(f'Livro encontrado: {encontrado}')
                print()
            else:
                print('Nenhum livro encontrado com esse Id.')
                print()
        elif opcao == 3:
            print()
            autor_busca = input('Digite o nome do autor do livro que deseja consultar: ')
            encontrado = None
            for livro in lista_livros:
                if livro['autor'] == autor_busca:
                    encontrado = livro
                    break
            if encontrado:
                print()
                print(f'Livro encontrado: {encontrado}')
                print()
            else:
                print()
                print('Nenhum livro encontrado com esse autor.')
                print()
                break
        elif op == 4:
            print('Voltando ao MENU PRINCIPAL. . .')
            print()
            break
    elif op == 3:
        
    elif op == 4:
        print('Encerrando programa . . . ')
        break