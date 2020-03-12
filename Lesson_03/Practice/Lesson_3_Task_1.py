Temporary_list = [2, 4, 6, 8, 12, 54]
a = 0
for index in Temporary_list:
    a += index
print(a)
a = 0
b=len(Temporary_list)
i=0
while i < b:
    a += Temporary_list[i]
    i += 1
print(a)
