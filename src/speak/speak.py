from gtts import gTTS
from playsound import playsound


def speak(audio: str) -> None:
    """

    :rtype: object
    """
    tts = gTTS(audio, lang='pt-br')
    tts.save("/home/lcs-42/Documents/python/marisa2.0/src/speak/feedback.mp3")
    playsound("/home/lcs-42/Documents/python/marisa2.0/src/speak/feedback.mp3")
    return
