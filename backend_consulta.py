from tkinter import messagebox
from ui_retorna import *

class Consulta():

   def __init__(self, lista):
      self.dados = lista
      self.operacao = self.dados[0]
      self.codigo = self.dados[1]

   def consultar_cliente(self):
      try:
         import mysql.connector
         conexao = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "projeto_limpo")
         cursor = conexao.cursor()

         select_id = "SELECT * FROM Cliente WHERE id = %(id)s"
         cursor.execute(select_id, {'id': self.dados[1]})
         dados_bd_cliente = cursor.fetchall()
         dados_tupla_cliente = tuple(dados_bd_cliente)
         id = (dados_tupla_cliente[0][0])
         nome = (dados_tupla_cliente[0][1])
         cpf = (dados_tupla_cliente[0][2])
         id_endereco = (dados_tupla_cliente[0][3])
         dados_cliente = []
         dados_cliente.append(id)
         dados_cliente.append(nome)
         dados_cliente.append(cpf)
         dados_cliente.append(id_endereco)

         select_id = "SELECT * FROM Endereço WHERE id = %(id)s"
         cursor.execute(select_id, {'id': id_endereco})
         dados_bd_endereco = cursor.fetchall()
         dados_cliente_enderco = []
         dados_tupla_endereco = tuple(dados_bd_endereco)
         estado = (dados_tupla_endereco[0][1])
         cep = (dados_tupla_endereco[0][2])
         cidade = (dados_tupla_endereco[0][3])
         rua = (dados_tupla_endereco[0][4])
         numero = (dados_tupla_endereco[0][5])
         dados_endereco = []
         dados_endereco.append(estado)
         dados_endereco.append(cep)
         dados_endereco.append(cidade)
         dados_endereco.append(rua)
         dados_endereco.append(numero)
         dados_cliente.extend(dados_endereco)

         instancia_consulta = retorna_dados(dados_cliente, self.operacao)
         instancia_consulta.mostrar_cliente()

      except:
         messagebox.showerror('Falha', 'Cadastro Não Existe!')

   def consultar_produto(self):
      import mysql.connector
      conexao = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "projeto_limpo")
      cursor = conexao.cursor()

      select_id = "SELECT * FROM Produto WHERE id = %(id)s"
      cursor.execute(select_id, {'id': self.dados[1]})
      dados_bd = cursor.fetchall()

      dados_tupla = tuple(dados_bd)
      id = (dados_tupla[0][0])
      nome = (dados_tupla[0][1])
      quantidade = (dados_tupla[0][2])
      valor = (dados_tupla[0][3])
      tipo = (dados_tupla[0][4])

      if tipo == self.dados[2]:
         lista_select = []
         lista_select.append(id)
         lista_select.append(nome)
         lista_select.append(quantidade)
         lista_select.append(valor)
         lista_select.append(tipo)

         instancia_consulta = retorna_dados(lista_select, self.operacao)
         instancia_consulta.mostrar_produto()
      else:
         messagebox.showerror('Falha', 'Cadastro Não Existe!')

   def consultar_servico(self):
      import mysql.connector
      conexao = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "projeto_limpo")
      cursor = conexao.cursor()

      select_id = "SELECT * FROM Serviço WHERE id = %(id)s"
      cursor.execute(select_id, {'id': self.dados[1]})
      dados_bd = cursor.fetchall()

      dados_tupla = tuple(dados_bd)
      id = (dados_tupla[0][0])
      descricao = (dados_tupla[0][1])
      valor = (dados_tupla[0][2])
      id_produto = (dados_tupla[0][3])
      id_cliente = (dados_tupla[0][4])

      lista_select = []
      lista_select.append(id)
      lista_select.append(descricao)
      lista_select.append(valor)
      lista_select.append(id_produto)
      lista_select.append(id_cliente)

      instancia_consulta = retorna_dados(lista_select, self.operacao)
      instancia_consulta.mostrar_servico()

