import pyautogui
import time

text = input("text: ")
repeat = int(input("repeat: "))

time.sleep(3)

for x in range(repeat):
    pyautogui.typewrite(text)
    pyautogui.press("enter")