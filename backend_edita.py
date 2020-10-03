from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Edita():
   def __init__(self, dados):
       self.dados = dados

   def editar_cliente(self):
       id = self.dados[0]
       nome = self.dados[1]
       cpf = self.dados[2]
       id_endereco = self.dados[3]
       estado = self.dados[4]
       cep = self.dados[5]
       cidade = self.dados[6]
       rua = self.dados[7]
       numero = self.dados[8]

       import mysql.connector

       conexao = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "projeto_limpo")
       cursor = conexao.cursor()

       desabilitar_chave = "SET FOREIGN_KEY_CHECKS = 0"
       cursor.execute(desabilitar_chave)

       cursor.execute("UPDATE Cliente SET nome = %s, cpf = %s where id = %s", (nome, cpf, id))
       cursor.execute("UPDATE Endereço SET estado = %s, cep = %s, cidade = %s, rua = %s, numero = %s where id = %s",
                      (estado, cep, cidade, rua, numero, id_endereco))


       habilitar_chave = "SET FOREIGN_KEY_CHECKS = 1"
       cursor.execute(habilitar_chave)

       conexao.commit()
       cursor.close()
       conexao.close()
       messagebox.showinfo('Sucesso', 'Operação Concluída!')

   def editar_produto(self):
       id = self.dados[0]
       nome = self.dados[1]
       quantidade = self.dados[2]
       valor = self.dados[3]

       import mysql.connector

       conexao = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "projeto_limpo")
       cursor = conexao.cursor()

       desabilitar_chave = "SET FOREIGN_KEY_CHECKS = 0"
       cursor.execute(desabilitar_chave)

       cursor.execute("UPDATE Produto SET nome = %s, quantidade = %s, valor = %s where id = %s",
                      (nome, quantidade, valor, id))

       habilitar_chave = "SET FOREIGN_KEY_CHECKS = 1"
       cursor.execute(habilitar_chave)

       conexao.commit()
       cursor.close()
       conexao.close()
       messagebox.showinfo('Sucesso', 'Operação Concluída!')

   def editar_servico(self):
       id = self.dados[0]
       id_cliente = self.dados[2]
       id_produto = self.dados[3]
       valor = self.dados[4]
       descricao = self.dados[5]

       import mysql.connector

       conexao = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "projeto_limpo")
       cursor = conexao.cursor()

       desabilitar_chave = "SET FOREIGN_KEY_CHECKS = 0"
       cursor.execute(desabilitar_chave)

       cursor.execute("UPDATE Serviço SET descricao = %s, valor = %s, id_produto = %s, id_cliente = %s where id = %s",
                      (descricao, valor, id_produto, id_cliente, id))

       habilitar_chave = "SET FOREIGN_KEY_CHECKS = 1"
       cursor.execute(habilitar_chave)

       conexao.commit()
       cursor.close()
       conexao.close()
       messagebox.showinfo('Sucesso', 'Operação Concluída!')
       
from backend import *
from ui_retorna import *
from ui_consulta import *