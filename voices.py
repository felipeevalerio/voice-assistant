import pyttsx3 as tts
import time


speaker = tts.init()
voices = speaker.getProperty('voices')
speaker.setProperty('rate',150)
for voice in voices:
    print(voice,voice.id)
    speaker.setProperty('voice',voice.id)
    speaker.say('Hello')
    speaker.runAndWait()
    speaker.stop()