from dataclasses import dataclass
from xml.etree import ElementTree
from typing import List
import os


@dataclass
class Stock:
    company: str
    last: float
    change: float
    min: float
    max: float

    def __str__(self):
        return f"{self.company:40}{self.last:<10}{self.change:<10}{self.min:<10}{self.max:<10}"


def get_xml_data(path: str) -> ElementTree.Element:
    # Consider using iterparse if dealing with very large XML files for better memory management
    data = ElementTree.parse(path)
    return data.getroot()


def get_headers(data: List[ElementTree.Element], default_header: List[str] = ["company"]) -> List[str]:
    headers = set(default_header)
    for row in data:
        headers.update(row.keys())
    return [text.upper() for text in headers]


def get_data(root_element: str, data: ElementTree.Element) -> List[ElementTree.Element]:
    return data.findall(root_element)


def get_rows_of_data(data: List[ElementTree.Element]) -> List[Stock]:
    return [Stock(company=row.text, **row.attrib) for row in data]


def print_data(header: List[str], data: List[Stock]) -> None:
    header_line = ''.join([h.ljust(40 if i == 0 else 10) for i, h in enumerate(header)])
    print(header_line)
    print("-" * 80)
    for row in data:
        print(row)

if __name__ == "__main__":

    os.chdir(os.path.dirname(__file__))

    try:
        data = get_data("quote", get_xml_data("../persistance/nyse.xml"))
        print_data(header=get_headers(data), data=get_rows_of_data(data))
    except FileNotFoundError:
        print("The file retrieved hasn't been found")
    except ElementTree.ParseError as err:
        print(f"XML parsing error: {err}")