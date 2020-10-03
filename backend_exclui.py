from tkinter import messagebox

class Exclui():
   def __init__(self, dados):
       self.dados = dados


   def excluir_cliente(self):
       import mysql.connector

       conexao = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "projeto_limpo")
       cursor = conexao.cursor()

       desabilitar_chave = "SET FOREIGN_KEY_CHECKS = 0"
       cursor.execute(desabilitar_chave)

       delete_cliente = "DELETE FROM Cliente WHERE  id = %(id_cliente)s"
       cursor.execute(delete_cliente, {'id_cliente': self.dados[0]})

       delete_endereco = "DELETE FROM Endereço WHERE id = %(id_endereco)s"
       cursor.execute(delete_endereco, {'id_endereco': self.dados[1]})

       habilitar_chave = "SET FOREIGN_KEY_CHECKS = 1"
       cursor.execute(habilitar_chave)

       conexao.commit()
       cursor.close()
       conexao.close()
       messagebox.showinfo('Sucesso', 'Operação Concluída!')

   def excluir_produto(self):
       import mysql.connector

       conexao = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "projeto_limpo")
       cursor = conexao.cursor()

       desabilitar_chave = "SET FOREIGN_KEY_CHECKS = 0"
       cursor.execute(desabilitar_chave)

       delete_produto = "DELETE FROM Produto WHERE id = %(id_produto)s"
       cursor.execute(delete_produto, {'id_produto': self.dados[0]})

       habilitar_chave = "SET FOREIGN_KEY_CHECKS = 1"
       cursor.execute(habilitar_chave)

       conexao.commit()
       cursor.close()
       conexao.close()
       messagebox.showinfo('Sucesso', 'Operação Concluída!')


   def excluir_servico(self):
       import mysql.connector

       conexao = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "projeto_limpo")
       cursor = conexao.cursor()

       desabilitar_chave = "SET FOREIGN_KEY_CHECKS = 0"
       cursor.execute(desabilitar_chave)

       delete_produto = "DELETE FROM Serviço WHERE id = %(id_servico)s"
       cursor.execute(delete_produto, {'id_servico': self.dados})

       habilitar_chave = "SET FOREIGN_KEY_CHECKS = 1"
       cursor.execute(habilitar_chave)

       conexao.commit()
       cursor.close()
       conexao.close()
       messagebox.showinfo('Sucesso', 'Operação Concluída!')