import speech_recognition as sr
import time
from Commands import Command
from playsound import playsound
from gtts import gTTS
import os
import requests
import sys
from loguru import logger
r = sr.Recognizer()
#Welcome MSG
def welcome_msg(text):
    fileName = "src/sound/welcome.mp3"
    tts = gTTS(text=text, lang="tr")
    tts.save(fileName)
    logger.info(text)
    playsound(fileName)
    os.remove(fileName)
def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        logger.error("İnternet bağlantısı yok!")
        playsound("src/sound/noconnection.mp3")
    return False
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        logger.debug("Arka plan gürültüsü:" + str(r.energy_threshold))
        logger.info("Seni Dinliyorum...")
        playsound('src/sound/senidinliyorum.mp3')
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio, language='tr')
        command = Command(data)
        if not command.findCommand():
            command.commandRun("ANLAMADIM")
        isSelena = False
    except sr.UnknownValueError:
        logger.error("Söylenen anlaşılamadı!")
        playsound('src/sound/error.mp3')
        isSelena = True

if check_internet() != True:
    sys.exit()
else:
    logger.info("Asistan'a Hoşgeldiniz.")
    #playsound("welcome_msg.mp3")
    #user= input("Adınızı Giriniz:")
    #welcomeMSG = "Merhaba {} Asistan'a Hoşgeldin. Ben senin kişisel asistanın Selena".format(user)
    #welcome_msg(welcomeMSG)
    #Network check

isSelena = False
while check_internet():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        logger.debug("Arka plan gürültüsü:" + str(r.energy_threshold))
        audio = r.listen(source)
    data = ""
    try:
        if(isSelena == False):
            data = r.recognize_google(audio, language='tr')
            sound = data.upper()
            soundBlocks = sound.split()
            if "SELENA" in soundBlocks:
                command = Command(data)
                if not command.findCommand():
                    listen()
    except sr.UnknownValueError:
        logger.error("Söylenen anlaşılamadı!")