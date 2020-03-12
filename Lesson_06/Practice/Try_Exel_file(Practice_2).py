from openpyxl import load_workbook

Python = set()
FrontEnd = set()
FullStack = set()
Java =set()

def Grouping(student, Number_of_group):
    if Number_of_group == 1:
        Python.add(student)
    elif Number_of_group == 2:
        FrontEnd.add(student)
    elif Number_of_group == 3:
        FullStack.add(student)
    elif Number_of_group == 4:
        Java.add(student)



# Loading of workbook
wb = load_workbook(r'D:\Python\Lessons_6\List_of_students.xlsx')


sheet = wb['First']  # Get name of sheet
several_groups = []
Groups = []
students = []
Vertical_gen = (str(i) for i in range(3, 30))
Gorizontal_gen = (chr(Alphabet) for Alphabet in range(65, 122))

Letter = str(next(Gorizontal_gen))
Number = str(next(Vertical_gen))
value = 1
while value:
    while value:
        value = sheet[Letter + Number].value
        Letter = str(next(Gorizontal_gen))
        Groups.append(value)
    Gorizontal_gen = (chr(Alphabet) for Alphabet in range(65, 122))
    students.append(Groups)
    Groups = []
    Number = str(next(Vertical_gen))
    Letter = str(next(Gorizontal_gen))
    value = sheet[Letter + Number].value

students = [item[0:-1] for item in students]
students_temp_copy = []
for item in students:
    Name_Surname = item[0] + ' ' + item[1]
    temp_list = []
    counter = 1
    for index in range(2, len(item)):
        if item[index] == 'No':
            counter +=1
        elif item[index] == 'Yes':
            temp_list.append(counter)
            counter += 1
    information = (Name_Surname, temp_list)
    if len(temp_list)>1:
        several_groups.append(Name_Surname)
    else:
        pass
    students_temp_copy.append(information)
students = students_temp_copy[:]
students_temp_copy = []

for student in students:
    for i in range(0, len(student[1])):
        Grouping(student[0], student[1][i])



temp_set = {}
several_groups = set(several_groups)
print(several_groups)

print(set.union(Python, FullStack, Java))


temp_set = Python ^ Java
temp_set.update(Python & Java)
print(temp_set)





