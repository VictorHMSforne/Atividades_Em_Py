import csv
import Cadastro
import os
def Listar_Clientes():
    cliente_csv = open("clientes.csv", encoding='utf-8')#abrindo o arquivo CSV
    dados_cliente = csv.DictReader(cliente_csv,delimiter=";")# lendo o conteudo
    os.system("cls") or None
    print("=========LISTAGEM DE CLIENTES==========")
    print(f'{"CPF":15}',f'{"NOME":12}',"RG")  #o f é uma função para espaçamento, chamada format e o 15 é a distância de caracteres
    for clientes in dados_cliente:
        print(f'{clientes["cpf"]:15}',f'{clientes["nome"]:12}',clientes["rg"])
    cliente_csv.close()

def Listar_Livros():
    livros_csv = open("livros.csv")#abrindo o arquivo CSV
    dados_livro = csv.DictReader(livros_csv,delimiter=";")# lendo o conteudo
    os.system("cls") or None
    print("=========LISTAGEM DE LIVROS==========")
    print(f'{"NOME":18}',f'{"CODIGO":15}',f'{"AUTOR":15}',f'{"EDITORA":18}',"ANO")
    for livros in dados_livro:
        print(f'{livros["nome"]:18}',f'{livros["codigo"]:15}',f'{livros["autor"]:15}',f'{livros["editora"]:18}',livros["ano"])
    livros_csv.close()



def Listar_Emprestimo():
    emprestimo_csv = open("emprestimo.csv")
    dados_emprestimo = csv.DictReader(emprestimo_csv,delimiter=";")
    os.system("cls") or None
    print("============LISTAGEM DE EMPRÉSTIMOS=============")
    print(f'{"CPF":16}',f'{"NOME":20}',f'{"CÓDIGO":21}',f'{"TÍTULO":25}',"DATA DE EMPRÉSTIMO")
    for emprestimo in dados_emprestimo:
        print(f'{emprestimo["cpf"]:16}',f'{emprestimo["nome_usuario"]:20}',f'{emprestimo["codigo_livro"]:21}',f'{emprestimo["titulo_livro"]:25}',emprestimo["data_emprestimo"])

Listar_Emprestimo()