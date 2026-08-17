import pandas as pd
from time import sleep
import pyautogui
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

cpf = os.getenv('CPF')
senha = os.getenv('SENHA')
cpf_sei = os.getenv('CPF_SEI')
senha_sei = os.getenv('SENHA_SEI')

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Configurações de segurança e velocidade
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3

subprocess.Popen([EDGE_PATH, "https://sigep.sme.prefeitura.sp.gov.br/Default.aspx?idPagina=13007"])
sleep(2)  # espera o Edge abrir e carregar
pyautogui.press("tab", presses=7)
sleep(1)
pyautogui.press("enter")
sleep(2)
pyautogui.dragTo(950,239, duration=0)
sleep(0.8)
pyautogui.click(950,239)
pyautogui.write(cpf)
sleep(0.8)
pyautogui.dragTo(951,273, duration=0)
sleep(0.8)
pyautogui.click(951,273)
pyautogui.write(senha)
pyautogui.press("enter")

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.5

subprocess.Popen([EDGE_PATH, "https://sei.prefeitura.sp.gov.br/"])
sleep(2)
pyautogui.dragTo(543,594, duration=0)
sleep(0.8)
pyautogui.click(543,594)
pyautogui.write(cpf_sei)
sleep(0.3)
pyautogui.press("tab")
pyautogui.write(senha_sei)
pyautogui.press("tab", presses=2)
pyautogui.press("enter")