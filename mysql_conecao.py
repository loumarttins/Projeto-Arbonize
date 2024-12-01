import mysql.connector

# Conexão com o banco de dados
try:
    db = mysql.connector.connect(
    host="137.184.193.139",
        user="arbonize",
        password="@Rb0n1z3.db",
        database="sgau"
    )
    print("Conexão bem-sucedida!")
except mysql.connector.Error as err:
    print(f"Erro de conexão: {err}")


