# Result of program is analyzing the input number
# If number more than 0 , the output will be '1'
# If number less than 0 , the output will be '-1'
# If number is 0 , the output will be '0'

Number = str(input())
if Number[0] == '-':
    print('-1')
else:
    Number = float(Number)
    if Number > 0:
        print('1')
    else:
        print('0')
