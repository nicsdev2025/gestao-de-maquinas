import psycopg2

hostname = 'localhost'
database = 'gestao_de_maquinas'
username = 'postgres'
pwd = '2911'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id,

       
    )
    cur = conn.cursor()

except Exception as erro:
    print(f"Não foi possivel fazer a conexão com o Postgres por conta do: {erro}")
    exit()



class Maquina:
    def __init__(self):
        self.usuario = None
        self.patrimonio = None
        self.hostname = None
        self.dia = None


    def adicionar_maquina(self):
        adicionar = input('Você deseja adicionar algum desktop no banco de dados? s/n: ')
        if adicionar == 's':
            add_user = input('Digite o seu NOME ou RE: ')
            while add_user == "":
                print('Você precisa digitar o seu Nome ou RE!')
                add_user = input('Digite o seu NOME ou RE: ')
            add_patri = input('Digite o Patrimônio do desktop: ')
            while add_patri == "":
                print('Você precisa digitar o Patrimônio do desktop!')
                add_patri = input("Digite o patrimônio do desktop: ")
            add_host = input('Digite o Hostname do desktop:')
            while add_host == "":
                print('Você precisa digitar o HOSTNAME do desktop!')
                add_host = input('Digite o Hostname do desktop:')
            add_data = input("Digite a data: ")
            while add_data == "":
                print('Você precisa digitar a Data!')
                add_data = input("Digite a data: ")

            cur.execute('INSERT INTO maquinas(usuario, patrimonio, hostname, dia) VALUES(%s, %s, %s, %s)', (add_user, add_patri, add_host, add_data))
            print(self.ver_tabela())
            print("Desktop adicionado com sucesso :)")


    def ver_tabela(self):
        verTabela = 's'
        verTabela = input("Deseja ver os dados da tabela? s/n: ")
        if verTabela != 's':
            return

        while verTabela == 's':
            cur.execute("SELECT * FROM maquinas;")
            resultado = cur.fetchall()
            break
        for linha in resultado:
            print(f'ID: {linha[0]} | Usuário: {linha[1]} ! Patrimônio: {linha[2]} | Hostname: {linha[3]} | Data: {linha[4]}')

    
    def atualizar_tabela(self):
        atualizacao = input("Você deseja atualizar algum DADO na tabela? s/n: ")
        if atualizacao == 's':
            print(self.ver_tabela())

            escolha = input('Digite as opções que você queira ATUALIZAR: (U - Usuário)|(H - hostname)|(D - data) - ')
            verifica = input('Digite o ID para alterar: ')
            while verifica == "":
                print("Você precisar digitar o ID para poder atualizar a tabela!")
                verifica = input('Digite o ID para alterar: ')

            if escolha == 'U' or 'u':
                novo_user = input('Digite o novo usuário: ')
                while novo_user == "":
                    print("Você precisa digitar NOME ou seu RE!")
                    novo_user = input("digite seu Nome/RE:")
                cur.execute('UPDATE maquinas SET usuario = %s WHERE id = %s', (novo_user, verifica))
                conn.commit()

            elif escolha == 'H' or 'h':
                novo_host = input('Digite o novo Hostaname: ')
                while novo_host == "":
                    print("Você precisa digitar o HOSTNAME do desktop!")
                    novo_host = input("digite o HOSTNAME: ")
                cur.execute('UPDATE maquinas SET hostname = %s WHERE id = %s', (novo_host, verifica))
                conn.commit()
                
            elif escolha == 'D' or 'd':
                nova_data = input("Digite a nova Data: ")
                while nova_data == "":
                    print("Você precisa digitar a DATA em que adicionou o desktop!")
                    nova_data = input("digite o dia (DD-MM-AAAA): ")
                cur.execute('UPDATE maquinas set data = %s WHERE id = %s', (nova_data, verifica))

            elif escolha == 'U|H|D':
                novo_user = input('Digite o novo Usuário: ')
                while novo_user == "":
                    print('Você precisa digitar o novo Usuário!')
                    novo_user = input("digite seu Nome/RE:")

                novo_host = input('Digite o novo Hostaname: ')
                while novo_host == "":
                    print("Você precisa digitar o HOSTNAME do desktop!")
                    novo_host = input("digite o HOSTNAME: ")

                nova_data = input("Digite a nova Data: ")
                while nova_data == "":
                    print("Você precisa digitar a DATA em que adicionou o desktop!")
                    nova_data = input("digite o dia (DD-MM-AAAA): ")
                cur.execute('UPDATE maquinas SET usuario = %s, hostname = %s WHERE id = %s', (novo_user, novo_host, nova_data, verifica))

            elif escolha == 'U|H':
                novo_user = input('Digite o novo Usuário: ')
                while novo_user == "":
                    print("Você precisa digitar NOME ou seu RE!")
                    novo_user = input("digite seu Nome/RE:")
                novo_host = input('Digite o novo Hostaname: ')
                while novo_host == "":
                    print("Você precisa digitar o HOSTNAME do desktop!")
                    novo_host = input("digite o HOSTNAME: ")
                cur.execute('UPDATE maquinas set usuario = %s, hostname = %s WHERE id = %s', (novo_user, novo_host, verifica))

            elif escolha == 'H|D':
                novo_host = input('Digite o novo Hostaname: ')
                while novo_host == "":
                    print("Você precisa digitar o HOSTNAME do desktop!")
                    novo_host = input("digite o HOSTNAME: ")
                nova_data = input("Digite a nova Data: ")
                while nova_data == "":
                    print("Você precisa digitar a DATA em que adicionou o desktop!")
                    nova_data = input("digite o dia (DD-MM-AAAA): ")
                cur.execute('UPDATE maquinas SET hostname = %s, dia = %s WHERE id = %s', (novo_host, nova_data, verifica))
            
                
            cur.execute("SELECT * FROM maquinas;")
            resultado = cur.fetchall()
            for linha in resultado:
                print(f'ID: {linha[0]} | Usuário: {linha[1]} ! Patrimônio: {linha[2]} | Hostname: {linha[3]} | Data: {linha[4]}')
            print("Tabela Atualizada com sucesso :)")
        


    def deletar_maquina(self):
        deletar = input("Você deseja deletar algum desktop? s/n: ")
        if deletar == 's':
            try:
                cur.execute("SELECT * FROM maquinas;")
                resultado = cur.fetchall()
                for linha in resultado:
                    print(f'ID: {linha[0]} | Usuário: {linha[1]} ! Patrimônio: {linha[2]} | Hostname: {linha[3]} | Data: {linha[4]}')
            
                deletar_desk = input("digite o ID do Desktop que você quer DELETAR: ")
                while deletar_desk == "":
                    print('Você digitar o ID do desktop para deletar!')
                    deletar_desk = input("digite o ID do Desktop que você quer DELETAR: ") 
                cur.execute('DELETE from maquinas WHERE id = (%s)', (deletar_desk))
                conn.commit()
                
                print(self.ver_tabela())
                print("O Desktop foi deletado com sucesso!")
                
                cur.close()
            except:
                print("Não foi possivel DELETAR o desktop :(")
        else:
            exit()

        
       

maquina_1 = Maquina()
maquina_1.adicionar_maquina()
