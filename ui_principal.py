from tkinter import *
import tkinter as tk
from tkinter import ttk
from ui_cadastro import *
from ui_consulta import *
from backend_edita import *
from ui_endereco import *
from ui_produto import *
from ui_servico import *

class janela_principal():

   def __init__(self, master):
      self.frame = Frame(master)
      self.frame.pack()
      self.menu = Menu(master)

      self.menu_cliente = Menu(self.menu)
      self.menu_cliente.add_command(label = 'Cadastrar', command = self.cadastro_Cliente)
      self.menu_cliente.add_command(label = 'Consultar', command = self.consulta_Cliente)
      self.menu_cliente.add_command(label = 'Editar', command = self.edita_Cliente)
      self.menu_cliente.add_command(label = 'Excluir', command = self.exclui_Cliente)
      self.menu.add_cascade(label = 'Cliente', menu = self.menu_cliente)

      self.menu_peça = Menu(self.menu)
      self.menu_peça.add_command(label = 'Cadastrar', command = self.cadastro_Peca)
      self.menu_peça.add_command(label = 'Consultar', command = self.consulta_Peca)
      self.menu_peça.add_command(label = 'Editar', command = self.edita_Peca)
      self.menu_peça.add_command(label = 'Excluir', command = self.exclui_Peca)
      self.menu.add_cascade(label = 'Peça', menu = self.menu_peça)

      self.menu_aparelho = Menu(self.menu)
      self.menu_aparelho.add_command(label = 'Cadastrar', command = self.cadastro_Aparelho)
      self.menu_aparelho.add_command(label = 'Consultar', command = self.consulta_Aparelho)
      self.menu_aparelho.add_command(label = 'Editar', command = self.edita_Aparelho)
      self.menu_aparelho.add_command(label = 'Excluir', command = self.exclui_Aparelho)
      self.menu.add_cascade(label = 'Aparelho', menu = self.menu_aparelho)

      self.menu_servico = Menu(self.menu)
      self.menu_servico.add_command(label = 'Cadastrar', command = self.cadastro_Servico)
      self.menu_servico.add_command(label = 'Consultar', command = self.consulta_Servico)
      self.menu_servico.add_command(label = 'Editar', command = self.edita_Servico)
      self.menu_servico.add_command(label = 'Exclur', command = self.exclui_Servico)
      self.menu.add_cascade(label = 'Serviço', menu = self.menu_servico)

      self.menu_relatorios = Menu(self.menu)
      self.menu_relatorios.add_command(label = 'Lucro')
      self.menu_relatorios.add_command(label = 'Clientes')
      self.menu_relatorios.add_command(label = 'Peças')
      self.menu_relatorios.add_command(label = 'Serviços')
      self.menu_relatorios.add_command(label = 'Aparelhos')
      self.menu.add_cascade(label = 'Relatórios', menu = self.menu_relatorios)

      self.menu_sobre = Menu(self.menu)
      self.menu_sobre.add_command(label = 'Sobre', command = '')
      self.menu.add_cascade(label = 'Sobre', menu = self.menu_sobre)

      master.config(menu = self.menu)

   def cadastro_Cliente(self):
      lista  = []
      lista.append(0)
      lista.append('cliente')
      executando_cadastro = janela_cadastro(lista)
      executando_cadastro.cadastrar_nome_codigo()

   def consulta_Cliente(self):
      lista = []
      lista.append(0)
      lista.append('cliente')
      executando_consulta = janela_consulta(lista)
      executando_consulta.janela_consultar()

   def edita_Cliente(self):
      lista = []
      lista.append(1)
      lista.append('cliente')
      executando_edicao = janela_consulta(lista)
      executando_edicao.janela_consultar()

   def exclui_Cliente(self):
      lista = []
      lista.append(2)
      lista.append('cliente')
      executando_exclusao = janela_consulta(lista)
      executando_exclusao.janela_consultar()

   def cadastro_Peca(self):
      lista = []
      lista.append(0)
      lista.append('peça')
      executando_cadastro = janela_cadastro(lista)
      executando_cadastro.cadastrar_nome_codigo()

   def consulta_Peca(self):
      lista = []
      lista.append(0)
      lista.append('peça')
      executando_consulta = janela_consulta(lista)
      executando_consulta.janela_consultar()

   def edita_Peca(self):
      lista = []
      lista.append(1)
      lista.append('peça')
      executando_edicao = janela_consulta(lista)
      executando_edicao.janela_consultar()

   def exclui_Peca(self):
      lista = []
      lista.append(2)
      lista.append('peça')
      executando_exclusao = janela_consulta(lista)
      executando_exclusao.janela_consultar()

   def cadastro_Aparelho(self):
      lista = []
      lista.append(0)
      lista.append('aparelho')
      executando_cadastro = janela_cadastro()
      executando_cadastro.cadastrar_nome_codigo(lista)

   def consulta_Aparelho(self):
      lista = []
      lista.append(0)
      lista.append('aparelho')
      executando_consulta = janela_consulta(lista)
      executando_consulta.janela_consultar()

   def edita_Aparelho(self):
      lista = []
      lista.append(1)
      lista.append('aparelho')
      executando_edicao = janela_consulta(lista)
      executando_edicao.janela_consultar()

   def exclui_Aparelho(self):
      lista = []
      lista.append(2)
      lista.append('aparelho')
      executando_exclusao = janela_consulta(lista)
      executando_exclusao.janela_consultar()

   def cadastro_Servico(self):
      lista = []
      lista.append(0)
      lista.append('serviço')
      executando_cadastro = janela_cadastro_servico(lista)
      executando_cadastro.cadastrar_servico()

   def consulta_Servico(self):
      lista = []
      lista.append(0)
      lista.append('serviço')
      executando_consulta = janela_consulta(lista)
      executando_consulta.janela_consultar()

   def edita_Servico(self):
      lista = []
      lista.append(1)
      lista.append('serviço')
      executando_edicao = janela_consulta(lista)
      executando_edicao.janela_consultar()

   def exclui_Servico(self):
      lista = []
      lista.append(2)
      lista.append('serviço')
      executando_exclusao = janela_consulta(lista)
      executando_exclusao.janela_consultar()


root = Tk()
root.geometry('600x400')
root.title('André Luís / Código Limpo')
janela_principal(root)
root.resizable(True, True)
imagem_de_fundo = PhotoImage(file = '/home/andre/Imagens/modernn.png')
fixando_imagem_no_fundo = Label(root, image = imagem_de_fundo).pack()
root.mainloop()

