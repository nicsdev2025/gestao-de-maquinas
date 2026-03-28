import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        
        password="2911",        
        database="controle_maquinas"
    )

conexao = get_connection()
cursor = conexao.cursor()

#comandos para o CREATE
maquina_usuario = input("digite seu RE:")
maquina_patri = input("digite o patrimônio:")
maquina_hostname = input("digite o HOSTNAME: ")
maquina_dia = input("digite o dia (AAAA-MM-DD): ")

cursor.execute("INSERT INTO maquinas (usuario, patrimonio, hostname, dia) VALUES (%s, %s, %s, %s)", (maquina_usuario, maquina_patri, maquina_hostname, maquina_dia))

conexao.commit()


# para ver os dados na tabela
cursor.execute("SELECT * FROM controle_maquinas.maquinas;")
resultado = cursor.fetchall()
print(resultado)
cursor.close()

verificacao = input("Você quer adicionar mais máquinas? s/n?: ")

while verificacao == "s":
    maquina_usuario = input("digite seu RE:")
    maquina_patri = input("digite o patrimônio:")
    maquina_hostname = input("digite o HOSTNAME: ")
    maquina_dia = input("digite o dia (AAAA-MM-DD): ")
    
    verificacao = input("Você quer adicionar mais máquinas? s/n?: ")

    if verificacao == "n":
        break
    elif verificacao != "s" and verificacao != "n":
        input("ERRO: digite s/n: ")