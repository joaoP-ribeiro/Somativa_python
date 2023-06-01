from time import sleep
from tkinter import *
from tkinter import ttk
import tkinter as tk

from crud import derrubar_construir, notebook_geral, excel
from web import Web

tela = Tk()


class Tela_cell():
    def __init__(self):
        self.tela = tela
        self.buscados = []
        self.interface()
        self.frames()
        self.botoes()
        self.marcas()
        self.lista_notebooks()
        self.mostrar_notebooks_geral()
        tela.mainloop()

    def interface(self):
        self.img_logo = tk.PhotoImage(file="kabum.png")
        self.tela.iconphoto(False, self.img_logo)
        self.tela.title("Espionando KaBuM")
        self.tela.configure(background="#0061B2")
        self.tela.geometry("500x400")
        self.tela.resizable(True, True)
        self.tela.maxsize(width=500, height=400)
        self.tela.minsize(width=500, height=400)
       

    def frames(self):
        bg = "#EC4500"
        self.frame_0 = Frame(self.tela, bg=bg)
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame_1 = Frame(self.tela, bg=bg)
        self.frame_1.place(relx=0.03, rely=0.18, relwidth=0.94, relheight=0.25)

        self.frame_2 = Frame(self.tela, bg=bg)
        self.frame_2.place(relx=0.03, rely=0.50, relwidth=0.94, relheight=0.45)

    def botoes(self):
        self.btBuscar = Button(self.frame_0, text="BUSCAR",  bg="#0061B2", fg="#fff", command=self.buscar_marca)
        self.btBuscar.place(relx=0.05, rely=0.28, relwidth=0.2, relheight=0.5)

    def marcas(self):
        options = [
            "NOTEBOOKS",
            "MACBOOK",
            "ACER",
            "ASUS",
            "CHROMEBOOK"
        ]
        self.clicked = StringVar()
        self.clicked.set("NOTEBOOKS")
        drop = OptionMenu(self.frame_0, self.clicked, *options)
        drop.place(relx=0.70, rely=0.28, relwidth=0.25, relheight=0.5)



    def lista_notebooks(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3,
                                     columns=("col1", "col2", "col3", "col4", "col5",))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="ID")
        self.listaCli.heading("#2", text="MODELO")
        self.listaCli.heading("#3", text="MARCA")
        self.listaCli.heading("#4", text="VALOR")


        self.listaCli.column("#0", width=3)
        self.listaCli.column("#1", width=20)
        self.listaCli.column("#2", width=260)
        self.listaCli.column("#3", width=65)
        self.listaCli.column("#4", width=77)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

    def selecionar_notebooks(self, marca):
        if marca == "chromebook":
            return "/chromebook", "chromebook"
        elif marca == "asus":
            return "/notebook-asus", "asus"
        elif marca == "acer":
            return "/notebook-acer", "acer"
        elif marca == "macbook":
            return "/macbook", "macbook"
        else:
            return "", "notebook"

    def mostrar_notebooks_geral(self):
        self.listaCli.delete(*self.listaCli.get_children())
        marca, banco = self.selecionar_notebooks(self.clicked.get().lower())
        for i in notebook_geral(banco):
            self.listaCli.insert(parent='', index=0, values=i) 

    def buscar_todos(self):
        marca, banco = self.selecionar_notebooks(self.clicked.get().lower())
        derrubar_construir(banco)
        Web(marca, banco)
        self.buscados.append(banco)


    def buscar_marca(self):
        if self.clicked.get().lower() in self.buscados:
            self.mostrar_notebooks_geral()
        else:
            marca, banco = self.selecionar_notebooks(self.clicked.get().lower())
            derrubar_construir(banco)
            Web(marca, banco)
            self.mostrar_notebooks_geral()
            self.buscados.append(banco)
    
    


