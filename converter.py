from gtts import gTTS
import os
from playsound import playsound

class AudioFile:
    def __init__(self):
        self.fname=""
        self.reader = ""
        self.addr =  ""

    def getSourceFile(self, content, file_name):
        self.reader = content
        fn = file_name.split('/')
        self.fname = fn[-1].split('.')[0]

    def getDestination(self, addr):
        self.addr = addr

    def makeAudioBook(self):
        try:
            try:
                os.mkdir(self.addr)
            except Exception:
                pass
            audio = gTTS(text=self.reader, lang='en', slow = False)
            path = self.addr + '/' + self.fname + '.mp3'
            audio.save(path)
        except Exception as e:
            print(e)
