import random

a=random.choice(range(0,101))
if 10 < a <= 90 and not a%2 and a%7:
    print(a)
else:
    print('Sorry, number is wrong')