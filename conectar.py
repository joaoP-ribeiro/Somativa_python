import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='notebooks',
    user='root',
    password=''
)
cursor = conexao.cursor()