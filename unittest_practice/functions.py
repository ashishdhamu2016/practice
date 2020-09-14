from typing import Union


def divide(dividend: Union[int, float], divisor:Union[int, float]):
    if divisor == 0:
        raise ValueError("divisor cannot be zero!")
    return dividend / divisor

def multiply(*args: Union[int, float]):
    if len(args) == 0:
        raise ValueError("there should be atleast one argument!")
    
    total = 1
    for arg in args:
        total *= arg
    print(f"total is: {total}")
    return total

data = [21,22,23]
from functools import reduce
total = reduce(lambda x,y: x if x < y else x,data)
print(total)
