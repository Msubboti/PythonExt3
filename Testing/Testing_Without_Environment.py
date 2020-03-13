from Program_for_Testing import Testing


def testing_Number_2855(Number = 2855):
    Dictionary = Testing(Number)
    banknotes = list(Dictionary.keys())
    print(Dictionary)
    result = 0
    for notes in banknotes:
        result += notes*Dictionary[notes]
    if result == 2855:
        print('Test is pass')
    else:
        print('Test is failed')


def testing_Number_35(Number = 35):
    Dictionary = Testing(Number)
    banknotes = list(Dictionary.keys())
    print(Dictionary)
    result = 0
    for notes in banknotes:
        result += notes*Dictionary[notes]
    if result == 35:
        print('Test is pass')
    else:
        print('Test is failed')



def testing_Number_12780(Number = 12780):
    Dictionary = Testing(Number)
    banknotes = list(Dictionary.keys())
    print(Dictionary)
    result = 0
    for notes in banknotes:
        result += notes*Dictionary[notes]
    if result == 12780:
        print('Test is pass')
    else:
        print('Test is failed')

def testing_Wrong_Value(Number = 47):
    Dictionary = Testing(Number)
    banknotes = list(Dictionary.keys())
    print(Dictionary)
    result = 0
    for notes in banknotes:
        result += notes*Dictionary[notes]
    if result == 0:
        print('Test is pass')
    else:
        print('Test is failed')


def testing_Wrong_Result(Number = 55):
    Dictionary = Testing(Number)
    banknotes = list(Dictionary.keys())
    print(Dictionary)
    result = 0
    for notes in banknotes:
        result += notes*Dictionary[notes]
    if result == 50:
        print('Test is pass')
    else:
        print('Test is failed')


testing_Number_2855()
testing_Number_35()
testing_Number_12780()
testing_Wrong_Value()
testing_Wrong_Result()