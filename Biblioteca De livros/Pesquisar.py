import csv


def Pesquisar_Cliente(nome_cliente):
    cliente_csv = open("clientes.csv")#abrindo o arquivo CSV
    dados_cliente = csv.DictReader(cliente_csv,delimiter=";")# lendo o conteudo


    for cliente in dados_cliente: #percorrendo as linhas do arquivo
        if(cliente["nome"].lower() == nome_cliente.lower()):
            nome = (cliente["nome"]) #listar o nome do cliente, a partir da chave
            cpf = (cliente["cpf"])
            return True, nome, cpf
            break
    return False



def Pesquisar_Livro(nome_livro):
    livros_csv = open("livros.csv")#abrindo o arquivo CSV
    dados_livro = csv.DictReader(livros_csv,delimiter=";")# lendo o conteudo

    for livros in dados_livro:
        if(livros["codigo"] == nome_livro):
            livro=(livros["codigo"])
            nomel=(livros["nome"])
            return True,livro,nomel
            break
    return False

print(Pesquisar_Livro("90"))


