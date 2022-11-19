from gtts import gTTS
from playsound import playsound


def speak(audio: str) -> None:
    """
    Salva e em seguida executa um audio '.mp3'
    :rtype: None
    """
    tts = gTTS(audio, lang='pt-br')
    tts.save("/home/lcs-42/Documents/python/marisa2.0/src/audio/feedback.mp3")
    playsound("/home/lcs-42/Documents/python/marisa2.0/src/audio/feedback.mp3")
    return
