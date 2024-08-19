from conexao import Conexao

# Criação da conexão com o banco de dados
conexaoBD = Conexao("localhost", "root", "mysql", "biblioteca")

while True:
    print('''
    Bem-vindo ao GERENCIADOR DE LIVROS
    
    Menu:
    
    1. Ver Livros
    2. Cadastrar Novo Livro
    3. Alterar Cadastro de Livro
    4. Remover Livro
    0. Sair      
    ''')
    
    op = input("Digite a opção do menu desejada: ")
    
    if op == "1":
        print("Ver Livros")
        
        livros = conexaoBD.consultar("SELECT * FROM livros")
        
        if livros == []:
            print("Não foram encontrados livros.")
        else:
            print("ID | Nome | Autor | Páginas | Preço")
            for livro in livros:
                print(f"{livro[0]} | {livro[1]} | {livro[2]} | {livro[3]} | R${livro[4]:.2f}")
            
            idLivro = 0
            try:
                idLivro = int(input("Digite o id do livro desejado: "))
            except Exception as e:
                print("Erro:", e)
                
            if idLivro == 0:
                print("Operação Cancelada!")     
            else:
                livroEspecifico = conexaoBD.consultarComParametros("SELECT * FROM livros WHERE id_livro = %s", (idLivro,))
                
                if livroEspecifico == []:
                    print("Livro não encontrado!")
                else:
                    print(f'''
    ID: {livroEspecifico[0][0]}                  
    Nome: {livroEspecifico[0][1]}
    Autor: {livroEspecifico[0][2]}
    Páginas: {livroEspecifico[0][3]}
    Preço: R${livroEspecifico[0][4]:.2f}                  
    ''')                 
                
    elif op == "2":
        nome = input("Digite o nome do novo livro: ")  
        idAutor = int(input("Digite o id do autor: "))
        qtdPaginas = int(input("Digite a quantidade de páginas: "))
        preco = float(input("Digite o preço do livro em R$: "))
        
        conexaoBD.manipularComParametros(
            "INSERT INTO livros (nome_livro, id_autor, qtd_paginas, preco_livro) VALUES (%s, %s, %s, %s)",
            (nome, idAutor, qtdPaginas, preco)
        )
        print("Livro inserido com sucesso!")
        
    elif op == "3":
        livros = conexaoBD.consultar("SELECT * FROM livros")
        
        if livros == []:
            print("Não foram encontrados livros!")
        else:
            print("ID | Nome | Autor | Páginas | Preço")
            for livro in livros:
                print(f"{livro[0]} | {livro[1]} | {livro[2]} | {livro[3]} | R${livro[4]:.2f}")
            
            try:
                idEscolhido = int(input("Digite o id do livro que deseja alterar: "))
            except Exception as e:
                print("Erro:", e)
                idEscolhido = 0
            
            livroEscolhido = conexaoBD.consultarComParametros("SELECT * FROM livros WHERE id_livro = %s", (idEscolhido,))
            
            if livroEscolhido == []:
                print("Livro não encontrado!")
            else:
                print(f'''
    ID: {livroEscolhido[0][0]}
    Nome: {livroEscolhido[0][1]}
    Autor: {livroEscolhido[0][2]}
    Páginas: {livroEscolhido[0][3]}
    Preço: R${livroEscolhido[0][4]:.2f}
    ''')
                
                novoNome = input("Digite o novo nome: ")
                if novoNome == "":
                    novoNome = livroEscolhido[0][1]
                    
                novoAutor = int(input("Digite o novo id do autor: "))
                if novoAutor == 0:
                    novoAutor = livroEscolhido[0][2]
                    
                novaQtdPaginas = int(input("Digite a nova quantidade de páginas: "))
                if novaQtdPaginas == 0:
                    novaQtdPaginas = livroEscolhido[0][3]
                    
                novoPreco = float(input("Digite o novo preço: "))
                if novoPreco == 0:
                    novoPreco = livroEscolhido[0][4]
                
                sqlAtualizar = '''
                UPDATE livros
                SET
                nome_livro = %s,
                id_autor = %s,
                qtd_paginas = %s,
                preco_livro = %s
                WHERE
                id_livro = %s
                '''
                conexaoBD.manipularComParametros(sqlAtualizar, (novoNome, novoAutor, novaQtdPaginas, novoPreco, idEscolhido))
                print("Livro atualizado com sucesso.")
                
    elif op == "4":
        livros = conexaoBD.consultar("SELECT * FROM livros")
        
        if livros == []:
            print("Não foram encontrados livros!")
        else:
            print("ID | Nome | Autor | Páginas | Preço")
            for livro in livros:
                print(f"{livro[0]} | {livro[1]} | {livro[2]} | {livro[3]} | R${livro[4]:.2f}")
        
            try:
                idLivro = int(input("Digite o id do livro que deseja remover: "))
            except Exception as e:
                print("Erro:", e)
                idLivro = 0
                
            if idLivro == 0:
                print("Operação Cancelada!")
            else:
                livroEscolhido = conexaoBD.consultarComParametros("SELECT * FROM livros WHERE id_livro = %s", (idLivro,))
                
                if livroEscolhido == []:
                    print("Livro não foi encontrado!")
                else:
                    print(f'''
    ID: {livroEscolhido[0][0]}
    Nome: {livroEscolhido[0][1]}
    Autor: {livroEscolhido[0][2]}
    Páginas: {livroEscolhido[0][3]}
    Preço: R${livroEscolhido[0][4]:.2f}
    ''')
                
                confirmacao = input("Deseja remover este livro? (sim/não) ")
                
                if confirmacao.lower() == "sim":
                    conexaoBD.manipularComParametros("DELETE FROM livros WHERE id_livro = %s", (idLivro,))
                    print("Livro removido com sucesso!")
                else:
                    print("Operação Cancelada!")   
                    
    elif op == "0":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida, tente novamente!")
