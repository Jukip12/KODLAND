import os
import speech_recognition as sr
def record_word():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        print("you said: " + r.recognize_google(audio, language = 'ru-RU'))
    except sr.UnknownValueError:
        print("could not understand!")
    except sr.RequestError as e:
        print("could not request results from Google; {0}".format(e))
    return r.recognize_google(audio)
        