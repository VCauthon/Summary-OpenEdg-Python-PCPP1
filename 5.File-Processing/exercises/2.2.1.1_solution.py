import os
from typing import Iterator, Tuple

import xml.etree.ElementTree as ET
from xml.etree.cElementTree import Element


class TemperatureConverter:
    @staticmethod
    def convert_celsius_to_fahrenheit(celsius: int):
        return round(9/5 * celsius + 32, 1)


class ForecastXmlParser:
    def __init__(self, path_xml: str) -> None:
        self.root = ET.parse(path_xml).getroot()

    def parse(self) -> Iterator[str]:
        for sel in self.root:
            day, celsius = self.__get_day_properties(sel)
            yield f"{day}: {celsius} Celsius, {TemperatureConverter.convert_celsius_to_fahrenheit(celsius)} Fahrenheit"

    @staticmethod
    def __get_day_properties(curr_day: Element) -> Tuple[str, int]:
        day = curr_day.find("day").text
        celsius = int(curr_day.find("temperature_in_celsius").text)
        return day, celsius


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    
    forecast = ForecastXmlParser("../persistance/forecast.xml")

    for day in forecast.parse():
        print(day)
