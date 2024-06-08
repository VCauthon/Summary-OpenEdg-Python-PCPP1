from datetime import datetime

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} executed".center(80, "*"))
        print(f"Executed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        func(*args, **kwargs)
    return wrapper


@logger
def sum_numbers(number_1: int, number_2: int):
    print(f"{number_1} + {number_2} = {number_1+number_2}")


@logger
def mul_numbers(number_1: int, number_2: int):
    print(f"{number_1} * {number_2} = {number_1*number_2}")

sum_numbers(1, 2)
mul_numbers(1, 2)