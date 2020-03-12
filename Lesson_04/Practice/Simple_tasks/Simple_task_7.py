Lising_of_Numbers = list()
Number= 0

while Number <= 1000:
    Number = int(input())
    if Number <= 1000:
        Lising_of_Numbers.append(Number)
    else:
        print(Lising_of_Numbers)
        print("""\tThe summa of numbers in list is\t {0}".
    The avarage is\t{1}"
    The max number is\t{2}
    The min number is \t{3}""".format(sum(Lising_of_Numbers), sum(Lising_of_Numbers)/len(Lising_of_Numbers), max(Lising_of_Numbers), min(Lising_of_Numbers)))
