import os
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

import main2

# CNTL + L puxa a barra de pesquisa

def mostrar_opcao():
    caminho_padrao = r"\\fs01\informatica$\PROGRAMA ADVOGADOS\12 - OUTROS\Sites"
    opcao_escolhida = opcao.get()

    janela.destroy()
    if opcao_escolhida == r"\Juridico Juliano": # COLOCAR NOME DO ARQUIVO
        caminho = r'\\fs01\informatica$\PROGRAMA ADVOGADOS\12 - OUTROS\Sites\Juridico Juliano\Juridico-Juliano - Novo HTML.html'
        main2.configuraNavegador(caminho=caminho)

janela = tk.Tk()
janela.title("Menu com RadioButton")
janela.geometry("960x540")

opcao = tk.StringVar()
opcao.set(r"\Juridico Juliano")  # Valor inicial

tk.Label(janela, text="Pasta para navegador:").pack(pady=10, anchor='w', padx=10)
tk.Radiobutton(janela, text="Juridico Juliano", variable=opcao, value=r"\Juridico Juliano").pack(anchor="w", padx=10)

btn_mostrar = tk.Button(janela, text="Confirmar", command=mostrar_opcao)
btn_mostrar.pack(pady=10)

janela.mainloop()