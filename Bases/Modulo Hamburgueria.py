def listar_clientes():
    for cliente in listar_clientes:
        print(f"{cliente('id_cliente')} - Nome:{cliente('none')}, email: {cliente('email')}")


def cadastrar_clientes():
    adicionar = 'sim'

    while adicionar == 'sim':
        nome = input('digite o  nome cliente:')
        email = input('digite o email do cliente:')
        listar_clientes.append({'none': nome, 'email': email, 'id_cliente': len(listar_clientes) + 1})


        adicionar = input("deseja adcionar mais clientes: (sim ou não)")

        if adicionar.lower == 'não':
            break

def listar_produtos():
        for produtos in listar_produtos:
            print(f"{produtos('id_produto')} - Nome_produto:{produtos('none')}, preco: {produtos('preço')}")


def cadastrar_produtos():
    adicionar_produtos = 'sim'

    while adicionar_produtos == 'sim':
        nome_produtos = input('digite o  nome do produto:')
        preco = float(input('digite o valor do produto:'))
        listar_produtos.append({'none': nome_produtos, 'preço': preco, 'id_produto': len(listar_produtos) + 1})
        
        adicionar_produtos = input("deseja adcionar mais produtos: (sim ou não)")

        if adicionar_produtos.lower == 'não':
            break

def listar_pedidos():
        for pedidos in listar_pedidos:
            print(f"{pedidos('id_pedido')} - mesa:{pedidos('mesa')}, valor_total: {pedidos('valor_total')}, hora_pedidos: {pedidos('hora_pedidos')}, data_pedidos:{pedidos('data_pedidos')}")


def cadastrar_pedidos():

    while adicionar_pedidos == 'sim':
        Valor_total = float(input('digite o valor total do pedido:'))
        mesa = int(input('digite a mesa do cliente:'))
        hora_pedido = input('digite a hora do pedido:')
        data_pedido = input('digite a data do pedido:')
        listar_pedidos.append(f"{'none': Valor_total, 'mesa': mesa, 'hora_pedido': hora_pedido, 'data_pedido': data_pedido  'id_pedido': len(listar_pedidos) + 1}")
        
        adicionar_pedidos = input("deseja adcionar mais pedidos: (sim ou não)")

        if adicionar_pedidos.lower == 'não':
            break

        