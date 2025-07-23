import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

def mostrar_opcao():
    opcao_escolhida = opcao.get()
    messagebox.showinfo("Opção Selecionada", f"Você escolheu: {opcao_escolhida}")

# Criar janela
janela = tk.Tk()
janela.title("Menu com RadioButton")
janela.geometry("960x540")

# Variável para armazenar a opção selecionada
opcao = tk.StringVar()
opcao.set("Opção 1")  # Valor inicial

# Campo Nome Completo
tk.Label(janela, text="Nome Completo:").pack(pady=10, anchor='w', padx=10)
entrada_nome = tk.Entry(janela, width=50)
entrada_nome.pack(anchor='w', padx=10)

# Campos login
tk.Label(janela, text="Login: ").pack(pady=10, anchor='w', padx=10)
entrada_nome = tk.Entry(janela, width=50)
entrada_nome.pack(anchor='w', padx=10)


# Radio buttons
tk.Label(janela, text="Pasta para navegador:").pack(pady=10, anchor='w', padx=10)
tk.Radiobutton(janela, text="Opcao 1", variable=opcao, value="Opção 1").pack(anchor="w", padx=10)
tk.Radiobutton(janela, text="Opcao 2", variable=opcao, value="Opção 2").pack(anchor="w", padx=10)
tk.Radiobutton(janela, text="Opcao 3", variable=opcao, value="Opção 3").pack(anchor="w", padx=10)
tk.Radiobutton(janela, text="Opcao 4", variable=opcao, value="Opção 1").pack(anchor="w", padx=10)
tk.Radiobutton(janela, text="Opcao 5", variable=opcao, value="Opção 2").pack(anchor="w", padx=10)
tk.Radiobutton(janela, text="Opcao 6", variable=opcao, value="Opção 3").pack(anchor="w", padx=10)
tk.Radiobutton(janela, text="Opcao 7", variable=opcao, value="Opção 1").pack(anchor="w", padx=10)
tk.Radiobutton(janela, text="Opcao 8", variable=opcao, value="Opção 2").pack(anchor="w", padx=10)
tk.Radiobutton(janela, text="Opcao 9", variable=opcao, value="Opção 3").pack(anchor="w", padx=10)
tk.Radiobutton(janela, text="Opcao 10", variable=opcao, value="Opção 3").pack(anchor="w", padx=10)

# Botão para mostrar a escolha
btn_mostrar = tk.Button(janela, text="Confirmar", command=mostrar_opcao)
btn_mostrar.pack(pady=10)

# Rodar interface
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