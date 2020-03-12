import random

def simple_number(integer):

    if integer <2:
        pass
    elif integer == 2:
        return integer
    else:
        indicator = 0
        counter = 2
        while counter < integer and indicator == 0:
            if integer % counter:
                indicator = 0
                counter += 1
            elif not integer % counter:
                indicator = 1
        if indicator == 0:
            return integer
        else:
            pass


list_of_numbers =[random.randint(1, 100) for i in range(0, 100)]

temp = list(map(simple_number, list_of_numbers))

result = [i**2 for i in temp if i]
print(result)








