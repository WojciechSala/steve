import commands
import playsound as playsound
import speech_recognition as sr
import pyaudio, pyautogui
import os, time
from pathlib import Path
from pygame import mixer
# from pywinauto.application import Application

mixer.init()
###################
notification_path = Path('steve/assets/notification.mp3').resolve()
mixer.music.load(str(notification_path))

invoked = False
dictate_mode = False

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening!")
        audio = r.listen(source)

    try:

        req = r.recognize_google(audio)

        # managing steve
        if req == "dictate":
            invoked = False
            dictate_mode = True
            mixer.music.play()

        if dictate_mode:
            if req != "dictate" and req != "start listening":
                pyautogui.typewrite(req)
                commands.keyPress(req)

        if req == "start listening":
            dictate_mode = False
            invoked = True
            mixer.music.play()

        if req == "stop listening":
            invoked = False
            mixer.music.play()

        #commands for OS management
        if  req == "exit" and invoked:
            break

        elif req == "Google" and invoked:
            os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')

        print("You said: ", req, "\nIncoked:", invoked, "\nDictateMode: ", dictate_mode)
    except sr.UnknownValueError:
        print("Couldn't understand")
    except sr.RequestError as e:
        print("Couldn't request results; {0}".format(e))
