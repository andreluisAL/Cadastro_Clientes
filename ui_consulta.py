
class janela_consulta():
   def __init__(self, lista):
      self.dados = lista
      self.operacao = self.dados[0]
      self.opcao = self.dados[1]

   def janela_consultar(self):
      self.janela_consulta = Tk()

      self.topo_consulta = Label(self.janela_consulta, text = 'Consulta', background = 'grey')
      self.cpf_codigo_consulta = Label(self.janela_consulta, text = 'CPF/CÓDIGO: ', background = 'grey')
      self.campo_do_cpf_codigo_consulta = Entry(self.janela_consulta)
      self.botão_buscar = Button(self.janela_consulta, text = 'Buscar', command = self.recuperar_valores_entry)

      self.topo_consulta.grid(row = 0, column = 2)
      self.cpf_codigo_consulta.grid(row = 5, column =  0)
      self.campo_do_cpf_codigo_consulta.grid(row = 5, column = 1)
      self.botão_buscar.grid(row = 10, column = 2)

      self.janela_consulta.geometry('500x200')
      self.janela_consulta.title('Consultar Cadastro')
      self.janela_consulta.config(background = 'grey')
      self.janela_consulta.resizable(True, True)
      self.janela_consulta.mainloop()

   def recuperar_valores_entry(self):
      self.codigo_cpf = self.campo_do_cpf_codigo_consulta.get()

      if self.codigo_cpf != '':
         self.janela_consulta.destroy()
         self.transformar()
      else:
         messagebox.showerror('Falha', 'Existe Campo Vázio')


   def transformar(self):
      try:
         self.dados = []
         self.codigo = int(self.codigo_cpf)
         self.dados.append(self.codigo_cpf)
         self.verificar()
      except ValueError:
          messagebox.showerror('Falha', 'Tipo de Dado Inválido')

   def verificar(self):
      if self.opcao == 'cliente':
         self.dados.insert(0, self.operacao)
         executar_backend = Consulta(self.dados)
         executar_backend.consultar_cliente()

      elif self.opcao == 'peça':
         self.dados.insert(0, self.operacao)
         self.dados.append('PEÇA')
         executar_backend = Consulta(self.dados)
         executar_backend.consultar_produto()

      elif self.opcao == 'aparelho':
         self.dados.insert(0, self.operacao)
         self.dados.append('APARELHO')
         executar_backend = Consulta(self.dados)
         executar_backend.consultar_produto()

      elif self.opcao == 'serviço':
         self.dados.insert(0, self.operacao)
         self.dados.append('SERVIÇO')
         executar_backend = Consulta(self.dados)
         executar_backend.consultar_servico()



from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from backend_consulta import *
