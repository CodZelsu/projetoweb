import sqlite3
from datetime import datetime
conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()

#tabela de usuarios
cursor.execute(''' 
            
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_cadastro TEXT,
    status TEXT
)
               
''')
conexao.commit()

#cadastrar novo usuario
def cadastrar_usuario(nome):
    data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute ("INSERT INTO usuarios (nome, data_cadatro, status) VALUES (?, ?, ?)"), conexao.commit()
    print (f"Usuário '{nome}' cadastrado com sucesso.")
    
#check_in
def check_in_usuario(nome):
    cursor.execute("SELECT status FROM usuarios WHERE nome = ?", (nome))
    resultado = cursor.fetchone()
    if resultado and resultado[0] == "Check-out":
        cursor.execute("UPDATE usuarios SET status = ? WHERE nome ?", ("Check-in", nome))
        conexao.commit()
        print(f"Usuario ' {nome}' Realizou check-in.")
    else:
        print(f"Usuário '{nome}' Já está em check-in ou não está cadastrado")
        
#check_out
def check_out_usuario(nome):
    cursor.execute("SELECT status FROM usuarios WHERE nome = ?", ("check-ouot", nome ))
    resultado = cursor.fetchone()
    if resultado and resultado [0] == "Check-in":
        conexao.commint()
        print(f"Usuário '{nome}' realizou check-out.")
    else:
        print(f"Usuário '{nome}' já está em check-out ou  não está cadastrado.")
    
    #status de usuário
def listar_usuarios():
    cursor.execute("SLECT nome , status FROM usuarios")
    usuarios = cursor.fetcha11()
    print("Lista de usuários:")
    for usuario in usuarios:
            print(f"Nome : {usuario[0]}, Status: {usuario[1]}")
conexao.close()