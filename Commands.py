import urllib.request
import json
import pandas as pd
import webbrowser
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from random import choice
import os
import sys
import datetime
import time
import wikipedia
import requests
from lxml import html


class Command():

    def __init__(self, inSound):
        self.r = sr.Recognizer()
        self.sound = inSound.upper()
        self.soundBlocks = self.sound
        self.soundBlocksSplit = self.sound.split()
        print(self.soundBlocks)
        self.commands = ["NASILSIN", "KAPAT", "NE HABER", "SAAT KAÇ", "SAATİ SÖYLE", "WIKIPEDIA", "GOOGLE\'I AÇ", "GOOGLE AÇ", "GOOGLE\'DA ARA", "TARAYICIDA", "ŞAKA", "KOMİKLİK", "FIKRA", ""]

    # KONUŞMA


    def speak(self, text):
        fileName = "sound.mp3"
        tts = gTTS(text=text, lang="tr")
        tts.save(fileName)
        print(text)
        playsound(fileName)
        os.remove(fileName)

    def listen(self, txt):
        with sr.Microphone() as source:
            print(txt)
            self.speak(txt)
            audio = self.r.listen(source)

        data = ""
        try:
            data = self.r.recognize_google(audio, language='tr')
            print(data)
        except sr.UnknownValueError:
            print("Üzgünüm Dostun ne dediğini anlamadım :(")
            playsound('error.mp3')
        return data.lower()


    #KOMUT İŞLEVLERİ
    def anlamadim(self):
        self.speak("Buna nasıl cevap vericeğimi bilmiyorum.")
    def kapat(self):
        self.speak("Kapatıyorum yakışıklı sonra görüşmek üzere ;)")
        sys.exit()

    def nasılsın(self):
        naberWords = ["Benim duygularım yok ama siz insanlar sanırım bu soruya İyiyim diye cevap veriyorsunuz",
                      "Bir bilgisayar kadar mutluyum. Yo yo hayır daha fazla mutluyum.",
                      "Milyonlarca parametrem var, çok sıkıcı olduğumu söylerler genelde. ama iyiyim teşekkürler."]
        wordchoose = choice(naberWords)
        self.speak(wordchoose)
    def saat(self):
        strTime = datetime.datetime.now()
        time = datetime.datetime.strftime(strTime, "%H %M")
        self.speak(f"Saat {time}")
    def wikipedia(self):
        while True:
            query = self.listen('Wikipedia\'da neyi aramamı istersin?')
            print(query)
            if query != "":
                break
        wikipedia.set_lang("tr")
        results = wikipedia.summary(query, sentences=3)
        self.speak("Wikipedia\'ya göre " + results)
    def googleac(self):
        self.speak("Tamam, google açılıyor\n")
        webbrowser.open("https://www.google.com/")
    def googleara(self):
        if(self.soundBlocks.replace("GOOGLE\'DA ARA", "").strip() == ""):
            while True:
                query = self.listen('Google\'da ne aramamı istersin?')
                print(query)
                if query != "":
                    break
            query = query.strip().replace(" ", "+")
        else:
            query = self.soundBlocks.replace("GOOGLE\'DA ARA", "").strip().replace(" ", "+")
        webbrowser.open("https://www.google.com/search?q=" + query)
    def tarayici(self):
        if (self.soundBlocks.replace("TARAYICIDA", "").replace("AÇ", "").strip() == ""):
            while True:
                query = self.listen('Tarayıcıda hangi siteyi açmamı istersin?')
                print(query)
                if query != "":
                    break
            query = query.strip()
        else:
            query = self.soundBlocks.replace("TARAYICIDA", "").replace("AÇ", "").strip()
        webbrowser.open(query)

    def joke(self):
        jokes = open("jokes.txt", encoding="utf8")
        joke = jokes.readlines()
        wordchoose = choice(joke)
        self.speak(wordchoose)

    # İŞLEVSEL
    def findCommand(self):
        i = 0
        for command in self.commands:
            if command in self.soundBlocks:
                self.commandRun(command)
            else:
                i = i+1
        if len(self.commands) == i:
            self.commandRun("ANLAMADIM")
    def commandRun(self, command):
        if command == "ANLAMADIM":
            self.anlamadim()

        if command == "KAPAT":
            self.kapat()

        if command == "NASILSIN" or command == "NE HABER":
            self.nasılsın()

        if command == "SAAT KAÇ" or command == "SAATİ SÖYLE":
            self.saat()

        if command == "WIKIPEDIA":
            self.wikipedia()

        if command == "GOOGLE AÇ" or command == "GOOGLE\'I AÇ":
            self.googleac()
        if command == "GOOGLE\'DA ARA":
            self.googleara()

        if command == "TARAYICIDA":
            self.tarayici()

        if command == "ŞAKA" or command == "KOMİKLİK" or command == "FIKRA":
            self.joke()
