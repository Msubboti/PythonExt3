Names = ['Sergii', 'Vlad', 'Andrii', 'Alexandr', 'Kiril']
Surname = ['Prokopenko', 'Saveliev', 'Severov', 'Andropov', 'Konev']
Groups = ['Python', 'FrontEnd', 'FullStack', 'Java']
Students = list(zip(Names, Surname))

def sorting_of_students(list):
    total_list = []
    for stud in list:
        temp_list = []
        print('''Please choose number of group(s) for students:
            Python = 1, FrontEnd =2 , FullStack = 3 , Java = 4
            for''',stud)
        indicator = 0
        while indicator != 'No':
            temp_list.append(int(input()))
            print('Is he want to learn some more?...(Yes or No)')
            indicator = str(input())
            if indicator == 'Yes':
                print('''Please choose number of group(s) for students:
            Python = 1, FrontEnd =2 , FullStack = 3 , Java = 4''')
            elif indicator == 'No':
                print("Ok, let's continue")
        student_information = (stud, temp_list)
        total_list.append(student_information)
    return total_list

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





Students = [''.join(Students[item][0] + ' ' + Students[item][1]) for item in range(0, len(Students))]

Listing = sorting_of_students(Students)
several_groups = list()
for student in Listing:
    if len(student[1]) > 1:
        several_groups.append(student[0])
    else:
        pass
    for i in range(0, len(student[1])):
        Grouping(student[0], student[1][i])


several_groups = set(several_groups)
print(several_groups)

temp_set = {}
print(set.union(Python, FullStack, Java))
temp_set = Python ^ Java
temp_set.update(Python & Java)
print(temp_set)