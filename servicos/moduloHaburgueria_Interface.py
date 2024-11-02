from servicos import modulo_clientes, modulo_produtos, modulo_pedidos

def interface_hamburgueria(opc: int):
    try:
        CONTADOR = 0
        while CONTADOR != 1:
            if (opc < 0 or opc > 3):
                print('==========')
                print("Valor invalido, insira um valor valido")

            elif (opc == 1):
                #chamar modulo de clientes
                pass
            
            elif (opc == 2):
                #chamar modulo de produtos
                pass
            
            elif (opc == 3):
                #chamar modulo de pedidos
                pass

            elif (opc == 0):
                #voltar
                return 0
            
            opc = int(input(""))

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)