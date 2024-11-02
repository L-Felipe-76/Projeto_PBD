from config.db import criar_conexao
from servicos.usuario_servicos import inserir_usuario, login

while True:
    print("1 - Cadastrar Usuário \n2 - Login")
    opc = input("Digite a opção desejada: ")
    
    if opc == '1':
        email = input("Digite o email: ")
        password = input("Digite a senha: ")
        inserir_usuario(email, password)
    elif opc == '2':
        email = input("Digite o email: ")
        password = input("Digite a senha: ")
        usuario_autenticado = login(email, password)
        if usuario_autenticado:
            print(f'Bem vindo {usuario_autenticado[1]}')
            break
        else:
            print("Usuário ou senha inválidos!")



