def calculating(left_list, right_list):
    total = sum(list(map(int, left_list)))
    elements = len(left_list)
    first_number = int(total/elements)
    rest = total - (elements*first_number)
    output = ''.join(str(elem)+'+' for elem in left_list)
    if first_number == int(right_list[0]) and rest == int(right_list[1]):
        result = '\tTrue'
    else:
        result = '\tFalse'
    output = str(output[:-1])+'/'+str(elements)+' = '+str(first_number)+' , and rest ' + str(rest) + result
    print(output)


input_file = open(r'D:\Python\Lessons_6\File_Test.txt', 'r')

content = [line.split(';') for line in input_file]
function = lambda x: x[1][:-1]
result_after_divide = list(map(function, content))
result_after_divide = [item.split(' ') for item in result_after_divide]
left_side = [item[0].split(' ') for item in content]
for i in range(0, len(left_side)):
    calculating(left_side[i], result_after_divide[i])
