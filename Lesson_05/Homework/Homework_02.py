# Reading the file
import re

def formating_string(number,FIZZ, BUZZ):
    if not (number % FIZZ) and number % BUZZ:
        out_number = "F "
    elif not (number % BUZZ) and number % FIZZ:
        out_number = 'B '
    elif not (number % FIZZ) and not (number % BUZZ):
        out_number = 'FB '
    else:
        out_number = str(number) + ' '
    return out_number


def fizzbuzz(string):
    string.strip()
    listing = string.split(' ')
    listing = list(map(int, listing))
    fizz = listing[0]
    buzz = listing[1]
    counter = listing[2]
    numbers = [i for i in range(1, counter+1)]
    formatting = ''.join(formating_string(one_number, fizz, buzz) for one_number in numbers)
    return formatting


f = open(r"D:\Python\values.txt", 'r')
output = open(r"D:\Python\Lessons_5\result.txt", 'w').close()

regular_exp = lambda line: re.search('\d+.\d+.\d+', line)

regular = [regular_exp(line) for line in f]

regular = [item.group(0) for item in regular]

output = open(r"D:\Python\Lessons_5\result.txt", 'a')
result = list(map(fizzbuzz, regular))


result = list(map(lambda line: output.write(line + '\n'), result))
output.close()
f.close()
