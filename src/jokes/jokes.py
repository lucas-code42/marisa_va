import random

from src.jokes import short_jokes


def create_joker() -> str:
    """
    :return: Uma piada aleatória.
    """
    random_joke = random.choice(short_jokes)
    return random_joke
