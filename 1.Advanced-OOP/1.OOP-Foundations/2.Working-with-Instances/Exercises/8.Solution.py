from typing import List
import random
        
class Apple:
    def __init__(self) -> None:
        self.weight = random.uniform(0.2, 0.5)
        Packaging.total_apple_processed += 1

class Packaging:
    total_apple_processed = 0

    def __init__(self) -> None:
        self.truck: List[List[Apple]] = []

    def make_a_demand(
        self,
        total_apples_need: int,
            limit_weight_by_package: int = 300) -> int:
        # Starting the assembly
        apple_package: List[Apple] = []
        for _ in range(total_apples_need):
            # Add one apple to the package
            apple_package.append(Apple())

            # Adds the package into the truck and start a new one
            if sum([val.weight for val in apple_package]) >= limit_weight_by_package:
                self.truck.append(apple_package)
                apple_package = []

        # Add the pending package to the truck
        if apple_package:
            self.truck.append(apple_package)

        return Packaging.total_apple_processed

# Making the demand
packaging_industry = Packaging()
print(f"Total apples processed: {packaging_industry.make_a_demand(1000)}")

# Showing all the packages of the truck
for num, package in enumerate(packaging_industry.truck, start=1):
    print(f"The package '{num}' has '{len(package)}' apples")
