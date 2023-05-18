import mysql.connector as sql 

con = sql.connect(host='localhost', database='recomendador_DB', user='root', password='g18u10s96')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conctado ao servidor MySQL versão", db_info)
    cursor = con.cursor()
    cursor.execute('SELECT database()')
    db_name = cursor.fetchone() 
    print('Conectado ao banco de dados:', db_name)
    query = 'SELECT * FROM pratos'
    cursor.execute(query)
    pratos = cursor.fetchall()
    print('\n Mostrando pratos cadastrados')
    for coluna in pratos: 
        print("nome:", coluna[0])
        print("descrição:", coluna[1])
        print("ingredientes:", coluna[2])
        print("categorias:", coluna[3])
