# Reading the file
import re


def fizzbuzz(lst):
    fizz = lst[0]
    buzz = lst[1]
    counter = lst[2]
    calculate = str()
    for i in range(1, counter+1):
        if not (i % fizz) and i % buzz:
            calculate += 'F '
        elif not (i % buzz) and i % fizz:
            calculate += 'B '
        elif not (i % fizz) and not (i % buzz):
            calculate += 'FB '
        else:
            calculate += str(i) + ' '
    return calculate


f = open(r"D:\Python\values.txt", 'r')
output = open(r"D:\Python\result.txt", 'w').close()
for line in f:
    regular = re.search('\d+.\d+.\d+', line)
    number = regular.group(0)
    number = number.split()
    new_number = list(map(int, number))
    output = open(r"D:\Python\result.txt", 'a')
    result = fizzbuzz(new_number)
    print(result)
    output.write(result + '\n')
    output.close()
f.close()
