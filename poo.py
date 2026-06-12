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
        self.usuario = input("digite seu Nome/RE:")
        self.patrimonio =  input("digite o patrimônio:")
        self.hostname = input("digite o HOSTNAME: ")
        self.dia = input("digite o dia (AAAA-MM-DD): ")
    
    def atualizar_tabela(self):
        maquina_atualizada = input()
        

maquina_1 = Maquina()
maquina_1.adicionar_maquina()
print(maquina_1.usuario, maquina_1.dia)
