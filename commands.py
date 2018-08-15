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

	# TODO: find another way to exec program
	if command.startswith('start'):
		os.system(command[6:] + ".exe")

	elif command == "start Google":
		os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')

