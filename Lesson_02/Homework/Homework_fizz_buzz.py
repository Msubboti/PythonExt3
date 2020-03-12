print('Enter first number please...')
fizz = int(input())
print('Enter second number please...')
buzz = int(input())
print('Enter last one number please...')
counter = int(input())
L = list()
for i in range(1, counter+1):
    if not (i % fizz) and i % buzz:
        L.append('F')
    elif not (i % buzz) and i % fizz:
        L.append('B')
    elif not (i % fizz) and not (i % buzz):
        L.append('FB')
    else:
        L.append(i)
print(L)
