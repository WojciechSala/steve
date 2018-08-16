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

def os_manager(command):
	# os main operations only on "OS" keyword
	if command.startswith('OS'):
		command[3:]
		if command.find("shutdown"):
			os.system('shutdown -s -t 0')

	if command == "exit":
		exit()

	elif command.startswith('start'):
		# User/stc/ which contains shortcut files
		program_to_run = "../../stc/" + command[6:] + ".lnk"
		programs_path = os.path.realpath(program_to_run)
		# App can continue running after exectuting, Thread eliminates the freeze
		Thread(target = lambda: os.system(programs_path)).start()

	# kills all processes with given name
	elif command.startswith('kill'):
		program_to_kill = command[5:] + ".exe"
		os.system("TASKKILL /F /IM " + program_to_kill)