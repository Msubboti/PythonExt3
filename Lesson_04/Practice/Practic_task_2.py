Names = ['Maxsim', 'Stas', 'Alex', 'Andrey', 'Sergey']
Surname = ['Ivanov', 'Petrov', 'Sidorov', 'Pavlov', 'Severov']

import random
People = list()
for interation in range(1,50):
    People.append(random.choice(Names) + ' ' +random.choice(Surname))

list_people = list(set(People))

Dictionary = dict.fromkeys(list_people, 0)

keys = list(Dictionary.keys())

for j in People:
    if j in keys:
        Dictionary[j] += 1
    else:
        pass
print(Dictionary)
