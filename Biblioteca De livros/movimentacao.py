import os, csv
import Pesquisar as p
from datetime import date

def Fazer_Emprestimo():
    emprestimo = []
    os.system("cls")or None
    print("---------------EMPRESTIMO DE LIVROS--------------")
    nome_usuario = input("Nome do Usuário: ")
    retorno = p.Pesquisar_Cliente(nome_usuario)
    
    if retorno[0] == True:
        codigo_livro= input("Codigo livro:")
        existe = p.Pesquisar_Livro(codigo_livro)
        if existe[0] == False:
            print("Livro não existe!!")
        else:
            data_emprestimo = date.today()

        colunas = ["cpf","nome_usuario","codigo_livro","titulo_livro","data_emprestimo"]
        file_exists = os.path.isfile("emprestimo.csv")
        with open("emprestimo.csv","a",newline="",encoding="utf-8") as emprestimo_csv:
            cadastrar = csv.DictWriter(emprestimo_csv, fieldnames=colunas, delimiter=';',lineterminator="\r\n")
            if not file_exists:
                 cadastrar.writeheader()
            cadastrar.writerow({'cpf':retorno[2],'nome_usuario':retorno[1],"codigo_livro":existe[1],"titulo_livro":existe[2],"data_emprestimo":data_emprestimo})
        print("empréstimo realizado com sucesso!!")          
    else:
        print("Usuário não cadastrado")

def Relatório_Atrasado():
    return 0