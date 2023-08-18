import csv,os
import Pesquisar
from datetime import datetime

def relatorio_atrasado():
    emprestimo_csv = open('emprestimo.csv')
    dados_emprestimos = csv.DictReader(emprestimo_csv, delimiter=';')

    os.system('cls') or None
    print("============== RELATÓRIO DE LIVROS ATRASADOS =============")
    print(f'{"CPF":15}',f'{"NOME":25}',f'{"TÍTULO":15}',f'{"EMPRÉSTIMO":15}',f'{"SITUAÇÃO":10}',f'{"DIAS"}')
    for emprestados in dados_emprestimos:
        data_emprestimo = datetime.strptime(emprestados['data_emprestimo'], '%Y-%m-%d')#transformar em dias para saber, pois dava erro
        #data_emprestimo = datetime.strftime(emprestados['data_emprestimo'],'%d/%m/Y')
        data_hoje = datetime.today()
        dias_atrasados = (data_hoje - data_emprestimo).days # o .days é so pra mostrar os dias

        if dias_atrasados > 7:
            situacao = str("ATRASADO!")
            print(f'{emprestados["cpf"]:15}',
                  f'{emprestados["nome_usuario"]:25}',
                  f'{emprestados["titulo_livro"]:15}',
                  f'{emprestados["data_emprestimo"]:15}',
                  f'{situacao:10}',
                  f'{dias_atrasados}')


