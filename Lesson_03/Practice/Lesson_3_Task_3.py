# -*- coding: utf-8 -*-

f = open("D:\Python\Lesson_3_Task_1.py", 'r')

for line in f:
    temp_list = list()
    a = len(line)
    for i in range(-1, 0 - (a + 1), -1):
        temp_list.append(line[i])
    print(''.join(temp_list))
f.close()
