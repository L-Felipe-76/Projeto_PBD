from servicos import modulo_clientes

#Interface de conexão

try:
    n1 = str("oi")
    n2 = str(" Sumido")
    f = n1 + n2
    print(f)
        
except Exception as e:
    print ("==========")
    print("Valor invalido, tente novamente.")
    print(e)