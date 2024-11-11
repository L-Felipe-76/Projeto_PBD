from config.db import criar_conexao

def interface_clientes(opc):
    c = 0
    while c != 1:
        if(opc < 1 or opc > 5):
            print("Valor invalido, tente novamente!")
        elif(opc == 1):
            pass
        elif(opc == 2):
            pass
        elif(opc == 3):
            pass
        elif(opc == 4):
            pass
        elif(opc == 5):
            return(0)
        opc = int(input("Digite o que desejar gerenciar: 1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Clientes \n4 - Deletar Clientes \n5 - Voltar"))



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
    
    finally:
        conn.close()

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

    finally:
        conn.close()

def alterar_clientes(escolha: int, nome: str, email: str):
    try:
        print('==========')
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'update clientes set nome = %s, email = %s where id_cliente = %s'
        cursor.execute(sql, [nome, email, escolha])
        conn.commit()
        print("Cliente alterado com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

    finally:
        conn.close()

def excluir_clientes(escolha: int):
    try:
        print("==========")
        conn = criar_conexao()
        cursor = conn.cursor()
        sql1 = 'delete from pedidos where id_cliente = %s'
        sql2 = 'delete from clientes where id_cliente = %s'
        cursor.execute(sql1, [escolha, ])
        cursor.execute(sql2, [escolha, ])
        conn.commit()
        print("Cliente excluído com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

    finally:
        conn.close()