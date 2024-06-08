import copy
from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    name: str
    price: float
    weight: int


warehouse: List[Item] = list()
warehouse.append(Item(**{'name': 'Lolly Pop', 'price': 0.4, 'weight': 133}))
warehouse.append(Item(**{'name': 'Licorice', 'price': 0.1, 'weight': 251}))
warehouse.append(Item(**{'name': 'Chocolate', 'price': 1, 'weight': 601}))
warehouse.append(Item(**{'name': 'Sours', 'price': 0.01, 'weight': 513}))
warehouse.append(Item(**{'name': 'Hard candies', 'price': 0.3, 'weight': 433}))

warehouse_with_discount_applied = copy.deepcopy(warehouse)

print('\nSource list of candies\n')
for index, item in enumerate(warehouse):
    print(item.name.center(25, "*"))
    print(f"- Price: {item.price}")
    print(f"- Weight: {item.weight}")
    # Update the price in the discount list if the weight it's over 300
    if item.weight > 300:
        warehouse_with_discount_applied[index].price -= item.price * 0.2
print("".center(25, "*"))


print('\nSource list with discount applied candies\n')
for index, item in enumerate(warehouse_with_discount_applied):
    print(item.name.center(25, "*"))
    print(f"- Price: {item.price}")
    print(f"- Weight: {item.weight}")
print("".center(25, "*"))