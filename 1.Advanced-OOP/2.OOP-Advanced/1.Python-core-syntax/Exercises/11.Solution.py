from typing import List

class Timer:
    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = self.__sanity_check_type(hours, [int])
        self.minutes = self.__sanity_check_type(minutes, [int])
        self.seconds = self.__sanity_check_type(seconds, [int])

    def __add__(self, val: 'Timer') -> 'Timer':
        self.__sanity_check_type(val, [Timer, int])

        own_seconds = self.__timer_to_seconds(self)

        # Subtract seconds to the own timer
        if isinstance(val, int):
            return self.__seconds_to_timer(
                own_seconds + val
            )
        # Sums the received timer with its own
        else:
            return self.__seconds_to_timer(
                own_seconds + self.__timer_to_seconds(val))
   
    def __sub__(self, val: 'Timer') -> 'Timer':
        self.__sanity_check_type(val, [Timer, int])

        own_seconds = self.__timer_to_seconds(self)

        # Subtract seconds to the own timer
        if isinstance(val, int):
            return self.__seconds_to_timer(
                own_seconds - val
            )
        # Subtract the received timer with its own
        else:
            return self.__seconds_to_timer(
                own_seconds - self.__timer_to_seconds(val))

    def __mul__(self, val: int):
        self.__sanity_check_type(val, [int])

        # Multiply the received int by the total of seconds
        return self.__seconds_to_timer(self.__timer_to_seconds(self) * val)

    @staticmethod
    def __sanity_check_type(arg, datatype: List[type]):
        if type(arg) not in datatype:
            raise TypeError('Unexpected type received for this method')
        return arg

    @staticmethod
    def __timer_to_seconds(obj_timer: 'Timer') -> int:
        return (obj_timer.hours * 3600) + (obj_timer.minutes * 60) + obj_timer.seconds

    @staticmethod
    def __seconds_to_timer(seconds: int) -> 'Timer':
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return Timer(hours, minutes, seconds)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

# Creation of the object
time_object_1 = Timer(1, 50, 1)
time_object_2 = Timer(20, 51, 1)

# Calling the magic methods
print(f"Example Sum Timer: {time_object_1 + 10}")
print(f"Example Sub Timer: {time_object_1 - 10}")
print(f"Example Mul Timer: {time_object_1 * 2}")