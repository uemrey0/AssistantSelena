# Assistant Selena [![GitHub release](https://badgen.net/github/release/uemrey0/AssistantSelena)](https://github.com/uemrey0/AssistantSelena/releases/) [![GitHub release](https://img.shields.io/github/last-commit/uemrey0/AssistantSelena.svg)](https://github.com/uemrey0/AssistantSelena/commit/)

Selena is a voice commanding assistant service in Python 3.10 It can recognize human speech, talk to user and execute basic commands in Turkish language. Cammands are texted as Turkish. Multi-language not supported for now.

### Requirements

- MacOS (developed on version 12.3.1)
- Python Version: 3.10 ![Python version](https://img.shields.io/github/pipenv/locked/python-version/uemrey0/AssistantSelena)

### Assistant Skills

- Opens a web page (e.g 'Selena tarayıcıda youtube aç')
- Search in google (e.g 'Selena Google'da mantarlar ara')
- Search in wikipedia (e.g 'Selena vikipedi'de mantar ara')
- Tells joke (e.g 'Selena bana bir şaka yapar mısın?')
- Tells the weather for a place (e.g 'Selena hava durumunu söyler misin?')
- Tells the current time and/or date (e.g 'Selena saat kaç?')
- (NEW) Increase/decrease the speakers master volume (also can set max/mute speakers volume) \*\* (e.g 'Selena sesi arttır!')
- (NEW) Tells the internet speed (ping, uplink and downling) (e.g 'Selena bağlantı hızını söyler misin?')
- (NEW) Spells a word in Turkish (e.g 'Selena kelime hecele. - Ananas')
- (NEW) Do basic calculations (e.g 'Selena bir artı bir')
- (NEW) Answers in general questions (via call Wolfram API and Google Translate), e.g ('Selena en yüksek bina nerededir?')

### Assistant Features

- Asynchronous command execution & speech recognition and interpretation
- Supports one user input modes (just speech)
- One type of sound that is gTTS
- Log preview in console
- Vocal or/and text response

### Installing dependencies
*Note*: You can skip this step, if you are installing the packages. 
Dependencies are listed below and in the `requirements.txt` file.

* gTTS
* playsound
* SpeechRecognition
* googletrans
* wikipedia
* wolframalpha
* osascript
* speedtest
* loguru
* requests

Install one of python package managers in your distro. If you install pip, then you can install the dependencies by running 
`pip3 install -r requirements.txt` 

### Installation

A `setup.py` file is provided in the repository. You can run `sudo python3 setup.py install` to install it at system level.
If you don't have privileges to do so, you can install it at user level by running `python3 setup.py install --user`.  

### Contributing to the repository.
* If you find any problem with the code, please feel free to open an issue.
* Found something you can improve, please send me a pull request with your changes.
I will be more than happy to review and approve them.
