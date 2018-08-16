import commands
import speech_recognition as sr
import pyautogui
import ctypes
from pathlib import Path
from pygame import mixer


# minimizes console window, for complete concealment -> rename to .pyw
ctypes.windll.user32.ShowWindow(
    ctypes.windll.kernel32.GetConsoleWindow(), 6)

# program's modes
command_mode = False
dictate_mode = False

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening!")
        audio = r.listen(source)
        keys = ["search", "space", "delete", "stop listening"]
        # notification sound path find and load
        mixer.init()
        notification_path = Path('assets/notification.mp3').resolve()
        mixer.music.load(str(notification_path))

    try:
        req = r.recognize_google(audio)

        # changing modes
        if req == "dictate":
            mixer.music.play()
            command_mode = False
            dictate_mode = True

        if req == "start listening":
            dictate_mode = False
            command_mode = True
            mixer.music.play()

        if req == "stop listening":
            mixer.music.play()
            command_mode = False
            dictate_mode = False

        # managing modes
        if command_mode:
            commands.os_manager(req)

        if dictate_mode:
            if req != "dictate" and req != "start listening":
                # write on screen only if keyword hasn't been said
                if req not in keys:
                    pyautogui.typewrite(req)
                # else exec the command
                commands.key_press(req)

        print("You said: ", req, "\nCommand Mode:", command_mode,
            "\nDictate Mode: ", dictate_mode, "\n----------------")

    except sr.UnknownValueError:
        print("Couldn't understand")
    except sr.RequestError as e:
        print("Couldn't request results; {0}".format(e))
