from tkinter import messagebox

class Cadastro():
    def __init__(self, dados, operacao):
        self.dados = dados
        self.operacao = operacao

    def conferir_dados(self):
        self.menu = self.dados[0]

        if self.menu == 'CLIENTE':
            self.salvar_dados_cliente()

        if self.menu == 'PEÇA':
            self.salvar_dados_produto()

        elif self.menu == 'APARELHO':
            self.salvar_dados_produto()

        elif self.menu == 'SERVIÇO':
            self.salvar_dados_servico()

    def salvar_dados_cliente(self):
        import mysql.connector

        nome = self.dados[1]
        cpf = self.dados[2]
        estado = self.dados[3]
        cep = self.dados[4]
        cidade = self.dados[5]
        rua = self.dados[6]
        numero = self.dados[7]

        conexao = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "projeto_limpo")
        cursor = conexao.cursor()
        desabilitar_chave = "SET FOREIGN_KEY_CHECKS = 0"
        cursor.execute(desabilitar_chave)

        cursor.execute("INSERT INTO Cliente (nome, cpf) VALUES (%s, %s)", (nome, cpf))
        cursor.execute("INSERT INTO Endereço (estado, cep, cidade, rua, numero)"
                       " VALUES (%s, %s, %s, %s, %s)", (estado, cep, cidade, rua, numero))

        habilitar_chave = "SET FOREIGN_KEY_CHECKS = 1"
        cursor.execute(habilitar_chave)

        conexao.commit()
        cursor.close()
        conexao.close()
        messagebox.showinfo('Sucesso', 'Operação Concluída!')


    def salvar_dados_produto(self):
        nome = self.dados[1]
        codigo = self.dados[2]
        quantidade = self.dados[3]
        valor = self.dados[4]
        tipo = self.dados[5]

        import mysql.connector

        conexao = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "projeto_limpo")
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Produto (nome, id, quantidade, valor, tipo)"
                       "VALUES (%s, %s, %s, %s, %s)", (nome, codigo, quantidade, valor, tipo))
        conexao.commit()
        cursor.close()
        conexao.close()
        messagebox.showinfo('Sucesso', 'Operação Concluída!')

    def salvar_dados_servico(self):
        codigo_cliente = self.dados[1]
        codigo_produto = self.dados[2]
        valor = self.dados[3]
        codigo_servico = self.dados[4]
        descricao = self.dados[5]

        import mysql.connector

        conexao = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "projeto_limpo")
        cursor = conexao.cursor()

        desabilitar_chave = "SET FOREIGN_KEY_CHECKS = 0"
        cursor.execute(desabilitar_chave)

        cursor.execute("INSERT INTO Serviço (descricao, id, valor, id_produto, id_cliente)"
                       "VALUES (%s, %s, %s, %s, %s)",
                       (descricao, codigo_servico, valor, codigo_produto, codigo_cliente))

        habilitar_chave = "SET FOREIGN_KEY_CHECKS = 1"
        cursor.execute(habilitar_chave)
        
        conexao.commit()
        cursor.close()
        conexao.close()
        messagebox.showinfo('Sucesso', 'Operação Concluída!')