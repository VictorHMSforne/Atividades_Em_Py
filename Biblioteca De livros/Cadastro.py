import os, csv

def Cadastrar_Cliente():
    dados = {} #criando dicionário, para armazenar os dados
    os.system('cls') or None #limpa caso necessario
    print("=========== CADASTRO DE CLIENTES ========")
    nome = input("Digite seu Nome: ")
    cpf = input("Digite seu CPF: ")
    rg = input("Digite seu RG: ")
    dados[cpf]=[nome,rg]
    coluna = ["cpf", "nome", "rg"]
    print(coluna)
    print(dados)

    files_exist = os.path.isfile("clientes.csv")
    with open("clientes.csv","a",newline="", encoding="utf-8")as clientes_csv: #utf-8 padrão brasileiro para acentuação### as é um apelido
        cadastrar = csv.DictWriter(clientes_csv,fieldnames=coluna, delimiter=";",lineterminator='\r''\n')
        if not files_exist:
            cadastrar.writeheader()
        cadastrar.writerow({"cpf":cpf, "nome":nome, "rg":rg})
    print ("Cadastro realizado com sucesso!!")


def Cadastrar_Livros():
    dadoslivro= {}
    os.system("cls") or None
    print("========== CADASTRO DE LIVOS =============")
    nome= input("Digite o nome do livro: ")
    codigo = input("Digite o código do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite a editora: ")
    ano = input("Digite o ano de lançamento: ")
    dadoslivro[codigo]=[nome, autor, editora, ano]
    coluna=["nome","codigo","autor","editora","ano"]
    print(coluna)
    print(dadoslivro)

    files_exist = os.path.isfile("livros.csv")
    with open("livros.csv","a",newline="", encoding="utf-8")as livros_csv:
        cadastrar = csv.DictWriter(livros_csv,fieldnames=coluna, delimiter=";",lineterminator='\r''\n')
        if not files_exist:
            cadastrar.writeheader()
        cadastrar.writerow({"nome":nome,"codigo":codigo,"autor":autor,"editora":editora,"ano":ano })
    print("Cadastro concluído com sucesso!!!")



        