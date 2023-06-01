from conectar import conexao, cursor
import pandas as pd
from openpyxl.workbook import Workbook


def fabricante(nomeb):
    if "Asus" in nomeb:
        return "Asus"
    if "Acer" in nomeb:
        return "Acer"
    if "Lenovo" in nomeb:
        return "Lenovo"
    if "Samsung" in nomeb:
        return "Samsung"
    if "Macbook" or "Mac" in nomeb:
        return "Apple"
    else:
        return "####"


def add_notebook(nome_completo, marca, valor, banco):
    add_notebooks = f"""insert into notebook_{banco}(modelo, marca, valor)
                    values
                    ('{nome_completo}', '{marca}', '{valor}');"""
    cursor.execute(add_notebooks)
    conexao.commit()


def notebook_geral(marca):
    notebooks_geral = f"SELECT * from notebook_{marca}"
    cursor.execute(notebooks_geral)
    linhas = cursor.fetchall()
    return linhas


def derrubar_construir(marca):
    delete = f"""drop table notebook_{marca}"""
    cursor.execute(delete)

    create = f"""create table notebook_{marca}(
                id int auto_increment primary key,
                modelo varchar(50),
                marca varchar(50),
                valor varchar(50)
                );"""
    cursor.execute(create)
    conexao.commit()

def excel(nome, marca, valor):
    coluna_valor = {"Nome":nome, "Marca":marca, "Valor":valor}
    dados = pd.DataFrame(data= coluna_valor)
    return dados
