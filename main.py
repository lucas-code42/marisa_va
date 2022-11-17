from time import sleep
import speech_recognition as sr
from src.speak.speak import speak
from __init__ import WELCOME_NEWS, DELAY, LISTEN_ME, QUICK_DELAY, READY_TO_LISTEN
from src.news.news import get_news


if "__main__" == __name__:
    speak(WELCOME_NEWS)
    sleep(DELAY)

    speak(LISTEN_ME)
    sleep(DELAY)
    while True:
        microphone = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                print(READY_TO_LISTEN)
                sleep(QUICK_DELAY)
                audio = microphone.listen(source)
                phrase = microphone.recognize_google(audio, language="pt-br")
                print(type(phrase))
                if "marisa" or "Marisa" in phrase and "notícias" or "notícia" in phrase:
                    news = get_news()
                    for last_news in news:
                        speak(str(last_news))
                    continue
                if "marisa" or "Marisa" in phrase and "clima" or "tempo" or "temperatura" in phrase:
                    speak("Função de clima ainda não foi desenvolvida!")
                    continue
                if "marisa" or "Marisa" in phrase and "piada" or "engraçado" or "engraçada" in phrase:
                    speak("Função de arroto")
                    continue
                else:
                    speak("comando não foi processado, diga meu nome antes... Marisa")
                    continue
            except sr.UnknownValueError:
                print("nao entendi")
            except sr.RequestError as e:
                print("erro -->", e)
