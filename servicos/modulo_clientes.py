from config.db import criar_conexao

def interface_clientes(opc):
    try:
        c = 0
        while c != 1:
            if(opc < 1 or opc > 5):
                print("Valor invalido, tente novamente!")
            
            elif(opc == 1):
                print('==========')
                nome = str(input("Digite o nome do cliente: "))
                email = str(input("Digite o email do cliente: "))
                cadastrar_cliente(nome, email)
            
            elif(opc == 2):
                print('==========')
                busca = str(input("Digite o nome ou email do cliente que deseja buscar: "))
                buscar_clientes(busca)
            
            elif(opc == 3):
                print('==========')
                busca = str(input("Digite o nome ou email do cliente que deseja buscar: "))
                buscar_clientes(busca)
                id = int(input("Digite o id do cliente que deseja alterar, caso nenhum cliente apareça digite 0 para cancelar: "))
                if (id == 0):
                    return(0)
                else:
                    nome = str(input("Digite o novo nome: "))
                    email = str(input("Digite o novo email: "))
                    alterar_clientes(id, nome, email)
            
            elif(opc == 4):
                print('==========')
                busca = str(input("Digite o nome ou email do cliente que deseja buscar: "))
                buscar_clientes(busca)
                id = int(input("Digite o id do cliente que deseja excluir, caso nenhum cliente apareça digite 0 para cancelar: "))
                if (id == 0):
                    return(0)
                else:
                    excluir_clientes(id)
            
            elif(opc == 5):
                return(0)
            
            print('==========')
            opc = int(input("Digite o que desejar gerenciar: \n1 - Cadastrar Cliente \n2 - Buscar Clientes \n3 - Alterar Clientes \n4 - Deletar Clientes \n5 - Voltar \nEscolha: "))
    
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)



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

def buscar_clientes(busca: str):
    try:
        print('==========')
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'SELECT * FROM clientes WHERE nome ILIKE %s or email ILIKE %s order by id_cliente'
        cursor.execute (sql, [f'%{busca}%', f'%{busca}%'])
        lista_clientes = cursor.fetchall()
        if (not lista_clientes):
            print("Nenhum cliente encontrado")
        for clientes in lista_clientes:
            print(f"{clientes[0]} - {clientes[1]} - {clientes[2]}")
        
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

    finally:
        conn.close()

def alterar_clientes(id: int, nome: str, email: str):
    try:
        print('==========')
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'UPDATE clientes SET nome = %s, email = %s WHERE id_cliente = %s'
        cursor.execute(sql, [nome, email, id])
        conn.commit()
        print("Cliente alterado com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

    finally:
        conn.close()

def excluir_clientes(id: int):
    try:
        print("==========")
        conn = criar_conexao()
        cursor = conn.cursor()
        sql1 = 'DELETE FROM pedidos WHERE id_cliente = %s'
        sql2 = 'DELETE FROM clientes WHERE id_cliente = %s'
        cursor.execute(sql1, [id, ])
        cursor.execute(sql2, [id, ])
        conn.commit()
        print("Cliente excluído com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

    finally:
        conn.close()