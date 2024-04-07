from dataclasses import dataclass, asdict
from json import dumps, loads

@dataclass
class Car:
    registration_number: str
    year_of_production: int
    passenger: bool
    mass: float

    def to_json(self):
        return dumps(asdict(self))


def create_car_with_inputs() -> Car:

    # User inputs
    registration_number = input("Registration number: ")
    year_of_production = int(input("Year of production: "))
    passenger = input("Passenger [y/n]: ")
    if passenger.lower() not in ["y", "n"]:
        raise Exception(f"The passenger can only has the values 'y' or 'n'.\n\t- Received: '{passenger.lower()}'")
    passenger = passenger.lower() == "y"
    mass = float(input("Vehicle mass: "))

    # Create car with the received inputs
    return Car(
        registration_number=registration_number,
        year_of_production=year_of_production,
        passenger=passenger,
        mass=mass
    )


print("What can I do for you?")
print("1 - produce a JSON string describing a vehicle")
print("2 - decode a JSON string into vehicle data")
choice = input("Your choice: ")

# Create a json with the user inputs
if choice == "1":
    user_car = create_car_with_inputs()
    print("Resulting JSON string is:")
    print(user_car.to_json())
# Parse into a DICT the received json from the user
elif choice == "2":
    str_json = input("Enter vehicle JSON string: ")
    print(Car(**loads(str_json)))
else:
    raise Exception(f"Invalid option received.\n\tExpected: 1 or 2\n\tReceived: {choice}")

print("Done")