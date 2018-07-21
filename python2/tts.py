import os
from gtts import gTTS

def speak(text):
    print(text)
    tts = gTTS(text=text, lang="en")
    tts.save("sample.mp3")
    os.system("mpg321 sample.mp3")

sampleText = "hi, my name is cat"

speak(sampleText)
