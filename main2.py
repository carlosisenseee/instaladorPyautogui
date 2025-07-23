import os
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

mensagem = r'\\fs01\informatica$\PROGRAMA ADVOGADOS'

def configuraNavegador(caminho):
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('Chrome')
    time.sleep(1)
    pyautogui.press('enter')

    while True:
        try:
            if pyautogui.locateOnScreen('google.png', confidence=0.9):
                print('Found')
                break
        except:
            pyautogui.sleep(0.5)
            print('Not Found')
    pyautogui.sleep(0.5)

    pyautogui.write('chrome://settings/importData')
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.sleep(1)

    local = pyautogui.locateOnScreen('arquivo_html_1.png', confidence=0.5)
    if local:
        centro = pyautogui.center(local)
        pyautogui.moveTo(centro)
        pyautogui.click()

    pyautogui.sleep(0.5)

    pyautogui.press('down')
    pyautogui.press('enter')

    # local2 = pyautogui.locateOnScreen('escolher_arquivo.png', confidence=0.5)
    # if local2:
    #     centro = pyautogui.center(local2)
    #     pyautogui.moveTo(centro)

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.sleep(1)

    pyautogui.write(caminho)

    pyautogui.sleep(0.5)
    pyautogui.press('enter')

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