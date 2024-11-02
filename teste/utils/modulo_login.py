list_users = ["Gerente01", "Funcionario01"]
list_password = ["Adm.Gerencia", "Adm.Funcionario"]


def interface_login(opc):
    try:
        contador = 1

        while contador != 0:
            if (opc <1 or opc > 3):
                print('==========')
                print("Valor invalido, insira um valor valido")
            


            if (opc == 1):
                print('==========')
                usuario = str(input("Digite seu usuario: "))
                senha = str(input("Digite sua senha: "))
                cadastrar(usuario, senha)
                print ("==========")

            elif (opc == 2):
                    print('==========')
                    usuario = str(input("Digite seu usuario: "))
                    senha = str(input("Digite sua senha: "))
                    teste = str(login(usuario, senha))
                    if (teste == '1'):
                        return ("Conectado")

            elif (opc == 3):
                print('==========')
                print("Programa encerrado")
                return ("Desligar")
            
            print('==========')
            opc = int(input("O que deseja fazer? \n1 - Cadastrar \n2 - Login \n3 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))
            
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)


def cadastrar(usuario: str, senha: str):
    try:
        print('==========')
        list_users.append(usuario)
        list_password.append(senha)
        print("Cadastro realizado com sucesso")
        

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def login(usuario: str, senha: str):
    contador = 0
    try:
        while contador <= len(list_users):
            if (contador == len(list_users)):
                print('==========')
                print("Usuario ou senha invalidos, favor tente novamente")
                return ('0')
            elif (usuario == list_users[contador] and senha == list_password[contador]):
                print('==========')
                print("Usuario conectado")
                return('1')
            else:
                contador += 1
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)