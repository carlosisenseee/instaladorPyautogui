import os
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

mensagem = r'\\fs01\informatica$\PROGRAMA ADVOGADOS'

def configuraNavegador(caminho):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.write('Chrome')
    time.sleep(1)
    pyautogui.press('enter')

    while True:
        try:
            if pyautogui.locateOnScreen(os.path.join(BASE_DIR, 'Assets', 'google.png'), confidence=0.9):
                print('Found')
                break
        except:
            pyautogui.sleep(0.5)
            print('Not Found')
    pyautogui.sleep(0.5)

    # Digite o url do import
    pyautogui.write('chrome://settings/importData')
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.sleep(1)

    # Seleciona a opcao certa
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.sleep(1)
    pyautogui.press('tab', 3)
    pyautogui.press('enter')
    pyautogui.sleep(1)

    # pyautogui.write(caminho)
    pyautogui.write(r'C:\Users\Carlos\Desktop\teste.html')

    pyautogui.sleep(0.5)
    pyautogui.press('enter')

    while True:
        try:
            if pyautogui.locateOnScreen(os.path.join(BASE_DIR, 'Assets', 'ok.png'), confidence=0.9):
                print('Found')
                break
        except:
            pyautogui.sleep(0.5)
            print('Not Found')

    pyautogui.sleep(0.5)
    pyautogui.press('enter')

    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.sleep(0.2)
    pyautogui.write('chrome://settings/defaultBrowser')
    # dar um jeito


    pyautogui.hotkey('ctrl', 't')
    pyautogui.sleep(0.4)
    pyautogui.write('CAMINHO OUTLOOK')

    pyautogui.hotkey('ctrl', 't')
    pyautogui.sleep(0.4)
    pyautogui.write('CAMINHO INTRANET')


    pyautogui.write('chrome://settings/onStartup')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('down', 2)
    pyautogui.press('tab', 2)
    pyautogui


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