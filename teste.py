from servicos import modulo_clientes

#Interface de conexão

try:
    print ("==========")
    busca = '@g'
    modulo_clientes.listar_clientes(busca)
        
except Exception as e:
    print ("==========")
    print("Valor invalido, tente novamente.")
    print(e)