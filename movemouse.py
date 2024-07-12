import random  # type: ignore
import time  # type: ignore
import pyautogui as pag  # type: ignore

while True:
    time.sleep(1)
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, duration=0.25)
