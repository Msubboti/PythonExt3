import random

list_numbers =[random.randint(1, 10000) for i in range(0,101)]

number = int(input())
if number in list_numbers:
    print(number)


