# Program should group users according to their age.
# 1 group = from 3 to 6
# 2 group = from 6 to 12
# 3 group = from 12 to 16
# 4 group = more than 16
print('Please enter your age...')
Age = str(input())
try:
    Age = int(Age)
except ValueError:
    Age = float(Age)

if 3 <= Age < 6:
    print('You was included to first group')
elif 6 <= Age < 12:
    print('You was included to second group')
elif 12 <= Age < 16:
    print('You was included to third group')
elif Age >= 16:
    print('You was included to fourth group')
else:
    print('Sorry, the content is not available')
