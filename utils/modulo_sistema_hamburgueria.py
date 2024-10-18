list_clientes_id = [1]
list_clientes_nomes = ['Roberto']
list_clientes_email = ['Roberto@gmail.com']
list_produtos_id = []
list_produtos_nomes = []
list_produtos_preco = []
list_pedidos_id = []
list_pedidos_nomeCliente = []
list_pedidos_nomeProduto = []
list_pedidos_valor = []
list_pedidos_mesa = []

#Interface

def interface_hamburgueria(opc):
    try:
        contador = 0
        
        while contador != 1:
            contador2 = 0
            while contador2 != 1:
                if (opc < 1 or opc > 13):
                    print('==========')
                    print("Valor invalido, insira um valor valido")
                    print('==========')
                    opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))
                else:
                    contador2 = 1
            
            if (opc == 1):
                print('==========')
                nome = str(input("Digite o nome do cliente: "))
                email = str(input("Digite o email do cliente: "))
                cadastrar_cliente(nome, email)
                print('==========')
                opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))
            
            elif (opc == 2):
                listar_clientes()
                print('==========')
                opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))
            
            elif(opc == 3):
                listar_clientes()
                print("==========")
                escolha = (int(input("Digite o id do cliente a ser alterado: "))) - 1
                c = 0
                while c != 1:
                    if (escolha < 0 or escolha > len(list_clientes_id)):
                        print('==========')
                        print("Valor invalido, insira um valor valido")
                        print('==========')
                        escolha = (int(input("Digite o id do cliente a ser alterado: "))) - 1
                    else:
                        c = 1
                print("==========")
                nome = str(input("Digite o novo nome: "))
                email = str(input("Digite o novo email: "))
                alterar_clientes(escolha, nome, email)
                print("==========")
                opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))

            elif (opc == 4):
                excluir_clientes()
                print("==========")
                opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))

            #Produtos

            elif (opc == 5):
                print('==========')
                nome = str(input("Digite o nome do produto: "))
                preco = float(input("Digite o preço do produto: "))
                cadastrar_produto(nome, preco)
                print('==========')
                opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))
            
            elif (opc == 6):
                listar_produtos()
                print('==========')
                opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))
            
            elif (opc == 7):
                listar_produtos()
                print("==========")
                escolha = (int(input("Digite o id do produto a ser alterado: "))) - 1
                c = 0
                while c != 1:
                    if (escolha < 0 or escolha > len(list_produtos_id)):
                        print('==========')
                        print("Valor invalido, insira um valor valido")
                        print('==========')
                        escolha = (int(input("Digite o id do produto a ser alterado: "))) - 1
                    else:
                        c = 1
                print("==========")
                nome = str(input("Digite o novo nome: "))
                preco = float(input("Digite o novo preço: "))
                alterar_produtos(escolha, nome, preco)
                print("==========")
                opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))

            elif (opc == 8):
                excluir_produtos()
                print("==========")
                opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))

            #Pedidos

            elif (opc == 9):
                listar_clientes()
                cliente = int(input("Digite o id do cliente que realizou o pedido: "))
                contador91 = 0
                while contador91 != 1:
                    if (cliente > len(list_clientes_id) or cliente < 0):
                        print("==========")
                        print("Valor invalido, digite um valor valido")
                        cliente = int(input("Digite o id do cliente que realizou o pedido: "))
                    else:
                        contador91 = 1
                nome_cliente = list_clientes_nomes[cliente - 1]
                listar_produtos()
                produto = int(input("Digite o id do produto: "))
                contador92 = 0
                while contador92 != 1:
                    if (produto > len(list_produtos_id) or produto < 0):
                        print("==========")
                        print("Valor invalido, digite um valor valido")
                        produto = int(input("Digite o id do produto: "))
                    else:
                        contador92 = 1
                nome_produto = list_produtos_nomes[produto - 1]
                print('==========')
                valor = list_produtos_preco[produto - 1]
                print("Mesas: 01, 02, 03, 04, 05")
                mesat = int(input("Digite o numero da mesa: "))
                c = 0
                while c != 1:
                    if (mesat > 0 and mesat < 6):
                        c = 1
                    else:
                        print('==========')
                        print("Valor invalido")
                        print("Mesas: 01, 02, 03, 04, 05")
                        mesat = int(input("Digite o numero da mesa: "))
                mesa1 = mesat
                cadastrar_pedidos(nome_cliente, nome_produto, valor, mesa1)
                opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))

            elif (opc == 10):
                listar_pedidos()
                print('==========')
                opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))
            
            elif (opc == 11):
                listar_pedidos()
                print("==========")
                escolha = (int(input("Digite o id do pedido a ser alterado: "))) - 1
                c = 0
                while c != 1:
                    if (escolha < 0 or escolha > len(list_pedidos_id)):
                        print('==========')
                        print("Valor invalido, insira um valor valido")
                        print('==========')
                        escolha = (int(input("Digite o id do pedido a ser alterado: "))) - 1
                    else:
                        c = 1
                print("==========")
                listar_clientes()
                cliente = int(input("Digite o id do novo cliente: "))
                contador91 = 0
                while contador91 != 1:
                    if (cliente > len(list_clientes_id) or cliente < 0):
                        print("==========")
                        print("Valor invalido, digite um valor valido")
                        cliente = int(input("Digite o id do novo cliente: "))
                    else:
                        contador91 = 1
                nome_cliente = list_clientes_nomes[cliente - 1]
                listar_produtos()
                produto = int(input("Digite o id do novo produto: "))
                contador92 = 0
                while contador92 != 1:
                    if (produto > len(list_produtos_id) or produto < 0):
                        print("==========")
                        print("Valor invalido, digite um valor valido")
                        produto = int(input("Digite o id do novo produto: "))
                    else:
                        contador92 = 1
                nome_produto = list_produtos_nomes[produto - 1]
                print('==========')
                valor = list_produtos_preco[produto - 1]
                print("Mesas: 01, 02, 03, 04, 05")
                mesat = int(input("Digite o novo numero da mesa: "))
                c = 0
                while c != 1:
                    if (mesat > 0 and mesat < 6):
                        c = 1
                    else:
                        print('==========')
                        print("Valor invalido")
                        print("Mesas: 01, 02, 03, 04, 05")
                        mesat = int(input("Digite o novo numero da mesa: "))
                mesa1 = mesat
                alterar_pedido(escolha, nome_cliente, nome_produto, valor, mesa1)
                print("==========")
                opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))

            elif (opc == 12):
                excluir_pedidos()
                print("==========")
                opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))

            #Encerramento

            elif (opc == 13):
                print("Programa encerrado! Volte sempre...")
                break

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

# Clientes

def cadastrar_cliente(nome: str, email:str):
    try:
        print('==========')
        list_clientes_id.append(len(list_clientes_id) + 1)
        list_clientes_nomes.append(nome)
        list_clientes_email.append(email)
        print("Cadastro realizado com sucesso")
    
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def listar_clientes():
    try:
        print('==========')
        contador1 = 0
        while contador1 < (len(list_clientes_id)):
            if (list_clientes_id[contador1] >= 1):
                print(f"Id: {list_clientes_id[contador1]} - Nome: {list_clientes_nomes[contador1]} - Email: {list_clientes_email[contador1]}")
                contador1 += 1
            else:
                contador1 += 1

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def alterar_clientes(escolha: int, nome: str, email: str):
    try:
        print("==========")
        list_clientes_nomes[escolha] = nome
        list_clientes_email[escolha] = email
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

# Produtos

def cadastrar_produto(nome: str, preco: float):
    try:
        print('==========')
        list_produtos_id.append(len(list_produtos_id) + 1)
        list_produtos_nomes.append(nome)
        list_produtos_preco.append(preco)
        print("Cadastro realizado com sucesso")
    
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def listar_produtos():
    try:
        print('==========')
        contador1 = 0
        while contador1 < (len(list_produtos_id)):
            if (list_produtos_id[contador1] >= 1):
                print(f"Id: {list_produtos_id[contador1]} - Nome: {list_produtos_nomes[contador1]} - preco: {list_produtos_preco[contador1]}")
                contador1 += 1
            else:
                contador1 += 1
    
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def alterar_produtos(escolha: int, nome: str, preco: float):
    try:
        print("==========")
        list_produtos_nomes[escolha] = nome
        list_produtos_preco[escolha] = preco
        print("Produto alterado com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def excluir_produtos():
    try:
        listar_produtos()
        print("==========")
        escolha = (int(input("Digite o id do produto a ser deletado: "))) - 1
        c = 0
        while c != 1:
            if (escolha < 0 or escolha > len(list_produtos_id)):
                print('==========')
                print("Valor invalido, insira um valor valido")
                print('==========')
                escolha = (int(input("Digite o id do produto a ser deletado: "))) - 1
            else:
                c = 1
        list_produtos_id[escolha] = - 1
        list_produtos_nomes[escolha] = 'null'
        list_produtos_preco[escolha] = 'null'
        print("Produto excluído com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

# Pedidos

def cadastrar_pedidos(nome_cliente: str, nome_produto: str, valor: float, mesa: int):
    try:
        print('==========')
        list_pedidos_id.append(len(list_pedidos_id) + 1)
        list_pedidos_nomeCliente.append(nome_cliente)
        list_pedidos_nomeProduto.append(nome_produto)
        list_pedidos_valor.append(valor)
        list_pedidos_mesa.append(mesa)
        print("Cadastro realizado com sucesso")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def listar_pedidos():
    try:
        print('==========')
        contador1 = 0
        while contador1 < (len(list_pedidos_id)):
            if (list_pedidos_id[contador1] >= 1):
                print(f"Id: {list_pedidos_id[contador1]} - Nome Cliente: {list_pedidos_nomeCliente[contador1]} - Produtos: {list_pedidos_nomeProduto[contador1]} - Valor Total: R${list_pedidos_valor[contador1]} - Mesa: {list_pedidos_mesa[contador1]}")
                contador1 += 1
            else:
                contador1 += 1
    
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def alterar_pedido(escolha: int, nome_cliente: str, nome_produto: str, valor: float, mesa: int):
    try:
        print("==========")
        list_pedidos_nomeCliente[escolha] = nome_cliente
        list_pedidos_nomeProduto[escolha] = nome_produto
        list_pedidos_valor[escolha] = valor
        list_pedidos_mesa[escolha] = mesa
        print("Pedido alterado com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def excluir_pedidos():
    try:
        listar_pedidos()
        print("==========")
        escolha = (int(input("Digite o id do pedido a ser deletado: "))) - 1
        c = 0
        while c != 1:
            if (escolha < 0 or escolha > len(list_pedidos_id)):
                print('==========')
                print("Valor invalido, insira um valor valido")
                print('==========')
                escolha = (int(input("Digite o id do pedido a ser deletado: "))) - 1
            else:
                c = 1
        list_pedidos_id[escolha] = - 1
        list_pedidos_nomeCliente[escolha] = 'null'
        list_pedidos_nomeProduto[escolha] = 'null'
        list_pedidos_valor[escolha] = 'null'
        list_pedidos_mesa[escolha] = 'null'
        print("Pedido excluído com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)
