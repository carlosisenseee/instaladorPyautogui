import os
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

import configurador

# CNTL + L puxa a barra de pesquisa

def mostrar_opcao():
    caminho_padrao = r'\\fs01\informatica$\PROGRAMA ADVOGADOS\12 - Outros\Sites'
    opcao_escolhida = opcao.get()

    janela.destroy()
    if opcao_escolhida == r'\Juridico Juliano': # COLOCAR NOME DO ARQUIVO
        caminho = caminho_padrao + opcao_escolhida
        print(caminho)
        configurador.configuraNavegador(caminho=caminho)

janela = tk.Tk()
janela.title("Menu com RadioButton")
janela.geometry("960x540")

opcao = tk.StringVar()
opcao.set(r"\Juridico Juliano")  # Valor inicial

tk.Label(janela, text="Pasta para navegador:").pack(pady=10, anchor='w', padx=10)
tk.Radiobutton(janela, text="Juridico Juliano", variable=opcao, value=r"\Juridico Juliano").pack(anchor="w", padx=10)
tk.Radiobutton(janela, text="Juridico Tatiane", variable=opcao, value=r"\Juridico Tatiane").pack(anchor="w", padx=10)
tk.Radiobutton(janela, text="Juridico Cintia", variable=opcao, value=r"\Juridico Cintia").pack(anchor="w", padx=10)

btn_mostrar = tk.Button(janela, text="Confirmar", command=mostrar_opcao)
btn_mostrar.pack(pady=10)

janela.mainloop()

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