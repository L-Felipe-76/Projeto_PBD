from servicos import modulo_clientes, modulo_produtos, modulo_pedidos

def interface_hamburgueria(opc: int):
    try:
        CONTADOR = 0
        while CONTADOR != 1:
            if (opc < 1 or opc > 4):
                print('==========')
                print("Valor invalido, insira um valor valido")

            elif (opc == 1):
                print ("==========")
                opc2 = int(input("Digite o que desejar fazer: \n1 - Cadastrar Cliente \n2 - Buscar Clientes \n3 - Alterar Clientes \n4 - Excluir Clientes \n5 - Voltar \nEscolha: "))
                local = modulo_clientes.interface_clientes(opc2)
            
            elif (opc == 2):
                print ("==========")
                opc2 = int(input("Digite o que desejar gerenciar: \n1 - Cadastrar Produtos \n2 - Buscar Produtos \n3 - Alterar Produtos \n4 - Deletar Produtos \n5 - Voltar \nEscolha: "))
                local = modulo_produtos.interface_produtos(opc2)
            
            elif (opc == 3):
                print ("==========")
                #chamar modulo de pedidos
                pass

            elif (opc == 4):
                #voltar
                return 0
            
            print ("==========")
            opc = int(input("Digite o que deseja gerenciar \n1 - Clientes \n2 - Produtos \n3 - Pedidos \n4 - Sair \nEscolha: "))

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)