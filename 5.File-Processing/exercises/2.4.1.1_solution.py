from dataclasses import dataclass, asdict
import os
from typing import Dict
import xml.etree.ElementTree as ET


@dataclass
class Product:
    name: str
    type: str
    producer: str
    price: str
    currency: str

    def get_attributes(self) -> Dict[str, str]:
        return {key: val for key, val in asdict(self).items() if key != "name"}


product_loaded = [
    Product(
        "Good Morning Sunshine", "cereals", "OpenEDG Testing Service", "9.90", "USD"
    ),
    Product("Spaguetti Veganietto", "pasta", "Programmers Eat Pasta", "15.49", "EUR"),
    Product("Fantastic Almond Milk", "beverages", "Drinks4Coders Inc.", "19.75", "USD"),
]


def load_product(root: ET.Element, product: Product) -> None:
    sub_element = ET.SubElement(root, "product", {"name": product.name})
    for key, val in product.get_attributes().items():
        property = ET.Element(key)
        property.text = val
        sub_element.append(property)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    # Creating the element shopt
    subroot = ET.Element("category")
    subroot.set("name", "Vegan Products")

    # Appending all the products
    for product in product_loaded:
        load_product(root=subroot, product=product)

    # Creating the root element
    root = ET.Element("shop")
    root.append(subroot)

    # Creating the ElementTree that will save te results
    rootTree = ET.ElementTree(root)
    rootTree.write_c14n
    rootTree.write("../persistance/shop.xml", encoding="utf-8", xml_declaration=True)
