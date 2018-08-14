import pyautogui

def keyPress(com):
    if com == "search":
        pyautogui.press('enter')
    if com == "space":
        pyautogui.press('space')
    if com == "delete":
        pyautogui.press('backspace')
