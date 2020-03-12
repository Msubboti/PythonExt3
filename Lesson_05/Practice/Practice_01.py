def hight_reg(string):
    return string.upper()

def low_reg(string):
    return string.lower()



list_country = ['Australia', 'America', 'Ukraine', 'Poland']

list_names = ['Nick', 'Bob', 'Simon', 'Anelli', 'Lena']

print(list(map(hight_reg, list_country)))
print(list(map(low_reg, list_names)))