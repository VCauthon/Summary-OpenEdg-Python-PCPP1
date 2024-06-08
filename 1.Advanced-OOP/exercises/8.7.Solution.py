class _Tires:
    def __init__(self, size: int, max_psi: int, min_psi: int) -> None:
        self.__size = size
        self.__min_psi = min_psi
        self.__max_psi = max_psi
        self.__current_psi = 0

    @property
    def size(self):
        print(f"The size of the tires is {self.__size} and the its psi must be between {self.__min_psi}~{self.__max_psi}")

    def get_pressure(self) -> str:
        print(f"The current pressure of the tires ({self.__class__.__name__})"
              f" is '{self.__current_psi}'")

    def pump(self, psi: int):
        
        print(f"Pumping {psi}")
        psi_after_pump = self.__current_psi + psi
        
        if self.__max_psi >= psi_after_pump >= self.__min_psi:
            self.__current_psi = psi_after_pump
            self.get_pressure()
        elif self.__max_psi < psi_after_pump:
            print(f"The pressure is greater (by {psi_after_pump - self.__max_psi}) than permitted")
        elif self.__min_psi > psi_after_pump:
            print(f"The pressure is lesser (by {self.__min_psi - psi_after_pump}) than permitted")


class CityTires(_Tires):
    def __init__(self) -> None:
        super().__init__(
            size=15,
            min_psi=30,
            max_psi=35)


class OffRoadTires(_Tires):
    def __init__(self) -> None:
        super().__init__(
            size=18,
            min_psi=32,
            max_psi=38)


class Engine:
    def __init__(self, engine_type: str) -> None:
        self.fuel = True
        self.engine_type = engine_type
        self.__cur_state = False

    def start(self):
        self.__cur_state = True
        print(f"The engine ({self.__class__.__name__})has been started")
    
    def stop(self):
        self.__cur_state = False
        print(f"The engine ({self.__class__.__name__}) has been stopped")
    
    def get_state(self):
        if self.__cur_state:
            print("The engine is running")
        else:
            print("The engine is stopped")


class ElectricEngine(Engine):
    def __init__(self) -> None:
        super().__init__(engine_type="Electric")


class PetrolEngine(Engine):
    def __init__(self) -> None:
        super().__init__(engine_type="Petrol")


class Vehicle:
    def __init__(self, VIN: str, engine: Engine, tires: _Tires) -> None:
        self.tires: _Tires = tires
        self.engine: Engine = engine
        self.VIN = VIN


# instantiate two objects representing cars:

# the first one is a city car, built of an electric engine and city tires
city_car = Vehicle("5TFUM5F18AX006026", ElectricEngine(), CityTires())
# the second one is an all-terrain car build of a petrol engine and off-road tires
all_terrain_car = Vehicle("1HD1KEM1XDB602203", PetrolEngine(), OffRoadTires())

# play with the cars by calling methods responsible for interaction with components.
print("City car object".center(80, "*"))
city_car.tires.size
city_car.tires.pump(30)
city_car.tires.pump(8)
city_car.engine.get_state()
city_car.engine.start()
city_car.engine.get_state()
city_car.engine.stop()

print("All terrain car object".center(80, "*"))
all_terrain_car.tires.size
all_terrain_car.tires.pump(32)
all_terrain_car.tires.pump(10)
all_terrain_car.engine.get_state()
all_terrain_car.engine.start()
all_terrain_car.engine.get_state()
all_terrain_car.engine.stop()