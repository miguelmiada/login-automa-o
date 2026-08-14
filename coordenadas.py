import pyautogui
from time import sleep

sleep(4)

x, y = pyautogui.position()

print(f"{x},{y}")