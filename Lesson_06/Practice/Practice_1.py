Students = dict(Sidorov=[], Petrov=[], Ivanov=[])
Students['Sosnov'] = []
Practic1 = (7, 6, 4, 7)
Practic2 = (6, 8, 9, 10)
Practic3 = (3, 8, 6, 11)
Values=list(zip(Practic1, Practic2, Practic3))
Students_temp = dict(zip(Students.keys(), Values))
average_value = dict()
for student in Students_temp:
    average_value[student] = sum(Students_temp[student]) / len(Students_temp[student])
print(average_value)
results = list(average_value.items())
values = list()
for i , y in enumerate(results):
        values.append(results[i][1])
temp = values.index(max(values))
Good_result = results[temp][0]
print(Good_result)
temp2 = values.index(min(values))
Bad_result = results[temp2][0]
print(Bad_result)



