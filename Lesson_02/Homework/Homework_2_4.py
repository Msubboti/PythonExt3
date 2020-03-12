# Program calculates how many banknotes, ATM should give to user.
# maximum 12000 dollars per day

import random

print('How much money do you want to get? Number should be from 100 till 12000 dollars')
Number = int(input())
Dictionary = dict()
banknotes = [500, 200, 100, 50]
a = random.randrange(0,4)
print(banknotes.pop(a))

if not (Number % min(banknotes)):
    for notes in banknotes:
        i = 0
        while Number >= notes:
            i = i + 1
            Number = Number - notes
            Dictionary[notes] = i
            print(Dictionary)
else:
    print('Sorry, value is not correct. The banknotes:', banknotes[0], banknotes[1], banknotes[2], 'are available')


