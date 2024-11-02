import psycopg2

def criar_conexao():
   try:
        conn = psycopg2.connect(
            dbname='Hamburgueria',
            user='postgres',
            password= 'post',
            host= 'localhost',
            port= '5432'
       )
        return conn
   except Exception as e:
       print(f"Erro ao conectar com o banco de dados: {e}")
       return None
   
   