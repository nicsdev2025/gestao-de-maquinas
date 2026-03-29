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

#comandos para insetir os dados na tabela CREATE
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

# para atualizar os dados no banco
atualizar_tabela = input("Deseja fazer alguma alteração? s/n: ")
while atualizar_tabela == "s":
    maquina_id = input("Digite o ID da máquina que deseja atualizar: ")
    atualizar_usuario = input("Digite o nome do usuario: ")
    atualizar_patri = input("Digite o novo patrimonio: ")
    atualizar_hostname = input("Digite o novo hostname: ")
    atualizar_dia = input("digite o dia (AAAA-MM-DD):")
    cursor.execute('UPDATE maquinas SET usuario = %s, patrimonio = %s, hostname = %s, dia = %s WHERE id = %s', (atualizar_usuario, atualizar_patri, atualizar_hostname, atualizar_dia,maquina_id))
    conexao.commit()
    print("Máquina atualizada com sucesso!")
    if atualizar_tabela != "s" and atualizar_tabela == "n":
        break
    break
   
# para deletar as máquinas
delete_maquina = input("Deseja deletar alguma máquina?")
while delete_maquina == "s":
    deletar_maquina = input("Digite o ID para deletar a máquina: ")
    cursor.execute('DELETE FROM maquinas WHERE id = (%s)', (deletar_maquina,))
    conexao.commit()
    cursor.close()
    print("Máquina deletada com sucesso!")
    if delete_maquina != "s" and deletar_maquina == "n":
        break
    break

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