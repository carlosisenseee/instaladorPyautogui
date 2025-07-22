import pyautogui
import time

# mensagem = r'\\fs01\informatica$\PROGRAMA ADVOGADOS'
#
# pyautogui.hotkey("win", "r")
# time.sleep(1)
# pyautogui.write(mensagem)
# pyautogui.press('enter')

pyautogui.PAUSE = 1
time.sleep(2)  # Te dá tempo para preparar a tela
pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write(r'C:\Users\Carlos\Downloads')
pyautogui.press('enter')

imagem = 'java_instalador.png'
local = pyautogui.locateOnScreen(imagem, confidence=0.9)

if local:
    centro = pyautogui.center(local)
    pyautogui.moveTo(centro, duration=0.5)
    pyautogui.doubleClick()
else:
    print("Imagem do instalador não encontrada na tela.")