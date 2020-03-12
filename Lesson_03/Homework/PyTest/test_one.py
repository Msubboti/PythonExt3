from Lesson_3_for_Test import Testing


def test_small_number():
    dictionary = Testing(245)
    banknotes = list(dictionary.keys())
    expected = 0
    for index in banknotes:
        expected += index * dictionary[index]

    assert (expected == 245)

def test_big_namber():
    dictionary = Testing(8765)
    banknotes = list(dictionary.keys())
    expected = 0
    for index in banknotes:
        expected += index * dictionary[index]
    assert (expected == 8765)


def test_uncorrect_value():
    dictionary = Testing(343)
    banknotes = list(dictionary.keys())
    expected = 0
    for index in banknotes:
        expected += index * dictionary[index]
    assert (expected == 0)

def test_850():
    dictionary = Testing(850)
    banknotes = list(dictionary.keys())
    expected = 0
    for index in banknotes:
        expected += index * dictionary[index]
    assert (expected == 850)

def test_25():
    dictionary = Testing(25)
    banknotes = list(dictionary.keys())
    expected = 0
    for index in banknotes:
        expected += index * dictionary[index]
    assert (expected == 25)


def test_765():
    dictionary = Testing(765)
    banknotes = list(dictionary.keys())
    expected = 0
    for index in banknotes:
        expected += index * dictionary[index]
    assert (expected == 765)

def test_12565():
    dictionary = Testing(12565)
    banknotes = list(dictionary.keys())
    expected = 0
    for index in banknotes:
        expected += index * dictionary[index]
    assert (expected == 12565)

def test_795():
    dictionary = Testing(795)
    banknotes = list(dictionary.keys())
    expected = 0
    for index in banknotes:
        expected += index * dictionary[index]
    assert (expected == 795)

def test_13540():
    dictionary = Testing(13540)
    banknotes = list(dictionary.keys())
    expected = 0
    for index in banknotes:
        expected += index * dictionary[index]
    assert (expected == 13540)

def test_65():
    dictionary = Testing(65)
    banknotes = list(dictionary.keys())
    expected = 0
    for index in banknotes:
        expected += index * dictionary[index]
    assert (expected == 65)


def test_955():
    dictionary = Testing(955)
    banknotes = list(dictionary.keys())
    expected = 0
    for index in banknotes:
        expected += index * dictionary[index]
    assert (expected == 958)