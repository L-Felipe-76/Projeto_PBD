list_produtos_id = []
list_produtos_nomes = []
list_produtos_preco = []

def cadastrar_produto(nome: str, preco: float):
    try:
        print('==========')
        list_produtos_id.append(len(list_produtos_id) + 1)
        list_produtos_nomes.append(nome)
        list_produtos_preco.append(preco)
        print("Cadastro realizado com sucesso")
    
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def listar_produtos():
    try:
        print('==========')
        contador1 = 0
        while contador1 < (len(list_produtos_id)):
            if (list_produtos_id[contador1] >= 1):
                print(f"Id: {list_produtos_id[contador1]} - Nome: {list_produtos_nomes[contador1]} - preco: {list_produtos_preco[contador1]}")
                contador1 += 1
            else:
                contador1 += 1
    
    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def alterar_produtos(escolha: int, nome: str, preco: float):
    try:
        print("==========")
        list_produtos_nomes[escolha] = nome
        list_produtos_preco[escolha] = preco
        print("Produto alterado com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)

def excluir_produtos():
    try:
        listar_produtos()
        print("==========")
        escolha = (int(input("Digite o id do produto a ser deletado: "))) - 1
        c = 0
        while c != 1:
            if (escolha < 0 or escolha > len(list_produtos_id)):
                print('==========')
                print("Valor invalido, insira um valor valido")
                print('==========')
                escolha = (int(input("Digite o id do produto a ser deletado: "))) - 1
            else:
                c = 1
        list_produtos_id[escolha] = - 1
        list_produtos_nomes[escolha] = 'null'
        list_produtos_preco[escolha] = 'null'
        print("Produto excluído com sucesso!")

    except Exception as e:
        print('==========')
        print('Erro, verificando bug... tente novamente!')
        print(e)