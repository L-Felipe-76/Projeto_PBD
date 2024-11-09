from servicos import modulo_clientes

#Interface de conexão

try:
    print ("==========")
    modulo_clientes.listar_clientes()
        
except Exception as e:
    print ("==========")
    print("Valor invalido, tente novamente.")
    print(e)