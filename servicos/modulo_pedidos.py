from config.db import criar_conexao
from servicos import modulo_clientes, modulo_produtos

def interface_pedidos(opc, usuario):
    try:
        cw = 0
        while cw != 1:
            if(opc < 1 or opc > 5):
                print("Valor invalido, tente novamente!")
            
            elif(opc == 1):
                print('==========')
                busca1 = str(input("Digite o nome do cliente a ser buscado: "))
                modulo_clientes.buscar_clientes(busca1)
                id_cliente = int(input("Digite o id do cliente que realizou o pedido, caso nenhum cliente apareça digite 0 para cancelar: "))
                if (id_cliente == 0):
                    return(0)
                else:
                    pass

                print('==========')
                busca2 = str(input("Digite o nome do produto a ser buscado: "))
                modulo_produtos.buscar_produtos(busca2)
                id_produto = int(input("Digite o id do produto pedido, caso nenhum produto apareça digite 0 para cancelar: "))
                if (id_produto == 0):
                    return(0)
                else:
                    pass
                
                valor_total = buscar_valor(id_produto)

                print('==========')
                c = 0
                while c != 1:
                    mesa1 = int(input("Digite em quais das seguintes mesas (01, 02, 03, 04, 05) o pedido será entregue: "))
                    if (mesa1 < 1 or mesa1 > 5):
                        print("Valor inválido, favor digite uma mesa existente!")
                    else:
                        mesa = mesa1
                        c = 1
                
                print('==========')
                c1 = 0
                while c1 != 1:
                    dia_str = str(input("Digite o dia do pedido: "))
                    mes_str = str(input("Digite o mês do pedido: "))
                    ano_str = str(input("Digite o ano do pedido: "))
                    dia = int(dia_str)
                    mes = int(mes_str)
                    ano = int(ano_str)

                    if(dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 2020):
                        print("Dia, mês ou ano incorretos, favor digite datas válidas!")
                    else:
                        data_pedido = str(ano_str+mes_str+dia_str)
                        c1 = 1
                
                print('==========')
                c2 = 0
                while c2 != 1:
                    hora_str = str(input("Digite a hora em que o pedido foi feito: "))
                    minutos_str = str(input("Digite o minuto em que o pedido foi feito: "))
                    hora = int(hora_str)
                    minutos = int(minutos_str)

                    if(hora < 0 or hora > 23 or minutos < 0 or minutos > 59):
                        print("Horário inválido, favor digite um horário válido!")
                    else:
                        hora_pedido = str(hora_str+minutos_str)
                        c2 = 1
                
                cadastrar_pedido(usuario, id_cliente, id_produto, valor_total, mesa, hora_pedido, data_pedido)
            
            elif(opc == 2):
                print('==========')
                busca = str(input("Digite o nome do cliente que realizou o pedido: "))
                buscar_pedido(busca, usuario)
            
            elif(opc == 3):
                print('==========')
                busca = str(input("Digite o nome do cliente a ser alterado que realizou o pedido: "))
                buscar_pedido(busca, usuario)
                id = int(input("Digite o id do pedido que deseja alterar, caso nenhum pedido apareça digite 0 para cancelar: "))
                if (id == 0):
                    return(0)
                else:
                    busca1 = str(input("Digite o nome do novo cliente a ser buscado: "))
                    modulo_clientes.buscar_clientes(busca1)
                    id_cliente = int(input("Digite o novo id do cliente que realizou o pedido: "))

                    print('==========')
                    busca2 = str(input("Digite o nome do produto a ser buscado: "))
                    modulo_produtos.buscar_produtos(busca2)
                    id_produto = int(input("Digite o novo id do produto pedido: "))
                    
                    valor_total = buscar_valor(id_produto)

                    print('==========')
                    c = 0
                    while c != 1:
                        mesa1 = int(input("Digite em quais das seguintes mesas (01, 02, 03, 04, 05) o pedido será entregue: "))
                        if (mesa1 < 1 or mesa1 > 5):
                            print("Valor inválido, favor digite uma mesa existente!")
                        else:
                            mesa = mesa1
                            c = 1
                    
                    print('==========')
                    c1 = 0
                    while c1 != 1:
                        dia_str = str(input("Digite o dia do pedido: "))
                        mes_str = str(input("Digite o mês do pedido: "))
                        ano_str = str(input("Digite o ano do pedido: "))
                        dia = int(dia_str)
                        mes = int(mes_str)
                        ano = int(ano_str)

                        if(dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 2020):
                            print("Dia, mês ou ano incorretos, favor digite datas válidas!")
                        else:
                            data_pedido = str(ano_str+mes_str+dia_str)
                            c1 = 1
                    
                    print('==========')
                    c2 = 0
                    while c2 != 1:
                        hora_str = str(input("Digite a hora em que o pedido foi feito: "))
                        minutos_str = str(input("Digite o minuto em que o pedido foi feito: "))
                        hora = int(hora_str)
                        minutos = int(minutos_str)

                        if(hora < 0 or hora > 23 or minutos < 0 or minutos > 59):
                            print("Horário inválido, favor digite um horário válido!")
                        else:
                            hora_pedido = str(hora_str+minutos_str)
                            c2 = 1
                            alterar_pedido(id, usuario, id_cliente, id_produto, valor_total, mesa, data_pedido, hora_pedido)
            
            elif(opc == 4):
                print('==========')
                busca = str(input("Digite o nome do cliente que realizou o pedido: "))
                buscar_pedido(busca, usuario)
                id = int(input("Digite o id do pedido que deseja excluir, caso nenhum pedido apareça digite 0 para cancelar: "))
                if (id == 0):
                    return(0)
                else:
                    excluir_pedido(id, usuario)
            
            elif(opc == 5):
                return(0)
            
            print('==========')
            opc = int(input("Digite o que desejar gerenciar: \n1 - Cadastrar Pedidos \n2 - Buscar Pedidos \n3 - Alterar Pedidos \n4 - Deletar Pedidos \n5 - Voltar \nEscolha: "))
            
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)




def cadastrar_pedido(usuario, id_cliente: str, id_produto: str, valor_total: float, mesa: int, hora_pedido: str, data_pedido: str):
     
    try:
        print('==========')
        conn = criar_conexao()
        cursor = conn.cursor()
        query = 'INSERT INTO pedidos(id_login, id_cliente, id_produto, valor_total, mesa, hora_pedido, data_pedido) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(query, [usuario, id_cliente, id_produto, valor_total, mesa, hora_pedido, data_pedido])
        conn.commit()
        print("Cadastro realizado com sucesso")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)
    
    finally:
        conn.close()

def buscar_pedido(busca: str, usuario):
    try:
        print('==========')
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'SELECT p.id_pedido, c.nome, p2.nome, p.mesa, p.valor_total, p.data_pedido, p.hora_pedido FROM pedidos p INNER JOIN clientes c on p.id_cliente = c.id_cliente INNER JOIN produtos p2 on p.id_produto = p2.id_produto WHERE c.nome ILIKE %s AND p.id_login = %s ORDER BY p.id_pedido'
        sql1 = 'SELECT p.id_pedido, c.nome, p2.nome, p.mesa, p.valor_total, p.data_pedido, p.hora_pedido FROM pedidos p INNER JOIN clientes c on p.id_cliente = c.id_cliente INNER JOIN produtos p2 on p.id_produto = p2.id_produto WHERE c.nome ILIKE %s ORDER BY p.id_pedido'
        if(usuario != 1):
            cursor.execute (sql, [f'%{busca}%', usuario])
        else:
            cursor.execute (sql1, [f'%{busca}%', ])
        lista_pedidos = cursor.fetchall()
        if (not lista_pedidos):
            print("Nenhum pedido encontrado")
        for pedidos in lista_pedidos:
            print(f"{pedidos[0]} - {pedidos[1]} - {pedidos[2]} - {pedidos[3]} - {pedidos[4]} - {pedidos[5]} - {pedidos[6]}")
        
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

    finally:
        conn.close()

def alterar_pedido(id: int, usuario: str, id_cliente: str, id_produto: str, valor_total: float, mesa: int, data_pedido: str, hora_pedido: str):
    try:
        print("==========")
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'UPDATE pedidos SET id_cliente = %s, id_produto = %s, valor_total = %s, mesa = %s, data_pedido = %s, hora_pedido = %s WHERE id_pedido = %s AND id_login = %s'
        cursor.execute(sql, [id_cliente, id_produto, valor_total, mesa, data_pedido, hora_pedido, id, usuario])
        conn.commit()
        print("Pedido alterado com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def excluir_pedido(id: int, usuario):
    try:
        print("==========")
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'DELETE FROM pedidos WHERE id_pedido = %s AND id_login = %s'
        sql1 = 'DELETE FROM pedidos WHERE id_login = %s'
        if(usuario != 1):
            cursor.execute(sql, [id, usuario])
        else:
            cursor.execute (sql1, [id, ])
        conn.commit()
        print("Pedido excluído com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def buscar_valor(id_produto):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'SELECT preco FROM produtos WHERE id_produto = %s'
        cursor.execute (sql, [id_produto, ])
        valor_total = cursor.fetchone()
        return(valor_total)
        
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

    finally:
        conn.close()

