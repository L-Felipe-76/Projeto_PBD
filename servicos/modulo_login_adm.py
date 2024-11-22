import pwinput
from config.db import criar_conexao
from servicos import modulo_login, modulo_pedidos

def inteface_logins(opc):
    try:
        CONTADOR = 0
        while CONTADOR != 1:
            if (opc < 1 or opc > 3):
                print('==========')
                print("Valor invalido, insira um valor valido")

            elif (opc == 1):
                print ("==========")
                usuario = str(input("Digite seu usuario: "))
                senha = str(pwinput.pwinput("Digite sua senha: "))
                local = modulo_login.cadastrar_login(usuario, senha)
            
            elif (opc == 2):
                print('==========')
                busca = str(input("Digite o usuario do login que deseja buscar: "))
                modulo_login.listar_logins(busca)
                id = int(input("Digite o id do login que deseja excluir, caso nenhum login apareça digite 0 para cancelar: "))
                if (id == 0):
                    return(0)
                elif (id == 1):
                    print('==========')
                    print("Impossivel apagar o login de administrador")
                else:
                    print('==========')
                    print("Excluindo pedidos relacionados ao login!")
                    modulo_pedidos.excluir_pedido(id, 1)
                    print('==========')
                    print("Excluindo login!")
                    modulo_login.excluir_login(id)
                

            elif (opc == 3):
                return 0
            
            print ("==========")
            opc = int(input("Digite o que deseja gerenciar \n1 - Cadastrar login \n2 - Excluir Login \n3 - Sair \nEscolha: "))
                
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)
    


