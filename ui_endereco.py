from tkinter import *
from tkinter import  messagebox
import tkinter as tk
from tkinter import ttk
from backend_cadastro import *
from backend_edita import *


class janela_endereco():

   def cadastrar_endereco(self, nome_codigo, operacao):
      self.nome_codigo = nome_codigo
      self.operacao = operacao
      self.window_endereco = Tk()
      self.topo_endereco = Label(self.window_endereco, text = 'Endereço', background = 'grey')
      self.nome_do_estado = tk.Label(self.window_endereco, text = 'Selecione o Estado: ', background = 'grey')
      self.lista_de_estados = ttk.Combobox(self.window_endereco,
                                          values = ['Acre', 'Alagoas', 'Amapá', 'Amazonas',
                                          'Bahia', 'Brasilia', 'Distrito Federal',
                                          'Ceará', 'Espírito Santo',
                                          'Goiás', 'Maranhão', 'Mato Grosso',
                                          'Mato Grosso do Sul', 'Minas Gerais',
                                          'Pará', 'Paraíba', 'Paraná', 'Pernambuco',
                                          'Piauí', 'Rio de Janeiro',
                                          'Rio Grande do Norte', 'Rio Grande do Sul',
                                          'Rondônia', 'Roraima', 'Santa Catarina',
                                          'São Paulo', 'Sergipe', 'Tocantins'])
      self.nome_da_cidade = Label(self.window_endereco, text = 'Cidade: ', background = 'grey')
      self.campo_da_cidade = Entry(self.window_endereco)
      self.cep_da_cidade = Label(self.window_endereco, text = 'CEP: ', background = 'grey')
      self.campo_do_cep = Entry(self.window_endereco)
      self.nome_da_rua = Label(self.window_endereco, text='Rua: ', background = 'grey')
      self.campo_da_rua = Entry(self.window_endereco)
      self.numero_da_rua = Label(self.window_endereco, text = 'N: ', background = 'grey')
      self.campo_do_numero = Entry(self.window_endereco)
      self.botão_salvar = Button(self.window_endereco, text = 'Salvar', command = self.recuperar_valores_entry)

      self.nome_do_estado.grid(row = 20, column = 2)
      self.lista_de_estados.grid(row = 20, column = 3)
      self.nome_da_cidade.grid(row = 25, column = 0)
      self.campo_da_cidade.grid(row = 25, column = 1)
      self.cep_da_cidade.grid(row = 30, column = 0)
      self.campo_do_cep.grid(row = 30, column = 1)
      self.nome_da_rua.grid(row = 35, column = 0)
      self.campo_da_rua.grid(row = 35, column = 1)
      self.numero_da_rua.grid(row = 40, column = 0)
      self.campo_do_numero.grid(row = 40, column = 1)
      self.botão_salvar.grid(row = 45, column = 2)

      self.window_endereco.geometry('600x400')
      self.window_endereco.title('Cadastrar Cliente')
      self.window_endereco.config(background = 'grey')
      self.window_endereco.resizable(True, True)
      self.window_endereco.mainloop()

   def recuperar_valores_entry(self):
      try:
         self.dados_endereco = []
         self.estado = self.lista_de_estados.get().upper()
         self.cidade = self.campo_da_cidade.get().upper()
         self.cep = int(self.campo_do_cep.get())
         self.rua = self.campo_da_rua.get().upper()
         self.numero = int(self.campo_do_numero.get())

         if self.estado != '' and self.cidade != '' and self.cep != '' and self.rua != '' and self.numero != '':
            self.dados_endereco.append(self.estado)
            self.dados_endereco.append(self.cep)
            self.dados_endereco.append(self.cidade)
            self.dados_endereco.append(self.rua)
            self.dados_endereco.append(self.numero)
            self.nome_codigo.extend(self.dados_endereco)
            self.window_endereco.destroy()
            self.verificar_operacao()

         else:
            messagebox.showerror('Erro', 'Existe Campo Vázio')

      except:
         messagebox.showerror('Falha', 'Tipo de Dado Inválido')

   def verificar_operacao(self):
      if self.operacao == 0:
         executar_backend = Cadastro(self.nome_codigo, self.operacao)
         executar_backend.conferir_dados()
      else:
         executar_backend = Edita(self.nome_codigo)
         executar_backend.editar_cliente()