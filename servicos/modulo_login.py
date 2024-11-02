from config.db import criar_conexao

#Interface

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

            elif (opc == 2):
                    print('==========')
                    usuario = str(input("Digite seu usuario: "))
                    senha = str(input("Digite sua senha: "))
                    autenticacao = login(usuario, senha)
                    if autenticacao:
                        print('==========')
                        print(f'Bem vindo {autenticacao}!')
                    else:
                        print('==========')
                        print("Usuario ou senha invalidos! \nTente novamente")

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

#Serviços

def cadastrar(usuario: str, senha: str):
    try:
        print('==========')
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'INSERT INTO logins(usuario, senha) VALUES (%s, %s)'
        cursor.execute(sql, [usuario, senha])
        conn.commit()
        print("Cadastro realizado com sucesso")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)
    
    finally:
        conn.close

def login(usuario: str, senha: str):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'SELECT * FROM logins WHERE usuario = %s AND senha = %s'
        cursor.execute (sql, [usuario, senha])
        return cursor.fetchone()
    
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)
    
    finally:
        conn.close