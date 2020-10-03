from tkinter import *
from tkinter import  messagebox
from backend_edita import *
from backend_exclui import *


class retorna_dados():

   def __init__(self, lista, operacao):
      self.lista_select = lista
      self.operacao = operacao

   def mostrar_cliente(self):
      id_dado = self.lista_select[0]
      nome_dado = self.lista_select[1]
      cpf_dado = self.lista_select[2]
      id_endereco_dado = self.lista_select[3]
      estado_dado = self.lista_select[4]
      cep_dado = self.lista_select[5]
      cidade_dado = self.lista_select[6]
      rua_dado = self.lista_select[7]
      numero_dado = self.lista_select[8]

      self.retorna_dados_cliente = Tk()

      id_text = Label(self.retorna_dados_cliente, text = 'id: ', background = 'grey', bd = 3)
      nome_tetx = Label(self.retorna_dados_cliente, text = 'nome: ', background ='grey', bd = 3)
      cpf_text = Label(self.retorna_dados_cliente, text = 'cpf: ', background = 'grey', bd = 3)
      id = Label(self.retorna_dados_cliente, text = id_dado , background = 'grey', bd = 3)
      nome = Label(self.retorna_dados_cliente, text = nome_dado, background = 'grey', bd = 3)
      cpf = Label(self.retorna_dados_cliente, text = cpf_dado, background = 'grey', bd = 3)

      id_endereco_text = Label(self.retorna_dados_cliente, text = 'id_endereco: ', background = 'grey', bd = 3)
      estado_text = Label(self.retorna_dados_cliente, text = 'estado: ', background = 'grey', bd = 3)
      cep_tetx = Label(self.retorna_dados_cliente, text = 'cep: ', background = 'grey', bd = 3)
      cidade_text = Label(self.retorna_dados_cliente, text = 'cidade: ', background = 'grey', bd = 3)
      rua_text = Label(self.retorna_dados_cliente, text = 'rua: ', background = 'grey', bd = 3)
      numero_tetx = Label(self.retorna_dados_cliente, text = 'numero: ', background = 'grey', bd = 3)
      id_endereco = Label(self.retorna_dados_cliente, text = id_endereco_dado, background = 'grey', bd = 3)
      estado = Label(self.retorna_dados_cliente, text = estado_dado, background = 'grey', bd = 3)
      cep = Label(self.retorna_dados_cliente, text = cep_dado, background = 'grey', bd = 3)
      cidade = Label(self.retorna_dados_cliente, text = cidade_dado, background = 'grey', bd = 3)
      rua = Label(self.retorna_dados_cliente, text = rua_dado, background = 'grey', bd = 3)
      numero = Label(self.retorna_dados_cliente, text = numero_dado, background = 'grey', bd = 3)

      id_text.grid(row = 1, column = 0)
      nome_tetx.grid(row = 2, column = 0)
      cpf_text.grid(row = 3, column = 0)

      id.grid(row = 1, column = 1)
      nome.grid(row = 2, column = 1)
      cpf.grid(row = 3, column = 1)

      id_endereco_text.grid(row = 4, column = 0)
      estado_text.grid(row = 5, column = 0)
      cep_tetx.grid(row = 6, column = 0)
      cidade_text.grid(row = 7, column = 0)
      rua_text.grid(row = 8, column = 0)
      numero_tetx.grid(row = 9, column = 0)

      id_endereco.grid(row = 4, column = 1)
      estado.grid(row = 5, column = 1)
      cep.grid(row = 6, column = 1)
      cidade.grid(row = 7, column = 1)
      rua.grid(row = 8, column = 1)
      numero.grid(row = 9, column = 1)

      if self.operacao == 1:
         botao = Button(self.retorna_dados_cliente, text = 'Clique para Editar',
                        command = self.chamando_recadastro_cliente, width = 35, height = 2)
         botao.place(x = 150, y = 250, anchor = CENTER)

      elif self.operacao == 2:
         botao = Button(self.retorna_dados_cliente, text = 'Clique para Excluir',
                        command = self.chamando_exclusao, width = 35, height = 2)
         botao.place(x = 150, y = 250, anchor = CENTER)


      self.retorna_dados_cliente.geometry('300x300')
      self.retorna_dados_cliente.title('Cliente Cadastrado')
      self.retorna_dados_cliente.config(background = 'grey')
      self.retorna_dados_cliente.resizable(False, False)
      self.retorna_dados_cliente.mainloop()

   def chamando_exclusao(self):
      self.retorna_dados_cliente.destroy()
      lista = []
      lista.append(self.lista_select[0])
      lista.append(self.lista_select[3])
      lista.append(self.operacao)
      executando_instancia = Exclui(lista)
      executando_instancia.excluir_cliente()

   def chamando_recadastro_cliente(self):
      lista = []
      lista.append(self.lista_select[0])
      lista.append(self.lista_select[3])
      lista.append(self.operacao)
      lista.append('cliente')

      self.retorna_dados_cliente.destroy()
      executando_instancia = janela_cadastro(lista)
      executando_instancia.cadastrar_nome_codigo()

   def mostrar_produto(self):
      id_dado = self.lista_select[0]
      nome_dado = self.lista_select[1]
      quantidade_dado = self.lista_select[2]
      valor_dado = self.lista_select[3]
      self.tipo = self.lista_select[4]

      self.retorna_dados_produto = Tk()

      id_text = Label(self.retorna_dados_produto, text = 'id: ', background = 'grey', bd = 3)
      nome_tetx = Label(self.retorna_dados_produto, text = 'nome: ', background ='grey', bd = 3)
      quantidade_text = Label(self.retorna_dados_produto, text = 'quantidade: ', background = 'grey', bd = 3)
      valor_text = Label(self.retorna_dados_produto, text = 'valor R$: ' , background = 'grey', bd = 3)

      id = Label(self.retorna_dados_produto, text = id_dado, background = 'grey', bd = 3)
      nome = Label(self.retorna_dados_produto, text = nome_dado, background = 'grey', bd = 3)
      quantidade = Label(self.retorna_dados_produto, text = quantidade_dado, background = 'grey', bd = 3)
      valor = Label(self.retorna_dados_produto, text = valor_dado, background = 'grey', bd = 3)

      id_text.grid(row = 1, column = 0)
      nome_tetx.grid(row = 2, column = 0)
      quantidade_text.grid(row = 3, column = 0)
      valor_text.grid(row = 4, column = 0)

      id.grid(row = 1, column = 1)
      nome.grid(row = 2, column = 1)
      quantidade.grid(row = 3, column = 1)
      valor.grid(row = 4, column = 1)

      if self.operacao == 1:
         botao = Button(self.retorna_dados_produto, text = 'Clique para Editar',
                        command = self.chamando_recadastro_produto, width = 20, height = 2)
         botao.place(x = 150, y = 150, anchor = CENTER)

      elif self.operacao == 2:
         botao = Button(self.retorna_dados_produto, text = 'Clique para Excluir', command = self.chamando_exclusao_produto,
                        width = 20, height = 2)
         botao.place(x = 150, y = 150, anchor = CENTER)

      self.retorna_dados_produto.geometry('300x200')
      self.retorna_dados_produto.title('Produto Cadastrado')
      self.retorna_dados_produto.config(background = 'grey')
      self.retorna_dados_produto.resizable(False, False)
      self.retorna_dados_produto.mainloop()

   def chamando_recadastro_produto(self):
      if self.tipo == 'PEÇA':
         lista = []
         lista.append(self.lista_select[0])
         lista.append(self.operacao)
         lista.append('peça')
      else:
         lista = []
         lista.append(self.lista_select[0])
         lista.append(self.operacao)
         lista.append('aparelho')

      self.retorna_dados_produto.destroy()
      executando_instancia = janela_cadastro()
      executando_instancia.cadastrar_nome_codigo(lista)

   def chamando_exclusao_produto(self):
      lista = []
      lista.append(self.lista_select[0])
      lista.append(self.operacao)
      lista.append('peça')

      self.retorna_dados_produto.destroy()
      executando_instancia = Exclui(lista)
      executando_instancia.excluir_produto()


   def mostrar_servico(self):
      id_dado = self.lista_select[0]
      descricao_dado = self.lista_select[1]
      valor_dado = self.lista_select[2]
      id_produto_dado = self.lista_select[3]
      id_cliente_dado = self.lista_select[4]

      self.retorna_dados_servico = Tk()

      id_text = Label(self.retorna_dados_servico, text = 'id: ', background = 'grey', bd = 3)
      descricao_tetx = Label(self.retorna_dados_servico, text = 'descrição: ', background ='grey', bd = 3)
      valor_text = Label(self.retorna_dados_servico, text = 'valor R$: ', background = 'grey', bd = 3)
      id_produto_text = Label(self.retorna_dados_servico, text = 'id_produto: ', background = 'grey', bd = 3)
      id_cliente_text = Label(self.retorna_dados_servico, text = 'id_cliente : ' , background = 'grey', bd = 3)

      id = Label(self.retorna_dados_servico, text = id_dado, background = 'grey', bd = 3)
      descricao = Label(self.retorna_dados_servico, text = descricao_dado, background = 'grey', bd = 3)
      valor = Label(self.retorna_dados_servico, text = valor_dado, background = 'grey', bd = 3)
      id_produto = Label(self.retorna_dados_servico, text = id_produto_dado, background = 'grey', bd = 3)
      id_cliente = Label(self.retorna_dados_servico, text = id_cliente_dado, background = 'grey', bd = 3)

      id_text.grid(row = 1, column = 0)
      descricao_tetx.grid(row = 2, column = 0)
      valor_text.grid(row = 3, column = 0)
      id_produto_text.grid(row = 4, column = 0)
      id_cliente_text.grid(row = 5, column = 0)

      id.grid(row = 1, column = 1)
      descricao.grid(row = 2, column = 1)
      valor.grid(row = 3, column = 1)
      id_produto.grid(row = 4, column = 1)
      id_cliente.grid(row = 5, column = 1)

      if self.operacao == 1:
         botao = Button(self.retorna_dados_servico, text = 'Clique para Editar',
                        command = self.recadastro_servico, width = 35, height = 2)
         botao.place(x = 150, y = 150, anchor = CENTER)

      elif self.operacao == 2:
         botao = Button(self.retorna_dados_servico, text = 'Clique para Excluir',
                        command = self.exclui_servico, width = 35, height = 2)
         botao.place(x = 150, y = 150, anchor = CENTER)

      self.retorna_dados_servico.geometry('300x200')
      self.retorna_dados_servico.title('Serviço Cadastrado')
      self.retorna_dados_servico.config(background = 'grey')
      self.retorna_dados_servico.resizable(False, False)
      self.retorna_dados_servico.mainloop()

   def recadastro_servico(self):
      lista = []
      lista.append(self.operacao)
      lista.append(self.lista_select[0])
      self.retorna_dados_servico.destroy()
      executando_insrancia = janela_cadastro_servico(lista)
      executando_insrancia.cadastrar_servico()

   def exclui_servico(self):
      self.retorna_dados_servico.destroy()
      executando_insrancia = Exclui(self.lista_select[0])
      executando_insrancia.excluir_servico()

from ui_servico import *
from ui_cadastro import *
