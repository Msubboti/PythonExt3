print("Please enter your number...\n ")
number = int(input())

divider = list()
a = len(str(number))
while number:
    temporary = number
    for index in range(1, 10):
        multiplier = 10 ** (a - 1)
        if int(temporary / (index * multiplier)):
            part_list = index * multiplier
        else:
            break
    number -= part_list
    a = len(str(number))
    divider.append(part_list)
print(divider)
dictionary = {}
for i in divider:
    listing = list()
    for j in range(1, i + 1):
        if not (i % j):
            listing.append(j)
            dictionary[i] = listing
print(dictionary)
