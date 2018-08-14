import speech_recognition as sr
import pyaudio
import os
import playsound as ps
from pathlib import Path

notification_path = Path("Desktop/steve/assets/notification.mp3").resolve()
invoked = False

while True:
# Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening!")
        audio = r.listen(source)

    try:
        req = r.recognize_google(audio)

        if req == "listen":
            invoked = True
            ps.playsound(str(notification_path), True)

        elif  req == "exit" and invoked:
            break

        elif req == "Google" and invoked:
            os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')

        print("You said: ", req, invoked)
    except sr.UnknownValueError:
        print("Couldn't understand")
    except sr.RequestError as e:
        print("Couldn't request results; {0}".format(e))