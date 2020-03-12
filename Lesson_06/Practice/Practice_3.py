def size_converter(size, unit):
    Dictionary ={'XXS': {'RU': 42, 'GER': 36, 'US': 8, 'FR': 38, 'UK': 24},
                 'XS': {'RU': 44, 'GER': 38, 'US': 10, 'FR': 40, 'UK': 26},
                 'S': {'RU': 46, 'GER': 40, 'US': 12, 'FR': 42, 'UK': 28},
                 'M': {'RU': 48, 'GER': 42, 'US': 14, 'FR': 44, 'UK': 30},
                 'L': {'RU': 50, 'GER': 44, 'US': 16, 'FR': 46, 'UK': 32},
                 'XL': {'RU': 52, 'GER': 46, 'US': 18, 'FR': 48, 'UK': 34},
                 'XXL': {'RU': 54, 'GER': 48, 'US': 20, 'FR': 50, 'UK': 36},
                 'XXXL': {'RU': 56, 'GER': 50, 'US': 22, 'FR': 52, 'UK': 38}}

    converted = Dictionary[size][unit]
    return converted





print('''Welcome to converter of size from international nomenclature to regional.''')
print('''Could you input the international size, please:
XXS , XS, S, M, L, XL, XXL, XXXL''')
int_size = str(input())
print('''Which is regional size do you want to know?
(RU, GER, US, FR, UK)''')
reg_unit = str(input())

result = size_converter(int_size, reg_unit)
print('Yor size is:\t', result)