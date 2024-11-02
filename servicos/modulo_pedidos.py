list_pedidos_id = []
list_pedidos_nomeCliente = []
list_pedidos_nomeProduto = []
list_pedidos_valor = []
list_pedidos_mesa = []

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
