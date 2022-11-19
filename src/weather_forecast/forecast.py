import requests

from src.weather_forecast import URL_SP


def get_weather_forecast() -> dict:
    """
    :return: retorno da API de clima tempo
    """
    r = requests.get(URL_SP, verify=False)
    r = r.json()
    return r


def create_forecast() -> str:
    """
    :return: uma 'string' formatada para ser usada como audio
    """
    forecast = get_weather_forecast()
    forecast_string = f"Em {forecast['results']['city']} são, {forecast['results']['time']} da " \
                      f"{forecast['results']['currently']} e está fazendo {forecast['results']['temp']} graus. "
    return forecast_string
