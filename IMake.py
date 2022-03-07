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
    fileName = "src/sound/welcome.mp3"
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
        playsound("src/sound/noconnection.mp3")
    return False
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Arka plan gürültüsü:" + str(r.energy_threshold))
        print("Seni Dinliyorum...")
        playsound('src/sound/senidinliyorum.mp3')
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio, language='tr')
        print(data)
        command = Command(data)
        command.findCommand()
        time.sleep(1)
        isSelena = False
    except sr.UnknownValueError:
        print("Üzgünüm Dostun ne dediğini anlamadım :(")
        playsound('src/sound/error.mp3')
        isSelena = True

if check_internet() != True:
    sys.exit()
else:
    print("Asistan'a Hoşgeldiniz.")
    #playsound("welcome_msg.mp3")
    #user= input("Adınızı Giriniz:")
    #welcomeMSG = "Merhaba {} Asistan'a Hoşgeldin. Ben senin kişisel asistanın Selena".format(user)
    #welcome_msg(welcomeMSG)
    #Network check

isSelena = False
while check_internet():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Arka plan gürültüsü:" + str(r.energy_threshold))
        audio = r.listen(source)
    data = ""
    try:
        if(isSelena == False):
            data = r.recognize_google(audio, language='tr')
            print(data)
            sound = data.upper()
            soundBlocks = sound.split()
            if "SELENA" in soundBlocks:
                listen()
            time.sleep(1)
    except sr.UnknownValueError:
        print(sr.UnknownValueError)