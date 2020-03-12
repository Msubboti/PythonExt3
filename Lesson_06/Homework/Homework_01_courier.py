def which_floor(apparment):
    entrance = 0
    while apparment > 0 and entrance <= 4:       #Number of entrance
        entrance += 1
        floor = 0
        while apparment > 0 and floor < 9:       #Number of floor
            floor += 1
            flat = 0
            while apparment > 0 and flat < 6:
                apparment -= 1
                flat += 1
    address = (entrance, floor)
    return address

print('Which apartment do you looking for?')

Number_of_app = int(input())


if Number_of_app > 216:
    print('Sorry, you has wrong address, could you check, please?')
else:

    result = which_floor(Number_of_app)
    print('You need to enter to {0} entrance and lift up to {1} floor!'.format(result[0], result[1]))


