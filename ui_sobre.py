from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


def janela_mostrar_sobre():
   janela_mostra_sobre = Tk()
   janela_mostra_sobre.geometry('600x300')
   janela_mostra_sobre.title('Sobre')
   imagem_de_fundo = PhotoImage(file = '/home/andre/Imagens/modernn.png')
   fixando_imagem_no_fundo = Label(janela_mostra_sobre, image = imagem_de_fundo).pack()
   janela_mostra_sobre.resizable(True, True)
   janela_mostra_sobre.mainloop()