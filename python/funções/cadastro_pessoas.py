def menu():
    print('\n=========Cadastrar========')
    print('==========================')
    print('[1]Cadastrar')
    print('[2]Listar')
    print('[3]Sair')
    print('==========================\n')

def checar_arquivo(lista):
    try:
        a = open(lista, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar_arquivo(lista):
    try:
        a = open(lista, 'wt+')
        a.close()
    except:
        print('Erro ao criar arquivo.')
    else:
        print(f'{lista} criado com sucesso!')

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def cadastrar_pessoa(lista, nome, idade, peso):
    try:
        a = open(lista, 'at')
    except:
        print('Erro ao cadastrar pessoa.')
    else:
        a.write(f'{nome}: {idade}, {peso}\n')
    finally:
        a.close()

def remover(arquivo, nome):
    try:
        with open(arquivo, 'r', encoding='utf-8') as a:
            linhas = a.readlines()

        encontrou = False
        linhas_filtradas = []

        for linha in linhas:
            if linha.startswith(nome.strip() + ":"):
                encontrou = True
            else:
                linhas_filtradas.append(linha)

        with open(arquivo, 'w', encoding='utf-8') as a:
            a.writelines(linhas_filtradas)

        if encontrou:
            print(f"Pessoa '{nome}' removida com sucesso!")
        else:
            print("Pessoa não encontrada.")

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as erro:
        print(f"Erro: {erro}")

def listar_pessoa(lista):
    try:
        a = open(lista, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        print(a.read())
    finally:
        a.close()

#Programa Principal

lista_pessoas = 'lista_pessoas.txt'

if checar_arquivo(lista_pessoas):
    print('Arquivo encontrado no computador.')
else:
    print('Arquivo não encontrado.')
    criar_arquivo(lista_pessoas)

while True:
    menu()
    op = valida_int('>>', 1, 3)
    if op == 1:
        nome = input('Digite o nome: ')
        idade = input('Digite a idade: ')
        peso = input('Digite o peso (KG): ')
        cadastrar_pessoa(lista_pessoas, nome, idade, peso)
    if op == 2:
        listar_pessoa(lista_pessoas)
    if op == 3:
        print('Encerrando programa . . .')
        break
    

