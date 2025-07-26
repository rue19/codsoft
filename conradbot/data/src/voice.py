from gtts import gTTS
from playsound import playsound
import os
import uuid

def speak(text):
    filename = f"temp_{uuid.uuid4().hex}.mp3"
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
