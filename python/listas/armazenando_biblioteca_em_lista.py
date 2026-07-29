lista = []
def cadastrar_livro(lista):
    Nome = input('Digite o nome do livro: ')
    Descricao = input('Digite uma descrição breve do livro: ')
    Autor = input('Digite o autor do livro: ')
    ISBN = input('Digite o ISBN do livro: ')

    livro = {'Nome':Nome,'Descricao':Descricao,'Autor':Autor,'ISBN':ISBN}
    lista.append(livro.copy())
    print('Livro cadastrado com sucesso!\n')
    return lista

def consultar_isbn(lista):
    isbn = input('Digite o ISBN do livro: ')
    for livro in lista:
        if livro['ISBN'] == isbn:
            print('\n Livro encontrado!')
            print(f"Nome: {livro['Nome']}")
            print(f"Descrição: {livro['Descricao']}")
            print(f"Autor: {livro['Autor']}")
            print(f"ISBN: {livro['ISBN']}")
            return
        print('Livro não encontrado')


while True:
    op = int(input('[1]Cadastrar [2]Consultar por ISBN [3] Sair \n>> '))
    if op == 1:
        cadastrar_livro(lista)
        print(f'Nova lista = {lista}')
    if op == 2:
        consultar_isbn(lista)
    if op == 3:
        print('Encerrando programa . . .')
        break
