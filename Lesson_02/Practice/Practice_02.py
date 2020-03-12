print("Please enter your number...")
number = int(input())
if number % 2:
    if not number % 3 and not number % 5 and number % 10:
        print('The number\t', number, '\tshould divide by 3 and 5, but not by 10')
    else:
        print('The\t', number, '\tis odd, but conditions are not fulfilled.')
else:
    print('The number is even')
