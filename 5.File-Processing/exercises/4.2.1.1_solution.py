import logging
import os
from random import randrange


os.chdir(os.path.dirname(__file__))
HANDLER = logging.FileHandler('../persistance/battery_temperature.log', mode='+w')
HANDLER.setLevel(logging.DEBUG)
HANDLER.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

LOGGER = logging.getLogger(__file__)
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.DEBUG)


def log_temperature(temperature: int) -> None:

    message = f"{temperature} C"

    if temperature > 35:
        LOGGER.critical(message)
    elif temperature >= 30 and temperature <= 35:
        LOGGER.warning(message)
    elif temperature > 20:
        LOGGER.debug(message)
    else:
        LOGGER.critical(f"'{temperature}' is not a valid temperature")


if __name__ == "__main__":
    
    for turn in range(10):
        log_temperature(randrange(20, 40))
