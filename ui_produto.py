from tkinter import *
import tkinter as tk
from tkinter import ttk
from backend_cadastro import *
from backend_edita import *

class janela_produto():

   def cadastrar_produto(self, dados, operacao):
      self.dados = dados
      self.operacao = operacao

      self.janela_cadastro_objeto = Tk()

      self.quantiadade_aparelho = Label(self.janela_cadastro_objeto, text = 'Quantidade: ', background = 'grey')
      self.campo_de_quantidade = Entry(self.janela_cadastro_objeto)
      self.valor_aparelho = Label(self.janela_cadastro_objeto, text = 'Valor unit.: ', background = 'grey')
      self.tipo_text = Label(self.janela_cadastro_objeto, text = 'Tipo de Produto: ', background = 'grey')
      self.lista_tipo = ttk.Combobox(self.janela_cadastro_objeto, values = ['APARELHO', 'PEÇA'])
      self.campo_do_valor = Entry(self.janela_cadastro_objeto)
      self.botão_salvar = Button(self.janela_cadastro_objeto, text = 'Salvar', command = self.recuperar_valores_entry)

      self.quantiadade_aparelho.grid(row = 10, column = 0)
      self.campo_de_quantidade.grid(row = 10, column = 1)
      self.valor_aparelho.grid(row = 20, column = 0)
      self.campo_do_valor.grid(row = 20, column = 1)
      self.tipo_text.grid(row = 30, column = 0)
      self.lista_tipo.grid(row = 30, column = 1)
      self.botão_salvar.grid(row = 50, column = 2)

      self.janela_cadastro_objeto.geometry('600x300')
      self.janela_cadastro_objeto.title('Cadastrar')
      self.janela_cadastro_objeto.config(background = 'grey')
      self.janela_cadastro_objeto.resizable(True, True)
      self.janela_cadastro_objeto.mainloop()

   def recuperar_valores_entry(self):
      #try:
         self.lista_dados_objeto = []

         self.quantidade = int(self.campo_de_quantidade.get())
         self.valor = float(self.campo_do_valor.get())
         self.tipo = self.lista_tipo.get().upper()
         self.verificar()

      #except:
      #messagebox.showerror('Falha', 'Tipo de Dado Inválido')

   def verificar(self):
      if self.operacao == 0:
         self.menu_produto_um()

      elif self.operacao == 1:
         self.menu_produto_dois()

   def menu_produto_um(self):
      if self.quantidade != '' and self.valor != '' and self.tipo != '':
         self.lista_dados_objeto.append(self.quantidade)
         self.lista_dados_objeto.append(self.valor)
         self.lista_dados_objeto.append(self.tipo)
         self.dados.extend(self.lista_dados_objeto)
         self.janela_cadastro_objeto.destroy()
         executar_backend = Cadastro(self.dados, self.operacao)
         executar_backend.conferir_dados()
      else:
         messagebox.showerror('Erro', 'Existe Campo Vázio')

   def menu_produto_dois(self):
      if self.quantidade != '' and self.valor != '' and self.tipo != '':
         self.lista_dados_objeto.append(self.quantidade)
         self.lista_dados_objeto.append(self.valor)
         self.lista_dados_objeto.append(self.tipo)
         self.dados.extend(self.lista_dados_objeto)
         self.janela_cadastro_objeto.destroy()
         executar_backend = Edita(self.dados)
         executar_backend.editar_produto()
      else:
         messagebox.showerror('Erro', 'Existe Campo Vázio')




