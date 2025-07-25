import os
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

import main2

# CNTL + L puxa a barra de pesquisa

def mostrar_opcao():
    caminho_padrao = r'\\fs01\informatica$\PROGRAMA ADVOGADOS\12 - Outros\Sites'
    opcao_escolhida = opcao.get()

    janela.destroy()
    if opcao_escolhida == r'\Juridico Juliano': # COLOCAR NOME DO ARQUIVO
        caminho = caminho_padrao + opcao_escolhida
        print(caminho)
        main2.configuraNavegador(caminho=caminho)

    login = entrada_nome.get()
    messagebox.showinfo("Opção Selecionada", f"Você escolheu: {opcao_escolhida} \n Login: {login}")

# Criar janela
janela = tk.Tk()
janela.title("Menu com RadioButton")
janela.geometry("960x540")

# Variável para armazenar a opção selecionada
opcao = tk.StringVar()
opcao.set(r"\Juridico Juliano")  # Valor inicial

# Campo Nome Completo
# tk.Label(janela, text="Nome Completo:").pack(pady=10, anchor='w', padx=10)
# entrada_nome = tk.Entry(janela, width=50)
# entrada_nome.pack(anchor='w', padx=10)
#
# Campos login
# tk.Label(janela, text="Login: ").pack(pady=10, anchor='w', padx=10)
# entrada_nome = tk.Entry(janela, width=50)
# entrada_nome.pack(anchor='w', padx=10)

# Radio buttons
tk.Label(janela, text="Pasta para navegador:").pack(pady=10, anchor='w', padx=10)
tk.Radiobutton(janela, text="Juridico Juliano", variable=opcao, value=r"\Juridico Juliano").pack(anchor="w", padx=10)
# tk.Radiobutton(janela, text="Juridico Tatiane", variable=opcao, value="Opção 2").pack(anchor="w", padx=10)
# tk.Radiobutton(janela, text="Juridico Cintia", variable=opcao, value="Opção 3").pack(anchor="w", padx=10)
# tk.Radiobutton(janela, text="Opcao 4", variable=opcao, value="Opção 4").pack(anchor="w", padx=10)
# tk.Radiobutton(janela, text="Opcao 5", variable=opcao, value="Opção 5").pack(anchor="w", padx=10)
# tk.Radiobutton(janela, text="Opcao 6", variable=opcao, value="Opção 6").pack(anchor="w", padx=10)
# tk.Radiobutton(janela, text="Opcao 7", variable=opcao, value="Opção 7").pack(anchor="w", padx=10)
# tk.Radiobutton(janela, text="Opcao 8", variable=opcao, value="Opção 8").pack(anchor="w", padx=10)
# tk.Radiobutton(janela, text="Opcao 9", variable=opcao, value="Opção 9").pack(anchor="w", padx=10)
# tk.Radiobutton(janela, text="Opcao 10", variable=opcao, value="Opção 10").pack(anchor="w", padx=10)

# Botão para mostrar a escolha
btn_mostrar = tk.Button(janela, text="Confirmar", command=mostrar_opcao)
btn_mostrar.pack(pady=10)

# Rodar interface
janela.mainloop()

main2.configuraNavegador(caminho=mostrar_opcao())

# mensagem = r'\\fs01\informatica$\PROGRAMA ADVOGADOS'
#
# pyautogui.hotkey("win", "r")
# time.sleep(1)
# pyautogui.write(mensagem)
# pyautogui.press('enter')

# pyautogui.PAUSE = 1
# time.sleep(2)  # Te dá tempo para preparar a tela
# pyautogui.hotkey("win", "r")
# time.sleep(1)
# pyautogui.write(r'C:\Users\Carlos\Downloads')
# pyautogui.press('enter')
#
# imagem = 'java_instalador.png'
# local = pyautogui.locateOnScreen(imagem, confidence=0.9)
#
# if local:
#     centro = pyautogui.center(local)
#     pyautogui.moveTo(centro, duration=0.5)
#     pyautogui.doubleClick()
# else:
#     print("Imagem do instalador não encontrada na tela.")