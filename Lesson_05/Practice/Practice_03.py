
def calculating(string):

    dictionary [string] += 1

    return dictionary



file = open(r'D:\Python\Lessons_5\File.txt', 'r')


my_str = ''.join(str(line.strip()) + ' ' for line in file)
my_str = my_str.lower()
print(my_str)
listing = ''.join(i for i in my_str if i !='.' and i !=',')

big_string = listing.split(' ')

my_set = set(big_string)

dictionary = {v:0 for v in my_set}
result = list(map(calculating, big_string))
dictionary = result[0]
dictionary.pop('')
print(dictionary)










