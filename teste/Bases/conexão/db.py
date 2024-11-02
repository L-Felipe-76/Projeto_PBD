import psycopg2

def criar_conexao():
    try:
        conn =  psycopg2.connect(
            dbname='FELIPE',
            user='postgres',
            password= 'post',
            host= 'localhost',
            port= '5432'
        )
        return conn
    except Exception as e:
        print (f"Erro ao conectar com O banco de dados:)")
        return None