# Program calculates how many banknotes, ATM should give to user.
# maximum 12000 dollars per day

print('How much money do you want to get? Number should be from 100 till 12000 grivnas')
Number = int(input())
Dictionary = {5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0}

banknotes = {5: 10, 10: 10, 20: 10, 50: 10, 100: 0, 200: 0, 500: 0, 1000: 0}


if not (Number % min(banknotes.keys())):
    temp_banknotes = list(banknotes.keys())
    lim_list=list()
    for limits in temp_banknotes:
        if banknotes[limits]:
            lim_list.append(limits)
        else:
            pass
    print(lim_list)
    if Number <= 350:
        for id , item in enumerate(lim_list):

            index = id
            if Number % lim_list[index + 1]:
                counter = banknotes[item] - 1
            else:
                counter = banknotes[item]
            while counter >0 and Number != 0:
                Number -= item
                counter -= 1
                Dictionary[item] +=1
            if Number == 0:
                break
    if 350 < Number < 850:
        b = Number - 350
    print(Dictionary)
else:
    print('Sorry, value is not correct. The banknotes:', banknotes[0], banknotes[1], banknotes[2], 'are available')
