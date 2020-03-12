# Program founds the numbers, which are divisor of our number
import math
divisor = list()
print('Please enter your number...')
number = int(input())
for i in range(1, number):
    if not (number % i):
        divisor.append(i)
print(divisor)
