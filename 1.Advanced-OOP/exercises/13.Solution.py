import copy
from typing import List


class Delicacy:
    
    def __init__(self, name: str, price: float, weight: int) -> None:
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self) -> str:
        return \
f"""{self.name.center(25, "*")}
- Price: {self.price}
- Weight: {self.weight}"""


warehouse: List[Delicacy] = list()
warehouse.append(Delicacy(**{'name': 'Lolly Pop', 'price': 0.4, 'weight': 133}))
warehouse.append(Delicacy(**{'name': 'Licorice', 'price': 0.1, 'weight': 251}))
warehouse.append(Delicacy(**{'name': 'Chocolate', 'price': 1, 'weight': 601}))
warehouse.append(Delicacy(**{'name': 'Sours', 'price': 0.01, 'weight': 513}))
warehouse.append(Delicacy(**{'name': 'Hard candies', 'price': 0.3, 'weight': 433}))

warehouse_with_discount_applied = copy.deepcopy(warehouse)

print('\nSource list of candies\n')
for index, item in enumerate(warehouse):
    print(item)
    # Update the price in the discount list if the weight it's over 300
    if item.weight > 300:
        warehouse_with_discount_applied[index].price -= item.price * 0.2
print("".center(25, "*"))


print('\nSource list with discount applied candies\n')
for item in warehouse_with_discount_applied:
    print(item)
print("".center(25, "*"))