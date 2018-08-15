import commands
import playsound as playsound
import speech_recognition as sr
import pyautogui
from pathlib import Path
from pygame import mixer
# from pywinauto.application import Application

# notification sound path find and load
mixer.init()
notification_path = Path('assets/notification.mp3').resolve()
mixer.music.load(str(notification_path))

# program's modes
command_mode = False
dictate_mode = False

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening!")
        audio = r.listen(source)
        keys = ["search", "space", "delete"]
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

        # managing modes
        if command_mode:
            commands.osManager(req)

        if dictate_mode:
            if req != "dictate" and req != "start listening":
                # wrie on screen only if keyword hasn't been said
                if req not in keys:
                    pyautogui.typewrite(req)
                # else exec the command
                commands.keyPress(req)

        print("You said: ", req, "\nCommandMode:", command_mode,
            "\nDictateMode: ", dictate_mode, "\n---------")

    except sr.UnknownValueError:
        print("Couldn't understand")
    except sr.RequestError as e:
        print("Couldn't request results; {0}".format(e))
