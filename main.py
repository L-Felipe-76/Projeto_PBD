from servicos import modulo_login

#Interface de conexão
try:
   print ("==========")
   opc = int(input("O que deseja fazer? \n1 - Login \n2 - Encerrar \n\nDigite o numero correspondente a sua escolha: "))
   modulo_login.interface_login(opc)
         
except Exception as e:
   print ("==========")
   print("Valor invalido, tente novamente.")
   print(e)