def calculating(Word, text, counter=0):
    for item in text:
        if Word == item:
            counter += 1
    result = counter
    return result

file = open(r'D:\Python\Lessons_5\File.txt','r')

big_string = ''.join(line.strip() for line in file)
big_string = ''.join(symbol for symbol in big_string if not symbol =='.' and not symbol ==',')
big_string = big_string.lower()

objects = big_string.split(' ')
words = set(objects)
words = list(words)

request_for_calculating = lambda x: calculating(x, objects)
sequence = list(map(request_for_calculating, words))
print(sequence)

Dictionary = dict(zip(words, sequence))
print(Dictionary)
