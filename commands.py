import pyautogui
import os
from threading import Thread


def key_press(command):
	if command == "search":
	    pyautogui.press('enter')

	if command == "space":
	    pyautogui.press('space')

	if command == "delete":
		pyautogui.press('backspace')

	if command == "comma":
		pyautogui.press(',')
		pyautogui.press('space')

	if command == "next line":
		pyautogui.keyDown('shift')
		pyautogui.press('enter')
		pyautogui.keyUp('shift')

	if command == "save":
		pyautogui.keyDown('ctrl')
		pyautogui.press('s')
		pyautogui.keyUp('ctrl')

def os_manager(command):
	if command == "exit":
		exit()

	# os main operations only on "OS" keyword
	if command.startswith('OS'):
		command[3:]
		if command.find("shutdown"):
			os.system('shutdown -s -t 0')

	elif command.startswith('start'):
		# User/stc/ which contains shortcut files
		program_to_run = "../../stc/" + command[6:] + ".lnk"
		# finding the full path of given file
		programs_path = os.path.realpath(program_to_run)
		# App can continue running after exectuting, Thread eliminates the freeze
		Thread(target = lambda: os.system(programs_path)).start()

	# kills all processes with given name
	elif command.startswith('kill'):
		program_to_kill = command[5:] + ".exe"
		os.system("TASKKILL /F /IM " + program_to_kill)