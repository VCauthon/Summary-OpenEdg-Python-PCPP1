from dataclasses import dataclass
from xml.etree import ElementTree
from typing import List


@dataclass
class Stock:
    company: str
    last: float
    change: float
    min: float
    max: float

    def __str__(self):
        return f"{self.company.ljust(40)}{str(self.last).ljust(10)}{str(self.change).ljust(10)}{str(self.min).ljust(10)}{str(self.max).ljust(10)}"


def get_xml_data(path: str) -> ElementTree.Element:
    data = ElementTree.parse(path)
    return data.getroot()


def get_headers(
        data: List[ElementTree.Element],
        default_header: List[str] = ["company"]) -> List[str]:
    headers = default_header
    for row in data:
        for key in row.keys():
            if key not in headers:
                headers.append(key)
    return [text.upper() for text in headers]


def get_data(root_element: str, data: ElementTree.Element) -> List[ElementTree.Element]:
    return data.findall(root_element)


def get_rows_of_data(
        data: List[ElementTree.Element]) -> List[Stock]:
    stocks = []
    for row in data:
        stocks.append(Stock(company=row.text, **row.attrib))
    return stocks


def print_data(header: List[str], data: List[Stock]) -> None:
    print(header[0].ljust(40), end="")
    for head in header[1:]:
        print(head.ljust(10), end="")
    print("")  # Lazy!
    print("-" * 80)
    for row in data:
        print(row)

try:
    data = get_data("quote", get_xml_data("4.RESTful-APIs/2.Exercises/nyse.xml"))
    print_data(header=get_headers(data), data=get_rows_of_data(data))
except FileNotFoundError:
    print("The file retrieved hasn't been found")
except ElementTree.ParseError as err:
    print(err)