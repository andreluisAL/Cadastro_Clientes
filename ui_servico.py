from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from backend_cadastro import *

class janela_cadastro_servico():

   def __init__(self, lista):
      self.lista = lista
      self.operacao = self.lista[0]

   def cadastrar_servico(self):
      self.janela_cadastro_servico = Tk()

      self.topo_do_servico = Label(self.janela_cadastro_servico, text = 'Serviço ', background = 'grey')
      self.codigo_cliente = Label(self.janela_cadastro_servico, text = 'Código Cliente: ', background = 'grey')
      self.campo_do_codigo_cliente = Entry(self.janela_cadastro_servico)
      self.codigo_aparelho = Label(self.janela_cadastro_servico, text = 'Código Produto: ', background = 'grey')
      self.campo_de_codigo_aparelho = Entry(self.janela_cadastro_servico)
      self.valor_servico = Label(self.janela_cadastro_servico, text = 'Valor unit Serviço: ', background = 'grey')
      self.campo_do_valor_servico = Entry(self.janela_cadastro_servico)
      self.codigo_servico = Label(self.janela_cadastro_servico, text = 'Código Serviço: ', background = 'grey')
      self.campo_de_codigo_servico = Entry(self.janela_cadastro_servico)
      self.descricao_problema = Label(self.janela_cadastro_servico, text = 'Descrição: ', background = 'grey')
      self.campo_de_descricao = Entry(self.janela_cadastro_servico)
      self.botão_salvar = Button(self.janela_cadastro_servico, text = 'Salvar', command = self.recuperar_valores_entry)

      self.topo_do_servico.grid(row = 0, column = 2)
      self.codigo_cliente.grid(row = 5, column = 0)
      self.campo_do_codigo_cliente.grid(row = 5, column = 1)
      self.codigo_aparelho.grid(row = 10, column = 0)
      self.campo_de_codigo_aparelho.grid(row = 10, column = 1)
      self.valor_servico.grid(row = 20, column = 0)
      self.campo_do_valor_servico.grid(row = 20, column = 1)
      self.codigo_servico.grid(row = 25, column = 0)
      self.campo_de_codigo_servico.grid(row = 25, column = 1)
      self.descricao_problema.grid(row = 30, column = 0)
      self.campo_de_descricao.grid(row = 30, column = 1)
      self.botão_salvar.grid(row = 45, column = 2)

      self.janela_cadastro_servico.geometry('600x300')
      self.janela_cadastro_servico.title('Cadastrar Serviço')
      self.janela_cadastro_servico.config(background = 'grey')
      self.janela_cadastro_servico.resizable(True, True)
      self.janela_cadastro_servico.mainloop()

   def recuperar_valores_entry(self):
      try:
         self.lista_dados_servico = []

         self.codigo_cliente = int(self.campo_do_codigo_cliente.get())
         self.codigo_produto = int(self.campo_de_codigo_aparelho.get())
         self.valor = float(self.campo_do_valor_servico.get())
         self.codigo = int(self.campo_de_codigo_servico.get())
         self.descricao = self.campo_de_descricao.get().upper()

         if self.codigo_cliente != '' and self.codigo_aparelho != '':
            if  self.valor != '' and self.codigo != '' and self.descricao != '':
               self.lista_dados_servico.append(self.codigo_cliente)
               self.lista_dados_servico.append(self.codigo_produto)
               self.lista_dados_servico.append(self.valor)
               self.lista_dados_servico.append(self.codigo)
               self.lista_dados_servico.append(self.descricao)
               self.lista.extend(self.lista_dados_servico)
               self.janela_cadastro_servico.destroy()
               self.lista_dados_servico.insert(0, 'SERVIÇO')
               self.verificar()
         else:
            messagebox.showerror('Erro', 'Existe Campo Vázio')

      except:
         messagebox.showerror('Falha', 'Tipo de Dado Inválido')

   def verificar(self):
      if self.operacao == 0:
         executar_backend = Cadastro(self.lista_dados_servico, self.lista[1])
         executar_backend.conferir_dados()
      elif self.operacao == 1:
         id = self.lista[1]
         self.lista_dados_servico.insert(0, id)
         self.lista_dados_servico.remove(self.codigo)
         executar_edita = Edita(self.lista_dados_servico)
         executar_edita.editar_servico()


from backend_edita import *



