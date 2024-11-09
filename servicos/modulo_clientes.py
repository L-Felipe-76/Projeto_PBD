from config.db import criar_conexao

def interface_clientes(opc):
    pass



def cadastrar_cliente(nome: str, email:str):
    try:
        print('==========')
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'INSERT INTO clientes(nome, email) VALUES (%s, %s)'
        cursor.execute(sql, [nome, email])
        conn.commit()
        print("Cadastro realizado com sucesso")
    
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def listar_clientes():
    try:
        print('==========')
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'SELECT * FROM clientes'
        cursor.execute (sql)
        lista_clientes = cursor.fetchall()
        for clientes in lista_clientes:
            print(f"{clientes[0]} - {clientes[1]} - {clientes[2]}")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def alterar_clientes(escolha: int, nome: str, email: str):
    try:
        print("==========")
        listar_clientes()
        
        print("Cliente alterado com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def excluir_clientes():
    try:
        listar_clientes()
        print("==========")
        escolha = (int(input("Digite o id do cliente a ser deletado: "))) - 1
        c = 0
        while c != 1:
            if (escolha < 0 or escolha > len(list_clientes_id)):
                print('==========')
                print("Valor invalido, insira um valor valido")
                print('==========')
                escolha = (int(input("Digite o id do cliente a ser deletado: "))) - 1
            else:
                c = 1
        list_clientes_id[escolha] = - 1
        list_clientes_nomes[escolha] = 'null'
        list_clientes_email[escolha] = 'null'
        print("Cliente excluído com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)