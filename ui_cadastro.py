from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

class janela_cadastro():

   def __init__(self, lista):
      self.lista = lista
      self.operacao = self.lista[0]
      self.menu = self.lista[1]

   def cadastrar_nome_codigo(self):
      if len(self.lista) == 2:
         self.operacao = self.lista[0]
         self.opcao = self.lista[1]

      elif len(self.lista) == 3:
         self.operacao = self.lista[1]
         self.opcao = self.lista[2]

      else:
         self.operacao = self.lista[2]
         self.opcao = self.lista[3]

      self.window_cadastro = Tk()
      self.topo_nome = Label(self.window_cadastro, text = 'Cadastro', background = 'grey')
      self.nome_objeto = Label(self.window_cadastro, text = 'Nome/Marca: ',  background = 'grey')
      self.campo_de_nome = Entry(self.window_cadastro)
      self.cpf_ou_codigo = Label(self.window_cadastro, text = 'CPF/Código: ', background = 'grey')
      self.campo_cpf_codigo = Entry(self.window_cadastro)
      self.botão_salvar = Button(self.window_cadastro, text = 'Continuar', command = self.recuperar_valores_entry)
      self.topo_nome.grid(row = 0, column = 2)
      self.nome_objeto.grid(row = 5, column = 0)
      self.campo_de_nome.grid(row = 5, column = 1)
      self.cpf_ou_codigo.grid(row = 10, column = 0)
      self.campo_cpf_codigo.grid(row = 10, column = 1)
      self.botão_salvar.grid(row = 20, column = 1)
      self.window_cadastro.geometry('600x400')
      self.window_cadastro.title('Cadastrar')
      self.window_cadastro.config(background = 'grey')
      self.window_cadastro.resizable(True, True)
      self.window_cadastro.mainloop()

   def recuperar_valores_entry(self):
      try:
         self.nome_codigo = []
         self.nome = self.campo_de_nome.get().upper()
         self.codigo = int(self.campo_cpf_codigo.get())
         if self.nome != '' and self.codigo != '':
            self.nome_codigo.append(self.nome)
            self.nome_codigo.append(self.codigo)
            self.verificar()

         else:
            messagebox.showerror('Erro', 'Existe Campo Vázio')
      except:
         messagebox.showerror('Falha', 'Tipo de Dado Inválido')

   def verificar(self):
      if self.opcao == 'cliente':
         self.menu_um_cliente()

      elif self.opcao == 'peça':
         self.menu_um_peca()

      elif self.opcao == 'aparelho':
         self.window_cadastro.destroy()
         self.nome_codigo.insert(0, 'APARELHO')
         executando_instancia = janela_produto()
         executando_instancia.cadastrar_produto(self.nome_codigo, self.operacao)

   def menu_um_cliente(self):
      if self.operacao == 0:
         self.window_cadastro.destroy()
         self.nome_codigo.insert(0, 'CLIENTE')
         executando_instancia = janela_endereco()
         executando_instancia.cadastrar_endereco(self.nome_codigo, self.operacao)

      else:
         self.segundo_menu_cliente()

   def segundo_menu_cliente(self):
      if self.operacao == 1:

         self.window_cadastro.destroy()
         executando_instancia = janela_endereco()
         self.nome_codigo.insert(0, self.lista[0])
         self.nome_codigo.insert(3, self.lista[1])
         executando_instancia.cadastrar_endereco(self.nome_codigo, self.operacao)

   def menu_um_peca(self):
      if self.operacao == 0:
         self.window_cadastro.destroy()
         self.nome_codigo.insert(0, 'PEÇA')
         executando_instancia = janela_produto()
         executando_instancia.cadastrar_produto(self.nome_codigo, self.operacao)
      else:
         self.segundo_menu_peca()

   def segundo_menu_peca(self):
      if self.operacao == 1:
         self.window_cadastro.destroy()
         self.nome_codigo.insert(0, self.lista[0])
         executando_instancia = janela_produto()
         executando_instancia.cadastrar_produto(self.nome_codigo, self.operacao)


from backend import *
from backend_edita import *
from ui_endereco import *
from ui_produto import *
