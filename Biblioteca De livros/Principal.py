import Cadastro  #importei o arquivo acima, chamado Cadastro(da pra usar as pra diminuir, estilo o static sytem)
import Listar
import Remover
import movimentacao
import relatorio
resposta = 's'

while resposta == 's':
    menu ='''---------- BIBLIOTECA TDS 10 ------------
    \r[1]Cadastrar Cliente
    \r[2]Listar Clientes
    \r[3]Cadastrar livro
    \r[4]Listar Livros
    \r[5]Fazer empréstimo
    \r[6]Listar empréstimo
    \r[7]Relatório de Livros atrasados
    \r[8]Remover Cliente
    \r[9]Remover Livro
    '''
    print(menu)
    opcao =int(input("Entre com uma opção:"))   #escolher a opção digitada por você
    if opcao ==1:
        Cadastro.Cadastrar_Cliente()
    elif opcao == 2 :
        Listar.Listar_Clientes()
    elif opcao == 3 :
        Cadastro.Cadastrar_Livros()#Usa-se o Cadastro(semelhante a biblioteca)
    elif opcao == 4 :
        Listar.Listar_Livros()
    elif opcao == 5 :
        movimentacao.Fazer_Emprestimo()
    elif opcao == 6 :
        Listar.Listar_Emprestimo()
    elif opcao == 7 :
        relatorio.relatorio_atrasado()
    elif opcao == 8 :
        Remover.Remover_Cliente()
    elif opcao == 9 :
        Remover.Remover_Livro()
    resposta = input("Deseja continuar?[s/n]")
    
    
