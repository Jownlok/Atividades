def menu():
    print("-" * 20)
    print("[1] CADASTRAR")
    print("[2] LISTAR")
    print("[3] SAIR ")
    print("-" * 20)

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

def escolha(Max, Min, Leitura):
    while True:
        try:
            opcao = int(input(Leitura))
            if opcao > Max or opcao < Min:
                print("Use um número válido.")
                continue
        except:
            print("Use um número válido.")
        else:
            return opcao

def cadastra_pessoa(lista, nome, idade, funcao, cidade, estado, rua):
    try:
         a = open(lista, 'at')
    except:
        print('Erro ao cadastrar pessoa.')
    else:
        a.write(f'{nome}: {idade}, {funcao}, {cidade}, {estado}, {rua}\n')
    finally:
         a.close()

def listar_pessoa(lista):
    try:
        a = open(lista, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        print(a.read())
    finally:
        a.close()

#Programa principal

lista_pessoas = "lista_de_pessoas14_09_2026.txt"

if checar_arquivo(lista_pessoas):
    print('Arquivo encontrado no computador.')
else:
    print('Arquivo não encontrado.')
    criar_arquivo(lista_pessoas)


while True:
    menu()
    x = escolha(3, 1, ">> ")
    if x == 1:
        print("-" * 5, "CADASTRAR", "-" * 5)
        n = input("Digite seu nome >> ")
        i = int(input("Digite sua idade >> "))
        f = input("Digite sua funcao  >> ")
        c= input("Digite seu estado >> ")
        e = input("Digite sua cidade >> ")
        r = input("Digite sua rua >> ")
        print("-" * 19)
        cadastra_pessoa(lista_pessoas, n, i, f, c, e, r)
    elif x == 2:
        listar_pessoa(lista_pessoas)
    else:
        print("Encerrando programa. . .")
        break