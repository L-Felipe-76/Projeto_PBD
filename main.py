from utils import modulo_login
from utils import modulo_sistema_hamburgueria

#Interface de conexão
contador = 0
while contador == 0:
    try:
        print ("==========")
        opc = int(input("O que deseja fazer? \n1 - Cadastrar \n2 - Login \n3 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))
        conexao = str(modulo_login.interface_login(opc))
        if (conexao == "Conectado"):
            contador = 1
        elif(conexao == "Desligar"):
            contador = 1
    except Exception as e:
        print ("==========")
        print("Valor invalido, tente novamente.")
        print(e)

#Passagem para interface do sistema
    try:
        print ("==========")
        if (conexao == 'Conectado'):
            opc = int(input("O que deseja fazer? \n1 - Cadastrar Cliente \n2 - Listar Clientes \n3 - Alterar Cliente \n4 - Excluir Cliente \n5 - Cadastrar Produto \n6 - Listar Produtos \n7 - Alterar Produto \n8 - Excluir Produto \n9 - Cadastrar Pedido \n10 - Listar Pedidos \n11 - Alterar Pedido \n12 - Excluir Pedidos \n13 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))
            modulo_sistema_hamburgueria.interface_hamburgueria(opc)

    except Exception as e:
        print ("==========")
        print("Valor invalido, tente novamente.")
        print(e)