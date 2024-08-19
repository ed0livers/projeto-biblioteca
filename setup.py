import mysql.connector

# Configurações de conexão com o banco de dados
host = "localhost"
user = "root"
password = "mysql"
database = "biblioteca"  # Nome do banco de dados para a biblioteca

conexao = None
cursor = None

try:
    # Criação da conexão e execução das operações SQL
    conexao = mysql.connector.connect(host=host, user=user, password=password)
    cursor = conexao.cursor()

    # Criação do banco de dados se não existir
    cursor.execute("DROP DATABASE IF EXISTS biblioteca")
    cursor.execute("CREATE DATABASE biblioteca")
    cursor.execute("USE biblioteca")
    
    # Criação da tabela livros
    sqlCreateTable = '''
    CREATE TABLE livros (
        id_livro INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        nome_livro VARCHAR(255) NOT NULL,
        id_autor INT NOT NULL,
        qtd_paginas INT NOT NULL,
        preco_livro DECIMAL(6,2) NOT NULL
    );
    '''
    cursor.execute(sqlCreateTable)
    
    # Inserção de 30 livros na tabela
    sqlInsertBooks = '''
    INSERT INTO livros (nome_livro, id_autor, qtd_paginas, preco_livro) VALUES
    ('O Senhor dos Anéis', 1, 1178, 99.90),
    ('Harry Potter e a Pedra Filosofal', 2, 223, 39.90),
    ('O Código Da Vinci', 3, 689, 49.90),
    ('A Game of Thrones', 4, 694, 59.90),
    ('Orgulho e Preconceito', 5, 432, 29.90),
    ('1984', 6, 328, 34.90),
    ('Dom Casmurro', 7, 256, 24.90),
    ('A Culpa é das Estrelas', 8, 336, 44.90),
    ('O Hobbit', 1, 310, 39.90),
    ('As Crônicas de Nárnia', 9, 767, 54.90),
    ('O Alquimista', 10, 208, 29.90),
    ('O Pequeno Príncipe', 11, 96, 19.90),
    ('A Arte da Guerra', 12, 130, 22.90),
    ('O Sol é para Todos', 13, 281, 39.90),
    ('O Grande Gatsby', 14, 180, 34.90),
    ('Moby Dick', 15, 585, 29.90),
    ('A Menina que Roubava Livros', 16, 550, 49.90),
    ('O Morro dos Ventos Uivantes', 17, 416, 24.90),
    ('O Conde de Monte Cristo', 18, 1276, 39.90),
    ('A Revolução dos Bichos', 6, 144, 22.90),
    ('O Nome do Vento', 19, 662, 59.90),
    ('O Último Desejo', 20, 272, 49.90),
    ('A Casa dos Espíritos', 21, 468, 44.90),
    ('O Senhor das Moscas', 22, 224, 34.90),
    ('O Giver', 23, 180, 29.90),
    ('O Diário de Anne Frank', 24, 283, 39.90),
    ('Anne of Green Gables', 25, 448, 24.90),
    ('O Príncipe', 26, 152, 19.90),
    ('A Vida Secreta das Abelhas', 27, 302, 34.90),
    ('Em Busca do Tempo Perdido', 28, 4215, 59.90),
    ('O Ciclo da Herança', 29, 528, 54.90),
    ('O Livro das Sombras', 30, 350, 39.90),
    ('A Noiva Fantasma', 31, 352, 44.90),
    ('O Clã dos Magos', 32, 448, 49.90),
    ('O Caçador de Pipas', 33, 371, 39.90);
    '''
    cursor.execute(sqlInsertBooks)
    conexao.commit()
    
    cursor.execute("SELECT VERSION()")
    resultado = cursor.fetchall()
    print(resultado[0][0])

except mysql.connector.Error as e:
    # Tratamento de erros e impressão de erros
    print("Erro SQL:", e)
except Exception as e:
    print("Erro Python:", e)
finally:
    # Finalizar as variáveis cursor e conexao
    if cursor is not None:
        cursor.close()
    if conexao is not None and conexao.is_connected():
        conexao.close()
