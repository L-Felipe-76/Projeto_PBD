from config.db import criar_conexao

def interface_produtos(opc):
    try:
        c = 0
        while c != 1:
            if(opc < 1 or opc > 5):
                print("Valor invalido, tente novamente!")
            
            elif(opc == 1):
                print('==========')
                nome = str(input("Digite o nome do produto: "))
                preco = float(input("Digite o preco do produto: "))
                cadastrar_produto(nome, preco)
            
            elif(opc == 2):
                print('==========')
                busca = str(input("Digite o nome do produto que deseja buscar: "))
                buscar_produtos(busca)
            
            elif(opc == 3):
                print('==========')
                busca = str(input("Digite o nome do produto que deseja buscar: "))
                buscar_produtos(busca)
                id = int(input("Digite o id do produto que deseja alterar, caso nenhum produto apareça digite 0 para cancelar: "))
                if (id == 0):
                    return(0)
                else:
                    nome = str(input("Digite o novo nome: "))
                    preco = float(input("Digite o novo preco: "))
                    alterar_produto(id, nome, preco)
            
            elif(opc == 4):
                print('==========')
                busca = str(input("Digite o nome do produto que deseja buscar: "))
                buscar_produtos(busca)
                id = int(input("Digite o id do produto que deseja excluir, caso nenhum produto apareça digite 0 para cancelar: "))
                if (id == 0):
                    return(0)
                else:
                    excluir_produto(id)
            
            elif(opc == 5):
                return(0)
            
            print('==========')
            opc = int(input("Digite o que desejar gerenciar: \n1 - Cadastrar Produtos \n2 - Buscar Produtos \n3 - Alterar Produtos \n4 - Deletar Produtos \n5 - Voltar \nEscolha: "))
            
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)



def cadastrar_produto(nome: str, preco: float):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = 'INSERT INTO produtos(nome, preco) VALUES (%s, %s)'
        cursor.execute(query, [nome, preco])
        conn.commit()
        print("Cadastro realizado com sucesso")  

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

    finally:
        conn.close()

def buscar_produtos(busca: str):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'SELECT * FROM produtos WHERE nome ILIKE %s'
        cursor.execute(sql, [f'%{busca}%', ])
        lista_produtos = cursor.fetchall()
        if (not lista_produtos ):
            print("Nenhum produto encontrado")
        for produtos in lista_produtos:
            print(f"{produtos[0]} - {produtos[1]} - {produtos[2]}")

    except Exception as e:
        print('===========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

    finally:
        conn.close()

def alterar_produto(id: int, nome: str, preco: float):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'UPDATE produtos set nome = %s, preco = %s  WHERE id_produto = %s'
        cursor.execute(sql, [nome, preco, id])
        conn.commit()
        print('produto alterado com sucesso')

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

    finally:
        conn.close()

def excluir_produto( id: int):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql1 = 'DELETE FROM pedidos WHERE id_produto = %s'
        sql2 = 'DELETE FROM produtos WHERE id_produto = %s'
        cursor.execute(sql1, [id, ])
        cursor.execute(sql2, [id, ])
        conn.commit()
        print('produto excluido com sucesso')

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)
    
    finally:
        conn.close()