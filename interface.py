from tkinter import *
from tkinter import ttk
from MenuBase import listar
from MenuBase import inserir
from MenuBase import consulta
from MenuBase import deletar


root = Tk()
root.title("ControleEstoque_v1")
root.geometry("210x150")
root.configure(background="#dde")
frm = ttk.Frame(root, padding=10)
frm.grid()

#def checar_produtos():


#def adicionar_produto():


#def deletar_produto():


#def consultar_fornecedor():



ttk.Label(frm, text="Checar Produtos").grid(column=0, row=1)
#Botao Listar
ttk.Button(frm, text="OK", command=listar).grid(column=1, row=1)

ttk.Label(frm, text="Adicionar item").grid(column=0, row=2)
#Botao Inserir
ttk.Button(frm, text="OK", command=inserir).grid(column=1, row=2)

ttk.Label(frm, text="Deletar item").grid(column=0, row=3)
#Botao Deletar
ttk.Button(frm, text="OK", command=deletar).grid(column=1, row=3)

ttk.Label(frm, text="Consultar Fornecedor").grid(column=0, row=4)
#Botao Consulta Fornecedor
ttk.Button(frm, text="OK", command=consulta).grid(column=1, row=4)

root.mainloop()