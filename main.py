from time import sleep

import speech_recognition as sr

from __init__ import WELCOME_NEWS, DELAY, LISTEN_ME, QUICK_DELAY, READY_TO_LISTEN
from src.jokes.jokes import create_joker
from src.news.news import get_news
from src.speak.speak import speak
from src.weather_forecast.forecast import create_forecast


def run_news() -> None:
    """
    Chama a função get news do pacote news, em seguida passa cada 'string' para função speak do pacote speak.
    :return: None
    """
    speech = get_news()
    for i in speech:
        speak(str(i))
    return


def run_weather_forecast() -> None:
    """
    Chama a função de previsão do tempo
    :return: None
    """
    speech = create_forecast()
    speak(speech)
    return


def run_joke() -> None:
    """
    Chama funcao de piadas
    :return: None
    """
    speak(create_joker())
    return


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
                print("--->", phrase)

                if "marisa" in phrase or "Marisa" in phrase:

                    if "notícias" in phrase or "notícia" in phrase:
                        run_news()
                        continue

                    elif "clima" in phrase or "tempo" in phrase or "temperatura" in phrase:
                        run_weather_forecast()
                        continue

                    elif "piada" in phrase or "engraçado" in phrase or "engraçada" in phrase:
                        run_joke()
                        continue

                else:
                    speak("comando não foi processado, diga meu nome antes... Marisa")
                    continue
            except sr.UnknownValueError:
                print("nao entendi")
            except sr.RequestError as e:
                print("erro -->", e)
