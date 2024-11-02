from config.db import criar_conexao

def inserir_usuario(email, password):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'INSERT INTO teste.usuarios (email, password) VALUES (%s, %s)'
        cursor.execute (sql, [email, password])
        conn.commit()
        print("Usuário Criado com sucesso")
    
    except Exception as e:
        print(e)
    
    finally:
        conn.close

def login(email, password):
    try:    
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = 'SELECT * FROM teste.usuarios WHERE email = %s AND password = %s'
        cursor.execute (sql, [email, password])
        return cursor.fetchone()
    
    except Exception as e:
        print(e)
    
    finally:
        conn.close