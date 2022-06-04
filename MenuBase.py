import MySQLdb

def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = MySQLdb.connect(
            db='',
            host='',
            user='',
            passwd=''
        )

        return conn
    except MySQLdb.Error as e:
        print(f'Erro na conexao ao MySQL Server: {e}')


def desconectar(conn):
    """
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()


def listar():
    """
    Função para listar estoque disponivel no sistema.
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM distribuicao')
    distribuicao = cursor.fetchall()

    if len(distribuicao) > 0:
        print('Listando Estoque...')
        print('--------------------')
        for distribuicao in distribuicao:
            print(f'ID: {distribuicao[0]}')
            print(f'Produto: {distribuicao[1]}')
            print(f'Categoria Do Produto: {distribuicao[2]}')
            print(f'Fornecedor: {distribuicao[3]}')
            print(f'Quantidade Disponivel: {distribuicao[4]}')
            print(f'Data De Entrada: {distribuicao[5]}')
            print('--------------------')

    else:
        print('Nao existem produtos cadastrados.')
    desconectar(conn)


def inserir():
    """
    Função para inserir Produtos ao Sistema.
    """
    conn = conectar()
    cursor = conn.cursor()

    produto = input('Informe o Produto que deseja inserir: ')
    categoria = input('Informe a Categoria do produto: ')
    fornecedor = input('Informe o Fornecedor: ')
    quantidade = int(input('Informe a Quantidade Disponivel: '))



    cursor.execute(f"INSERT INTO distribuicao (produto, categoria, fornecedor, quantidade) VALUES ('{produto}', '{categoria}', '{fornecedor}', {quantidade})")

    conn.commit()

    if cursor.rowcount == 1:
        print(f'O Produto {produto} foi cadastrado com sucesso!')
    else:
        print('Nao foi possivel inserir o produto.')
    desconectar(conn)

"""
Falta arrumar o def atualizar---------------
"""
def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    id = int(input('Informe o ID do produto: '))
    produto = input('Informe o Produto que deseja inserir: ')
    categoria = input('Informe a Categoria do produto: ')
    fornecedor = input('Informe o Fornecedor: ')
    quantidade = int(input('Informe a Quantidade Disponivel: '))

    cursor.execute(f"UPDATE distribuicao SET produto='{produto}', categoria'{categoria}', fornecedor'{fornecedor}', quantidade{quantidade} WHERE ID={id}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O Produto foi atualizado com sucesso!')
    else:
        print('Erro ao atualizar o produto')
        desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    id = int(input('Informe o codigo do produto: '))

    cursor.execute(f'DELETE FROM distribuicao WHERE id={id}')
    conn.commit()

    if cursor.rowcount == 1:
        print('Produto excluido com sucesso!')
    else:
        print(f'Erro ao excluir produto com id = {id}')
    desconectar(conn)

def consulta():
        """
        Função para gerar um relatorio sobre a ultima entrada dos fornecedores
        """

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT id, fornecedor, data_entrada FROM distribuicao;')
        distribuicao = cursor.fetchall()

        if len(distribuicao) > 0:
            print('Listando Fornecedores...')
            print('--------------------')
            for distribuicao in distribuicao:
                print(f'ID: {distribuicao[0]}')
                print(f'Fornecedor: {distribuicao[1]}')
                print(f'Ultima Entrada: {distribuicao[2]}')
                print('--------------------')


def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    print('5 - Consultar Fornecedores.')

    opcao = int(input())
    if opcao in [1, 2, 3, 4, 5]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        elif opcao == 5:
            consulta()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')


