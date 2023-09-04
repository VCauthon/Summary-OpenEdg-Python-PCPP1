import random

class MobilePhone:

    def __init__(self, number: str) -> None:
        self.number = number

    def turn_on(self) -> str:
        return f'mobile phone {self.number} is turned on'
    
    def turn_off(self) -> str:
        return f'mobile phone {self.number} is turned off'

    def call(self, number: str):
        return f'The number {self.number} is calling to {number}'

# Creating the mobiles
mobile_a = MobilePhone(f'{random.randint(0, 10000):05}-{random.randint(0, 100000):06}')
mobile_b = MobilePhone(f'{random.randint(0, 10000):05}-{random.randint(0, 100000):06}')
print(mobile_a.turn_on())
print(mobile_b.turn_on())
print(mobile_a.call('555-34343'))
print(mobile_a.turn_off())
print(mobile_b.turn_off())