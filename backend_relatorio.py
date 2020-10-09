from tkinter import *
from tkinter import messagebox

class Relatorio():
   def __init__(self, gastos = 6000):
      self.gastos = gastos


   def Lucro(self):
       import mysql.connector
       conexao  = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "projeto_limpo")
       cursor = conexao.cursor()

       soma_valores = "SELECT SUM(valor) FROM Produto"
       cursor.execute(soma_valores)
       dados_valores = cursor.fetchall()
       dados = tuple(dados_valores)
       self.lucro = self.gastos - dados[0][0]
       cursor.close()
       conexao.close()
       self.mostrar(self.lucro, 'Lucro Mensal R$: ')

   def Produto(self, tipo):
       import mysql.connector
       conexao  = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "projeto_limpo")
       cursor = conexao.cursor()

       if tipo == 'PEÇA':
          max_valores = "SELECT MAX(quantidade) FROM Produto WHERE tipo = %(tipo)s"
          cursor.execute(max_valores, {'tipo': 'PEÇA'})
          dados_valores = cursor.fetchall()
          dados_quantidade = tuple(dados_valores)
          numero = dados_quantidade[0][0]
          self.text = 'Peça Mais Recorrente: '

       else:
           max_valores = "SELECT MAX(quantidade) FROM Produto WHERE tipo = %(tipo)s"
           cursor.execute(max_valores, {'tipo': 'APARELHO'})
           dados_valores = cursor.fetchall()
           dados_quantidade = tuple(dados_valores)
           numero = dados_quantidade[0][0]
           self.text = 'Aparelho Mais Recorrente: '


       nome_produto = "SELECT nome FROM Produto WHERE quantidade = %(maximo)s"
       cursor.execute(nome_produto, {'maximo': numero})
       dados_nome = cursor.fetchall()
       produto = tuple(dados_nome)
       self.produto = produto[0][0]

       cursor.close()
       conexao.close()
       self.mostrar(self.produto,  self.text)

   def Servico(self):
       import mysql.connector
       conexao  = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "projeto_limpo")
       cursor = conexao.cursor()

       max_valores = "SELECT MAX(valor) FROM Serviço"
       cursor.execute(max_valores)
       dados_valores = cursor.fetchall()
       dados_quantidade = tuple(dados_valores)
       numero = dados_quantidade[0][0]

       descricao_servico = "SELECT descricao FROM Serviço WHERE valor = %(maximo)s"
       cursor.execute(descricao_servico, {'maximo': numero})
       dados_nome = cursor.fetchall()
       servico = tuple(dados_nome)
       self.servico = servico[0][0]

       cursor.close()
       conexao.close()
       self.mostrar(self.servico, 'Serviços Mais Taxativos: ')

   def mostrar(self, dado, text):

       window_lucro = Tk()
       text = Label(window_lucro, text = text, background = 'grey', bd = 3)
       text_lucro = Label(window_lucro, text = dado, background = 'grey', bd = 2)

       text.grid(row = 0, column = 0)
       text_lucro.grid(row = 0, column = 1)

       window_lucro.geometry('300x100')
       window_lucro.title('Lucro André Luís/Software')
       window_lucro.config(background = 'grey')
       window_lucro.resizable(False, False)
       window_lucro.mainloop()
