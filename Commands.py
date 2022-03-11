from gettext import translation
import urllib.request
import json
import pandas as pd
import webbrowser
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from random import choice, randrange
import os
import sys
import datetime
import googletrans
from googletrans import Translator
import wikipedia
import requests
import wolframalpha as wa
from subprocess import call
import osascript
import speedtest
from lxml import html
from src.engiene.spell import Spelling
from src.engiene.weather import Weather

class Command():

    def __init__(self, inSound):
        self.r = sr.Recognizer()
        self.sound = inSound
        self.soundBlocks = self.sound.upper()
        self.soundBlocksSplit = self.sound.split()
        print(self.soundBlocks)
        self.commands = ["NASILSIN", "NE HABER", "SAAT", "WIKIPEDIA", "VIKIPEDI", "GOOGLE", "TARAYICIDA", "ŞAKA", "KOMİKLİK", "FIKRA", "HAVA", "SES", "HIZ", "HECELE", "KAPAT"]

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
            self.r.adjust_for_ambient_noise(source)
            print("Arka plan gürültüsü:" + str(self.r.energy_threshold))
            print(txt)
            self.speak(txt)
            audio = self.r.listen(source)

        data = ""
        try:
            data = self.r.recognize_google(audio, language='tr')
            print(data)
        except sr.UnknownValueError:
            print("Üzgünüm Dostun ne dediğini anlamadım :(")
            playsound('src/sound/error.mp3')
        return data.lower()


    #KOMUT İŞLEVLERİ
    def translate(self, txt, to):
        translator = Translator()
        trans = translator.translate(txt,dest=to)
        print (trans.text)
        return trans.text
    def wolframSearch(self, query):
        app_id = "API_KEY"
        client = wa.Client(app_id)
        res = client.query(self.translate(query,"en"))
        try:
            answer = next(res.results).text
            print(answer)
            return self.translate(answer,"tr")
        except StopIteration:
            return "404"
    def anlamadim(self):
        anlamadimWords = ["Hmm... Bunun için bir cevabım yok. Yardımcı olabileceğim başka bir konu var mı?",
                          "Buna nasıl cevap vericeğimi bilmiyorum."]
        wordchoose = choice(anlamadimWords)
        self.speak(wordchoose)
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
    def google(self):
        if "AÇ" in self.soundBlocks:
            self.speak("Tamam, google açılıyor\n")
            webbrowser.open("https://www.google.com/")
        elif "ARA"in self.soundBlocks:
            query = self.soundBlocks.replace("GOOGLE", "").replace("\'DA", "").replace("ARA", "").strip().lower()
            if(query == ""):
                while True:
                    query = self.listen('Google\'da ne aramamı istersin?')
                    print(query)
                    if query != "":
                        break
                query = query.strip().replace(" ", "+")
            else:
                query = query.replace(" ", "+")
                webbrowser.open("https://www.google.com/search?q=" + query)
        else:
            self.anlamadim()
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
        jokes = open("src/txt/jokes.txt", encoding="utf8")
        joke = jokes.readlines()
        wordchoose = choice(joke)
        self.speak(wordchoose)
        rand = randrange(1,3)
        print(rand)
        playsound("src/sound/jokesound"+str(rand)+".mp3")

    def havadurumu(self):
        citiesJson = json.load("src/json/cities.json")
        foundCity = False;
        city_name = ""
        for x in self.soundBlocksSplit:
            if x.capitalize() in citiesJson:
                foundCity = True
                city_name = x.lower()
                break
        if foundCity == False:       
            city_name_split = self.listen("Hangi şehir?").split()
            for x in city_name_split:
                if x.capitalize() in citiesJson:
                    city_name = x.lower()
                    break
        if city_name != "":
            obj = Weather()
            cond = obj.getWeather(city_name)
            current_temperature = cond["curent"]
            feels_like = cond["feels"]
            weather_description = cond["desc"]
            min = cond["min"]
            max = cond["max"]
            if "BUGÜN" in self.soundBlocks:
                self.speak(city_name + "bugün en yüksek sıcaklık " + str(
                    round(max - 273.15)) + "; en düşük " + str(
                    round(min - 273.15)) + " santigrat derece\n ve " + str(
                    weather_description))
            else:
                self.speak(city_name + "için sıcaklık " + str(
                    round(current_temperature - 273.15)) + "; hissedilen " + str(
                    round(feels_like - 273.15)) + " santigrat derece\n ve " + str(
                    weather_description))
        else:
            self.speak("Bir hata oluştu")
    def systemVolume(self, op):
        result = osascript.osascript('get volume settings')
        print(result)
        print(type(result))
        volInfo = result[1].split(',')
        outputVol = volInfo[0].replace('output volume:', '')
        target_volume = int(outputVol)
        if op == "increase":
            target_volume += 20
        elif op == "decrease":
            target_volume -= 20
        elif op == "max":
            target_volume = 100
        elif op == "min":
            target_volume = 0
        else:
            target_volume = op
        if target_volume<0:
            target_volume = 0
        elif target_volume>100:
            target_volume = 100
        osascript.osascript("set volume output volume {}".format(str(target_volume)))
        self.speak("Tamam")  
    def ses(self):
        if "AZALT" in self.soundBlocks or "KIS" in self.soundBlocks or "DÜŞÜR" in self.soundBlocks or "İNDİR" in self.soundBlocks or "AŞAĞI" in self.soundBlocks:
            op = "decrease"
        elif "YÜKSELT" in self.soundBlocks or "YUKARI" in self.soundBlocks or "ARTTIR" in self.soundBlocks or "YÜKSELT" in self.soundBlocks:
            op = "increase"
        elif "YÜKSEK" in self.soundBlocks or "FULLE" in self.soundBlocks or "KÖKLE" in self.soundBlocks or "SON" in self.soundBlocks or "100" in self.soundBlocks or "YÜZ" in self.soundBlocks:
            op = "max"
        elif "SUSTUR" in self.soundBlocks or "KAPAT" in self.soundBlocks or "SESSİZ" in self.soundBlocks or "0" in self.soundBlocks or "SIFIR" in self.soundBlocks:
            op = "min"
        print(op)
        self.systemVolume(op)
    def speedtest(self):
        st = speedtest.Speedtest()
        self.speak("Bağlantını kontrol ediyorum, lütfen bekle.")
        down = round(st.download()/(1024*1024))
        up = round(st.upload()/(1024*1024))
        ping = round(st.results.ping)
        self.speak("Tamam! İndirme hızı {} Mbps, Yükleme hızı {} Mbps ve gecikme {} milisaniye".format(down,up,ping))
    def hecele(self):
        word = self.listen("Hangi kelimeyi hecelememi istiyorsun?")
        self.speak("Tamam bir bakalım...")
        obj = Spelling()
        spelledList = Spelling.spellword(obj,word)
        speakWord = " "
        for x in spelledList:
            speakWord += x + ". "
        self.speak("Şu şekilde " + word + ";" + speakWord)
    # İŞLEVSEL
    def findCommand(self):
        i = 0
        for command in self.commands:
            if command in self.soundBlocks:
                self.commandRun(command)
                break
            else:
                i = i+1
        if len(self.commands) == i:
            answer = self.wolframSearch(self.sound)
            if(answer != "404"):
                self.speak(answer)
            else:
                self.commandRun("ANLAMADIM")
    def commandRun(self, command):
        if command == "ANLAMADIM":
            self.anlamadim()

        if command == "KAPAT":
            self.kapat()

        if command == "NASILSIN" or command == "NE HABER":
            self.nasılsın()

        if command == "SAAT":
            self.saat()

        if command == "WIKIPEDIA" or command == "VIKIPEDI":
            self.wikipedia()

        if command == "GOOGLE":
            self.google()

        if command == "TARAYICIDA":
            self.tarayici()

        if command == "ŞAKA" or command == "KOMİKLİK" or command == "FIKRA":
            self.joke()

        if command == "HAVA":
            self.havadurumu()
        
        if command == "SES":
            self.ses()
        
        if command == "HIZ":
            self.speedtest()
        
        if command == "HECELE":
            self.hecele()
