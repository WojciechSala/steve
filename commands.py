import pyautogui
import os

def keyPress(command):
	if command == "search":
	    pyautogui.press('enter')
	if command == "space":
	    pyautogui.press('space')
	if command == "delete":
	    pyautogui.press('backspace')


def osManager(command):
	if command == "exit":
		exit()
	elif command == "start Google":
		os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')

