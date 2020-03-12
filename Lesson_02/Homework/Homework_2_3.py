# Program is feedback message from ATM
print('How much money do you want to get? Number should be from 1 till 9999 dollars')
Number = int(input())
temporary = str(Number)
a = len(temporary)

while Number > 0:
    if a == 4:
        if int(temporary[0]) == 1:
            print('\t', int(temporary[0]), '\t тысяча')
        elif 1 < int(temporary[0]) < 5:
            print('\t', int(temporary[0]), '\t тысячи')
        elif 5 <= int(temporary[0]) <= 9:
            print('\t', int(temporary[0]), '\t тысяч')
        c = int(temporary[1] + temporary[2] + temporary[3])
        if c == 0:
            print('\t долларов')
        else:
            pass
        Number = Number - (int(temporary[0]) * 1000)
        temporary = str(Number)
        a = len(temporary)
    elif a == 3:
        dictionary = {2: 'две', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь',
                      8: 'восемь', 9: 'девять'}
        if int(temporary[0]) == 1:
            print('\t сто')
        elif int(temporary[0]) == 2:
            print('\t', dictionary.get(int(temporary[0])), 'сти', sep='')
        elif 3 <= int(temporary[0]) <= 4:
            print('\t', dictionary.get(int(temporary[0])), 'ста', sep='')
        elif 5 <= int(temporary[0]) <= 9:
            print('\t', dictionary.get(int(temporary[0])), 'сот', sep='')
        c = int(temporary[1] + temporary[2])
        if c == 0:
            print('\t долларов')
        else:
            pass
        Number = Number - (int(temporary[0]) * 100)
        temporary = str(Number)
        a = len(temporary)
    elif a == 2:
        b = int(temporary[0] + temporary[1])
        if not (b % 10):
            dictionary = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят',
                          70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}
            print('\t', dictionary.get(b), ' долларов')
            Number = Number - b
        else:
            if int(temporary[0]) == 0:
                b = int(temporary[1])
                dictionary = {2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь',
                              8: 'восемь', 9: 'девять'}
                if b == 1:
                    print('\t', dictionary.get(b), ' доллар')
                elif 2 <= b <= 4:
                    print('\t', b, ' доллара')
                elif b == 0 and int(temporary[0]) == 0:
                    print('\tдолларов')
                else:
                    print('\t', b, '\t долларов')
                Number = Number - b
            elif int(temporary[0]) == 1:
                b = int(temporary[0] + temporary[1])
                dictionary = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать',
                              15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать',
                              19: 'девятнадцать'}
                print('\t', dictionary.get(b), 'долларов')
                Number = Number - b
            else:
                b = int(temporary[0])
                dictionary = {1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят',
                              6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
                print('\t', dictionary.get(b))
                Number = Number - (b * 10)
                temporary = str(Number)
                a = len(temporary)
    elif a == 1:
        b = int(temporary[0])
        dictionary = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь',
                      8: 'восемь', 9: 'девять'}
        if b == 1:
            print('\t', dictionary.get(b), ' доллар')
        elif 2 <= b <= 4:
            print('\t', dictionary.get(b), ' доллара')
        else:
            print('\t', dictionary.get(b), '\t долларов')
        Number = Number - b
