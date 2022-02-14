import speech_recognition as sr
import time
from Commands import Command
from playsound import playsound
from gtts import gTTS
import os
import requests
import sys
r = sr.Recognizer()
#Welcome MSG
def welcome_msg(text):
    fileName = "welcome.mp3"
    tts = gTTS(text=text, lang="tr")
    tts.save(fileName)
    print(text)
    playsound(fileName)
    os.remove(fileName)
def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("İnternet bağlantısı yok.")
        playsound("noconnection.mp3")
    return False

if check_internet() != True:
    sys.exit()
else:
    print("Asistan'a Hoşgeldiniz.")
    playsound("welcome_msg.mp3")
    user= input("Adınızı Giriniz:")
    welcomeMSG = "Merhaba {} Asistan'a Hoşgeldin. Ben senin kişisel asistanın Selena".format(user)
    welcome_msg(welcomeMSG)
    #Network check

while check_internet():
    with sr.Microphone() as source:
        print ("Seni Dinliyorum...")
        playsound('senidinliyorum.mp3')
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio, language='tr')
        for selena in data:
            if selena in "SELENA":
                isSelena = True
        if(isSelena):
            print(data)
            command = Command(data)
            command.findCommand()
            time.sleep(1)
        else:
            print(isSelena)

    except sr.UnknownValueError:
        print("Üzgünüm Dostun ne dediğini anlamadım :(")
        playsound('error.mp3')
