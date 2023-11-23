#!/usr/bin/python3
from sys import argv

def find_primef(num):
    if num <= 3:
        return int(num)
    if num % 2 == 0:
        return 2
    elif num % 3 == 0:
        return 3
    else:
        for divisor in range(5, int(num)**0.5) + 1, 6):
            if num % divisor == 0:
                return int(divisor)
            if num % (divisor + 2) == 0:
                return find_primef(num/(divisor+2))
    return int(num)
print(find_primef(int(argv[1])))
