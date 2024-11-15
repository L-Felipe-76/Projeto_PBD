import bcrypt
import pwinput
from config.db import criar_conexao
from servicos import moduloHaburgueria_Interface

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
                senha = str(pwinput.pwinput("Digite sua senha: "))
                cadastrar(usuario, senha)

            elif (opc == 2):
                    print('==========')
                    usuario = str(input("Digite seu usuario: "))
                    senha = str(pwinput.pwinput("Digite sua senha: "))
                    autenticacao = login(usuario, senha)
                    if autenticacao:
                        print('==========')
                        print(f'Bem vindo {autenticacao[1]}!')
                        usuariopassagem = autenticacao[0]
                        print('==========')
                        opc = int(input("Digite o que deseja gerenciar \n1 - Clientes \n2 - Produtos \n3 - Pedidos \n4 - Sair \nEscolha: "))
                        moduloHaburgueria_Interface.interface_hamburgueria(opc, usuariopassagem)
                    else:
                        print('==========')
                        print("Usuario ou senha invalidos! \nTente novamente")

            elif (opc == 3):
                print('==========')
                print("Programa encerrado")
                break
            
            print('==========')
            opc = int(input("O que deseja fazer? \n1 - Cadastrar \n2 - Login \n3 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))
            
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)



def criotpgrafar(password):
 password_bytes = password.encode('utf-8')
 salt = bcrypt.gensalt()
 hashed = bcrypt.hashpw(password_bytes, salt)
 return hashed

def checar_password(password, hashed):
 password_bytes = password.encode('utf-8')
 return bcrypt.checkpw(password_bytes, hashed)



def cadastrar(usuario: str, senha: str):
    try:
        hashed_password = criotpgrafar(senha)

        print('==========')
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'INSERT INTO logins(usuario, senha) VALUES (%s, %s)'
        cursor.execute(sql, [usuario, hashed_password])
        conn.commit()
        print("Cadastro realizado com sucesso")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)
    
    finally:
        conn.close()

def login(usuario: str, senha: str):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'SELECT * FROM logins WHERE usuario = %s'
        cursor.execute (sql, [usuario,])
        resultado = cursor.fetchone()
    
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)
    
    finally:
        conn.close()

    if resultado:
        senha_hash = resultado[2]        
        if isinstance(senha_hash, memoryview):
            senha_hash = bytes(senha_hash) 

        if checar_password(senha, senha_hash):
            return resultado 
    return False