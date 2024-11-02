list_clientes_id = [1]
list_clientes_nomes = ['Roberto']
list_clientes_email = ['Roberto@gmail.com']

def cadastrar_cliente(nome: str, email:str):
    try:
        print('==========')
        list_clientes_id.append(len(list_clientes_id) + 1)
        list_clientes_nomes.append(nome)
        list_clientes_email.append(email)
        print("Cadastro realizado com sucesso")
    
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def listar_clientes():
    try:
        print('==========')
        contador1 = 0
        while contador1 < (len(list_clientes_id)):
            if (list_clientes_id[contador1] >= 1):
                print(f"Id: {list_clientes_id[contador1]} - Nome: {list_clientes_nomes[contador1]} - Email: {list_clientes_email[contador1]}")
                contador1 += 1
            else:
                contador1 += 1

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def alterar_clientes(escolha: int, nome: str, email: str):
    try:
        print("==========")
        list_clientes_nomes[escolha] = nome
        list_clientes_email[escolha] = email
        print("Cliente alterado com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def excluir_clientes():
    try:
        listar_clientes()
        print("==========")
        escolha = (int(input("Digite o id do cliente a ser deletado: "))) - 1
        c = 0
        while c != 1:
            if (escolha < 0 or escolha > len(list_clientes_id)):
                print('==========')
                print("Valor invalido, insira um valor valido")
                print('==========')
                escolha = (int(input("Digite o id do cliente a ser deletado: "))) - 1
            else:
                c = 1
        list_clientes_id[escolha] = - 1
        list_clientes_nomes[escolha] = 'null'
        list_clientes_email[escolha] = 'null'
        print("Cliente excluído com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)